from guest.models import Guest
from rest_framework import serializers


class Guestserializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Guest