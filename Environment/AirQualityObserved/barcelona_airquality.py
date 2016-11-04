#!../bin/python
# -*- coding: utf-8 -*-

import datetime
import json
import urllib2
import logging
import re

import sys

AIRQUALITY_TYPE_NAME = 'AirQualityObserved'

FIWARE_SERVICE = 'AirQuality'
FIWARE_SPATH = '/Spain/Barcelona'

MIME_JSON = 'application/json'

# Orion service that will store the data
orion_service = 'http://130.206.83.68:1026'

pollutant_descriptions = {
  'SO2': 'Sulfur Dioxide',
  'CO': 'Carbon Monoxide',
  'NO': 'Nitrogen Monoxide',
  'NO2': 'Nitrogen Dioxide',
  'PM2.5': 'Particles less than 2.5',
  'PM10': 'Particles less than 10',
  'NOx': 'Nitrogen oxides',
  'O3': 'Ozone',
  'TOL': 'Toluene',
  'BEN': 'Benzene',
  'EBE': 'Etilbenzene',
  'MXY': 'Metaxylene',
  'PXY': 'Paraxylene',
  'OXY': 'Orthoxylene',
  'TCH': 'Total Hydrocarbons',
  'CH4': 'Hydrocarbons (Methane)',
  'NHMC': 'Non-methane hydrocarbons (Hexane)'
}

# Station codes of the Barcelona metropolitan area
station_codes = ['08019050', '08015021', '08019044', '08019004', '08019042',
                 '08089005', '08019057', '08019054', '08019043',
                 '08194008', '08169009', '08169008', '08101001',
                 '08245012', '08263007', '08263001', '08211004', '08221004',
                 '08301004']

# Provides air quality station information (probably in the future we are not going to need this call)
dataset_url = 'http://dtes.gencat.cat/icqa/AppJava/getEstacio.do?codiEOI={}'
# Provides per hour data for the current day, per station
dataset_url2 = 'http://dtes.gencat.cat/icqa/AppJava/getDadesDiaries.do?codiEOI={}'

persisted_entities = 0
already_existing_entities = 0
in_error_entities = 0

# Sanitize string to avoid forbidden characters by Orion
def sanitize(str_in):
  return re.sub(r"[<(>)\"\'=;]", "", str_in)

# Retrieves all the data from the target stations    
def get_air_quality_barcelona(target_stations):
  for station in target_stations:
  
    logging.debug('Going to harvest data coming from : %s', station)
    
    service_url1 = dataset_url.format(station)
    
    # Request to obtain station data
    station_req = urllib2.Request(url=service_url1, headers={'Accept': MIME_JSON})
    try: f = urllib2.urlopen(station_req)
    except urllib2.URLError as e:
      logging.error('Error while calling: %s : %s', service_url1, e)
      continue
      
    # deal with wrong encoding
    json_str = f.read().replace("'",'"')
    data = json.loads(json_str,encoding='ISO-8859-15')
    
    service_url2 = dataset_url2.format(station)
    # Request to obtain pollutants data
    data_req = urllib2.Request(url=service_url2, headers={'Accept': MIME_JSON})
    try: f2 = urllib2.urlopen(data_req)
    except urllib2.URLError as e:
      logging.error('Error while calling: %s : %s', service_url2, e)
      continue
    
    logging.debug("All data from %s retrieved properly", station)
    
    # deal with wrong encoding
    json_pollutants_str = f2.read().replace("'",'"')
    pollutant_data_st = json.loads(json_pollutants_str,encoding='ISO-8859-15')
    
    station_code = data['codiEOI']
    
    station_data = {
      'type': AIRQUALITY_TYPE_NAME,
      'stationCode': {
        'value': station_code
      },
      'stationName': {
        'value': sanitize(data['nom'])
      },
      'address': {
        'value' : {
          'addressCountry': 'ES',
          'addressLocality': sanitize(data['municipi']),
          'streetAddress': sanitize(data['direccioPostal'])
        },
        'type': 'PostalAddress'
      },
      'location': {
        'value': {
          'type': 'Point',
          'coordinates': [float(data['longitud']),float(data['latitud'])]
        },
        'type': 'geo:json',
      },
      # Source of the data Generalitat of Catalonia
      'source': {
        'value': 'http://dtes.gencat.cat/',
        'type': 'URL'
      },
      # Provider operator TEF
      'dataProvider': {
        'value': 'TEF'
      }
    }
    
    pollutant_data = pollutant_data_st['contaminants']
    measurands = []
    
    for pollutant_info in pollutant_data.values():
      values = pollutant_info['dadesMesuresDiaria']
      # It comes with units between parenthesis
      pollutant_name = pollutant_info['abreviatura'].split('(')[0]
      pollutant_unit = 'GQ'
      if pollutant_name == 'CO':
        pollutant_unit = 'GP'
        
      # We get last value
      counter = 0
      hour = 0
      for v in values:
        if v['valor'] <> '' and counter < 24:
          value = v['valor']
          hour = counter
        counter = counter + 1
      
      measurand_data = [pollutant_name, value, pollutant_unit, pollutant_descriptions[pollutant_name]]
      measurands.append( ','.join(measurand_data))
    
      station_data[pollutant_name] = {
        'value': float(value)
      }
    
    # 'data' in catalan is 'date' 
    observ_date = datetime.datetime.strptime(pollutant_data_st['data'],'%d/%m/%Y')
    observ_date = observ_date.replace(hour=hour,minute=0,second=0,microsecond=0)
    one_hour_delta = datetime.timedelta(hours=1)
    observ_corrected_date = observ_date + one_hour_delta
    station_data['dateObserved'] = {
      'value': observ_corrected_date.isoformat(),
      'type': 'DateTime'
    }
    station_data['measurand'] = {
      'value': measurands,
      'type': 'List'
    }
    # Convenience data for filtering by target hour
    station_data['hour'] = {
      'value': str(hour) + ':' + '00'
    }
    
    logging.debug("Retrieved data for %s at %s",station_data['stationCode']['value'], station_data['dateObserved']['value'])
    # Entity id corresponds to the observed date starting period
    station_data['id'] = 'Barcelona-AirQualityObserved' + '-' + station_code + '-' + station_data['dateObserved']['value']
    
    post_data(station_data)

  
