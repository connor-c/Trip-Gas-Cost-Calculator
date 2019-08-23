import json
import urllib.request, urllib.parse

def get_response(url):
    response = None
    try:
        response = urllib.request.urlopen(url)
        return json.load(response)
    finally:
        if response is not None:
            response.close()


def get_distance(origin_address, destination_address):
    distance = get_response('http://open.mapquestapi.com/directions/v2/route?'
                            + urllib.parse.urlencode([('key', ''),
                            ('from', origin_address), ('to', destination_address)]))['route']['distance']
    return distance
