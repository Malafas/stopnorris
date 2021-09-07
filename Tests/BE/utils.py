import json
import re
import datetime
from robot.api.deco import keyword
from jsonschema import validate

@keyword("Validate Schema")
def validate_schema(schema, payload):
    """ Validates JSON schema """
    print("Payload: " + str(payload))
    print("Expected Schema: " + str(schema))
    validate(instance=payload, schema=schema)

@keyword("Validate Random Payload")
def validate_random_payload(payload, expected_values_random, categories_array):
    """  Validates random joke payload values """
    data = json.dumps(payload)
    payload_dict = json.loads(data)
    print("The converted dictionary : " + str(payload_dict))

    categories = False
    created_at = False
    icon_url   = False
    id_pl      = False
    updated_at = False
    url        = False
    regex_id_pattern = '^[a-zA-Z0-9-_]{22}$'
    expected_url = expected_values_random["url"]+payload_dict["id"]

    # categories
    if not payload_dict["categories"]:
        categories = True
        print("Value for categories is correct.")
    elif payload_dict["categories"][0] in categories_array:
        categories = True
        print("Value for categories is correct.")
    else:
        print("Value for categories is incorrect.")
    print(payload_dict["categories"])
    # created_at
    try:
        datetime.datetime.strptime(payload_dict["created_at"], '%Y-%m-%d %H:%M:%S.%f')
        created_at = True
        print("Value for created_at is correct.")
    except ValueError:
        print("Value for created_at is incorrect.")
    print(payload_dict["created_at"])
    # icon_url
    if payload_dict["icon_url"] == expected_values_random["icon_url"]:
        icon_url = True
        print("Value for icon_url is correct.")
    else:
        print("Value for icon_url is incorrect.")
    print(payload_dict["icon_url"])
    # id
    if re.match(regex_id_pattern, payload_dict["id"]):
        id_pl = True
        print("Value for id is correct.")
    else:
        print("Value for id is incorrect.")
    print(payload_dict["id"])
    # updated_at
    try:
        datetime.datetime.strptime(payload_dict["updated_at"], '%Y-%m-%d %H:%M:%S.%f')
        updated_at = True
        print("Value for updated_at is correct.")
    except ValueError:
        print("Value for updated_at is incorrect.")
    print(payload_dict["updated_at"])
    # url
    if payload_dict["url"] == expected_url:
        url = True
        print("Value for url is correct.")
    else:
        print("Value for url is incorrect.")
    print(payload_dict["url"])

    # Exit criteria
    if categories and created_at and icon_url and id_pl and updated_at and url:
        print("PASS : Payload is correct")
    else:
        raise ValueError("FAIL : Payload has unexpected results.")
