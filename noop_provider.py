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
from base_image_processing_optimize_process import BaseImageProcessingOptimizeProcess

class NoOpProvider(BaseImageProcessingOptimizeProcess):
    def __init__(self, image_processor_image_format, image):
        super(NoOpProvider, self).__init__(image_processor_image_format, image)

    def optimize(self):
        return self.image.make_blob()