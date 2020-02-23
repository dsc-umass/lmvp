# Lightweight Model Versioning Platform (LMVP)
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

## Task Groups
| Branch | Features |
| --- | --- |
| client | Utilities such as Python modules to allow team members to transfer models to/from the central server. |
| versioning | System for keeping track of how models and weights change over time. |
| webapp | The web administrator console. Built using Django, frontend framework TBD. |

## Comparison with other platforms
![Traditional Cloud Worlflow](/docs/images/TraditionalCloudWorkflow.PNG?raw=true)
![Local Training Workflow](/docs/images/LocalTrainingWorkflow.PNG?raw=true)
