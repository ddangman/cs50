# Ignores query and fragment

import re

url_input = input("URL: ").strip()

# (captured group)
# (?: non-capturing group)
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url_input, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))
# matches.group(0) is re.search input: url_input
#    print(matches.group(0))
