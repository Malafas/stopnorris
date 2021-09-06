*** Settings ***
Documentation     Simple test using Selenium, imported variables and keywords from python.
Suite Setup       Open Page and Navigate to Stopwatch
Suite Teardown    Close Browser
Resource          keywords.robot

*** Test Cases ***
FE-01 Initial Values
    [Documentation]    Verify that the initial values are displayed when the stopwatch option is first started.
    [Tags]    FE
    Validate Initial Values


