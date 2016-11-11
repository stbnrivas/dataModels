#!../bin/python
# -*- coding: utf-8 -*-

import csv
import datetime
import json
import urllib2
import StringIO
import logging


AMBIENT_TYPE_NAME = 'AirQualityObserved'

# List of known air quality stations
station_dict = { }

MIME_JSON = 'application/json'

# Orion service that will store the data
orion_service = 'http://130.206.83.68:1026'

pollutant_dict = {
  '01': 'SO2',
  '06': 'CO',
  '07': 'NO',
  '08': 'NO2',
  '09': 'PM2.5',
  '10': 'PM10',
  '12': 'NOx',
  '14': 'O3',
  '20': 'TOL',
  '30': 'BEN',
  '35': 'EBE',
  '37': 'MXY',
  '38': 'PXY',
  '39': 'OXY',
  '42': 'TCH',
  '43': 'CH4',
  '44': 'NHMC'
}

pollutant_descriptions = {
  '01': 'Sulfur Dioxide',
  '06': 'Carbon Monoxide',
  '07': 'Nitrogen Monoxide',
  '08': 'Nitrogen Dioxide',
  '09': 'Particles < 2.5',
  '10': 'Particles < 10',
  '12': 'Nitrogen oxides',
  '14': 'Ozone',
  '20': 'Toluene',
  '30': 'Benzene',
  '35': 'Etilbenzene',
  '37': 'Metaxylene',
  '38': 'Paraxylene',
  '39': 'Orthoxylene',
  '42': 'Total Hydrocarbons',
  '43': 'Hydrocarbons (Methane)',
  '44': 'Non-methane hydrocarbons (Hexane)'
}

other_dict = {
  '80': 'ultravioletRadiation',
  '81': 'windSpeed',
  '82': 'windDirection',
  '83': 'temperature',
  '86': 'relativeHumidity',
  '87': 'barometricPressure',
  '88': 'solarRadiation',
  '89': 'precipitation',
  '92': 'acidRainLevel'
}

other_descriptions = {
  '80': 'Ultraviolet Radiation',
  '81': 'Wind Speed',
  '82': 'Wind Direction',
  '83': 'temperature',
  '86': 'Relative Humidity',
  '87': 'Barometric Pressure',
  '88': 'Solar Radiation',
  '89': 'Precipitation',
  '92': 'Acid Rain Level'
}

dataset_url = 'http://datos.madrid.es/egob/catalogo/212531-7916318-calidad-aire-tiempo-real.txt'

# Statistics for tracking purposes
persisted_entities = 0
already_existing_entities = 0
in_error_entities = 0

FIWARE_SERVICE = 'AirQuality'
FIWARE_SPATH =   '/Spain/Madrid'
    
def get_air_quality_madrid(target_hour=-1):
  req = urllib2.Request(url=dataset_url)
  f = urllib2.urlopen(req)
  
  csv_data = f.read()
  csv_file = StringIO.StringIO(csv_data)
  reader = csv.reader(csv_file, delimiter=',')
  
  # Dictionary with station data indexed by station code
  # An array per station code containing one element per hour
  stations = { }
  
  for row in reader:
    station_code = str(row[0]) + str(row[1]) + str(row[2])
    
    station_num = row[2]
    if not station_dict[station_num]:
      continue
    
    if not station_code in stations:
      stations[station_code] = []
    
    magnitude = row[3]
            
    if (not magnitude in pollutant_dict) and (not magnitude in other_dict):
      continue
    
    is_other = None
    if magnitude in pollutant_dict:
      property_name = pollutant_dict[magnitude]
      property_desc = pollutant_descriptions[magnitude]
      is_other = False
   
    if magnitude in other_dict:
      property_name = other_dict[magnitude]
      property_desc = other_descriptions[magnitude]
      is_other = True
      
    hour = 0
    
    for x in xrange(9, 57, 2):
      if len(stations[station_code]) < hour + 1:
        stations[station_code].append(build_station(station_num, station_code, hour, row))
        
      value = row[x]
      value_control = row[x + 1]
    
      if value_control == 'V':  
        param_value = float(value)
          
        if not is_other:
          unit_code = 'GQ'
          if property_name == 'CO':
            unit_code = 'GP'
          
          measurand_data = [property_name, str(param_value), unit_code, property_desc]
          stations[station_code][hour]['measurand']['value'].append(','.join(measurand_data))
        else:
          stations[station_code][hour][property_name] = param_value
    
      hour += 1

  
  # Returning data as an array
  station_list = []
  
  for station in stations:
    station_data = stations[station]
    index_from = 0
    index_to = len(station_data)
    if target_hour <> -1:
     index_from = target_hour
     index_to = index_from + 1
      
    data_list = station_data[index_from:index_to]
    
    for data in data_list:  
      if data['measurand'] or 'temperature' in data:
        station_list.append(data)
  
  print json.dumps(station_list)      
  # logging.debug(json.dumps(station_list))

