# end_to_end-ML_Project_with_MLFLOW
 It's an end to end product using MLflow.

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the config manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

# How to run?

### STEPS:

```bash 
https://github.com/param-unik/end_to_end-ML_Project_with_MLFLOW
```

### STEP 01—create a conda environment after opening the repo

```bash
conda create -n mlProj python=3.8 -y
```

``` bash 
conda activate mlProj
```

### STEP 02- install the requirements.txt

``` bash
pip install -r requirements.txt
```

```bash
python app.py
```

```bash
open up local host and port 
```

### CMD 
- mlflow ui 

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/param-unik/end_to_end-ML_Project_with_MLFLOW.mlflow \
MLFLOW_TRACKING_USERNAME=param-unik \
MLFLOW_TRACKING_PASSWORD=3d3a1a07fbf32e2de561ef8dc2ca04e8fb341be4 \
python script.py


Run this export as env variables:

```bash 
export MLFLOW_TRACKING_URI=https://dagshub.com/param-unik/end_to_end-ML_Project_with_MLFLOW.mlflow
export MLFLOW_TRACKING_USERNAME=param-unik
export MLFLOW_TRACKING_PASSWORD=3d3a1a07fbf32e2de561ef8dc2ca04e8fb341be4
```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

    # with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws

    # Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    # Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image

    - Save the URI: 954653715191.dkr.ecr.us-east-1.amazonaws.com/mlproj

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

    # optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# 6. Configure EC2 as self-hosted runner:

    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup GitHub secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

## About MLflow

MLflow

- Its Production Grade
- Trace all of your experiments
- Logging & tagging your model