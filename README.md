This is the first certification project in the [Python Certification Course](https://www.freecodecamp.org/learn/python-v9) on freeCodeCamp. 

**bold text**Project Instructions:**bold text**   

You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

The add_setting function should:

Convert the key and value to lowercase.
If the key exists, return Setting '[key]' already exists! Cannot add a new setting with this name.
If the key doesn't exist, add the key-value pair to the given dictionary of settings and return Setting '[key]' added with value '[value]' successfully!
The messages returned should have the key and value in lowercase.
You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

The update_setting function should:

Convert the key and value to lowercase.
If the key exists, update its value in the given dictionary of settings and return Setting '[key]' updated to '[value]' successfully!
If the key doesn't exist, return Setting '[key]' does not exist! Cannot update a non-existing setting.
The messages returned should have the key and value in lowercase.
You should define a function named delete_setting with two parameters representing a dictionary of settings and a key.

The delete_setting function should:

Convert the key passed to lowercase.
If the key exists, remove the key-value pair from the given dictionary of settings and return Setting '[key]' deleted successfully!
If the key does not exist, return Setting not found!
The messages returned should have the key in lowercase.
You should define a function named view_settings with one parameter representing a dictionary of settings.

The view_settings function should:

Return No settings available. if the given dictionary of settings is empty.
If the dictionary contains any settings, return a string displaying the settings. The string should start with Current User Settings: followed by the key-value pairs, each on a new line and with the key capitalized, and the string should end with a newline character after the last setting. For example, view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) should return:
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high

For testing the code, you should create a dictionary named test_settings to store some user configuration preferences.
