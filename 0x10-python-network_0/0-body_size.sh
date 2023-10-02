#!/bin/bash
# Get the content length of a response
curl -sI "$1" | awk '/Content-Length/{print $2}'
