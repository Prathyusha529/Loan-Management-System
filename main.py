import mysql.connector
try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mypassword",
        database="loan_management"
    )
    cursor = con.cursor()
    print("Database Connected Successfully")
except mysql.connector.Error as e:
    print("Database Connection Failed")
    print(e)
    exit()


# ===================== CUSTOMER MANAGEMENT =====================

def add_customer():
    print("\n========== ADD CUSTOMER ==========")
    name = input("Enter Customer Name : ")
    phone = input("Enter Phone Number : ")
    email = input("Enter Email : ")
    address = input("Enter Address : ")
    dob = input("Enter Date Of Birth (YYYY-MM-DD): ")
    query = """INSERT INTO customers(name,phone,email,address,date_of_birth) VALUES(%s,%s,%s,%s,%s)"""
    cursor.execute(query,(name,phone,email,address,dob))
    con.commit()
    print("Customer Added Successfully")


def view_customer():
    query="select * from customers"
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        print("\n================ CUSTOMER LIST ================")
        print("ID\tNAME\tPHONE\tEMAIL\tADDRESS\tDOB")
        print("-"*100)
        for row in result:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5])
    else:
        print("No Customer Records Found")


def search_customer():
    customer_id=input("Enter Customer ID : ")
    query="select * from customers where customer_id=%s"
    cursor.execute(query,(customer_id,))
    result=cursor.fetchone()
    if result:
        print("\nCustomer ID :",result[0])
        print("Name        :",result[1])
        print("Phone       :",result[2])
        print("Email       :",result[3])
        print("Address     :",result[4])
        print("DOB         :",result[5])
    else:
        print("Customer Not Found")


def update_customer():
    customer_id=input("Enter Customer ID : ")
    query="select * from customers where customer_id=%s"
    cursor.execute(query,(customer_id,))
    result=cursor.fetchone()
    if result:
        name=input("Enter New Name : ")
        phone=input("Enter New Phone : ")
        email=input("Enter New Email : ")
        address=input("Enter New Address : ")
        dob=input("Enter New DOB : ")
        query="""update customers set name=%s,phone=%s,email=%s,address=%s,date_of_birth=%s
        where customer_id=%s"""
        cursor.execute(query,
        (name,phone,email,address,dob,customer_id))
        con.commit()
        print("Customer Updated Successfully")
    else:
        print("Customer Not Found")


def delete_customer():
    customer_id=input("Enter Customer ID : ")
    query="select * from customers where customer_id=%s"
    cursor.execute(query,(customer_id,))
    result=cursor.fetchone()
    if result:
        ch=input("Delete Customer (Y/N): ")
        if ch.upper()=="Y":
            query="delete from customers where customer_id=%s"
            cursor.execute(query,(customer_id,))
            con.commit()
            print("Customer Deleted Successfully")
        else:
            print("Deletion Cancelled")
    else:
        print("Customer Not Found")


# ===================== LOAN MANAGEMENT =====================

