*** Settings ***
Documentation     Stopwatch website testing using Selenium.
Suite Setup       Open Page and Navigate to Stopwatch
Suite Teardown    Close Browser
Resource          keywords.robot

*** Test Cases ***
FE-01 Initial Values
    [Documentation]    Verify that the initial values are displayed when the stopwatch option is first started.
    [Tags]    FE
    Validate Initial Values

FE-03 Initial Values
    [Documentation]    Verify that the stopwatch time returns to the initial value when reset.
    [Tags]    FE
    Validate Initial Values
    Start and Stop for a Random time    1   5
    Reset Stopwatch

