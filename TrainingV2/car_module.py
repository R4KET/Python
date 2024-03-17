def car(make, model, **kwargs):
    """Building a dictionary containing everything we know about a user."""
    kwargs['make'] = make
    kwargs['model'] = model
    return kwargs