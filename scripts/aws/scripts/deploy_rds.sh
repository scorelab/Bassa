#!/usr/bin/env bash
aws cloudformation create-stack --stack-name ${STACK_NAME} --template-body file://${PROJECT_ROOT}/scripts/aws/stacks/rds/template.json --parameters file://${PROJECT_ROOT}/scripts/aws/stacks/rds/environments/rds-dev.json
