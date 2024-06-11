from datetime import datetime

def CreateUsers():
    print("Create users, passwords, and roles")
    Userfile = open("Users.txt", "a+")
    while True:
        username = GetUserName():
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassword()
        userrole = GetUserRole()
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        Userfile.write(UserDetail)
        
    Userfile.close()
    printuserinfo()
        