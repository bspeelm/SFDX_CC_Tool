#Parse Code Coverage json file from SFDX Cli 
import json
import math

filepath = '/Users/bryanspeelman/Desktop/ccReport/test-result-codecoverage.json'
with open(filepath) as f:
    tests = json.load(f)
for test in tests:
    name = test["name"]
    if test["coveredPercent"] != 100 and name.find("fflib") == -1:
        print(test["name"] + "  |   " + str(math.trunc(test["coveredPercent"])) + "%")
        print("\n")