# Buils a new entity of type AirQualityObserved
def build_station(station_num, station_code, hour, row):
  station_data = {
    'type': AMBIENT_TYPE_NAME,
    'measurand': {
      'type': 'List',
      'value': []
    },
    'stationCode': {
      'value': station_code
    },
    'stationName': {
      'value': station_dict[station_num]['name']
    },
    'address': {
      'type': 'PostalAddress',
      'value': {
        'addressCountry': 'ES',
        'addressLocality': 'Madrid',
        'streetAddress': station_dict[station_num]['address']  
      }
    },
    'location': {
      'type': 'geo:json',
      'value': station_dict[station_num]['location']['value'] or None
    },
    'source': {
      'type': 'URL',
      'value': 'http://datos.madrid.es'
    }
  }
  valid_from = datetime.datetime(int(row[6]), int(row[7]), int(row[8]), hour)
  valid_to = (valid_from + datetime.timedelta(hours=1))

  station_data['validity'] = {
    'value': {
      'from': valid_from.isoformat(),
      'to': valid_to.isoformat()  
    },
    'type': 'StructuredValue'
  }
  
  station_data['hour'] = {
    'value': str(hour) + ':' + '00' 
  }
  
  # Correction of 1 hour in order to deal with CB bug with timezones
  one_hour_delta = datetime.timedelta(hours=1)
  observ_corrected_date = valid_from - one_hour_delta
  station_data['dateObserved'] = {
    'type': 'DateTime',
    'value': observ_corrected_date.isoformat() 
  } 
    
  station_data['id'] = 'Madrid-AmbientObserved-' + station_code + '-' + valid_from.isoformat()
    
  return station_data

# Reads station data from CSV file
def read_station_csv():
  with open('madrid_airquality_stations.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    index = 0
    for row in reader:
      if index <> 0:
        station_code = row[2]
        station_name = row[3]
        station_address = row[4]
        station_coords = {
          'type': 'geo:json',
          'value': {
            'type': 'Point',
            'coordinates': [float(row[0]), float(row[1])]
          } 
        }
        
        station_dict[station_code.zfill(3)] = {
          'name': station_name,
          'address': station_address,
          'location': station_coords
        }
      index += 1
     
    station_dict['099'] = {
      'name': 'average',
      'address': None,
      'location': None
    }
    
      
if __name__ == '__main__':
  read_station_csv()
  
  logging.basicConfig(filename='harvest_madrid.log', level='DEBUG', format='%(levelname)s %(asctime)s %(message)s')
  
  logging.debug('#### Starting a new harvesting and harmonization cycle ... ####')
  logging.debug('Number of air quality stations known: %d', len(station_dict.keys()))
  get_air_quality_madrid()
  
  logging.debug('Number of entities persisted: %d', persisted_entities)
  logging.debug('Number of entities already existed: %d', already_existing_entities)
  logging.debug('Number of entities in error: %d', in_error_entities)
  logging.debug('#### Harvesting cycle finished ... ####')

  
