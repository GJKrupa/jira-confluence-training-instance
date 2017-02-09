#!/bin/sh
docker ps -a -q | xargs docker kill
docker ps -a -q | xargs docker rm
