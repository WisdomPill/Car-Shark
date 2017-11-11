from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from trip.models import Dummy
from trip.serializers import DummySerializer


class RideRequest(TemplateView):
    template_name = 'trip/request_ride.html'


class RideLoading(TemplateView):
    template_name = 'trip/loading.html'


class RideSuggestion(TemplateView):
    template_name = 'trip/suggestion_ride.html'


class DummyView(APIView):
    def get(self, request, format=None):
        serializer = self.get_first_dummy()
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, format=None):
        change_dummy('asked')
        serializer = self.get_first_dummy()
        return Response(serializer.data, status=HTTP_200_OK)

    def get_first_dummy(self):
        dummy = Dummy.objects.first()
        serializer = DummySerializer(dummy)
        return serializer

    def put(self, request, format=None):
        change_dummy('answered')
        serializer = self.get_first_dummy()
        return Response(serializer.data, status=HTTP_200_OK)

    def delete(self, request, format=None):
        change_dummy('')
        serializer = self.get_first_dummy()
        return Response(serializer.data, status=HTTP_200_OK)


def change_dummy(verb):
    dummy = Dummy.objects.first()
    dummy.verb = verb
    dummy.save()
