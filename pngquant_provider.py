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
import pngquant

from base_image_processing_optimize_process import BaseImageProcessingOptimizeProcess
from helpers import convert_to_bytes

class PNGQuantProvider(BaseImageProcessingOptimizeProcess):
    def __init__(self, image_processor_image_format, image):
        super(PNGQuantProvider, self).__init__(image_processor_image_format, image)
    def optimize(self):

        image_blob = self.image.make_blob()

        # Should only optimize if needed, to avoid loss of quality
        max_size = self.image_processor_image_format.max_file_size
        measure_type = self.image_processor_image_format.max_file_size_type

        current_file_size = len(image_blob)
        max_file_size = convert_to_bytes(max_size, measure_type)

        if not max_size or max_size == 0 or current_file_size <= max_file_size:
            return image_blob

        pngquant.config(min_quality=65, max_quality=90)
        compression, blob = pngquant.quant_data(image_blob)

        return blob 