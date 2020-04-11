#!/bin/bash
python3 django/manage.py test | grep 'FAIL'
if [[ $? -ne 0 ]]; then
  exit 1 #if the test output has "FAIL" in it, then exit with error code
fi
exit 0 # tests pass
