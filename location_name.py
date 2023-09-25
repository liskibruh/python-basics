def get_location_name(city, country, population=''):
    if population:
        location = f"{city}, {country}- {population}"
    else:
        location = f"{city}, {country}"
    
    return location.title()