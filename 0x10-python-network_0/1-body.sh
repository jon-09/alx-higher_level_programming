#!/bin/bash
# This script takes in a URL, sends GET request and displays body of response
curl -sfL "$1" -X GET
