def is_valid_number(s):
    try:
        float(s)
        return True
    except valueerror:
        return False

s = input("Enter a string: ")
if is_valid_number(s):
    print(s, "is a valid number")
else:
    print(s, "is not a valid number")