def add_loan():
    customer_id=input("Enter Customer ID : ")
    query="select * from customers where customer_id=%s"
    cursor.execute(query,(customer_id,))
    result=cursor.fetchone()
    if result is None:
        print("Customer Not Found")
        return
    loan_type=input("Enter Loan Type : ")
    principal=float(input("Enter Loan Amount : "))
    interest=float(input("Enter Interest Rate : "))
    months=int(input("Enter Loan Period (Months): "))
    loan_date=input("Enter Loan Date (YYYY-MM-DD): ")
    query="""insert into loans(customer_id,loan_type,principal_amount,interest_rate,tenure_months,disbursement_date,status)
    values(%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(query,(customer_id,loan_type,principal,interest,months,loan_date,"Active"))
    con.commit()
    print("Loan Added Successfully")


def view_loan():
    query="""select loan_id,customer_id,loan_type,principal_amount,interest_rate,tenure_months,disbursement_date,status from loans"""
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        print("\n================ LOAN LIST ================")
        print("LoanID\tCustID\tType\tAmount\tRate\tMonths\tDate\tStatus")
        print("-"*100)
        for row in result:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",
                  row[6],"\t",row[7])
    else:
        print("No Loan Records Found")


def search_loan():

    loan_id=input("Enter Loan ID : ")

    query="select * from loans where loan_id=%s"

    cursor.execute(query,(loan_id,))

    result=cursor.fetchone()

    if result:

        print("\n========== LOAN DETAILS ==========")
        print("Loan ID        :",result[0])
        print("Customer ID    :",result[1])
        print("Loan Type      :",result[2])
        print("Loan Amount    :",result[3])
        print("Interest Rate  :",result[4])
        print("Loan Period    :",result[5])
        print("Loan Date      :",result[6])
        print("Loan Status    :",result[7])

    else:

        print("Loan Not Found")


def update_loan():
    loan_id=input("Enter Loan ID : ")
    query="select * from loans where loan_id=%s"
    cursor.execute(query,(loan_id,))
    result=cursor.fetchone()
    if result:
        loan_type=input("Enter New Loan Type : ")
        amount=float(input("Enter New Loan Amount : "))
        interest=float(input("Enter New Interest Rate : "))
        months=int(input("Enter New Loan Period : "))
        loan_date=input("Enter New Loan Date (YYYY-MM-DD): ")
        status=input("Enter Status (Active/Closed): ")
        query="""update loans set loan_type=%s,principal_amount=%s,interest_rate=%s,tenure_months=%s,
        disbursement_date=%s,status=%s where loan_id=%s"""
        cursor.execute(query,
        (loan_type,amount,interest,months,loan_date,status,loan_id))
        con.commit()
        print("Loan Updated Successfully")
    else:
        print("Loan Not Found")


def delete_loan():
    loan_id=input("Enter Loan ID : ")
    query="select * from loans where loan_id=%s"
    cursor.execute(query,(loan_id,))
    result=cursor.fetchone()
    if result:
        ch=input("Delete Loan (Y/N): ")
        if ch.upper()=="Y":
            query="delete from loans where loan_id=%s"
            cursor.execute(query,(loan_id,))
            con.commit()
            print("Loan Deleted Successfully")
        else:
            print("Deletion Cancelled")
    else:
        print("Loan Not Found")



# ================= EMI MANAGEMENT ===================

def calculate_emi():
    loan_id=input("Enter Loan ID : ")
    query="""select principal_amount,interest_rate,tenure_months from loans where loan_id=%s"""
    cursor.execute(query,(loan_id,))
    result=cursor.fetchone()
    if result:
        principal=float(result[0])
        annual_rate=float(result[1])
        months=int(result[2])
        monthly_rate=annual_rate/(12*100)
        emi=(principal*monthly_rate*(1+monthly_rate)**months)/((1+monthly_rate)**months-1)
        total_amount=emi*months
        total_interest=total_amount-principal
        print("\n========== EMI DETAILS ==========")
        print("Loan Amount     :",principal)
        print("Interest Rate   :",annual_rate)
        print("Loan Period     :",months)
        print("Monthly EMI     :",round(emi,2))
        print("Total Interest  :",round(total_interest,2))
        print("Total Amount    :",round(total_amount,2))
    else:
        print("Loan Not Found")


def emi_schedule():
    loan_id=input("Enter Loan ID : ")
    query="""select principal_amount,interest_rate,tenure_months from loans where loan_id=%s"""
    cursor.execute(query,(loan_id,))
    result=cursor.fetchone()
    if result:
        principal=float(result[0])
        annual_rate=float(result[1])
        months=int(result[2])
        monthly_rate=annual_rate/(12*100)
        emi=(principal*monthly_rate*(1+monthly_rate)**months)/((1+monthly_rate)**months-1)
        balance=principal
        print("\n==============================================================")
        print("Month\tEMI\tInterest\tPrincipal\tBalance")
        print("==============================================================")
        for month in range(1,months+1):
            interest=balance*monthly_rate
            principal_paid=emi-interest
            balance=balance-principal_paid
            if balance<0:
                balance=0
            print(month,"\t",round(emi,2),"\t",round(interest,2),"\t\t",round(principal_paid,2),"\t\t",
                  round(balance,2))
    else:
        print("Loan Not Found")



# ================= PAYMENT MANAGEMENT ===================

def make_payment():
    loan_id=input("Enter Loan ID : ")
    payment_date=input("Enter Payment Date (YYYY-MM-DD): ")
    amount=float(input("Enter Amount : "))
    payment_mode=input("Enter Payment Mode (Cash/UPI/Card): ")
    query="""insert into payments(loan_id,payment_date,amount_paid,payment_mode) values(%s,%s,%s,%s)"""
    cursor.execute(query,(loan_id,payment_date,amount,payment_mode))
    con.commit()
    print("Payment Successful")


def view_payment():
    query="select * from payments"
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        print("\n================ PAYMENT HISTORY ================")
        print("ID\tLoan\tDate\t\tAmount\tMode")
        print("-"*70)
        for row in result:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])
    else:
        print("No Payment Records Found")


def search_payment():
    payment_id=input("Enter Payment ID : ")
    query="select * from payments where payment_id=%s"
    cursor.execute(query,(payment_id,))
    result=cursor.fetchone()
    if result:
        print("\nPayment ID  :",result[0])
        print("Loan ID       :",result[1])
        print("Payment Date  :",result[2])
        print("Amount Paid   :",result[3])
        print("Payment Mode  :",result[4])
    else:
        print("Payment Not Found")


def delete_payment():
    payment_id=input("Enter Payment ID : ")
    query="select * from payments where payment_id=%s"
    cursor.execute(query,(payment_id,))
    result=cursor.fetchone()
    if result:
        ch=input("Delete Payment (Y/N): ")
        if ch.upper()=="Y":
            query="delete from payments where payment_id=%s"
            cursor.execute(query,(payment_id,))
            con.commit()
            print("Payment Deleted Successfully")
        else:
            print("Deletion Cancelled")
    else:
        print("Payment Not Found")




# ================= REPORTS ===================

def customer_report():
    cursor.execute("select count(*) from customers")
    result=cursor.fetchone()
    print("\nTotal Customers :",result[0])


def loan_report():
    cursor.execute("select count(*) from loans")
    result=cursor.fetchone()
    print("\nTotal Loans :",result[0])


def payment_report():
    cursor.execute("select sum(amount_paid) from payments")
    result=cursor.fetchone()
    if result[0]==None:
        print("\nTotal Collection : 0")
    else:
        print("\nTotal Collection :",result[0])


def active_loans():
    cursor.execute("select * from loans where status='Active'")
    result=cursor.fetchall()
    if result:
        print("\n============== ACTIVE LOANS ==============")
        for row in result:
            print(row)
    else:
        print("No Active Loans")


def closed_loans():
    cursor.execute("select * from loans where status='Closed'")
    result=cursor.fetchall()
    if result:
        print("\n============== CLOSED LOANS ==============")
        for row in result:
            print(row)
    else:
        print("No Closed Loans")


# ================= LOAN CLOSURE ===================

def close_loan():
    loan_id=input("Enter Loan ID : ")
    query="select * from loans where loan_id=%s"
    cursor.execute(query,(loan_id,))
    result=cursor.fetchone()
    if result:
        query="update loans set status='Closed' where loan_id=%s"
        cursor.execute(query,(loan_id,))
        con.commit()
        print("Loan Closed Successfully")
    else:
        print("Loan Not Found")



# ================= LOGIN ===================

def login():
    username=input("Enter Username : ")
    password=input("Enter Password : ")
    query="""select * from users where username=%s and password=%s"""
    cursor.execute(query,(username,password))
    result=cursor.fetchone()
    if result:
        print("\nLogin Successful")
        return True
    else:
        print("\nInvalid Username or Password")
        return False


# ================= CUSTOMER MENU ===================

def customer_menu():
    while True:
        print("\n========== CUSTOMER MANAGEMENT ==========")
        print("1. Add Customer")
        print("2. View Customer")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Back")
        ch=input("Enter Your Choice : ")
        if ch=="1":
            add_customer()
        elif ch=="2":
            view_customer()
        elif ch=="3":
            search_customer()
        elif ch=="4":
            update_customer()
        elif ch=="5":
            delete_customer()
        elif ch=="6":
            break
        else:
            print("Invalid Choice")


# ================= LOAN MENU ===================

def loan_menu():
    while True:
        print("\n========== LOAN MANAGEMENT ==========")
        print("1. Add Loan")
        print("2. View Loan")
        print("3. Search Loan")
        print("4. Update Loan")
        print("5. Delete Loan")
        print("6. Back")
        ch=input("Enter Your Choice : ")
        if ch=="1":
            add_loan()
        elif ch=="2":
            view_loan()
        elif ch=="3":
            search_loan()
        elif ch=="4":
            update_loan()
        elif ch=="5":
            delete_loan()
        elif ch=="6":
            break
        else:
            print("Invalid Choice")


# ================= EMI MENU ===================

def emi_menu():
    while True:
        print("\n========== EMI MANAGEMENT ==========")
        print("1. Calculate EMI")
        print("2. EMI Schedule")
        print("3. Back")
        ch=input("Enter Your Choice : ")
        if ch=="1":
            calculate_emi()
        elif ch=="2":
            emi_schedule()
        elif ch=="3":
            break
        else:
            print("Invalid Choice")


# ================= PAYMENT MENU ===================

def payment_menu():
    while True:
        print("\n========== PAYMENT MANAGEMENT ==========")
        print("1. Make Payment")
        print("2. View Payments")
        print("3. Search Payment")
        print("4. Delete Payment")
        print("5. Back")
        ch=input("Enter Your Choice : ")
        if ch=="1":
            make_payment()
        elif ch=="2":
            view_payment()
        elif ch=="3":
            search_payment()
        elif ch=="4":
            delete_payment()
        elif ch=="5":
            break
        else:
            print("Invalid Choice")


# ================= REPORT MENU ===================

def report_menu():
    while True:
        print("\n========== REPORTS ==========")
        print("1. Customer Report")
        print("2. Loan Report")
        print("3. Payment Report")
        print("4. Active Loans")
        print("5. Closed Loans")
        print("6. Back")
        ch=input("Enter Your Choice : ")
        if ch=="1":
            customer_report()
        elif ch=="2":
            loan_report()
        elif ch=="3":
            payment_report()
        elif ch=="4":
            active_loans()
        elif ch=="5":
            closed_loans()
        elif ch=="6":
            break
        else:
            print("Invalid Choice")


# ================= MAIN MENU ===================

def main_menu():
    while True:
        print("\n")
        print("====================================")
        print("      LOAN MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Customer Management")
        print("2. Loan Management")
        print("3. EMI Management")
        print("4. Payment Management")
        print("5. Loan Closure")
        print("6. Reports")
        print("7. Logout")
        print("8. Exit")
        choice=input("Enter Your Choice : ")
        if choice=="1":
            customer_menu()
        elif choice=="2":
            loan_menu()
        elif choice=="3":
            emi_menu()
        elif choice=="4":
            payment_menu()
        elif choice=="5":
            close_loan()
        elif choice=="6":
            report_menu()
        elif choice=="7":
            print("Logged Out Successfully")
            break
        elif choice=="8":
            print("Thank You")
            con.cose()
            exit()
        else:
            print("Invalid Choice")


# ================= PROGRAM START ===================

if login():
    main_menu()
cursor.close()
con.close()