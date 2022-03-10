def get_res_data(status, message=None, data=None, **kwargs):
    if message is None and data is None:
        raise ValueError("Message or data is required")
    return {"status": status, "message": message, "data": data, **kwargs}
