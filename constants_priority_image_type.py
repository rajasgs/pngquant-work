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
from enum import Enum


class ImagePriorityImageType(Enum):
    JPEG_LOW = 'JPEG_LOW'
    JPEG_MEDIUM = 'JPEG_MEDIUM'
    JPEG_HIGH = 'JPEG_HIGH'
    PNG_WHITE = 'PNG_WHITE'
    PNG_TRANSPARENT = 'PNG_TRANSPARENT'
    TIFF = 'TIFF'

    @staticmethod
    def generate(image_type):
        if image_type == 'JPEG_LOW':
            return ImagePriorityImageType.JPEG_LOW
        if image_type == 'JPEG_MEDIUM':
            return ImagePriorityImageType.JPEG_MEDIUM
        if image_type == 'JPEG_HIGH':
            return ImagePriorityImageType.JPEG_HIGH
        if image_type == 'PNG_WHITE':
            return ImagePriorityImageType.PNG_WHITE
        if image_type == 'PNG_TRANSPARENT':
            return ImagePriorityImageType.PNG_TRANSPARENT
        if image_type == 'TIFF':
            return ImagePriorityImageType.TIFF
        return ImagePriorityImageType.JPEG_LOW
