from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.finders import BaseStorageFinder
from django.conf import settings


class StaticFinder(BaseStorageFinder):
    """
    Forces Django to use STATIC_ROOT for serving static files.
    
    http://stackoverflow.com/a/5964786
    """
    storage = FileSystemStorage(settings.STATIC_ROOT, settings.STATIC_URL)