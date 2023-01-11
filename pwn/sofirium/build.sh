#!/usr/bin/bash

docker build -t pwn-sofirium challenge \
	&& docker tag pwn-sofirium gcr.io/idekctf-374221/pwn-sofirium \
	&& docker push gcr.io/idekctf-374221/pwn-sofirium