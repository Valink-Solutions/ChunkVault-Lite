def remove_none_values(dict: dict) -> dict:
    return {k: v for k, v in dict if v is not None}