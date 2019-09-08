# hello-world
user_temp = input("Please enter the temperature in Celsius that you want to convert to Farenheit: ")
def converter(number_in_c):
    return number_in_c * 9 / 5 + 32

if user_temp is float:
    number_in_f = converter(user_temp)
    print("Here is your temperature in Farenheit: ")
    print(number_in_f)

else:
    print("Sorry, your temperature is not valid")
  
