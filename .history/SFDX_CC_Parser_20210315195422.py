#Parse Code Coverage json file from SFDX Cli 
import json

filepath = '/Users/bryanspeelman/Desktop/ccReport/test-result-codecoverage.json'
with open(filepath) as f:
    tests = json.load(f)
for test in tests:
    if test["coveredPercent"] != 100:
        print(test["name"])