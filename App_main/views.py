from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import generics
from .models import SoftwarePackage, Booking
from .serializers import SoftwarePackageSerializer, BookingCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from App_login.models import ProfileMOdel
import json


# Create your views here.
class SoftwarePackageList(generics.ListCreateAPIView):
    queryset = SoftwarePackage.objects.all()
    serializer_class = SoftwarePackageSerializer


class SoftwarePackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoftwarePackage.objects.all()
    serializer_class = SoftwarePackageSerializer


class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()

    def post(self, request):
        packageID = request.data['package']
        company_name = request.data['company_name']
        phone_number = request.data['phone_number']
        address = request.data['address']
        try:
            linkedIn = request.data['linkedIn']
        except:
            linkedIn = ""
        country = request.data['country']
        user = request.user
        profile_find = ProfileMOdel.objects.filter(profileUser=user)
        if not profile_find.exists():
            profile = ProfileMOdel(
                profileUser=user,
                company_name=company_name,
                phone_number=phone_number,
                address=address,
                linkedIn=linkedIn,
                country=country,
            )
            profile.save()
        else:
            profile = profile_find[0]
            if profile.company_name != company_name:
                profile.company_name = company_name
            if profile.phone_number != phone_number:
                profile.phone_number = phone_number
            if profile.address != address:
                profile.address = address
            if profile.linkedIn != linkedIn:
                profile.linkedIn = linkedIn
            if profile.country != country:
                profile.country = country
            profile.save()

        package = SoftwarePackage.objects.get(id=packageID)
        booking = Booking.objects.create(package=package, user=user)
        return Response({"success": "booked"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    profile_find = ProfileMOdel.objects.filter(profileUser=request.user)
    if profile_find.exists():
        profile = profile_find[0]
        profile_dict = {'company_name': profile.company_name,
                        'phone_number': profile.phone_number,
                        'address': profile.address,
                        'linkedIn': profile.linkedIn,
                        'country': profile.country}
        profile_json = json.dumps(profile_dict)
        return Response(profile_dict, status=status.HTTP_200_OK)


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer


class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Thank you so much. We will contact you soon."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
