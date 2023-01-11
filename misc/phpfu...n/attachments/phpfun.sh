#!/bin/bash

read -e -p "Input script: " USER_SCRIPT

case "${USER_SCRIPT}" in
  ("" | *[!\[\]\(\)\.\'\^\,]*)
    echo >&2 "Invalid payload, only [(,.^')] characters are allowed.";;
  (*)
    php -d auto_prepend_file=/error_handler.php \
      -d disable_functions="restore_error_handler" \
      -f <(echo -e "<?php\n${USER_SCRIPT}\n?>")
esac
