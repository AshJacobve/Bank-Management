import mysql.connector
import os
import random
import time




conn = mysql.connector.connect(host='localhost', database='bankdb2', user='root', password='ashkechumve', buffered=True)
cursor = conn.cursor()


def clear():
    os.system('cls')

def incorrect():
    print("Invalid Input")

class Admin:

    def __init__(self):
        self.id = "AshJacob"
        self.passkey = "ashkechumve"
        self.access = False

    def admin_login(self):
        check_id = input("Enter admin id: ")
        check_pass = input("Enter passkey: ")
        if (check_id == self.id and check_pass == self.passkey):
            self.access = True

        else:
            print("Incorrect Username and/or Password.")

    def view_closed(self):
        if (self.access == True):
            print("---------------All Accounts---------------")
            sql = """SELECT * FROM bankdb2.closedacc"""
            cursor.execute(sql)
            for i in cursor:
                print(i)



class bank:
    def crypto(self):
          print("Which cryptocurrency would you like to buy?\n\
              [1]Bitcoin (BTC)\n\
              [2]Ethereum (ETH)\n\
              [3]Tether (USDT)\n\
              [4]Binance Coin (BNB)\n\
              [5]U.S. Dollar Coin (USDC)")
          cryp=int(input()) 
          if cryp==1:
                              amount2=int(input("How much would you like to buy with?"))
                              converted=amount2/(81.566*17266)
                              rounded='%.2f'%converted
                              print("You have purchased "+ rounded +"% of a BTC.")
                              bank_object.removecash(amount2)            
          if cryp==2:
                              amount2=int(input("How much would you like to buy with?"))

                              converted=amount2/(81.566*1331)
                              rounded='%.2f'%converted
                              print("You have purchased "+ int(rounded)/100 +"coins of a ETH.")
                              bank_object.removecash(amount2)  
          if cryp==3:
                              amount2=int(input("How much would you like to buy with?"))

                              converted=amount2/(81.566*1.02)
                              rounded='%.2f'%converted
                              print("You have purchased "+ rounded/100 +"coins of a USDT.")
                              bank_object.removecash(amount2)
          if cryp==4:
                              amount2=int(input("How much would you like to buy with?"))
                              print("You have purchased "+ rounded +"coins of the BNB.")
                              converted=amount2/(81.566*275)
                              rounded='%.2f'%converted
                              print("YYou have purchased "+ rounded/100 +"coins of a BNB.")
                              bank_object.removecash(amount2)
          if cryp==5:
                              amount2=int(input("How much would you like to buy with?"))
                              converted=amount2/(81.566*0.85)
                              rounded='%.2f'%converted
                              print("You have purchased ", float(rounded)/100 ,"coins of a USDC.")
                              bank_object.removecash(amount2)
    def stocks(self):
        print("Which cryptocurrency would you like to buy?\n\
              [1]Tesla, Inc (TSLA)\n\
              [2]Advanced Micro Devices, Inc. (AMD)\n\
              [3]Apple Inc. (AAPL)\n\
              [4]Amazon.com, Inc. (AMZN)\n\
              [5]NVIDIA Corporation(NVDA)")
        stock=int(input()) 
        if stock==1:
            cash=int(input("How much would you like to buy with?"))
            k=cash/(81.566*143.92)
            rk=float('%.2f'%k)
            print("You have purchased",rk/100	,"of TSLA.")
            bank_object.removecash(cash)

        if stock==2:
            cash=int(input("How much would you like to buy with?"))
            k=cash/(81.566*74.69)
            rk=float('%.2f'%k)
            print("You have purchased",rk/100	,"of AMD.")
            bank_object.removecash(cash)
            
        if stock==3:
            cash=int(input("How much would you like to buy with?"))
            k=cash/(81.566*142.35)
            rk=float('%.2f'%k)
            print("You have purchased",rk/100,"of AAPL.")
            bank_object.removecash(cash)

        if stock==4:
            cash=int(input("How much would you like to buy with?"))
            k=cash/(81.566*97.04)
            rk=float('%.2f'%k)
            print("You have purchased",rk/100,"of AMZN.")
            bank_object.removecash(cash)

        if stock==5:
            cash=int(input("How much would you like to buy with?"))
            k=cash/(81.566*192.27)
            rk=float('%.2f'%k)
            print("You have purchased",rk/100	,"of NVDA.")
            bank_object.removecash(cash)
    
    def removecash(self, amount):

        if self.client_details_list[4] == 'savings':
            sql1 = 'select * from bankdb2.savingsacc where accno =' + self.client_details_list[1] + ';'
            cursor.execute(sql1)

        if self.client_details_list[4] == 'current':
            sql2 = 'select * from bankdb2.currentacc where accno =' + self.client_details_list[1] + ';'
            cursor.execute(sql2)

        result = cursor.fetchone()
        left_cash = self.client_details_list[5] - amount
        print(amount ,"Rs. was deducted from your account.")
        self.client_details_list[5] = left_cash

        if left_cash > 0:
            if self.client_details_list[4] == 'savings':
                cursor.execute('select * from bankdb2.savingsacc;')
                sql = """update bankdb2.savingsacc set cash = %s where accno = %s"""
                cursor.execute(sql, (left_cash, self.client_details_list[1],))
                conn.commit()

            if self.client_details_list[4] == 'current':
                cursor.execute('select * from bankdb2.currentacc;')
                sql = """update bankdb2.currentacc set cash = %s where accno = %s"""
                cursor.execute(sql, (left_cash, self.client_details_list[1],))
                conn.commit()
        else:
            print("Insufficient Balance.")

        time.sleep(2)
        
    def __init__(self):
        self.client_details_list = []
        self.loggedin=False
        self.cashtransfer=False
        
    
        
    def register(self, name, address, acctype, password):

        accno = random.randint(100000, 999999)
        cash = int(input("Enter opening balance(greater than 5K for current acc.) : "))
        conditions = True

        if (acctype == 'current' and cash < 5000):
            conditions = False
            print("For current accounts opening balance should be greater than 5000")
            time.sleep(3)
            return

        if conditions == True:
            self.client_details_list = [name, accno, password, address, acctype, cash]
            if (acctype == 'savings'):
                sql1 = 'insert into savingsacc(naam,accno,passwd,address,acctype,cash) values (%s,%s,%s,%s,%s,%s);'
                cursor.execute(sql1, self.client_details_list)
                print("Account created successfully")
                print("Your account number is ", accno, ".")
            if (acctype == 'current'):
                sql2 = 'insert into currentacc(naam,accno,passwd,address,acctype,cash) values (%s,%s,%s,%s,%s,%s);'
                cursor.execute(sql2, self.client_details_list)
                print("Account created successfully")
                print("Your account number is ", accno, ".")
            if acctype != 'current' or acctype != 'current':
                print("Please choose a valid account type.")
                
            conn.commit()
            return

    def login(self, accno, password):

        actype = input("Enter your account type : ")
        if (actype == "savings"):
            sql = 'select * from bankdb2.savingsacc where accno =' + str(accno) + ';'
        elif (actype == "current"):
            sql = 'select * from bankdb2.currentacc where accno =' + str(accno) + ';'
        else:
            print("Please enter a valid account type.")
        cursor.execute(sql)
        result = cursor.fetchone()

        if result[1] == str(accno):
            if result[2] == str(password):
               self.loggedin = True

        if self.loggedin == True:
            print("You are logged in")
            self.client_details_list = [result[0], result[1], result[2], result[3], result[4], result[5]]
        else:
            print("Wrong details")

        time.sleep(2)

    def add_cash(self, amount):
        if amount > 0:
            self.client_details_list[5] += amount
            if self.client_details_list[4] == 'savings':
                cursor.execute('select * from bankdb2.savingsacc;')
                sql = """update bankdb2.savingsacc set cash = %s where accno = %s"""
                cursor.execute(sql, (self.client_details_list[5], self.client_details_list[1],))
                conn.commit()

            if self.client_details_list[4] == 'current':
                cursor.execute('select * from bankdb2.currentacc;')
                sql = """update bankdb2.currentacc set cash = %s where accno = %s"""
                cursor.execute(sql, (self.client_details_list[5], self.client_details_list[1],))
                conn.commit()

            print("Amount added successfully")

        else:
            print("Enter correct value of amount")

        time.sleep(3)

    def draw_cash(self, amount):

        if self.client_details_list[4] == 'savings':
            sql1 = 'select * from bankdb2.savingsacc where accno =' + self.client_details_list[1] + ';'
            cursor.execute(sql1)

        if self.client_details_list[4] == 'current':
            sql2 = 'select * from bankdb2.currentacc where accno =' + self.client_details_list[1] + ';'
            cursor.execute(sql2)

        result = cursor.fetchone()
        left_cash = self.client_details_list[5] - amount
        self.client_details_list[5] = left_cash

        if left_cash > 0:
            if self.client_details_list[4] == 'savings':
                cursor.execute('select * from bankdb2.savingsacc;')
                sql = """update bankdb2.savingsacc set cash = %s where accno = %s"""
                cursor.execute(sql, (left_cash, self.client_details_list[1],))
                conn.commit()
                print("Balance updated")

            if self.client_details_list[4] == 'current':
                cursor.execute('select * from bankdb2.currentacc;')
                sql = """update bankdb2.currentacc set cash = %s where accno = %s"""
                cursor.execute(sql, (left_cash, self.client_details_list[1],))
                conn.commit()
        else:
            print("Insufficient Balance.")

        time.sleep(2)
        



    def cash_transfer(self, amount, accno, recacctype):

        if recacctype == 'savings':
            sql3 = """select * from bankdb2.savingsacc where accno = %s"""
            cursor.execute(sql3, (accno,))
            result = cursor.fetchone()
            if result[1] == accno:
                self.cashtransfer = True
            else:
                return

        if recacctype == 'current':
            sql3 = """select * from bankdb2.currentacc where accno = %s"""
            cursor.execute(sql3, (accno,))
            result = cursor.fetchone()
            if result[1] == accno:
                self.cashtransfer = True
            else:
                return

        if self.cashtransfer == True:

            if self.client_details_list[4] == 'savings':
                sql1 = """select * from bankdb2.savingsacc where accno = %s"""
                cursor.execute(sql1, (self.client_details_list[1],))

            if self.client_details_list[4] == 'current':
                sql2 = """select * from bankdb2.currentacc where accno = %s"""
                cursor.execute(sql2, (self.client_details_list[1],))

            result = cursor.fetchone()
            total_cash = result[5] + amount
            left_cash = self.client_details_list[5] - amount
            self.client_details_list[5] = left_cash
            if amount > 0:
                if recacctype == 'savings':
                    cursor.execute('select * from bankdb2.savingsacc')
                    result = cursor.fetchone()
                    sql3 = """update bankdb2.savingsacc set cash =%s where accno = %s"""
                    cursor.execute(sql3, (total_cash, accno,))
                    conn.commit()

                if recacctype == 'current':
                    cursor.execute('select * from bankdb2.currentacc')
                    result = cursor.fetchone()
                    sql3 = """update bankdb2.currentacc set cash =%s where accno = %s"""
                    cursor.execute(sql3, (total_cash, accno,))
                    conn.commit()

                if self.client_details_list[4] == 'savings':
                    cursor.execute('select * from bankdb2.savingsacc')
                    sql = """update bankdb2.savingsacc set cash =%s where accno = %s"""
                    cursor.execute(sql, (self.client_details_list[5], self.client_details_list[1],))
                    conn.commit()

                if self.client_details_list[4] == 'current':
                    cursor.execute('select * from bankdb2.currentacc')
                    sql = """update bankdb2.currentacc set cash =%s where accno = %s"""
                    cursor.execute(sql, (self.client_details_list[5], self.client_details_list[1],))
                    conn.commit()

                print("Amount Transfered Successfully to", accno)
                print("Balance left =", self.client_details_list[5])
                time.sleep(2)

        else:
            print("Receiver's account does not exist.")
            time.sleep(2)



    def acc_close(self):
        clear()
        closed_date = input("Enter the closing date : ")
        if (self.client_details_list[4] == 'savings'):
            sql = 'insert into closedacc(naam,accno,address,acctype,closedate) values (%s,%s,%s,%s,%s);'
            cursor.execute(sql, (self.client_details_list[0], self.client_details_list[1], self.client_details_list[3],
                                 self.client_details_list[4], closed_date,))

            sql1 = """DELETE FROM savingsacc WHERE accno = %s"""
            cursor.execute(sql1, (self.client_details_list[1],))

            print("Account closed successfully!")

        if (self.client_details_list[4] == 'current'):
            sql = 'insert into closedacc(naam,accno,address,acctype,closedate) values (%s,%s,%s,%s,%s);'
            cursor.execute(sql, (self.client_details_list[0], self.client_details_list[1], self.client_details_list[3],
                                 self.client_details_list[4], closed_date,))

            sql1 = """DELETE FROM currentacc WHERE accno = %s"""
            cursor.execute(sql1, (self.client_details_list[1],))

            print("Account closed successfully!")

        time.sleep(2)
        conn.commit()

    def simpleinterest(self):
        if (self.client_details_list[4] == "savings"):
            interest = (self.client_details_list[5] * 1 * 7.5) / 100
            print("Simple interest for a year on amount ", self.client_details_list[5], "is", interest)
        else:
            print("Your account type is unsuitable!")
        time.sleep(3)
     
