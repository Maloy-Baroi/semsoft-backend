from django.urls import path
from .views import ContactView, SoftwarePackageList, SoftwarePackageDetail, BookingCreateView, BookingDetail, get_profile

app_name = 'App_main'

urlpatterns = [
    path('software-packages/', SoftwarePackageList.as_view()),
    path('software-packages/<int:pk>/', SoftwarePackageDetail.as_view()),
    path('bookings/', BookingCreateView.as_view()),
    path('bookings/<int:pk>/', BookingDetail.as_view()),
    path('contact-us/', ContactView.as_view(), name='contact'),
    path('get-profile/', get_profile, name='get-profile'),
]

