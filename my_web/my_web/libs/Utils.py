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
    if not os.path.exists(dir):
        os.mkdir(dir)

    absolute_path = '/md/%s/' % tag + name
    path = dir + name

    with open(path,'w+') as f:
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


class Pagination(object):
    # pagination = {
    #     'objs': objs,  # 需要显示model数据
    #     'all_obj_counts': all_obj_counts,  # 一共多少行数据
    #     'start_pos': start_pos,  # 数据分页开始的数据
    #     'end_pos': end_pos,  # 数据分页结束的数据
    #     'all_page': all_page,  # 一共有多少页
    #     'cur_page': cur_page,  # 当前的页码
    #     'pre_page': pre_page,  # 上一页的页码
    #     'next_page': next_page,  # 下一页的页码
    #     'page_items': page_items, 能点击的页数
    #         'start_page_omit_symbol': start_page_omit_symbol,  # 开始的省略号
    #                                   'end_page_omit_symbol': end_page_omit_symbol,  # 结束的省略号
    # }

    @classmethod
    def pagination(self,all_obj_counts=0,page_count=10,cur_page=2,show_page_item=5):
        num = 0
        all_page = 0
        if all_obj_counts != 0:
            all_page, num = divmod(all_obj_counts, page_count)
        if num > 0:
            all_page += 1
        cur_page = 1 if cur_page < 1 else cur_page
        cur_page = all_page if cur_page > all_page else cur_page

        pre_page = cur_page - 1
        pre_page = 1 if pre_page < 1 else pre_page

        next_page = cur_page + 1
        next_page = all_page if next_page > all_page else next_page

        start_page = int(cur_page - show_page_item / 2)
        if start_page > all_page - show_page_item:
            start_page = all_page - show_page_item + 1
        start_page = 1 if start_page < 1 else start_page

        end_page = int(cur_page + show_page_item / 2)
        end_page = all_page if end_page > all_page else end_page
        if end_page < show_page_item and all_page > show_page_item:
            end_page = show_page_item

        page_items = range(start_page, end_page + 1)

        pagination = {
            'all_obj_counts': all_obj_counts,
            'all_page': all_page,
            'cur_page': cur_page,
            'pre_page': pre_page,
            'next_page': next_page,
            'page_items': page_items,
        }
        return pagination

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