# POST data to an Orion Context Broker instance using NGSIv2 API
def post_data(data):
  data_as_str = json.dumps(data)
  
  headers = {
    'Content-Type':   MIME_JSON,
    'Content-Length': len(data_as_str),
    'Fiware-Service': FIWARE_SERVICE,
    'Fiware-Servicepath': FIWARE_SPATH
  }
  
  req = urllib2.Request(url=(orion_service + '/v2/entities/'), data=data_as_str, headers=headers)
  
  logging.debug('Going to persist %s to %s', data['id'], orion_service)
  
  try:
    f = urllib2.urlopen(req)
  except urllib2.URLError as e:
    if e.code == 422:
      global already_existing_entities
      logging.debug("Entity already exists: %s", data['id'])
      already_existing_entities = already_existing_entities + 1
    else:
      global in_error_entities
      logging.error('Error while POSTing data to Orion: %d %s', e.code, e.read())
      logging.debug('Data which failed: %s', data_as_str)
      in_error_entities = in_error_entities + 1
  else:
    global persisted_entities
    logging.debug("Entity successfully created: %s", data['id'])
    persisted_entities = persisted_entities + 1
    
    
if __name__ == '__main__':
  logging.basicConfig(filename='harvest.log', level='DEBUG', format='%(levelname)s %(asctime)s %(message)s')
  
  logging.debug('#### Starting a new harvesting and harmonization cycle ... ####')
  logging.debug('Number of air quality stations known: %d', len(station_codes))
  get_air_quality_barcelona(station_codes)
  
  logging.debug('Number of entities persisted: %d', persisted_entities)
  logging.debug('Number of entities already existed: %d', already_existing_entities)
  logging.debug('Number of entities in error: %d', in_error_entities)
  logging.debug('#### Harvesting cycle finished ... ####')

# Provides per hour data for the current day, per station
dataset_url2 = 'http://dtes.gencat.cat/icqa/AppJava/getDadesDiaries.do?codiEOI={}'

persisted_entities = 0
already_existing_entities = 0
in_error_entities = 0

# Sanitize string to avoid forbidden characters by Orion
def sanitize(str_in):
  return re.sub(r"[<(>)\"\'=;]", "", str_in)

