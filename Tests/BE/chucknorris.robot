*** Settings ***
Documentation     Chuck Norris API test suite using RobotFramework Requests.
Resource           keywords.robot

*** Test Cases ***
BE-01 Jokes Categories
    [Documentation]    Get jokes categories' list.
    [Tags]    BE
    Get JSON    ${endpoint_categories}
    Validate Schema    ${schema_categories}    ${payload_categories}
    Lists Should Be Equal    ${response_json}    ${payload_categories}

