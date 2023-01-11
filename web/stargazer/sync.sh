#!/bin/bash

scp -r ./attachments root@34.86.140.156:/home/liukuirong/
scp -r ./.env root@34.86.140.156:/home/liukuirong/attachments/.env
echo "Finished, make sure to rebuild the container."