#!../bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement
import sys
import os
import xml.dom.minidom
import json
import re
import hashlib
import urllib2
import contextlib

DEFAULT_SOURCE_FOLDER =       'INECO'
BEACH_FOLDER =                '20170303_muestra_playas'
MUSEUM_FOLDER =               '20170303_muestra_museos'
TOURIST_INFO_FOLDER =         '20170303_muestra_oficina_turismo'

folders = [BEACH_FOLDER, MUSEUM_FOLDER, TOURIST_INFO_FOLDER]

categories_values = ['113', '311', '439']
categories_names = ['Beach', 'Museum', 'TouristInformationCenter']
 
# Orion service that will store the data
orion_service = 'http://localhost:1030'

FIWARE_SERVICE = 'POI'
FIWARE_SPATH   = '/Spain'

MIME_JSON = 'application/json'

# Dictionary containing all the POIs
pois = { }

persisted_entities = 0
in_error_entities = 0

# Sanitize string to avoid forbidden characters by Orion
def sanitize(str_in):
  return re.sub(r"[<(>)\"\'=;]", "", str_in)

def transform_data(source_folder_param):
  index_poi_type = 0
  
  source_folder = source_folder_param
  if source_folder is None:
    source_folder = DEFAULT_SOURCE_FOLDER
  
  for folder in folders:
    folder = os.path.join(source_folder, folder)
    
    files = os.listdir(folder)
    
    num_processed = 0
    
    poi_list = []
    pois[categories_names[index_poi_type]] = poi_list
    
    for a_file in files:
      full_file_path = os.path.join(folder, a_file)
      f = open(full_file_path, 'r')
      xml_data = f.read()
      f.close()
        
      DOMTree = xml.dom.minidom.parseString(xml_data).documentElement
      
      try:
        name = sanitize(DOMTree.getElementsByTagName('nombre')[1].firstChild.nodeValue)
        longitude = float(DOMTree.getElementsByTagName('longitud')[0].firstChild.nodeValue)
        latitude = float(DOMTree.getElementsByTagName('latitud')[0].firstChild.nodeValue)
      except:
        num_processed += 1
        continue
      
      municipality = sanitize(DOMTree.getElementsByTagName('municipio')[0].firstChild.nodeValue)
      province = sanitize(DOMTree.getElementsByTagName('provincia')[0].firstChild.nodeValue)
      
      description_nodes = DOMTree.getElementsByTagName('descripcion')
      found = False
      for node in description_nodes:
        if found is True:
          break
        content_nodes = node.getElementsByTagName('content')
        for content_node in content_nodes:
          if content_node.firstChild != None and content_node.firstChild.nodeValue != None:
            description = sanitize(content_node.firstChild.nodeValue)
            found = True
            break
      
      id_input = categories_names[index_poi_type] + '-' + a_file + '-' + str(num_processed)
      m = hashlib.md5()
      m.update(id_input.decode())
            
      poi_entity = {
        'id': categories_names[index_poi_type] + '-' + m.hexdigest(),
        'type': 'PointOfInterest',
        'name': {
          'value': name
        },
        'description': {
          'value': description
        },
        'category': {
          'type': 'List',
          'value': [
            categories_values[index_poi_type]
        ]},
        'location': {
          'type': 'geo:json',
          'value': {
            'type': 'Point',
            'coordinates': [longitude, latitude]
          }
        },
        'address': {
          'type': 'PostalAddress',
          'value': {
            'addressRegion': province,
            'addressLocality': municipality,
            'addressCountry': 'ES'
          }
        },
        'source': {
          'type': 'URL',
          'value': 'http://www.tourspain.es'
        },
        'dataProvider': {
          'value': 'FIWARE Foundation e.V.'
        }
      }
      
      poi_list.append(poi_entity)
      
      num_processed += 1
      
    index_poi_type += 1


def import_data():
  for poi_type in pois:
    poi_list = pois[poi_type]
    
    print poi_type, len(poi_list)
    
    post_data(poi_list)


# POST data to an Orion Context Broker instance using NGSIv2 API
def post_data(data):
  if len(data) == 0:
    return
  
  payload = {
    'actionType': 'APPEND',
    'entities': data
  }
  
  data_as_str = json.dumps(payload)
  
  headers = {
    'Content-Type':   MIME_JSON,
    'Content-Length': len(data_as_str),
    'Fiware-Service': FIWARE_SERVICE,
    'Fiware-Servicepath': FIWARE_SPATH
  }
  
  req = urllib2.Request(url=(orion_service + '/v2/op/update'), data=data_as_str, headers=headers)
  
  try:
    with contextlib.closing(urllib2.urlopen(req)) as f:
      global persisted_entities
      persisted_entities = persisted_entities + 1
  except urllib2.URLError as e:
    global in_error_entities
    in_error_entities = in_error_entities + 1     



if __name__ == '__main__':
  transform_data(sys.argv[1])
  import_data()
  
  print "Persisted entities: ", persisted_entities
  print "In error entities: ", in_error_entities
