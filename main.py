from password_checker import check_password


print("==============================")
print(" Password Strength Checker ")
print("==============================")

password = input("Enter password: ")


score, strength, feedback = check_password(password)


print("\nResult:")
print("Score:", score, "/6")
print("Strength:", strength)


if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)
else:
    print("Excellent password!")