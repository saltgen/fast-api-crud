# Project Architecture

- A dockerized Postgres database has been used to simplify the setup
- fastapi is being used to serve the API endpoints
- Alembic is used to handle the database migrations
- pytest is being for testing purposes

### Clone Git repo and change directory

- Open Terminal and execute `git clone git@github.com:saltgen/fast-api-crud.git`
- Execute, `cd fast-api-crud/`
### Initialize the Postgres database

- `make run-db`

### Create a virtual environment:

 - `python3 -m venv venv`

### Activate the same:

 - `source venv/bin/activate`

### Install requirements:

- `pip install -r requirements.txt`

### Database Setup and Migrations:

 - `alembic revision --autogenerate -m "Initialize tables"`
 - `alembic upgrade head`

### Run the server:

- `uvicorn app.main:app --reload`
- Please ensure the api service is running locally on `http://127.0.0.1:8000`,
  this is necessary for the tests to function


### Run the tests:

- Open a new shell, reactivate the virtual environment, `source venv/bin/activate` and execute `pytest tests/`

### Sending requests (Postman):

 - POST: Open Postman, select POST method, paste the following url - `http://127.0.0.1:8000/songs`

 - Sample data for song, audiobook, podcast audio types can be found [here](tests/test_endpoints.py), under post methods

 - The same URL with different audio types will work, `http://127.0.0.1:8000/audiobooks` or `http://127.0.0.1:8000/podcasts`

 - Create multiple objects for each audio type to check Get, Update and Delete functionalities

 - GET all objects: Select GET method and paste the URL, `http://127.0.0.1:8000/songs`, similarly `http://127.0.0.1:8000/audiobooks` for all audiobooks

 - GET single object `http://127.0.0.1:8000/songs/id`, the id needs to be replaced with the id of the object

 - DELETE: Similar to GET single object, the method needs to be changed to DELETE on Postman, click on Send

 - PATCH: Select PATCH method and paste the URL, `http://127.0.0.1:8000/songs/id`, sample data
   can be found [here](tests/test_endpoints.py), after updating the data body, click on Send


### Few things that can be improved:

- Updating the Postgres URI string on the alembic.ini file can be automated using the python-dotenv package

- Currently, the tests can run only if the dev server is up, this can be improved
  using mock objects and a separate database just for testing purposes, although a proper teardown has been ensured

- There are two endpoints for GET, for some reason the optional path parameter is not working,
  Github issue, [here](ttps://github.com/tiangolo/fastapi/issues/945)

- Faced another issue the schemas are not getting mapped to the model classes, this project has been built
  entirely by following the FastAPI documentation, but for some reason, mapping pydantic schema to ORM model
  is still an issue, found a similar question [here](https://stackoverflow.com/questions/65709591/sqlalchemy-class-is-not-mapped)
  I have ensured that the request body is fed into the schema object for validations before getting saved into the database




