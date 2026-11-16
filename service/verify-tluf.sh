#!/bin/bash
curl -s -o /dev/null -w "submit.html %{http_code}\n" https://tluf.org/submit.html
curl -s https://tluf.org/ | grep -c "Submit a paper"
curl -s -o /dev/null -w "api/health %{http_code}\n" https://tluf.org/api/health
