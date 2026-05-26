str1 = "the" ## changing the capitalisation means it will return false, thus its case sensitive
str2 = "Thumbs up"
str3 = "Theatre can be boring"


def check_string(string):
    if string.startswith("The"):
        return "Found it!"
    else:
        return "Nope."

print(check_string(str1))  # Found it!
print(check_string(str2))  # Nope.
print(check_string(str3))  # Found it!

    