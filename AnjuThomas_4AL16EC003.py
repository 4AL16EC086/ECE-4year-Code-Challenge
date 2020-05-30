def credentials():
    for i in range (0,3):
        name= input("Name ")
        password=input("Password ")

        if name== "Micheal" and password== "e3$WT89x":
           return( print("Hi Micheal"))
            
        else:
            print("Invalid credentials")
    return(print("Account Locked"))

credentials()


