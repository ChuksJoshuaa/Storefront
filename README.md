# Building an Ecommerce store Restful Api WITH DJANGO REST FRAMEWORK

[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements

- Python 3.7
- Django 3.1
- Django REST Framework

## Installation

After you clone the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command

```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running

```
pip install -r requirements.txt
```

## Structure

In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

In our case, we have one single resource, `store`, so we will use the following URLS - `/store/products/` and `/store/collections/` for getting the list of products and their respective collections

| Endpoint             | HTTP Method | CRUD Method | Result               |
| -------------------- | ----------- | ----------- | -------------------- |
| `store`              | GET         | READ        | Get all Api Root     |
| `store/products/`    | GET         | READ        | Get all products     |
| `store/collections/` | GET         | READ        | Get all collections  |
| `store/products/:id` | POST        | CREATE      | Create a new product |
| `store/products/:id` | PUT         | UPDATE      | Update a product     |
| `store/products/:id` | DELETE      | DELETE      | Delete a product     |

## Use

We can test the API using [Postman](https://www.postman.com/)

Postman, it is an HTTP client that tests HTTP requests, utilizing a graphical user interface, through which we obtain different types of responses that need to be subsequently validated.

First, we have to start up Django's development server.

```
python manage.py runserver
```

Only authenticated users can use the API services, for that reason, we use this to create an account:

```
http  http://127.0.0.1:8000/auth/users
```

## Create users and Tokens

After we create an account we can use those credentials to get a token

To get a token first we need to request

```
http http://127.0.0.1:8000/auth/jwt/create
username="username" password="password"

```

after that, we get the token. Something like this.

```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA2MjIxLCJqdGkiOiJjNTNlNThmYjE4N2Q0YWY2YTE5MGNiMzhlNjU5ZmI0NSIsInVzZXJfaWQiOjN9.Csz-SgXoItUbT3RgB3zXhjA2DAv77hpYjqlgEMNAHps"
}
```

We got two tokens, the access token will be used to authenticate all the requests we need to make, this access token will expire after a day.

`
The API has some restrictions:

- The store are always associated with the admins or users with neccessary permissions.
- Only authenticated users may read and see store products and their collections.
- Only the admin or users with necessary permissions may update or delete it.
- The API doesn't allow unauthenticated requests.
