# hive_technical_assessment
This repo contains all to be presented for HiveOnline Technical Assessment
# Using PostgreSQL with FastAPI, snd Docker container

To run this project, you'll need to have [Docker](https://docs.docker.com/get-docker/) installed, or connect to a database yourself modifying the connection in the codebase.

## Getting started

Set up a virtual environment for the project:  
`python3 -m venv virtualenv`

Activate the environment:  
`source virtualenv/bin/activate`

Install the dependencies:  
`pip install -r requirements.txt`

Start the container in order to use Postgres:  
`./runContainer.sh`

Run the API with Uvicorn:  
`./runApp.sh`

Run the database migration:  
`alembic upgrade head`

To use The endpoints follow the links on the swagger documentation provided by the first route:  
`4look ata documentation links`


