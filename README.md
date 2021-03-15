SFDX Code Coverage Tool 

Create python script to parse a codeCoverage.json file from a SFDX report

Phase 1: 
    - User runs sfdx command: 'sfdx force:apex:test:run -c -l RunLocalTests -r human -d ~/Desktop/ccReport'
    - User will use this program to parse tests that need to be expanded
    - Output will be in a seperate file in a json format that is human readable 
Phase 2:
    - Remove the need for the user to run the sfdx command to run the tests