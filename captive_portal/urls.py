from django.contrib import admin
from django.urls import path, include
from user_auth import urls as u_auth_urls
from two_factor.urls import urlpatterns as tf_urls
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(u_auth_urls)),
    path('', include(tf_urls)),
    path('', include(tf_twilio_urls)),
]
