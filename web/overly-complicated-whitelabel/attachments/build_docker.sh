#!/bin/bash
docker build --tag=overly_complicated_whitelabel .
docker run -p 1337:1337 --rm --name=overly_complicated_whitelabel -it overly_complicated_whitelabel
