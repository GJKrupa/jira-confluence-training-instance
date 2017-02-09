#!/bin/sh
docker build -t uxian/jira -f Dockerfile-jira .
docker build -t uxian/confluence -f Dockerfile-confluence .
