test_settings = {
    "theme": "light", 
    "language": "English", 
    "notifications": "enabled"
}

def add_setting(settings_dict: dict, item: tuple):
    key, value = item
    key = key.lower()
    value = value.lower()

    if key in settings_dict:
       return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict: dict, item: tuple):
    key, value = item
    key = key.lower()
    value = value.lower()
    
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict: dict, key):
    key = key.lower()
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    
    return f"Setting not found!"

def view_settings(settings_dict):
    if not settings_dict:
        return 'No settings available.'

    result = "Current User Settings:\n"
    for key, value in settings_dict.items():
        result += f"{key.capitalize()}: {value}\n"
    return result


print(add_setting(test_settings, ('Volume', 'High')))
print(add_setting(test_settings, ('Brightness', 'High')))
print(update_setting(test_settings, ('Theme', 'Dark')))
print(delete_setting(test_settings, ('Brightness')))
print(view_settings(test_settings))
