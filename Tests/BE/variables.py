# Endpoints
endpoint_categories = "https://api.chucknorris.io/jokes/categories"
endpoint_random = "https://api.chucknorris.io/jokes/random"

# Schemas
schema_test = {
    "type" : "object",
    "properties": {
        "price": {"type" : "number"},
        "name": {"type" : "string"},
    },
}

schema_categories = {"type": "array"}

# Payloads
payload_test = {'name': 'Eggs', 'price': 34.99}

payload_categories = ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money',
                      'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']
