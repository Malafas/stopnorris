*** Settings ***
Library           SeleniumLibrary
Library           BuiltIn
Library           utils.py
Variables         variables.py

*** Keywords ***
Open Page and Navigate to Stopwatch
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Click Element    ${stopwatch_menu_button}

Validate Initial Values
    Capture Page Screenshot
    Wait Until Element Is Visible    ${start_button}
    Element Text Should Be    ${start_button}    ${start_button_text}
    Element Text Should Be    ${reset_button}    ${reset_button_text}
    Page Should Contain    ${initial_value}

Start and Stop for a Random time
    [Arguments]    ${min}   ${max}
    Click Element    ${start_button}
    Element Text Should Be    ${stop_button}    ${stop_button_text}
    Element Text Should Be    ${lap_button}    ${lap_button_text}
    ${stop_time}    Generate Random Number    ${min}   ${max}
    Sleep    ${stop_time}s
    Click Element    ${stop_button}
    Element Text Should Be    ${start_button}    ${start_button_text}
    Element Text Should Be    ${reset_button}    ${reset_button_text}
    Capture Page Screenshot
    ${stopwatch_time}    Convert Int to Time    ${stop_time}
    Page Should Contain    ${stopwatch_time}

Reset Stopwatch
    Click Element    ${reset_button}
    Capture Page Screenshot
    Page Should Contain    ${initial_value}


