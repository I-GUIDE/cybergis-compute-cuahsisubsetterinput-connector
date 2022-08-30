#!/bin/bash

mkdir /compute_shared/${job_id}

cd ${result_folder}

cp *.nc /compute_shared/${job_id}/
