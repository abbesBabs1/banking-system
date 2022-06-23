import sys,random,time,pyttsx3
import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="myatm")
# print(mydb)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE myatm")
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customer (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), address VARCHAR(255), gender VARCHAR(255), account_type VARCHAR(255), pin VARCHAR(255), account_number VARCHAR(255), balance INT(255))")

text_speech = pyttsx3.init()
print("*****WELCOME TO MY BANKING SYSTEM*****")
var = "WELCOME TO MY BANKING SYSTEM"
text_speech.say(var)
text_speech.runAndWait()
time.sleep(1)
def open():
      print('''
      1. Open New Account
      2. Withdraw
      3. Deposit
      4. Transfer
      5. Check Account Details
      6. Close Account''')
      print("Select one from the above")
      user = input(">>> ")
      if user == "1":
            while True:
                  first_name = input("Enter your first name>>> ").capitalize()
                  if first_name != "":
                        break
            while True:
                  last_name = input("Enter your last name>>> ").capitalize()
                  if last_name != "":
                        break
            while True:
                  address = input("Enter your address>>> ").capitalize()
                  if address != "":
                        break
            while True:
                  gender = input("Male/female>>> ").capitalize()
                  if gender != "":
                        break
            while True:
                  acct_type = input("Visa/Master>>> ").capitalize()
                  if acct_type != "":
                        break
            while True:
                  try:
                        pin = int(input("Enter your 4 digit pin: "))
                        if pin != "":
                              break
                  except ValueError:
                        print("-----------------------------")
                        print("Please input only digits...")
                        print("-----------------------------")

            print("-----------------------------")
            print("Please wait while we generate your account number for you...")
            time.sleep(3)
            fullname = first_name + " " + last_name
            account_number = random.randint(1000000, 9000000000)

            balance = "0"
            print("-----------------------------")
            print("Dear " + fullname + " you have successfully open a banking account with my bank your account number is " + str(account_number))
            print("-----------------------------")
            mycursor = mydb.cursor()
            dev = "INSERT INTO customer (firstname, lastname, address, gender, account_type, pin, account_number, balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            n = (first_name, last_name, address, gender, acct_type, pin, account_number, balance)
            mycursor.execute(dev, n)
            mydb.commit()

#--------withdraw
      if user == "2":
            accno = input("Enter your account number>>> ")
            dp = int(input("Enter amount you want to withdraw>>> "))
            a = "SELECT balance FROM customer where account_number = %s"
            data = (accno,)
            mycursor = mydb.cursor()
            mycursor.execute(a, data)
            myresult = mycursor.fetchone()
            tam = myresult[0] - dp
            ev = "UPDATE customer SET balance = %s WHERE account_number= %s"
            d = (tam, accno)
            mycursor.execute(ev, d)
            mydb.commit()
            print("Please wait, while your withdraw is been processed...")
            time.sleep(3)
            print("-----------------------------")
            print("Dear customer you withdraw " + str(dp) + " from your account was successful, thanks for banking with us!!!")
            print("-----------------------------")

#--------------Deposit
      if user == "3":
            accno = input("Enter your account number>>> ")
            dp = int(input("Enter amount to be deposited>>> "))
            a = "SELECT balance FROM customer where account_number = %s"
            data = (accno,)
            mycursor = mydb.cursor()
            mycursor.execute(a, data)
            myresult = mycursor.fetchone()
            tam = myresult[0] + dp
            ev = "UPDATE customer SET balance = %s WHERE account_number= %s"
            d = (tam, accno)
            mycursor.execute(ev, d)
            mydb.commit()
            print("Please wait, while your request is been processed...")
            time.sleep(3)
            print("-----------------------------")
            print("Dear customer you deposited " + str(dp) + " into your account was successful, thanks for banking with us!!!")
            print("-----------------------------")

#----------Transfer
      if user == "4":
            accno = input("Enter your account number>>> ")
            dp = int(input("Enter amount you want to transfer>>> "))
            a = "SELECT balance FROM customer where account_number = %s"
            data = (accno,)
            mycursor = mydb.cursor()
            mycursor.execute(a, data)
            myresult = mycursor.fetchone()
            tam = myresult[0] - dp
            ev = "UPDATE customer SET balance = %s WHERE account_number= %s"
            d = (tam, accno)
            mycursor.execute(ev, d)
            mydb.commit()

            accno = input("Enter the receiver account number>>> ")
            a = "SELECT balance FROM customer where account_number = %s"
            data = (accno,)
            mycursor = mydb.cursor()
            mycursor.execute(a, data)
            myresult = mycursor.fetchone()
            tam = myresult[0] + dp
            ev = "UPDATE customer SET balance = %s WHERE account_number= %s"
            d = (tam, accno)
            mycursor.execute(ev, d)
            mydb.commit()
            print("Please wait...")
            time.sleep(3)
            print("-----------------------------")
            print("Transaction Successful!!!")
            print("-----------------------------")

#----------Account status
      if user == "5":
            accno = input("Enter your account number>>> ")

            a = "SELECT * FROM customer WHERE account_number = %s"
            data = (accno,)
            mycursor = mydb.cursor()
            mycursor.execute(a, data)
            myresult = mycursor.fetchone()
            for i in myresult:
                  print(i)

#-------------close Account
      if user == "6":
            accno = input("Enter your account number>>> ")
            mycursor = mydb.cursor()
            a = "DELETE FROM customer WHERE account_number = %s"
            data = (accno,)
            mycursor.execute(a, data)
            mydb.commit()
            time.sleep(3)
            print("-----------------------------")
            print("Dear customer you have Successfully close your account with my Bank")
            print("-----------------------------")

      mainMenu = input("Press <yes> to go back to main menu or <no> to exist?:yes/no>>> ")
      if mainMenu == "yes" or mainMenu == "Yes" or mainMenu == "YES":
            return open()
      else:
            text_speech = pyttsx3.init()
            print("-----------------------------")
            print("Thanks for Banking with us!!!")
            print("-----------------------------")
            var = "Thanks for Banking with us!!!"
            text_speech.say(var)
            text_speech.runAndWait()
            sys.exit()
open()


