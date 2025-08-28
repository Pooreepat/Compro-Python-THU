def format_string(*args):
   return "".join(args).replace(" ", "-").upper()

print(format_string("Hello","World","We","are","INET"))
print(format_string("Python","is","fun"))
print(format_string("concatenate","these","string","please"))