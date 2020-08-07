<!-- [![Build Status](https://travis-ci.org/abhinavtripathy/XAuth.svg?branch=master)](https://travis-ci.org/abhinavtripathy/XAuth) -->
[![License](https://img.shields.io/badge/License-BSD%203%20Clause-brightgreen.svg)](./LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/dsc-umass/lmvp.svg?color=red)
![GitHub stars](https://img.shields.io/github/stars/dsc-umass/lmvp.svg)

# LMVP

> Lightweight Model Versioning Platform

## Contributing

Please read the entire guide [here](https://github.com/jbinvnt/small-team-tutorial).

## About
An open source neural network versioning system designed to separate model management functions and computationally expensive training operations.

## Getting Started
[Docker Compose](https://docs.docker.com/compose/install/) is the recommended way to run the API server. After cloning or downloading the repository, run `export DB_PASSWORD=arbitrarypassword` and then `docker-compose run web python3 manage.py migrate` to build the initial tables in thedatabase. Then run `docker-compose up` to start LMVP. From there, you can navigate to the server in a web browser to see the Django Rest Framework interface, or use another tool to make API requests.

## Features

- Fetch, update, and publish models from anywhere
- Track metrics
- Manage model history on the web
- Add team members, make contributions

### Example commands
```
>>> localModel = lmvp.download(modelName)
```
```
>>> lmvp.showHistory(project)
```
```
>>> lmvp.update(modelname, localModel)
```

## Task Groups

Milestones for each group are available in the *Projects* tab. Please make sure to assign each issue to the correct milestone.

| Group | Features |
| --- | --- |
| Python module | Allow team members to manage their models from Colab or another environment. Makes API requests to the central server. |
| Central server | Provides a REST API for versioning, organization, and model storage. Built using Django REST Framework. |
| Web Interface | The web administrator console to allow project management. Makes API requests to the central server. |

## Comparison with other platforms
![Traditional Cloud Worlflow](/docs/images/TraditionalCloudWorkflow.PNG?raw=true)
![Local Training Workflow](/docs/images/LocalTrainingWorkflow.PNG?raw=true)

## Docker Hub
You can use Docker to pull an autobuild image from Docker Hub. Right now it is available [here](https://hub.docker.com/r/jbinvnt/lmvp). Be aware that they seem to only work for the x86 architecture, so if you want ARM or something else you will need to build it yourself.

## Troubleshooting starting Docker container

Here are some problems you might run in to when trying to start the docker container:

### psql: FATAL: password authentication failed for user "postgres"

This will happen if you tried to start the docker container without exporting the database password first. To fix this, run these commands

`$ docker kill $(docker ps -q)`  
`$ docker rm $(docker ps -a -q)`  
`$ docker rmi $(docker images -q)`

then export the password

`$ export DB_PASSWORD=arbitrarypassword`

and then run these commands to build and run the container

`$ docker-compose run web python3 manage.py migrate`  
`$ docker-compose up`

### Cannot connect to the Docker daemon. Is 'docker daemon' running on this host?

I ran into this problem while running Docker on a VM with WSL 2. Try installing [docker-desktop](https://hub.docker.com/editions/community/docker-ce-desktop-windows) on Windows first, and then starting docker on your Linux VM with

`$ sudo service docker start`

To make sure Docker automatically starts on boot, run

`$ sudo systemctl enable docker`

this shouldn't be necessary, but you may as well run it just to be safe.



## JWT Tokens And Authentication

> JWT is the JSON Web Token authentication plugin for the Django REST Framework.

> JWT generates, access and refresh tokens for Users wanting to access information from the API

>The command `permission_classes = (permissions.IsAuthenticated,)` located in `views.py` ensure that in order to access information of the API you must have logged in with your access token.

* In order to get a JWT Token, you have to register a new user. 

* When a new user is created, email verification is sent to their email. You can try this by creating a user for yourself

* After the User has been registered and has verified their email, they are able to login to the API (View Procedure to Login to the API Below)

* Upon Logging In, when correct credentials are entered, you receive a 201 response from the API with the entered username, email and two tokens generated.


After you receive the tokens by logging in. You will notice that there is one that states, "Refresh" and another one that states "Access". 

* The Refresh token has a life span of 30 days (which can be changed in `settings.py` ) and is used to generate a new token when required.

* The Acces token enables the users to have direct access to the API, it has a life span of 20 minutes (which can be changed in `settings.py` )

* When you have these tokens you can then login into the API interface and access all features.

## How To Login A User

> To be able to use the API and access all the information, a user has to login with generated access token

To use the login feature and fully have access to the API, run these command in terminal:

    $ export DB_PASSWORD=arbitrarypassword
    $ docker-compose run web python3 manage.py migrate
    $ docker-compose up

On your web browser access the API using http://localhost:8000


* When the API has loaded up, you would see an interphace with various function as shown in the image below
 
![Swagger Interface](/docs/images/SW-1.PNG?raw=true)

* Click the button that states `(Authorize)`

* Upon clicking Authorize you will see a pop-up requesting for API Key

![Swagger Interface: Authorise Function](/docs/images/SW-2.PNG?raw=true)

* At this point enter Bearer followed by the ACCESS token and click Authorize `Example:(Bearer **************)`. This will give you full access to the API and its functions

## How To Use Login Feature For User And Get Tokens

>To be able to use the API and access all the information, a user has to login to access the login tokens

To use the login feature for a user follow the following steps, run these command in terminal:

    $ export DB_PASSWORD=arbitrarypassword
    $ docker-compose run web python3 manage.py migrate
    $ docker-compose up

On your web browser access the API using http://localhost:8000

* When the API has loaded up, you would see an interphace with various function as shown in the image below

![Swagger Interface](/docs/images/SW-3.PNG?raw=true)
 
* This shows various options and function. Click the function that states `(“/auth/login/)`

* Upon click `(“/auth/login/)`, you will see an option that states `Try it out`, this will show you an area where you will have to input some parameters (email and password) accordingly, to test use sample users listed below.

* Once this has been entered click `EXECUTE`

* Please note, if you have registered a user and not verifid the email sent, you will be unable to login.
 
![Swagger Interface: Login Feature](/docs/images/SW-4.PNG?raw=true)

* If the current credentials have been entered you will see a Response Code 200 (OK) with the username and email entered, and the two tokens (REFRESH AND ACCESS TOKENS) showing that the user has been successfully registered.

![Swagger Interface: User Login Features With Tokens ](/docs/images/SW-5.PNG?raw=true)

## How To Register A User

> To be able to use the API and access all the information, a user has to be created to access the login tokens

To create a user follow the following steps, run these command in terminal:

    $ export DB_PASSWORD=arbitrarypassword
    $ docker-compose run web python3 manage.py migrate
    $ docker-compose up

On your web browser access the API using http://localhost:8000


* When the API has loaded up, you would see an interphace with various function as shown in the image below

![Swagger Interface](/docs/images/SW-6.PNG?raw=true)

![Swagger Interface](/docs/images/SW-7.PNG?raw=true)

* This shows various options and function. Click the function that states `(“/auth/register/)`

* Upon click `(“/auth/register/)`, you will see an option that states try it out, this will show you an area where you will have to input some parameters (email, username and password) accordingly. 

* Once this has been entered click `EXECUTE`

![Swagger Interface: Register Function](/docs/images/SW-8.PNG?raw=true)
 
* After a few seconds you will see a Response Code 201 (CREATED) with the username and email entered, showing that the user has been successfully registered.

![Swagger Interface: User Successfully Registered](/docs/images/SW-9.PNG?raw=true)
 

## How To Create Superuser

>In order to log into the admin interface, you have to create a superuser. 

To create a super user follow the following steps, run these command in terminal:

    $ export DB_PASSWORD=arbitrarypassword
    $ docker-compose run web python3 manage.py createsuperuser
    $ Fill in the details accordingly 

## How To Log In To Admin Interface

> In order to access the admin interface , you have to use your created superuser details. 

In order to acces the admin interphace follow the following steps, run these command in terminal:

    $ export DB_PASSWORD=arbitrarypassword
    $ docker-compose run web python3 manage.py migrate
    $ docker-compose up

Access localhost http://localhost:8000/admin from your web browser

Login in with superuser details
