#!/bin/bash
# display response after a POST and setting variables
curl -d  "email: test@gmail.com" -d "subject: I will always be here for PLD" -X POST -s "$1"
