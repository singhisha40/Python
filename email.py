#This python code slices emails and printsg the username and doman separately.
#Simple Project


print("Please enter your Email Id:")


email = input().strip()

if email.find("@") != -1:
    username = email[:email.index("@")]     
    domain = email[email.index("@") + 1:]   
    print("Your username is: ", username)
    print("Your domain is: ", domain)
else:
    print("Please enter a valid Email Id.")
