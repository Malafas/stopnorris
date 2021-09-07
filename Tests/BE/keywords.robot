*** Settings ***
Library           RequestsLibrary
Library           JSONLibrary
Library           Collections
Variables         variables.py
Library           utils.py

*** Keywords ***
Get JSON
    [Documentation]    Gets a JSON payload.
    [Arguments]    ${endpoint}
    ${response}    GET    ${endpoint}    expected_status=200
    ${response_json}    Set Variable    ${response.json()}
    Log    ${response_json}    repr=True
    Set Test Variable    ${response_json}
