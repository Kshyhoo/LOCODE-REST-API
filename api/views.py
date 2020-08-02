from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer
from .models import Location
from api.serializers import LocationSerializer

from bs4 import BeautifulSoup as bs
import requests
import zipfile

DOMAIN = 'http://www.unece.org'
URL = 'http://www.unece.org/cefact/codesfortrade/codes_index.html'
FILETYPE = 'csv'


def get_file(url):
    return bs(requests.get(url).text, 'html.parser')


for link in get_file(URL).find_all('a', class_='download'):
    file_link = link.get('href')
    if FILETYPE in file_link:
        print(file_link)
        response = requests.get(DOMAIN + file_link)
        filename = 'locodes.rar'
        with open(filename, 'wb') as file:
            file.write(response.content)

with zipfile.ZipFile('./locodes.rar', 'r') as my_zip:
    my_zip.extractall()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
