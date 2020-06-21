import datetime

class Header:

    def header(self):

         print("::::::::::::::::::::::::Alphatuts++:::::::::::::::::::::::")
         print("::::::::::::::: Let's Learn Coding Together ::::::::::::::")

    def info(self):

         print("\n\n\n        Author : Usama Shafique")
         print("        Github : usamashafqiu3 ")
         print("     Software Engineer | enterprenurer | Freelancer")
         print("      SOFTWARE ENGINEERING DEPARTMENT")
         print(" ARMY PUBLIC COLLEGE OF MANAGMENT & SCIENCES")
         print("Visit My Portfolio :https://github.com/usama-shafiqu3")

    def data_time(self):

        PST = datetime.datetime.now()
        print(PST.strftime("%A, %m %B, %Y %I:%M:%S %p"))