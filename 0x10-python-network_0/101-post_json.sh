#!/bin/bash
# Sends JSON POST request, and displays the body of the response.
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
