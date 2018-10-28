#!/usr/bin/env bash
aws cloudformation create-stack --stack-name ${STACK_NAME} --template-body file://${PROJECT_ROOT}/scripts/aws/stacks/ecs_cluster/template.json --parameters file://${PROJECT_ROOT}/scripts/aws/stacks/ecs_cluster/environments/ecs-cluster-dev.json  --capabilities CAPABILITY_IAM