# Retrieves all the data from the target stations    
def get_air_quality_barcelona(target_stations):
  for station in target_stations:
  
    logging.debug('Going to harvest data coming from : %s', station)
    
    service_url1 = dataset_url.format(station)
    
    # Request to obtain station data
    station_req = urllib2.Request(url=service_url1, headers={'Accept': MIME_JSON})
    try: f = urllib2.urlopen(station_req)
    except urllib2.URLError as e:
      logging.error('Error while calling: %s : %s', service_url1, e)
      continue
      
    # deal with wrong encoding
    json_str = f.read().replace("'",'"')
    data = json.loads(json_str,encoding='ISO-8859-15')
    
    service_url2 = dataset_url2.format(station)
    # Request to obtain pollutants data
    data_req = urllib2.Request(url=service_url2, headers={'Accept': MIME_JSON})
    try: f2 = urllib2.urlopen(data_req)
    except urllib2.URLError as e:
      logging.error('Error while calling: %s : %s', service_url2, e)
      continue
    
    logging.debug("All data from %s retrieved properly", station)
    
    # deal with wrong encoding
    json_pollutants_str = f2.read().replace("'",'"')
    pollutant_data_st = json.loads(json_pollutants_str,encoding='ISO-8859-15')
    
    station_code = data['codiEOI']
    
    station_data = {
      'type': AIRQUALITY_TYPE_NAME,
      'stationCode': {
        'value': station_code
      },
      'stationName': {
        'value': sanitize(data['nom'])
      },
      'address': {
        'value' : {
          'addressCountry': 'ES',
          'addressLocality': data['municipi'],
          'streetAddress': sanitize(data['direccioPostal'])
        },
        'type': 'PostalAddress'
      },
      'location': {
        'value': {
          'type': 'Point',
          'coordinates': [float(data['longitud']),float(data['latitud'])]
        },
        'type': 'geo:json',
      },
      # Source of the data Generalitat of Catalonia
      'source': {
        'value': 'http://dtes.gencat.cat/',
        'type': 'URL'
      },
      # Provider operator TEF
      'dataProvider': {
        'value': 'TEF'
      }
    }
    
    pollutant_data = pollutant_data_st['contaminants']
    measurands = []
    
    for pollutant_info in pollutant_data.values():
      values = pollutant_info['dadesMesuresDiaria']
      # It comes with units between parenthesis
      pollutant_name = pollutant_info['abreviatura'].split('(')[0]
      pollutant_unit = 'GQ'
      if pollutant_name == 'CO':
        pollutant_unit = 'GP'
        
      # We get last value
      counter = 0
      hour = 0
      for v in values:
        if v['valor'] <> '' and counter < 24:
          value = v['valor']
          hour = counter
        counter = counter + 1
      
      measurand_data = [pollutant_name, value, pollutant_unit, pollutant_descriptions[pollutant_name]]
      measurands.append( ','.join(measurand_data))
    
      station_data[pollutant_name] = {
        'value': float(value)
      }
    
    station_data['dateObserved'] = {
      'value': datetime.datetime.now().replace(hour=hour,minute=0,second=0,microsecond=0).isoformat(),
      'type': 'DateTime'
    }
    station_data['measurand'] = {
      'value': measurands,
      'type': 'List'
    }
    # Convenience data for filtering by target hour
    station_data['hour'] = {
      'value': str(hour) + ':' + '00'
    }
    
    logging.debug("Retrieved data for %s at %s",station_data['stationCode']['value'], station_data['dateObserved']['value'])
    # Entity id corresponds to the observed date starting period
    station_data['id'] = 'Barcelona-AirQualityObserved' + '-' + station_code + '-' + datetime.datetime.now().replace(hour=hour,second=0,minute=0,microsecond=0).isoformat()
    
    post_data(station_data)

  
# POST data to an Orion Context Broker instance using NGSIv2 API
def post_data(data):
  data_as_str = json.dumps(data)
  
  headers = {
    'Content-Type':   MIME_JSON,
    'Content-Length': len(data_as_str),
    'Fiware-Service': FIWARE_SERVICE,
    'Fiware-Servicepath': FIWARE_SPATH
  }
  
  req = urllib2.Request(url=(orion_service + '/v2/entities/'), data=data_as_str, headers=headers)
  
  logging.debug('Going to persist %s to %s', data['id'], orion_service)
  
  try:
    f = urllib2.urlopen(req)
  except urllib2.URLError as e:
    if e.code == 422:
      global already_existing_entities
      logging.debug("Entity already exists: %s", data['id'])
      already_existing_entities = already_existing_entities + 1
    else:
      global in_error_entities
      logging.error('Error while POSTing data to Orion: %d %s', e.code, e.read())
      logging.debug('Data which failed: %s', data_as_str)
      in_error_entities = in_error_entities + 1
  else:
    global persisted_entities
    logging.debug("Entity successfully created: %s", data['id'])
    persisted_entities = persisted_entities + 1
    
    
if __name__ == '__main__':
  logging.basicConfig(filename='barcelona_airquality.log', level='DEBUG', format='%(asctime)s %(message)s')
  
  logging.debug('#### Starting a new harvesting cycle ... ####')
  get_air_quality_barcelona(station_codes)
  
  logging.debug('Number of entities persisted: %d', persisted_entities)
  logging.debug('Number of entities already existed: %d', already_existing_entities)
  logging.debug('Number of entities in error: %d', in_error_entities)
  logging.debug('#### Harvesting cycle finished ... ####')
