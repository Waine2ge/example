
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male nor tall")


