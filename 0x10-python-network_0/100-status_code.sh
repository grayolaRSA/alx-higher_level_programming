#!/bin/bash
# Script that sends an URL request and displays only status code of the response
curl -so /dev/null -w "%{http_code}" "$1"
