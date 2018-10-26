#Deploy Bass with AWS

Bassa can be deployed completely on AWS using theses scripts. 
Can be used for both deployment and production. 

##Prerequisite
AWS CLI is needed for CloudFormation Templates deployment. 
Install AWS CLI with following scipt.

```bash
bash scripts/aws/scripts/install_aws_linux.sh
```

##Infrastructure
Create required resources for deployment.
Export environment variables with appropriate values.
`PROJECT_ROOT` should be the root path of your Bassa project folder.

```bash
export PROJECT_ROOT=.
```

###Create a ECS cluster 

Environment variables. 

```bash
export STACK_NAME=ScoreLab-ECS-Cluster-NonProd
```

Then run the following scripts.

```bash
bash ${PROJECT_ROOT}/scripts/aws/scripts/deploy_ecs.sh
```

###Create a MySQL instance

Environment variables. 

```bash
export STACK_NAME=ScoreLab-RDS
```

Then run the following scripts.

```bash
bash ${PROJECT_ROOT}/scripts/aws/scripts/deploy_rds.sh
```