def setattrs(obj: object, attrs: dict):
    for k, v in attrs.items():
        setattr(obj, k, v)
