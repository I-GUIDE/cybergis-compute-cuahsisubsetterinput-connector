#!/bin/env python3

import yaml
import os

connector_dict = {'$1': {'Input': {'CUAHSISubsetterInput': {'huc12_id':os.environ['param_huc12_id']}}}}

with open('/job/executable/cuahsisubsetterinput.yml','w') as subsetterfile:
    yaml.dump(connector_dict,subsetterfile)
