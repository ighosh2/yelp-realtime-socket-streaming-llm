config = {
    "openai": {
        "api_key": "your key here"
    },
    "kafka": {
        "sasl.username": "your username here",
        "sasl.password": "your password here",
        "bootstrap.servers": "your server here",
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'PLAIN',
        'session.timeout.ms': 50000
    },
    "schema_registry": {
        "url": "SCHEMA_REGISTRY_URL",
        "basic.auth.user.info": "SR_API_KEY:SR_API_SECRET"

    }
}