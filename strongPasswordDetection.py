# Strong Password Detection
# Write a function that uses regular expressions to make sure least eight characters long,
# contains both uppercase and lowercase characters, and has at least one digit.
# we need to verify the string against multiple regex patterns to validate its strength.

# module used is regular expression
import re

# The (?=pattern) is known as positive lookahead. 
#positive lookahead ^(?=.{1,64}@) sets maximum of 64 characters before the '@' sign 
#VERBOSE This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments.
#Whitespace within the pattern is ignored, except when in a character class, or when preceded by an unescaped backslash, or within tokens like *?, 
passwordRegex = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])                # at least two capital letters
    (?=.*[!@#$&*])                     # at least one of these special characters
    (?=.*[0-9].*[0-9])                 # at least two numeric digits
    (?=.*[a-z].*[a-z].*[a-z])          # at least three lower case letters
    .{10,}                              # at least 10 total digits
    $
    )''', re.VERBOSE)

def userInputPasswordCheck():
    ppass = input("Enter a potential password: ")
    mo = passwordRegex.search(ppass)
    if (not mo):
        print("Not strong, bling blong")
        return False
    else:
        print("Long, Strong, and down to get the crypto on")
        return True


userInputPasswordCheck()


