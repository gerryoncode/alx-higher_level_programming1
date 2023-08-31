#!/bin/bash
#display the http methods the server will allow
curl -sI "$1" | grep "Allow" | cut -d' ' -f2
