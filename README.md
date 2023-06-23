# module_4
def Palindrome_test_string(input_str):

    lower = input_str.lower()

    return lower == lower[::-1]



print(Palindrome_test_string('лепсспел'))

print(Palindrome_test_string('helloworld'))
