'''
Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.
'''
Regex_Pattern = r"(?<=[13579])\d"	# Do not delete 'r'.
import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))
