from rest_framework import status as status_codes
from geopy.geocoders import Nominatim
from math import radians, cos, sin, asin, sqrt
import sys

class NearestCityService():

    const_location = {
        "del": "Delhi",
        "mum": "Mumbai",
        "blr": "Bangalore",
        "hyd": "Hyderabad",
        "jpr": "Jaipur",
        "pne": "Pune",
        "ngr": "Nagpur",
        "srt": "Surat",
        "asr": "Amritsar",
        "chn": "Chennai",
        "jdpr": "Jodhpur",
        "cgrh": "Chandigarh",
        "goa": "Goa",
        "nsk": "Nashik",
        "adb": "Ahmedabad",
        "indb": "Indore",
        "mert": "Meerut",
        "ludh": "Ludhiana",
        "jldh": "Jhalandar",
        "lknw": "Lucknow",
        "knpr": "Kanpur",
        "rjkt": "Rajkot",
        "udpr": "Udaipur",
        "bknr": "Bikaner",
        "ptn": "Patna",
        "ripr": "Raipur",
        "rnch": "Ranchi",
        "bvnshr": "Bhubaneswar",
        "drdn": "Dehradun",
        "shmla": "Shimla",
        "klkta": "Kolkata",
        "asansl": "Asansol",
        "guwht": "Guwahati",
        "silgri": "Siliguri",
        "vrnsi": "Varanasi",
        "jmmu": "Jammu",
        "kshmr": "Kashmir",
        "ajmr" : "Ajmer",
        "pshkr" : "Pushkar",
        "kta" : "Kota",
        "vadodara": "Vadodara",
        "jamshedpur": "Jamshedpur",
        "agra": "Agra",
        "kerala": "Kerala",
        "nainital": "Nainitaal",
        "northeast": "Northeast",
        "dehradoon": "Dehradoon",
        "tripura": "Tripura",
        "nagaland": "Nagaland",
        "arunachal": "Arunachal Pradesh",
        "shillong": "Shillong",
        "mizoram": "Mizoram",
        "manipur": "Manipur",
        "bhopal": "Bhopal",
        "cuttack": "Cuttack",
        "jamshedpur": "Jamshedpur",
        "vadodra": "Vadodra",
        "vishakhapatnam": "Vishakhapatnam",
        "vijayawada": "Vijayawada",
        "madurai": "Madurai",
        "coimbatore": "Coimbatore",
        "haldwani": "Haldwani",
        "poducherry": "Poducherry",
        "jabalpur": "Jabalpur"
    }

    def haversine(lat1, lon1, lat2, lon2):

      R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km

      dLat = lat2 - lat1
      dLon = lon2 - lon1
      

      a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
      c = 2*asin(sqrt(a))

      return R * c


    def get_nearest_city_by_distance(self, data) -> dict:

        print(type(data))

        geolocator = Nominatim(user_agent="Your_Name")

        min_distance = sys.maxsize
        min_key = None
        min_value = None
        


        for key, value in self.const_location.items():
            location = geolocator.geocode(value)
            print(location)
            print(type(location))
            if(location != None):
                new_distance = NearestCityService.haversine(location.latitude, location.longitude, radians(data['latitude']), radians(data['longitude']))
                if(new_distance < min_distance):
                    min_distance = new_distance
                    min_key = key
                    min_value = value

        response = {
            'success': True,
            'nearest_city ': {
                min_key : min_value
            }
        }

        return response


