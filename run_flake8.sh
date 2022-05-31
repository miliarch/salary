#!/bin/bash

# Check for syntax errors and undefined names
flake8 wage --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 test --count --select=E9,F63,F7,F82 --show-source --statistics

# Full round, emitting errors as warnings
flake8 wage --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
flake8 test --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
