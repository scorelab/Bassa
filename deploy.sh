#! /bin/bash

# Build production and development use docker images
# Build these images with two build args for better commit history
# shows only logs pushed to stderr
# release tag should be updated here for every release

git_sha=$(git rev-parse --short HEAD)
build_date=$(date -u +”%Y-%m-%dT%H:%M:%SZ”)

docker build --build-arg VCS_REF=$git_sha --build-arg BUILD_DATE=$build_date -t scoreucsc/bassa-ui:prod -t scoreucsc/bassa-ui:latest -t scoreucsc/bassa-ui:v1.0.0  ui >/dev/null
docker build -f ui/Dockerfile.dev --build-arg VCS_REF=$git_sha --build-arg BUILD_DATE=$build_date -t scoreucsc/bassa-ui:dev ui >/dev/null
docker build -f components/core/Dockerfile.prod --build-arg VCS_REF=$git_sha --build-arg BUILD_DATE=$build_date -t scoreucsc/bassa-server:prod -t scoreucsc/bassa-server:latest -t scoreucsc/bassa-server:v1.0.0 components/core >/dev/null
docker build --build-arg VCS_REF=$git_sha --build-arg BUILD_DATE=$build_date -t scoreucsc/bassa-server:dev components/core >/dev/null
docker build --build-arg VCS_REF=$git_sha --build-arg BUILD_DATE=$build_date -t scoreucsc/bassa-aria2c:latest -t scoreucsc/bassa-aria2c:v1.0.0 components/aria2c >/dev/null

# push production docker images with tags prod, latest, release:v1.0.0
# push development docker images with tag dev
docker login -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"

# Production tag
docker push scoreucsc/bassa-ui:prod
docker push scoreucsc/bassa-server:prod

# Latest tag
docker push scoreucsc/bassa-ui:latest
docker push scoreucsc/bassa-server:latest
docker push scoreucsc/bassa-aria2c:latest

# v1.0.0 tag
docker push scoreucsc/bassa-ui:v1.0.0
docker push scoreucsc/bassa-server:v1.0.0
docker push scoreucsc/bassa-aria2c:v1.0.0

# Development tag
docker push scoreucsc/bassa-ui:dev
docker push scoreucsc/bassa-server:dev