def crypto(self):
        print("Which cryptocurrency would you like to buy?\n\
              [1]Bitcoin (BTC)\n\
              [2]Ethereum (ETH)\n\
              [3]Tether (USDT)\n\
              [4]Binance Coin (BNB)\n\
              [5]U.S. Dollar Coin (USDC)")
        cryp=int(input()) 
        if cryp==1:
            wo=int(input("How much would you like to buy with?"))
            print("You have purchased"+wo/81.566*17,266+"% of a BTC.")
        if cryp==2:
            wo=int(input("How much would you like to buy with?"))
            print("You have purchased"+wo/81.566*1,331+"% of a ETH.")
        if cryp==3:
            wo=int(input("How much would you like to buy with?"))
            print("You have purchased"+wo/81.566*1.02+"% of the USDT.")
        if cryp==4:
            wo=int(input("How much would you like to buy with?"))
            print("You have purchased"+wo/81.566*275+"% of the BNB.")
        if cryp==5:
            wo=int(input("How much would you like to buy with?"))
            print("You have purchased"+wo/81.566*0.85+"% of the USDC.")
     
        

        
            
     

if __name__ == "__main__":

    bank_object=bank()
    clear()
    print("Welcome to 12-C Bank")
    print("[1].Login")
    print("[2].Create a new Account")
    print("[3].Admin Login")
    user=int(input("Select an option : "))

    if user == 1:
        clear()
        print("Logging in")
        accno = int(input("Enter account Number : "))
        password = input("Enter password : ")
        bank_object.login(accno, password)
        while True:
            if bank_object.loggedin:
                clear()
                print("[1].Add Amount")
                print("[2].Withdraw Amount")
                print("[3].Check Balance")
                print("[4].Transfer Money")
                print("[5].Close Account")
                print("[6].View Account Details")
                print("[7].Calculate interest on current balance")
                print("[8].Invest")
                print("[9].Logout")
                print("Enter your choice : ")
                login_user = int(input())

                if login_user == 1:
                    print("Balance =", bank_object.client_details_list[5])
                    amount = int(input("Enter amount : "))
                    bank_object.add_cash(amount)
                    print("\n[1].Back menu")
                    print("\n[2].Logout")
                    print("Enter your choice : ")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 2:
                    print("Balance =", bank_object.client_details_list[5])
                    amount = int(input("Enter amount : "))
                    bank_object.draw_cash(amount)
                    print("\n[1].Back menu")
                    print("\n[2].Logout")
                    print("Enter your choice : ")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 3:
                    clear()
                    print("Balance =", bank_object.client_details_list[5])
                    print("\n[1].Back menu")
                    print("\n[2].Logout")
                    print("Enter your choice : ")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 4:
                    clear()
                    print("Balance =", bank_object.client_details_list[5])
                    amount = int(input("Enter amount : "))
                    if amount >= 0 and amount <= bank_object.client_details_list[5]:
                        accno = input("Enter reciever's account number : ")
                        recacctype = input("Enter reciver's account type :")
                        bank_object.cash_transfer(amount, accno, recacctype)
                        print("\n[1].Back menu")
                        print("\n[2].Logout")
                        print("Enter your choice : ")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0:
                        print("Enter please correct value of amount")

                    elif amount > bank_object.client_details_list[5]:
                        print("Not enough balance")


                elif login_user == 5:
                    clear()
                    bank_object.acc_close()
                    break

                elif (login_user == 6):
                    clear()
                    if (bank_object.client_details_list[4] == 'savings'):
                        sql = """select* from savingsacc where accno=%s;"""
                        cursor.execute(sql, (bank_object.client_details_list[1],))

                    elif (bank_object.client_details_list[4] == 'current'):
                        sql = """select* from currentacc where accno=%s;"""
                        cursor.execute(sql, (bank_object.client_details_list[1],))

                    result = cursor.fetchone()
                    print("Name : {}\nAccount number : {}\nAddress : {}\nAccount type : {}\nBalance : {}".format(
                        result[0], result[1], result[3], result[4], result[5]))
                    time.sleep(4)

                elif login_user == 7:
                    clear()
                    bank_object.simpleinterest()
                    
                elif login_user == 8:
                    clear()
                    print("Would you Like to invest in Crypto or Stocks (1 or 2) ?")
                    choose = int(input())
                    if choose == 1:   
                       bank_object.crypto()
                    elif choose == 2:
                       clear()
                       bank_object.stocks()
                        

                elif login_user == 9:
                    break

    if user == 2:
        clear()
        print("--------------------ACCOUNT CREATION--------------------")
        name = input("Enter Name : ")
        password = input("Enter password : ")
        address = input("Enter address : ")
        acctype = input("Enter account type (savings/current) : ")
        bank_object.register(name, address, acctype, password)

    if user == 3:
        clear()
        Admin_object = Admin()
        Admin_object.admin_login()

        if (Admin_object.access == True):
            print("--------------------ADMIN ACCESS--------------------")
            print("\n[1].View closed accounts")
            print("\n[2].Logout")
            print("Enter your choice : ")
            choose = int(input())
            if choose == 1:
                Admin_object.view_closed()
            elif choose == 2:
                pass

        else:
            print("Cannot login!")

conn.close()
