#!/bin/bash

if [ "$1" = "delete" ]; then
    echo "Clearing the cluster."
    kubectl delete -f ./manifests/web/00-namespace.yml
    echo "Bassa is removed from the cluster"
elif [ "$1" = "create" ]; then
    echo "Deploying Bassa to kubernetes cluster"
    # Deploy web pod
    kubectl create -R -f ./manifests/web/
    # Deploy api and aria2c pod
    kubectl create -R -f ./manifests/api_and_aria2c/
    # Deploy database pod
    kubectl create -R -f ./manifests/database/
    echo "Bassa got deployed at"
    kubectl get ingress -n bassa | awk '{ print $3 }'
fi