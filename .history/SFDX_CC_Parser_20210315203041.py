#Parse Code Coverage json file from SFDX Cli 
import json
import math

filepath = '/Users/bryanspeelman/Desktop/ccReport/test-result-codecoverage.json'
with open(filepath) as f:
    tests = json.load(f)
for test in tests:
    name = test["name"]
    if type(test["coveredPercent"]) == float:
        coveredPercent = math.trunc(test["coveredPercent"])
    elif test["coveredPercent"] == "None":
        coveredPercent = 0
    else:
        coveredPercent = test["coveredPercent"]
    if test["coveredPercent"] != 100 and name.find("fflib") == -1:
        print(name + "  |   " + str(coveredPercent) + "%")
        print("\n")