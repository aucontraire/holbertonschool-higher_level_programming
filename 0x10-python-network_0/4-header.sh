#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL
curl -H "X-HolbertonSchool-User-Id:98" -sLX GET "$1"
