#!/bin/bash
# Display only the status code
curl -sI $1 | grep HTTP/ | cut -d ' ' -f 2
