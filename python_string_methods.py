test_str = 'test String string Test'

#Capitialize Method
print("==========Capitialize Method==============")
print("---Sets the First Letter to a captial and rest to .lower()")
print(test_str.capitalize())


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

#=========endswith() Method============#
#Syntax
#str.endswith(suffix[, start[, end]])
"""Parameters"""
#suffix - String or tuple of suffixes to be checked
#start (optional) - Beginning position where suffix is to be checked within the string.
#end (optional) - Ending position where suffix is to be checked within the string.



print(f"============Endswith() Method===============")
text = "Python is pog."

result = text.endswith('pog')
#returns false
print(result)

result = text.endswith('pog.')
# returns True
print(result)

#==============expandtabs() method================#
# Syntax
#string.expandtabs(tabsize)

print(f"============Expand Tabs Method===========")
expand_string = 'xyz\t12345\tabc'
expand_string_result = expand_string.expandtabs()
print(expand_string_result)

#===================Endcode() str method()===========#
print("===========Encoding Methods===============")
#Syntax 
# string.encode(encoding="UTF-8", errors="strict")
unicode_string = 'pythön!'
print('unicode_string',unicode_string)
string_utf = unicode_string.encode()
print("encoded string", string_utf)
"""The string is: pythön!
The encoded version is: b'pyth\xc3\xb6n!'
"""

#===================Find() method======================#
#syntax 
#str.find(sub[, start[, end]])
"""params"""
#sub - It's the substring to be searched in the str string.
#start and end (optional) - substring is searched within str[start:end]
print("==================find() method===================")
quote = 'Let it be, let it be, let it be'

find_result = quote.find('let it')
print("Substring 'let it':", find_result)

find_result = quote.find('small')
print("Substring 'small ':", find_result)

# How to use find()
if  (quote.find('be,') != -1):
  print("Contains substring 'be,'")
else:
  print("Doesn't contain substring")


#=======================Format Method===================# 
print("==================Format method=============")
# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))



