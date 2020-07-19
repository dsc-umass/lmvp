<!-- [![Build Status](https://travis-ci.org/abhinavtripathy/XAuth.svg?branch=master)](https://travis-ci.org/abhinavtripathy/XAuth) -->
[![License](https://img.shields.io/badge/License-BSD%203%20Clause-brightgreen.svg)](./LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/dsc-umass/lmvp.svg?color=red)
![GitHub stars](https://img.shields.io/github/stars/dsc-umass/lmvp.svg)

# LMVP

> Lightweight Model Versioning Platform

## Contributing and Workflow

Welcome to the team! The work for this project is managed using GitHub issues. Each issue represents something that needs to be done: usually fixing a bug or adding a new feature. **Every change you make** should have its own **issue** and its own **branch**. If you've used Jira before, you will recognize issues as being the analogous to tickets. First, clone the repository by running:

```
$ git clone git@github.com:dsc-umass/lmvp.git
$ cd lmvp/
```

### Create a new issue

Go to the *Issues* tab at the top of GitHub, then click the green *New issue* button. Give it a short descriptive title and add more information in the text box below. Then make sure you choose the **gear next to "Projects"** and click on LMVP.

![Assign GitHub project](/docs/images/AssignGitHubProject.PNG?raw=true)

You can assign an issue to yourself or a teammate right away if you've discussed it and are ready to start work. Alternatively, you can leave it unassigned and someone can later take responsibility for it when they need a new task.

### Claim an issue

Go to the *Projects* tab at the top, and choose LMVP. You should see a page with several columns, each containing cards showing issues. Drag the issue you're about to start from the "New" column to "Working on". Make sure that the issue is assigned to you if it isn't already (but don't work on an issue assigned to someone else or change its assignment without asking them first).

Almost always you should only work on one issue at a time. This is to make sure that features get finished and the team makes steady progress. There are some exceptions such as fixing a significant bug and "unblocking" someone by fulfilling a prerequisite for their own work.

### Create a branch

This is one of the most important steps in the contribution workflow. Especially if you're new to Git, it's easy to accidentally make changes on the wrong branch and **erase your work or someone else's**.

Each branch needs to be named after the issue that you're working on. In GitHub, each issue has a number as shown here:

![Assign GitHub project](/docs/images/GitHubIssueNumber.PNG?raw=true)

You should always name your branch `LMVP-<your issue number>`. So in my example the branch I create should be named `LMVP-18`. Here are the commands I would run to create this branch:

```
$ git checkout master
$ git checkout -b LMVP-18
```

Remember to replace `18` with your own issue number.

Now, make your changes to the code. To save a benchmark of your work at any time, run:

```
$ git add .
$ git commit -m "Put a message describing your work here"
```

### Be careful with pushing!

Pushing a branch allows you to send your code to GitHub so others can see your work and it can be saved online. But pushing incorrectly can be **dangerous**. Always make sure you are pushing to the **correct branch** and never push with the `--force` flag, except after a rebase.

Before pushing, always make sure you are on the correct branch:

```
$ git status
On branch LMVP-18
nothing to commit, working tree clean
```

Never push to the `master` branch. To get to a different branch, run

```
$ git checkout <correct branch name here>
```

If the branch doesn't exist, see the above section for how to create it. Once you're on the right branch, run:

```
$ git push -u origin LMVP-<your issue number here>
```

You can make and push multiple commits. Any subsequent times you push commits while on this branch, you can just run `git push` without the extra arguments.

### Creating a pull request

A pull request is used to indicate that you're ready for your work to be reviewed before being added to the master version of the codebase. Pull request a place for others to comment with feedback and for you to make changes in response to their suggestions. If you've used GitLab before, you will recognize pull requests as being analogous to merge requests.

Go to the *Pull requests* tab at the top of GitHub, then click the green *New pull request* button. Make sure that **base** is set to master and change **compare** to be the branch with your changes. Remember to [link the pull request to your issue](https://docs.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue). After that, you can submit the pull request. Do not merge your own pull request without review!

### Reviewing a pull request

In response to review, you can make new commits on your branch and push them. They will be visible in the pull request once they are pushed. Make sure to notify a reviewer when your new commits respond to their feedback.

### Merging a pull request




Running the project is best done by cloning the repository and starting it with Docker Compose. Learn how to install Compose [here](https://docs.docker.com/compose/install/). **Note: you may be more likely to run into volume and networking problems when using Compose on a non-Linux platform.** You may need to migrate the database using `docker-compose run web python3 manage.py migrate`. Starting the container can be done with `docker-compose up`. When you want to run the tests, use `docker-compose -f docker-compose.test.yml up`. To run an arbitrary command in a specific service, the pattern is `docker-compose run <servicename> <commandname>`. To get to a shell you can type `bash` as the command name. After changes to the repository, you should rebuild the container with `docker-compose build`.

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
