URL = https://www.list.am/

Test case 1
1. Navigate to lits.am
2. Search by "house" word
3. Filter by Currency with USD and Price with 0-50 $
4. Click on blue icon
5. Check that result's prices are in filtered range

Test case 2
1. Navigate to list.am
2. Try add random item as favorite
3. System show popup for required login


Files and folders
helpers.py/Helpers ---------------------------- general functions
header.py, result.py, favorite.py/Pages ------- pages' functions for test cases
config.py ------------------------------------- url to call
conftest.py ----------------------------------- fixture and logging, common for each test case
testdata.py ----------------------------------- test data to call
test cases 1,2 -------------------------------- test cases, descriptions are above

Created files
test_run.log


pep8 standart is kept
POM is used


For execution call pytest