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

class BaseImageProcessingOptimizeProcess(object):
    def __init__(self, image_processor_image_format, image):
        self.image_processor_image_format = image_processor_image_format
        self.image = image

    def optimize(self):
        raise NotImplementedError()