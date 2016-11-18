"""
This file, expectations.py, defines expected test results and is not added to
the test source tarball.
"""
import os

buildreqs = []
license = 'IJG'
with open('testfiles/libjpeg-turbo/spec-expectations', 'r') as spec:
    specfile = spec.read()

specfile = specfile.replace('{}', os.getcwd()).split('\n')
output_strings = []