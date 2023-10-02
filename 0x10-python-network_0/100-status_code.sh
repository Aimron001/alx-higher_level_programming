#!/bin/bash
# Sends a request and displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
