#Deploy Bass with AWS

Bassa can be deployed completely on AWS using theses scripts. 
Can be used for both deployment and production. 

##Infrastructure
Create required resources for deployment.

###Create a ECS cluster
Export following environment variables with appropriate values.

```bash
export PROJECT_ROOT=.
export STACK_NAME=ScoreLab-ECS-Cluster-NonProd
```

Then run the following scripts.

```bash
bash ${PROJECT_ROOT}/scripts/aws/scripts/deploy_ecs.sh
```