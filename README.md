<!-- [![Build Status](https://travis-ci.org/abhinavtripathy/XAuth.svg?branch=master)](https://travis-ci.org/abhinavtripathy/XAuth) -->
[![License](https://img.shields.io/badge/License-BSD%203%20Clause-brightgreen.svg)](./LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/dsc-umass/lmvp.svg?color=red)
![GitHub stars](https://img.shields.io/github/stars/dsc-umass/lmvp.svg)

# LMVP

> Lightweight Model Versioning Platform

## About
An open source neural network versioning system designed to separate model management functions and computationally expensive training operations.

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
## Contributing
*Before contributing*, please create a branch called `yourname-experiments` that you can stay on while setting up the server on your local machine and getting a feel for what the different components do. Other options include creating a fork if you want to build something completely different, or just downloading a zip file if you don't want to publish your changes.

Once you're ready to have your changes reviewed, create a branch with a descriptive name for the change you made and submit a pull request to `dev`. Once it is confirmed that the CI tests pass on `dev`, the changes will be merged into `master`.

Running the project is best done by cloning the repository and starting it with Docker Compose. Learn how to install Compose [here](https://docs.docker.com/compose/install/). **Note: you may be more likely to run into volume and networking problems when using Compose on a non-Linux platform.** You may need to migrate the database using `docker-compose run web python3 manage.py migrate`. Starting the container can be done with `docker-compose up`. When you want to run the tests, use `docker-compose -f docker-compose.test.yml up`. To run an arbitrary command in a specific service, the pattern is `docker-compose run <servicename> <commandname>`. To get to a shell you can type `bash` as the command name. After changes to the repository, you should rebuild the container with `docker-compose build`.

## Docker Hub
You can use Docker to pull the autobuild images from Docker Hub. Be aware that they seem to only work for the x86 architecture, so if you want ARM or something else you will need to build it yourself. 

## Task Groups
Commits addressing issues in a group may now be added to the corresponding branch. The *dev* branch may be used for generating test builds, which are available at the Docker repository `jbinvnt/lmvp:latest`. The *master* branch gets built at `jbinvnt/lmvp:stable` and should be used once features have been tested.

Issues for each group are available in the *Projects* tab.

| Group | Features |
| --- | --- |
| client | Utilities such as Python modules to allow team members to transfer models to/from the central server. |
| versioning | System for keeping track of how models and weights change over time. |
| webapp | The web administrator console. Built using Django, frontend framework TBD. |

## Comparison with other platforms
![Traditional Cloud Worlflow](/docs/images/TraditionalCloudWorkflow.PNG?raw=true)
![Local Training Workflow](/docs/images/LocalTrainingWorkflow.PNG?raw=true)
