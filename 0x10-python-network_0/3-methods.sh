#!/bin/bash
#display the http methods the server will allow
curl -X OPTIONS -i "$1"
