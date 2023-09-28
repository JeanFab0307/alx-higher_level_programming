#!/bin/bash
# displays the size of the body of the response
curl -X POST -sI "$1" | grep -i "Content-Lenght" | awk '{print $1/8}'
