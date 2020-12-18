#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:
    
'''

# Import necessary modules
from constants_file_size_type import FileSizeType
from constants_priority_image_type import ImagePriorityImageType
from enum import Enum

def convert_to_bytes(size, max_file_size_type):
    if size:
        if max_file_size_type == FileSizeType.kB:
            return size * 1024
        elif max_file_size_type == FileSizeType.MB:
            return size * 1024 * 1024
    return size

def get_image_type(image_type):
    if isinstance(image_type, ImagePriorityImageType):
        return image_type
    if isinstance(image_type, Enum):
        return ImagePriorityImageType.generate(image_type.name)
    return ImagePriorityImageType.generate(image_type)