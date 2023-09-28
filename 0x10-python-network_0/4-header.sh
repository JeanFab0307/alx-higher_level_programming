#!/bin/bash
#sends a GET and display the response and set a header var
curl -H "X-School-User-Id:98" -X GET -s "$1"
