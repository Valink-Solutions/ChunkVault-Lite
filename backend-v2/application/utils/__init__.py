def remove_none_values(dict: dict) -> dict:
    return {k: v for k, v in dict.items() if v is not None}
