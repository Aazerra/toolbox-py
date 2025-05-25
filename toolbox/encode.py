from base64 import b64encode


def encode_to_base64(data):
    if isinstance(data, bytes) or isinstance(data, str):
        return b64encode(data).decode('utf-8')
    elif isinstance(data, dict):
        return {key: encode_to_base64(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [encode_to_base64(item) for item in data]
    else:
        return data
