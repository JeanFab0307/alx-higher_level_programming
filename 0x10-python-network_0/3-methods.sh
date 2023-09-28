#!/bin/bash
# displays all HTTP methods the server will accept
curl -X OPTIONS -si "$1" | grep "Allow" | awk '{print $1}'
