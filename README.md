# A CyberGIS Compute Model for Executing the CUAHSISubsetterInput GeoEDF Connector

This repo implements a model for executing a GeoEDF connector via CyberGIS-Compute V2. 

## mainfest.json

Supported HPCs are listed by key "supported_hpc" and default HPC by key "default_hpc";

The key "pre_processing_stage", "execution_stage" and "post_processing_stage" specify the commands (and scripts) to run in preprocessing, model execution and postprocessing stages;

The key "container" lists the singularity GeoEDF container to use on HPC (placed on HPC already);

## create_connector_yml.py

This script creates a GeoEDF workflow YML file using the parameter values for the connector's parameters. These parameters are defined in the manifest for the model to be prompted for user input in the CyberGIS Compute UI.

## main.sh

This script is called inside the Singularity connector container. It runs the primary workflow execution script *run-workflow-stage.sh* that is provided by the GeoEDF workflow framework. 
The workflow YML file containing the connector instance is specified as an environment variable (CyberGIS Compute parameter), all other parameters need to be hardcoded in the main.sh script.

## transfer_shared_outputs.sh

This script is responsible for transferring the outputs for this connector from the HPC scratch folder to a shared folder for use in subsequent compute jobs.
