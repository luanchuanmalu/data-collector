# -*- coding: utf-8 -*-

'''
Created on 2015��9��23��

@author: Yang
'''

# flake8: noqa
from qiniu import Auth
from qiniu import put_file

import qiniu.config

def uploadfile():
    access_key = 'rMcfYHy4t1E18QHa_JcLp59Yjv3WAJgqS5HakDZe'
    secret_key = '4I7EoHMdXpNlNj4p5aALF60tBJISZsXI8dtQzL99'
    bucket_name = '...'
    q = Auth(access_key, secret_key)
    mime_type = "text/plain"
    
    params = {'x:a': 'a'}
    localfile = '.../.../...'
    key = 'big'
    token = q.upload_token(bucket_name, key)
    progress_handler = lambda progress, total: progress
    ret, info = put_file(token, key, localfile, params, mime_type, progress_handler=progress_handler)
    print(info)
    assert ret['key'] == key
    
if __name__ == '__main__':
    pass