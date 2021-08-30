from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .parser import parser
from .models import Url
from .serializers import UrlSerializer
import requests


class UrlViewClass(ListCreateAPIView):
    """Url view class"""
    serializer_class = UrlSerializer
    queryset = Url.objects.all()

    def create(self, request, *args, **kwargs):
        """New create method. Saving new url and give it to parser"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        context = parser(request.data['url'])
        return context

    def post(self, request, *args, **kwargs):
        """New post method. Trying send GET request to new url"""
        url_id = request.data['url']
        if request.data['url'].isdigit():
            try:
                current_url = Url.objects.get(id=url_id)
                context = parser(current_url.url)
            except Url.DoesNotExist:
                context = {
                    'error': 'this id does not exist',
                }
            return Response(context, status=status.HTTP_200_OK)
        else:
            try:
                r = requests.get(request.data['url'])
                r.raise_for_status()
            except (requests.HTTPError, requests.exceptions.MissingSchema):
                context = {
                    'error': 'Could\'t connect to your url, plz check it'
                }
                return Response(context, status=status.HTTP_200_OK)
            except requests.exceptions.ConnectionError:
                context = {
                    'error': 'Connection to your url refused, too often'
                }
                return Response(context, status=status.HTTP_200_OK)
            context = self.create(request, *args, **kwargs)
            return Response(context, status=status.HTTP_200_OK)
