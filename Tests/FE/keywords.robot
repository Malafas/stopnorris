*** Settings ***
Library           SeleniumLibrary
Library           BuiltIn
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

