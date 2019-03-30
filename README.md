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


## Run 1st and 2nd Test Case -- Load Google.com Webpage and Perform Search
In terminal window with the virtual environment activated:
1. run this command: `python tests/google_search_page_test.py -v`

## Run 3rd Test Case -- AOL Mail App
In terminal window with the virtual environment activated:
1. run this command: `python tests/aol_mail_app_test.py -v`

## Run All Tests
In the terminal window with the virtual environment activated:
1. run this command:  `python -m unittest discover -s tests -p "*_test.py" -v`


# Commentary 

## Overall

Desired Capability needs to be improved and loaded in a way that is more platform independent -- so that it can run on any developer's machine, on Sauce Labs, or BrowserStack without needing to modify the desired capabilities files.

For now, please review the two desired capability JSON file, and tweak as neede for your system.

## Commentary on Loading Google.com Website Test

As far as loading the Google search page, in the future I could ad voice search button and a few other elements that did not have clean and reliable attributes to build robust locators from, so I left them out.  The `aria-label` is likely constant so could be used to build an xpath locator but this value will vary based on the user's language preference, so is not a great candidate to build off of.

Note that for the purposes of this exercise, I have left out tackling localiztion.  The tests and page objects would need to be extended to accomodate loading different regional variations of the page (e.g. the Voice Search button that appears on the right hand side of the search box, is absent from the Canadian French version of the page.)

## Commentary on Performing Google Search Test

This is the standard search test of Google.  In the future we could add support for signed in versus not-signed in users.

## Commentary on AOL Mail App Test

This test is only partially done currently.  I rearched the point of loading the AOL signin page for mail from the MailTabPage page object -- but I'm not able to access the locators in the embedded webview that appears on first run.  Ideally I probably would have liked to separate out the Signin page with its webview as its own page object -- but until I got it working I wasn't sure if that would be appropriate or necessary.  