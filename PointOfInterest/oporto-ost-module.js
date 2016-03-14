'use strict';

var Orion = require('fiware-orion-client'), 
            OrionHelper = Orion.NgsiHelper;

var Request = require('request');

const OST = 'https://api.ost.pt/ngsi10'
const TYPES = 'contextEntityTypes';
const ENTITIES = 'contextEntities';
const PORTO = '&municipality=806';
const PARAMS = 'key=hackacityporto2015_server';


function getData(type, category, limit, offset, location) {
  return new Promise (function (resolve, reject) {
    var url = OST + '/' + TYPES + '/' + type + '?' + PARAMS + PORTO;
    
    if (category) {
      url += '&category=' + category
    }
    
    if (limit) {
      url += '&limit=' + limit;
    }
    
    if (offset) {
      url += '&offset=' + offset;
    }
    
    if (location) {
      var coords = location.coords.split(',');
      url += '&center=' + coords[1] + ',' + coords[0];
      url += '&range=' + location.radius / 1000;
    }
    
    console.log(url);
    
    Request(url, function (error, response, body) {
      console.log(error, response.statusCode);
      
      if (!error && response.statusCode == 200) {
        var out = OrionHelper.parse(body, {
          GeoJSON: true
        });
        
        console.log(JSON.stringify(out));
        
        if (!Array.isArray(out)) {
          out = [out];
        }
        
        var data = [];
        var byId = Object.create(null);
        out.forEach(function(aElement) {
          var adapted = translate(aElement);
          byId[adapted.id] = adapted;
          data.push(adapted);
        });
        
        resolve({
          data: data,
          byId: byId,
          headers: response.headers['link']
        });
      }
      else {
        console.error('Error while getting list: ',
                        error, response && response.statusCode);
        reject(error);
      }
    });
  });
}

function getEntity(id)  {
  return new Promise(function(resolve, reject) {
    var idTokens = id.split('-');
    if (idTokens.length < 3) {
      reject('malformed id');
      return;
    }
    var entityId = 'poi' + '_' + idTokens[2];
    
    var url = OST + '/' + ENTITIES + '/' +
              entityId + '?' + PARAMS + PORTO;
    
    console.log(url);
    
    Request(url, function (error, response, body) {
      console.log(error, response.statusCode);
      
      if (!error && response.statusCode == 200) {
        var out = OrionHelper.parse('{"contextResponses": [' + body + ']}',{
          GeoJSON: true
        });
        var data = translate(out);
        resolve(data);
      }
      else if (response.statusCode == 404) {
        resolve(null);
      }
      else {
        console.error('Error while getting entityId: ',
                        error, response && response.statusCode);
        reject(error);
      }
    });
  });
}


function translate(aElement) {
  var out = Object.create(null);
  
  out.id = 'porto-poi-' + aElement.id;
  out.type = 'PointOfInterest';
  out.source = 'http://fiware-porto.citibrain.com/docs';
  out.category = Array.isArray(aElement.categories) &&
                  aElement.categories[0];
  out.created = aElement.publication_date ||  new Date();
  out.updated = aElement.last_modified || new Date();
  out.location = aElement.geom_feature;
  out.description = aElement.metadata &&
                    aElement.metadata.description &&
                    aElement.metadata.description.eng &&
                    aElement.metadata.description.eng.replace(/\r\n/g,'');
   
  return out;
}

exports.getData = getData;
exports.getEntity = getEntity;