# UI_Automation_Exam

#### Test cases

The project contains 2 test cases:
1)Searching data on the list.am page ("test_1_search_data")
2)Checking the favorites saving functionality("test_2_check_favorite")

We keep PEP8 standard

### Pages

We are using POM and distributed 4 pages:
-favorite
-header
-login
-result

### All structure
Except pages, we have other files in the project. 
We are keeping logger.

The environment credentials are keeping in TestData.
Also, there you can find other relating to test data.

In the conftest.py file you can find main fixtures for the project, including driver.
Helpers file combines all basis functions for the project. 
All required items for installation is presented in the requirements.txt file

# **Launching**
To run the project please navigate to the project location and enter 'pytest' command. To run the specific test case 
use the command 'pytest + filename.py'