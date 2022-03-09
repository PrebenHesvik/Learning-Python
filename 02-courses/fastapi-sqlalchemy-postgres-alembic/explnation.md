### Install fastapi
- pip install fastapi[all]

### Postgres date insert
- click the edit button on the left to the column name
- Set constraint equal to NOW()


### Postman
- When login functionality has been added then you have to remember
  to inlcude the jwt bearer token in the requests..
  Auth  --> Bearer Token --> {{JWT}}
- or set login_user settings to pm.environment.set("JWT", pm.response.json().access_token);

### Alembic
- pip install alembic
- type alembic init alembic to create a new directory called alembic and a file called alembic.ini
  - in alembic.ini change value assigned to variable sqlalchemy.url
- alembic revision -m "create tables" --> will add a new file inside the alembic folder
  - Inside the new file there are two functions; upgrade and downgrade
  - The logic for upgrading or downgrading the database goes into these functions
  - at the top of the file there is a variable called revision
  - to upgrade 
    - alembic upgrade <revision number> 
    - alembic upgrade +1 to go back up one step 
    - alembic upgrade +2 to go back up two steps
    - alembic upgrade head
  - to downgrade --> alembic downgrade <revision number> OR alembic downgrade -1 to go back one step
- to find current revision --> alembic revision
- alembic revision --autogenerate -m "automatically add some stuff" and then alembic upgrade head
  - This will automatically add tables that are in the models.py but not in the database. 


