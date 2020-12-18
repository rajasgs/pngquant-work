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
from pngquant_provider import PNGQuantProvider
from priority_image_type import ImagePriorityImageType
from noop_provider import NoOpProvider

def create_instance(image_type, image_processor_image_format, image, allow_quality_shift=False):
    
    if image_type == ImagePriorityImageType.PNG_TRANSPARENT:
        return PNGQuantProvider(image_processor_image_format, image)

    if image_type == ImagePriorityImageType.PNG_WHITE:
        return PNGQuantProvider(image_processor_image_format, image)

    return NoOpProvider(image_processor_image_format, image)