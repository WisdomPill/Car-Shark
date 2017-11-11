from datetime import datetime

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from trip.models import Trip


class TripView(APIView):
    def get(self, request, format=None):
        response = {
            'departure': {
                'time': datetime(2017, 11, 10, 23, 26, 55),
                'location': {
                    'name': 'trento',
                    'geo_point': {
                        'lat': 235,
                        'lon': 432674
                    }
                }
            },
            'arrival': {
                'time': datetime(2017, 11, 11, 3, 26, 55),
                'location': {
                    'name': 'bolzano',
                    'geo_point': {
                        'lat': 3242,
                        'lon': 79534
                    }
                }
            },
            'checkpoints': [
                {
                    'action': 'pick up',
                    'location': {
                        'name': 'san michele',
                        'geo_point': {
                            'lat': 3242,
                            'lon': 79534
                        }
                    }
                },
                {
                    'action': 'drop',
                    'location': {
                        'name': 'lives',
                        'geo_point': {
                            'lat': 3242,
                            'lon': 79534
                        }
                    }
                }
            ]
        }
        return Response(response, HTTP_200_OK)

class TripListView(APIView):
    def get(self, request, format=None):
        s = Trip.search()

        response = s.execute()
        hits = response.hits
        return Response(response, HTTP_200_OK)
