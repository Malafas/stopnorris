from robot.api.deco import keyword
from jsonschema import validate

@keyword("Validate Schema")
def validate_schema(schema, payload):
    """ Validates JSON schema """
    print("Payload: " + str(payload))
    print("Expected Schema: " + str(schema))
    validate(instance=payload, schema=schema)
