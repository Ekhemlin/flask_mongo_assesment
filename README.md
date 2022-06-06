# Assessment for Python, MongoDB, and React.js 

## How to run the project 

- Get the `.env` file from Eitan 
- Place the `.env` file in `backend/`
- Run `cd backend && python3 flask_server.py`
- Run `cd ../frontend && npm start`

## Installing dependencies 

Dependencies for both the front end and backend can be installed with 

```
pip3 install -r backend/requirements.txt  
cd frontend && npm install 
```

Data can be imported into a new mongo database with the following commands 
  
```
mongoimport "<Mongo  URL>" --db imperva_db --collection customers --file data/DVDRentals-customers.json

mongoimport "<Mongo  URL>" --db imperva_db --collection rentals --file data/DVDRentals-films.json
```

## Other  documentation 

Documentation for the REST API endpoints can be found in `backend/endpoints.md` 
Todos / improvements for the projects can be found in `todo.txt`