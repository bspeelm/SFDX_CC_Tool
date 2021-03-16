#Parse Code Coverage json file from SFDX Cli 
import json

filepath = '/Users/bryanspeelman/Desktop/ccReport/test-result-codecoverage.json'
with open(filepath) as f:
    data = json.load(f)

print(data["name"])