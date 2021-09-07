*** Settings ***
Documentation     Chuck Norris API test suite using RobotFramework Requests.
Resource          keywords.robot

*** Test Cases ***
BE-01 Jokes Categories
    [Documentation]    Verify the categories list values.
    [Tags]    BE
    Get JSON    ${endpoint_categories}
    Validate Schema    ${schema_categories}    ${response_json}
    Lists Should Be Equal    ${response_json}    ${payload_categories_validation}

BE-02 Random Joke
    [Documentation]    Verify a retrieved random joke.
    [Tags]    BE
    Get JSON    ${endpoint_random}
    Validate Schema    ${schema_random}    ${response_json}
    Validate Random Payload    ${response_json}    ${expected_values_random}    ${payload_categories_validation}

