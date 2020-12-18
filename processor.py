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
from wand.image import Image
from wand.color import Color

import optimize_factory
from helpers import get_image_type
from constants_priority_image_type import ImagePriorityImageType

def customize_image(
    headers,

    target_image_type,

    # Image Blob
    content=None
):

    image_type = get_image_type(target_image_type)

    # resizing it accordingly
    with Image(blob=content) as img:
        if image_type != ImagePriorityImageType.PNG_TRANSPARENT:
            img.alpha_channel = 'background'
            img.background_color = Color('white')
        image_blob = resize_factory.create_instance(image_processor_image_format, img).resize()

    # Change DPI, quality, format and add white border if needed
    with Image(blob=image_blob) as img:

        # Handle Optimization processes
        blob_result = optimize_factory.create_instance(
            image_type,
            image_processor_image_format,
            img,
            allow_quality_shift=allow_quality_shift
        ).optimize()

    return blob_result, headers