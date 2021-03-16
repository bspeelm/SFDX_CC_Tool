#Parse Code Coverage json file from SFDX Cli 
import os
import os.path
from os import path
import sys
import json
import math

#take args from std in    
filepath = sys.argv[1]
with open(filepath) as f:
    tests = json.load(f)
#open file for writing
dirPath = input("Enter file output dir: ")
filePath = dirPath+'.txt'
if path.exists(filepath):
    f = open(filePath, "w")
else: 
    f = open(filePath, "x")
#loop json in
for test in tests:
    name = test["name"]
#Check type of covered percent and clean var
    if type(test["coveredPercent"]) == float:
        coveredPercent = math.trunc(test["coveredPercent"])
    elif test["coveredPercent"] == None:
        coveredPercent = 0 
    else:
        coveredPercent = test["coveredPercent"]
#Print to stout and file 
    if test["coveredPercent"] != 100 and name.find("fflib") == -1:
        print(name + "  |   " + str(coveredPercent) + "%")
        print("\n")
        f.write(name + '\n')
        f.write(str(coveredPercent) + '%\n\n')
        
#close file
f.close