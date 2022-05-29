#!/bin/bash
tests="test/test_salary.py"
for t in $tests
do
    echo ""
    echo "Running test module: ${t}"
    python -m unittest $t
done
