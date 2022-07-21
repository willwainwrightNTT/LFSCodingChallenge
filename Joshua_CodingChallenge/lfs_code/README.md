# FWF -> CSV Parser

## Explanation
* This package is able to convert a fixed-width-file to a csv.

* It will generate a fixed width file of the spec provided, save that locally then parse it turning it into a csv.

* It is possible to parse your own fixed-width-file as long as it is named "fwf_lfs_test_file.txt". 
  It would be possible to allow the user to define whatever name they would like for this however that 
  was not a requirement of this specific challenge and thus has not been implemented.

* When creating the fixed-width-file a random number of lines is chosen from 1-1000 this is partially a testing
  technique but should also show off the robustness of the parser created.

* It will work for any length of file and will also work if the specifications change.

## How to run on Docker
* 1\. Open cmd or powershell
* 2\. Navigate to the folder called lfs_code
* 3\. docker compose up

Output file should now be in the local "output" folder.

## How to run locally
* 1\. Navigate to the "lfs_code/app/" folder
* 2\. Double click the "fwf_parser_test_local.py" file.

Output file should now be in the same folder as the "fwf_parser_test_local.py" file. The fixed-width-file generated should be there as well.