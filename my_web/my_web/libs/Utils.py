import hashlib

from django.conf import settings
from django.core.files.storage import FileSystemStorage,Storage
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage,FileSystemStorage
from django.core.files import File

import os

def save_md(content, name,tag):
    name = name + '.md'
    file = ContentFile(content,name)
    dir = settings.MEDIA_ROOT+'/md/%s/' % tag
    os.mkdir(dir)
    absolute_path = '/md/%s/' % tag + name
    path = dir + name

    with open(path,'a+') as f:
        file = File(f)
        file.write(content)
    return absolute_path

def read_md(path):
    path = settings.MEDIA_ROOT + path
    contents=[]
    with open(path,'r+') as f:
        for line in f:
            contents.append(line)
    content = "".join(contents)
    return content






class MDStorage(Storage):

    def __init__(self, option=None):
        if not option:
            pass

    def open(self, name, mode='rb'):
        pass

    def save(self, name, content, max_length=None):
        pass

    def path(self, name):
        pass

    def delete(self, name):
        pass

    def exists(self, name):
        pass

    def listdir(self, path):
        pass

    def size(self, name):
        pass

    def url(self, name):
        pass

    def get_valid_name(self, name):
        pass

    def get_available_name(self, name, max_length=None):
        pass

#get ip
def getIPFromDJangoRequest(self, request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        return request.META['REMOTE_ADDR']