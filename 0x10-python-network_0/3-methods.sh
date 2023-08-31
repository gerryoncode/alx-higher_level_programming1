#!/bin/bash
#display the http methods the server will allow
curl -X OPTIONS -i "$1" | grep "Allow" | cut -d' ' -f2
