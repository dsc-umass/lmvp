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
[Docker Compose](https://docs.docker.com/compose/install/) is the recommended way to run the API server. After cloning or downloading the repository, run `docker-compose run web python3 manage.py migrate` to build the initial tables in thedatabase. Then run `docker-compose up` to start LMVP. From there, you can navigate to the server in a web browser to see the Django Rest Framework interface, or use another tool to make API requests.

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

## Docker Hub
You can use Docker to pull an autobuild image from Docker Hub. Right now it is available [here](https://hub.docker.com/r/jbinvnt/lmvp). Be aware that they seem to only work for the x86 architecture, so if you want ARM or something else you will need to build it yourself.

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
