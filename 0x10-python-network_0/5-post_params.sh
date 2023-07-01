#!/bin/bash
#A Bash script that sends a POST request and sets values to variables
curl -s -X POST "$1" -d "email=test%40gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
