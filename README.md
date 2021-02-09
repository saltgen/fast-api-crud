# Project Architecture

- A dockerized postgres database has been used to simplify setup
- fastapi is being used to serve the api endpoints
- Alembic is used to handle the database migrations
- pytest is being for testing purposes

### Initialize the postgres database

- `make run-db`

### Create a virtual environment:

 - `python3 -m venv venv`

### Activate the same:

 - `source venv/bin/activate`

### Install requirements:

- `pip install -r requirements.txt`

### Database Setup and Migrations:

 - `alembic init alembic`
   
   *** Find the variable `sqlalchemy.url` in alembic.ini file and set the value to `postgresql://postgres:postgres@localhost:5432/postgres` ***
   
 - `alembic revision --autogenerate -m "Initialize tables"`
 - `alembic upgrade head`
 

### Run the server:

- `uvicorn app.main:app --reload`

### Run the tests:
- `pytest tests/`

### Few things that can be improved:

- Updating the postgres uri string on the alembic.ini file can be automated using python-dotenv package
- Currently, the tests can run only if the dev server is up, this can improved
  using mock objects and seperate database just for testing purposes


