from datetime import datetime

def CreateUsers():
    print("Create users, passwords, and roles")
    UserFile = open("Users.txt", "a+")
    while True:
        username = GetuserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassword()
        userrole = GetUserRole()
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
        
    UserFile.close()
    printuserinfo()
    
def GetuserName():
    username = input("Enter a username or  'END' to quit: ")
    return username

def GetUserPassword():
    pwd = input("Enter a password: ")
    return pwd

def GetUserRole():
    userrole = input("Enter a role (Admin or User): ")
    while True:
        if userrole.upper() == "ADMIN" or userrole.upper() == "USER":
            return userrole
        else:
            userrole = input("Enter a role (Admin or User): ")
          
def printuserinfo():
    UserFile = open("Users.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpwd = UserList[1]
        userrole = UserList[2]
        print("User Name: ", username, "Password: ", userpwd, "Role: ", userrole)
        
def Login():
    UserFile = open("Users.txt", "r")
    UserList = []
    UserName = input("Enter your username: ")
    UserPwd = input("Enter your password: ")
    UserRole = "None"
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            return UserRole, UserName, UserPwd
        UserDetail = UserDetail.replace("\n", "")
        
        UserList = UserDetail.split("|")
        if UserName == UserList[0] and UserPwd == UserList[1]:
            UserRole = UserList[2]
            return UserRole, UserName
        
    return UserRole, UserName

def GetEmpName():
    empname = input("Enter the employee's name: ")
    return empname

def GetDatesWorked():
    fromdate = input("Enter the date worked (mm/dd/yyyy): ")
    todate = input("Enter the date worked (mm/dd/yyyy): ")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input("Enter the number of hours worked: "))
    return hours

def GetHourlyRate():
    rate = float(input("Enter the hourly rate: "))
    return rate

def GetTaxRate():
    taxrate = float(input("Enter the tax rate: "))
    taxrate = taxrate / 100
    return taxrate

def CalculateTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    TotEmployees = [0]
    TotHours = 0.00
    TotGrossPay = 0.00
    TotIncomeTax = 0.00
    TotNetPay = 0.00
    UserFile = open("Employees.txt", "r")
    while True:
        rundate = input("Enter start date for report (mm/dd/yyyy): or All for all data: ")
        if rundate.upper() == "ALL":
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try Again.")
            print()
            continue
        
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "")
        EmpList = EmpDetail.split("|")
        empname = EmpList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(EmpList[1], "%m/%d/%Y")
            if (checkdate < rundate):
                continue
            
        todate = EmpList[1]
        empName = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate = float(EmpList[4])
        taxrate = float(EmpList[5])
        grosspay = float(EmpList[6])
        grosspay, incometax, netpay= CalculateTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{taxrate:,.2f}", f"{grosspay:,.2f}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHours"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay
        DetailsPrinted = True
        
    if (DetailsPrinted):
        PrintTotals(EmpTotals)
    else:
        print("No data found.")
        
def PrintTotals(EmpTotals):
        print("Total Employees: ", EmpTotals["TotEmp"])
        print("Total Hours: ", f"{EmpTotals['TotHours']:,.2f}")
        print("Total Gross Pay: ", f"{EmpTotals['TotGrossPay']:,.2f}")
        print("Total Income Tax: ", f"{EmpTotals['TotTax']:,.2f}")
        print("Total Net Pay: ", f"{EmpTotals['TotNetPay']:,.2f}")
        
if __name__ == "__main__":
    CreateUsers()
    print()
    print("Data Entry")
    UserRole, UserName = Login()
    DetailsPrinted = False
    EmpTotals = {}
    if (UserRole.upper() == "NONE"):
        print(UserName, "is not a valid user.")
    else:
        if (UserRole.upper() == "ADMIN"):
            EmpFile = open("Employees.txt", "a+")
            while True:
                empname = GetEmpName()
                if (empname.upper() == "END"):
                    break
                fromdate, todate = GetDatesWorked()
                hours = GetHoursWorked()
                hourlyrate = GetHourlyRate()
                taxrate = GetTaxRate()
                EmpDetail = fromdate + "|" + todate + "|" + empname + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxrate) + "\n"
                EmpFile.write(EmpDetail)
                
            EmpFile.close()
            
        printinfo(DetailsPrinted)
        
        
    
   
    
    
        