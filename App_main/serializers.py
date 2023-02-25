from rest_framework import serializers
from .models import Contact, SoftwarePackage, Booking
from App_login.models import ProfileMOdel
import json


class SoftwarePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwarePackage
        fields = '__all__'


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['package']

    def create(self, validated_data):
        packageID = validated_data['package']
        company_name = validated_data['company_name']
        phone_number = validated_data['phone_number']
        address = validated_data['address']
        try:
            linkedIn = validated_data['linkedIn']
        except:
            linkedIn = ""
        country = validated_data['country']
        user = self.context['request'].user
        profile = ProfileMOdel.objects.create(
            profileUser = user,
            company_name = company_name,
            phone_number = phone_number,
            address = address,
            linkedIn = linkedIn,
            country = country,
        )
        booking = Booking.objects.create(package=packageID, user=user)
        return json.dumps({"success": "booked"})


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
