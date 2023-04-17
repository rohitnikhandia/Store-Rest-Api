# Stores REST API
This project is a REST API built with Flask that enables users to create and manage stores and their items. The API includes user authentication to protect sensitive endpoints and utilizes SQLAlchemy for data modeling and querying. The application is containerized using Docker and uses PostgreSQL for data storage. The API is hosted on Render.com for easy deployment.

## Features
User authentication for secure access to certain endpoints
Ability to create and manage stores and their items
Data modeling and querying with SQLAlchemy
Containerization with Docker
Data storage with PostgreSQL
Deployed on Render.com

## Technologies
Flask - Python web framework
Python - Programming language
SQLAlchemy - Object-relational mapping library
Docker - Containerization platform
PostgreSQL - Relational database management system
Render.com - Cloud hosting platform

## Installation
Clone the repository
Install the required packages using pip install -r requirements.txt
Create a .env file and include the following variables:
```DATABASE_URL=<your_postgresql_database_url>
SECRET_KEY=<your_secret_key_for_flask_session>
```
Run the application using python app.py

## Usage
The following endpoints are available:

### Authentication
POST /register - Register a new user with email and password
POST /login - Log in a user with email and password

### Store
GET /store/<string:name> - Get a store by name
POST /store/<string:name> - Create a new store with name
PUT /store/<string:name> - Update a store by name
DELETE /store/<string:name> - Delete a store by name
GET /stores - Get a list of all stores

### Item
GET /store/<string:name>/item/<string:item_name> - Get an item by name in a store
POST /store/<string:name>/item/<string:item_name> - Create a new item with name and price in a store
PUT /store/<string:name>/item/<string:item_name> - Update an item by name in a store
DELETE /store/<string:name>/item/<string:item_name> - Delete an item by name in a store
GET /store/<string:name>/items - Get a list of all items in a store

### Authorization
Some endpoints require a valid token obtained from authentication to be accessed. These endpoints include:

POST /store/<string:name>
PUT /store/<string:name>
DELETE /store/<string:name>
POST /store/<string:name>/item/<string:item_name>
PUT /store/<string:name>/item/<string:item_name>
DELETE /store/<string:name>/item/<string:item_name>
To access these endpoints, include a valid token in the request headers with the following format:

```
Authorization: Bearer <access_token>
```

Deployment
The API is deployed on Render.com. To deploy the API on Render.com, create a new web service and link it to your GitHub repository. Render.com will automatically build and deploy the application from the Dockerfile in the repository. Make sure to include the DATABASE_URL and SECRET_KEY environment variables in the Render.com dashboard under "Environment Variables".

Contributing
Contributions to the project are welcome. To contribute, fork the repository, make your changes, and submit a pull request. Please include a clear description of your changes and why they are necessary.

