#Parse Code Coverage json file from SFDX Cli 
import json

filepath = '/Users/bryanspeelman/Desktop/ccReport/test-result-codecoverage.json'
with open(filepath) as f:
    tests = json.load(f)
for test in tests:
    name = test["name"]
    if test["coveredPercent"] != 100 and name.find("fflib") == -1:
        print(test["name"])
        print(test["codeCoverage"])
        print("\n")