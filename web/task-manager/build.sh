#!/usr/bin/bash

docker build -t web-task-manager challenge \
	&& docker tag web-task-manager gcr.io/idekctf-374221/web-task-manager \
	&& docker push gcr.io/idekctf-374221/web-task-manager