# Flask Application for CRUD Operations on MongoDB

This repository contains a Flask application that enables CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. The application's REST API endpoints are accessible via HTTP requests and can be tested using Postman.

## Requirements

Before running the application, make sure you have the following prerequisites installed on your system:

- Python (3.6 or higher)
- Flask
- PyMongo
- Postman (for testing the REST API endpoints)
- Docker (optional, for containerization)

## Setup

1. **Clone the repository**

   Use Git to clone this repository to your local machine:

   ```bash
   git clone https://github.com/s-chandr/CoRider.git
   cd flask-mongodb-crud
    ```
2. **Install all the required packages**
```
  pip install -r requirements.txt
  ```
3. Set up a .env file to read the environment variables and paste the below lines
```
  DATABASE_URI = mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority

```
replace with your creds generate from mongo atlas.

4. Finally, run the wsgi application
```
  python app.py
```

5. Docker container :
```docker pull schandrdocker/corider-flask-v1```
## REST API Endpoints

### Get All Users

**Endpoint:** `GET /users`

Returns a list of all users.
![Screenshot (1138)](https://github.com/s-chandr/CoRider/assets/71585216/25bf6889-b9c5-4d93-9b14-ff3c722360bc)


### Get User by ID

**Endpoint:** `GET /users/<id>`

Returns the user with the specified ID.
![Screenshot (1133)](https://github.com/s-chandr/CoRider/assets/71585216/8846ce01-1174-49ad-abcc-365e9fc28d1c)


### Create New User

**Endpoint:** `POST /users`

Creates a new user with the specified data.
![Screenshot (1134)](https://github.com/s-chandr/CoRider/assets/71585216/24f4d47c-c199-45a9-9545-62c8e0e5cce8)


### Update User by ID

**Endpoint:** `PUT /users/<id>`

Updates the user with the specified ID with the new data.
![Screenshot (1136)](https://github.com/s-chandr/CoRider/assets/71585216/105d48b2-d2dc-4023-9989-d9cb2945fea9)


### Delete User by ID

**Endpoint:** `DELETE /users/<id>`

Deletes the user with the specified ID.
![Screenshot (1135)](https://github.com/s-chandr/CoRider/assets/71585216/3e2a3857-efc6-4785-9f8b-7eb2115b7012)

### Install MongoDbCompass and use the same DATABASE_URI to connect to view the updates in db
![Screenshot (1137)](https://github.com/s-chandr/CoRider/assets/71585216/f5fac0b1-969e-42cf-bc5a-32a2820ba471)
