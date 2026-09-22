import re
string = input("enter")
if re.fullmatch(r'[a-zA-z0-9]+', string):
  print("string contains a-z A-Z 0-9")
else:
  print("does not contain")