test_str = 'test String string Test'

#Capitialize Method
print("==========Capitialize Method==============")
print("---Sets the First Letter to a captial and rest to .lower()")
print(test_str.capitalize())
print(f"========================================")

#============Center Method===============#
#Syntax
# string.center(width[, fillchar])
string = 'Test String'
new_string = string.center(24, '*')
print("===========.Center() method==========")
print("Centered String: ", new_string)

#==========Casefold Method==============#
#Syntax
#string.casefold()
case_test = "Lets keep GOING :pog:"
print("============.casefold() Method =============")
print(case_test.casefold())
print(f"========================================")

#=========Count Method===========#
#Syntax
#string.count(substring, start=..., end=...)
#--- The .count method returns the total number of occurences a substring appears in a main string
"""Parameters"""
#substring - string whose count is to be found.
#start (Optional) - starting index within the string where search starts.
#end (Optional) - ending index within the string where search ends.
main_string = "I am a gangster"
substring = "gangster"
counted = main_string.count(substring)
print(f"========.count() method=========")
print(f"main_sting has {counted} occurences of {substring}")
print(f"========================================")
#=========endswith() Method============#
#Syntax
#str.endswith(suffix[, start[, end]])
"""Parameters"""
#suffix - String or tuple of suffixes to be checked
#start (optional) - Beginning position where suffix is to be checked within the string.
#end (optional) - Ending position where suffix is to be checked within the string.


print(f"========================================")
print(f"============Endswith() Method===============")
text = "Python is pog."

result = text.endswith('pog')
#returns false
print(result)

result = text.endswith('pog.')
# returns True
print(result)
print(f"========================================")