# Endpoints
endpoint_categories = "https://api.chucknorris.io/jokes/categories"
endpoint_random = "https://api.chucknorris.io/jokes/random"

# Schemas
schema_categories = {"type": "array"}
schema_random = {
    "type" : "object",
    "properties": {
        "categories": {"type" : "array"},
        "created_at": {"type" : "string"},
        "icon_url": {"type" : "string"},
        "id": {"type": "string"},
        "updated_at": {"type": "string"},
        "url": {"type": "string"},
        "value": {"type": "string"},
    },
}
# Payload Validations
payload_categories_validation = ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money',
                      'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']
expected_values_random = {
        "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
        "url": "https://api.chucknorris.io/jokes/",
}
