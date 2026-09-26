import re

def check(value):
    conditions = r"^(?!.*(\d)\1\1\1)([456]\d{15}|[456]\d{3}-\d{4}-\d{4}-\d{4})$"

    if not re.match(conditions, value):
        print("Invalid")
        return

    value = value.replace("-", "")
    
    if re.search(r"(\d)\1\1\1", value):
        print("Invalid")
    else:
        print("Valid")

count = int(input())
for i in range(count):
    value = input()
    check(value)

