# StockAnalyzer

# Virtual Environment
$ bash venv_stock

This will activate your virtual environment for the stock analysis project.

# DataPipeline Directory
## Data Ingestion
This directory is where all the data ingestion processes will happen. This includes external API's, manual uploads of data and any other ingress into the system.

## Data Transformation
This directory is where all the data transformation/processing will happen.

## Data Orchestration
This direcotry is responsible for handling all of the orchestration of the data. Processes will rely on logic within this directory retrieve data for the rest of the system to use.
This will act as an internal API to the rest of the system.
