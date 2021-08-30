from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UrlViewClass


urlpatterns = [
    path('urls/', UrlViewClass.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
