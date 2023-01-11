<?php

function exception_error_handler($errno, $errstr, $errfile, $errline ) {
    die("$errstr in $errfile line $errline");
}
set_error_handler("exception_error_handler");
