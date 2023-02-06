#!/bin/env python3

import yaml
import os

huc12_ids_str = os.environ['param_huc12_id']
huc12_ids_list = huc12_ids_str.split(',')

connector_dict = {'$1': {'Input': {'CUAHSISubsetterInput': {'huc12_id':huc12_ids_list}}}}

with open('/job/executable/cuahsisubsetterinput.yml','w') as subsetterfile:
    yaml.dump(connector_dict,subsetterfile)
