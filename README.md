# appium-mobile-test-with-py

## Prerequisites 
* Appium server set up and running
* Emulator running Android Q (or with Chrome upgraded to Chrome 73)

## Linux/macOS Setup
0. install Python 3.x
1. open a terminal window
2. clone repository `git clone https://github.com/tomdwp/appium-mobile-test-with-py.git`
3. change directory to the 'appium-mobile-test-with-py' directory
4. create a python virtual environment: `python3 -m venv .env`
5. activate the virtual enviroment: `source ./.env/bin/activate`
6. install the needed packages: `pip install -r requirements.txt`


## Run 1st Test Case -- Load Google.com Website
In terminal windows with the virtual environment activated:
1. run this command: `python google_search_page_test.py -v`



loading google search page
-- could add the voice search button and the google search button as locators on the field -- but these web elements did not have clean and reliable attributes to build robust locators from, so I left them out.  The `aria-label` is likely constant so could be used to build an xpath locator but this value will vary based on the user's language preference, so is not a great candidate to build off of.

-- assuming that the correct page to load is the https page.  adding tests that check that the https page is the one returned -- regardless of whether the http page or the https page was requested.

-- I have punted here on localiztion.  The tests and page objects would need to be extended to accomodate loading different regional variations of the page (e.g. the Voice Search button that appears on the right hand side of the search box, is absent from the Canadian French version of the page.)

