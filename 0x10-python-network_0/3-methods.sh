#!/bin/bash
# Display all HTTP methods accepted
curl -sI $1 | grep Allow | cut -d ' ' -f 2-10
