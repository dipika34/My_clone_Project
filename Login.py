print('"/Login Project for App using Python in console/"')

userName = input("Enter your UserName:")
entered_userName = input("Have you entered UserName?")
password = int(input("Enter your password:"))
entered_password = int(input("Have you entered your password:"))
if(userName == entered_userName) and (password == entered_password):
    print("Successfully signed in!")
    
else:
    print("Incoorect userName or password!")
    print("forgot your passowrd?")
print("-----------or----------")
print("Do you have Gmail Account?")
