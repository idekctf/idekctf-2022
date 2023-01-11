#!/usr/bin/bash

echo "MAKE SURE MOUNT TMP LINE IS MISSING IN DOCKERFILE ENTRYPOINT"

docker build -t web-proxy-viewer challenge \
	&& docker tag web-proxy-viewer gcr.io/idekctf-374221/web-proxy-viewer \
	&& docker push gcr.io/idekctf-374221/web-proxy-viewer