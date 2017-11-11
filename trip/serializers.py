from rest_framework.serializers import ModelSerializer

from trip.models import Dummy


class DummySerializer(ModelSerializer):
    class Meta:
        model = Dummy
        fields = '__all__'
