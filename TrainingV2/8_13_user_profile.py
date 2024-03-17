def build_profile(first, last, **user_info):
    """Building a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Michal', 'R.', location='Cracow', field='Data Scienece', university="AGH")
print(user_profile)