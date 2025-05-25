from base64 import b64decode


def decode_from_base64(data):
    if isinstance(data, str):
        return b64decode(data, validate=True)
    elif isinstance(data, dict):
        return {key: decode_from_base64(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [decode_from_base64(item) for item in data]
    else:
        return data
