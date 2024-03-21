def format_city_country(city, country, population=None):
    """Return a formatted string: City, Country - population xxx."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

