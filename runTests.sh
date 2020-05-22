#!/bin/bash
cd /django
python3 manage.py test | grep 'FAIL'
if [[ $? -eq 0 ]]; then
  exit 1 #if the test output has "FAIL" in it, then exit with error code
fi
exit 0 # tests pass
