# alphavantage-automation

**Project Overview:**  
**Automation of GET request for TIMES_SERIES_DAILY section.**
**url: https://www.alphavantage.co/documentation/#daily**

Below are the test cases defined as part of automation:

1. **test_get_times_daily_ibm**:
   - This test case submits the basic GET request with:
   Function=TIMES_SERIES_DAILY; symbol=IBM and output=default
   - This test assert the response status code as 200.

2. **test_get_times_daily_ibm_output_full**:
   -  This test case submits the basic GET request with:
      Function=TIMES_SERIES_DAILY; symbol=IBM and outputsize=full
   - This test assert the response status code as 200.

3. **test_get_times_daily_tsco_output_default**:
   -  This test case submits the basic GET request with:
      Function=TIMES_SERIES_DAILY; symbol=TSCO.LON and outputsize=default
   - This test assert the response status code as 200.

4. **test_get_times_daily_invalid_symbol**:
   -  This test case submits the basic GET request with:
      Function=TIMES_SERIES_DAILY; invalid symbol
   - This test assert the response status code as 200 as well as assert ' "Error Message"' in response_text

5. **test_get_times_daily_invalid_api_key**:
   -  This test case submits the basic GET request with:
      Function=TIMES_SERIES_DAILY; invalid api key
   - This test assert the response status code as 200 as well as assert 'the parameter apikey is invalid or missing' in response_text

6. **test_get_exceeds_throttle_limit:**
   - This test case submits the basic GET request with:
     Function=TIMES_SERIES_DAILY; symbol=ibm
   - This test loops the request 6 times in a minute, which exceeds the
     throttle limit.
   - This test assert the response status code as 200 as well as assert
     text related to throttle limit in 6th response_text.
   - This adds only last submitted request to report.

**Important Points:**
1. **To execute all the test cases together:**
   -  select tests folder and open terminal
   -  type command: pytest test_alphavantage_api.py -s -v and hit enter.
   -  Report will generated in reports folder with current time stamp
      folder.

2.  **To execute all invalid test cases together:**
    - select tests folder and open terminal
    - type command: pytest test_advantage_api.py -s -v -m invalid
    - hit enter
    - it will run all invalid test cases which is marked invalid in
      tests folder.
    - Report will be generated in reports folder with current time stamp.

3. **To execute only throttle test case:**
   - select tests folder and open terminal
   - type command pytest test_advantage_api.py::test_get_exceeds_throttle_limit -s -v
   - hit enter
   - it will run the particular test and report will be saved in reports
     folder.

4. config.py file has all the configuration for the tests.
5. common_methods.py has a class property to create a run time folder for
   reports.
6. conftest.py has pytest fixtures and runs before every test cases.
7. helper.py has helper functions to build service url, submit request and export report methods.
8. To View the Report after the execution done, Please navigate to reports folder and then open latest time stamp folder to find the my_report.html
