from datetime import datetime
from datetime import date
import mysql.connector as sqlcon
con1=sqlcon.connect(host="localhost",user="root",passwd="root")
mycursor=con1.cursor(buffered=True)

mycursor.execute("Create database if not exists test8")
mycursor.execute("use test8")
mycursor.execute("create table if not exists stock(PID int Primary key,Pname varchar(30),Category varchar(5),Quantity int,Price float)")
mycursor.execute("insert into stock values(8989,'Denim Jeans','M',500,1499),(2356,'T-shirt','M',700,2000),(3546,'Plain-Shirt','M',400,1999),(3564,'Full Jacket','M',450,3699),(3579,'Trousers','M',300,1899),(4670,'Check-Shirt','M',500,1999),(4756,'Sports-Track','M',560,1900),(5690,'Half-Jacket','M',700,2599),(5786,'Shorts','M',900,2299),(6879,'Kurta','M',230,4000),(1358,'Suit','F',700,1499),(9866,'Jeans','F',1000,999),(8755,'Lehenga','F',1000,2499),(6532,'Gown','F',1000,1199),(5422,'Leggings','F',1000,499),(9753,'Skirt','F',1000,799),(7532,'Top','F',1000,399),(8744,'Plazo','F',1000,699),(9999,'Night-suit','F',1000,599),(7633,'Frock','F',1000,899)")
mycursor.execute("create table if not exists customer(CID int Primary key,Cname varchar(30),Phone int,Address varchar(30))")
mycursor.execute("create table if not exists invoice(InvoiceNo int Primary key AUTO_INCREMENT,CID int,Foreign Key(CID) references customer(CID))")
mycursor.execute("create table if not exists bill(CID int ,PID int,Pname varchar(30),quantity int,Total_Amount float,Foreign Key(PID) references Stock(PID),Foreign Key(CID) references customer(CID))")
mycursor.execute("create table if not exists user(Username varchar(30),Password varchar(30),Status varchar(30))")

###ADMIN FUNCTIONS###
def adminstock():
    print("\nWhat would you like to do? \n1.Add a column \n2.Remove a column \n3.Update data")
    inp=int(input("Enter your choice: "))
    if inp==1:
        d=input("\nEnter name of column to add: ")
        typo=int(input("Data type of column-\n1.varchar \n2.int \n3.date \n4.float \n"))
        if typo==1:
            s="alter table STOCK add %s varchar(40)"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==2:
            s="alter table STOCK add %s int"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==3:
            s="alter table STOCK add %s date"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==4:
            s="alter table STOCK add %s float"%(d)
            mycursor.execute(s)
            con1.commit()
        else:
            print("Incorrect input")
    elif inp==2:
        d=input("\nEnter name of column to delete: ")
        s="alter table STOCK drop column %s "%(d)
        mycursor.execute(s)
        con1.commit()
    elif inp==3:
        print("\nWhat would you like to do? \n1.Add data \n2.Delete data \n3.Change data")
        data=int(input("Enter choice: "))
        if data==1:
            pid=int(input("\nEnter PID: "))
            pname=input("Enter Pname: ")
            category=input("Enter Category: ")
            quant=int(input("Enter Quantity: "))
            price=int(input("Enter Price: "))
            s="insert into STOCK values(%s, %s, %s, %s, %s) "
            t=(pid, pname, category, quant, price)
            mycursor.execute(s, t)
            con1.commit()
        elif data==2:
            Id=int(input("\nEnter PID: "))
            s="delete from STOCK where PID=%s"%(Id)
            mycursor.execute(s)
            con1.commit()
        elif data==3:
            print("\nWhat would you like to change? \n1.PID \n2.Pname \n3.Category \n4.Quantity \n5.Price")
            what=int(input("Enter choice: "))
            if what==1:
                t=int(input("\nEnter PID to change: "))
                p=int(input("Enter new PID: "))
                s="update STOCK set PID=%s where PID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==2:
                t=int(input("\nEnter PID whose Pname has to be changed: "))
                p=input("Enter new Pname: ")
                s="update STOCK set Pname=%s where PID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==3:
                t=int(input("\nEnter PID whose Category has to be changed: "))
                p=int(input("Enter new Category: "))
                s="update STOCK set Category=%s where PID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==4:
                t=int(input("\nEnter PID whose Quantity has to be changed: "))
                p=int(input("Enter new Quantity: "))
                s="update STOCK set Quantity=%s where PID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==5:
                t=int(input("\nEnter PID whose Price has to be changed: "))
                p=int(input("Enter new Price: "))
                s="update STOCK set Price=%s where PID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()

def admincustomer():
    print("\nWhat would you like to do? \n1.Add a column \n2.Remove a column \n3.Update data")
    inp=int(input("Enter your choice: "))
    if inp==1:
        d=input("\nEnter name of column to add: ")
        typo=int(input("Data type of column-\n1.varchar \n2.int \n3.date \n4.float \n"))
        if typo==1:
            s="alter table customer add %s varchar(40)"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==2:
            s="alter table customer add %s int"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==3:
            s="alter table customer add %s date"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==4:
            s="alter table customer add %s float"%(d)
            mycursor.execute(s)
            con1.commit()
        else:
            print("Incorrect input")
    elif inp==2:
        d=input("\nEnter name of column to delete: ")
        s="alter table customer drop column %s "%(d)
        mycursor.execute(s)
        con1.commit()
    elif inp==3:
        print("\nWhat would you like to do? \n1.Add data \n2.Delete data \n3.Change data")
        data=int(input("Enter choice: "))
        if data==1:
            cid=int(input("\nEnter PID: "))
            cname=input("Enter Pname: ")
            phone=int(input("Enter Category: "))
            add=input("Enter Quantity: ")
            s="insert into STOCK values(%s, %s, %s, %s) "
            t=(cid, cname, phone, add)
            mycursor.execute(s, t)
            con1.commit()
        elif data==2:
            Id=int(input("\nEnter CID: "))
            s="delete from customer where CID=%s"%(Id)
            mycursor.execute(s)
            con1.commit()
        elif data==3:
            print("\nWhat would you like to change? \n1.CID \n2.Cname \n3.Phone \n4.Address")
            what=int(input("Enter choice: "))
            if what==1:
                t=int(input("\nEnter CID to change: "))
                p=int(input("Enter new CID: "))
                s="update customer set CID=%s where CID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==2:
                t=int(input("\nEnter CID whose Cname has to be changed: "))
                p=input("Enter new Cname: ")
                s="update customer set Cname=%s where CID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==3:
                t=int(input("\nEnter CID whose Phone has to be changed: "))
                p=int(input("Enter new Phone: "))
                s="update customer set Phone=%s where CID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==4:
                t=int(input("\nEnter CID whose Address has to be changed: "))
                p=input("Enter new Address: ")
                s="update customer set Address=%s where CID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()

def adminbilling():
    print("\nWhat would you like to do? \n1.Add a column \n2.Remove a column \n3.Update data")
    inp=int(input("Enter your choice: "))
    if inp==1:
        d=input("\nEnter name of column to add: ")
        typo=int(input("Data type of column-\n1.varchar \n2.int \n3.date \n4.float"))
        if typo==1:
            s="alter table BILL add %s varchar(40)"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==2:
            s="alter table BILL add %s int"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==3:
            s="alter table BILL add %s date"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==4:
            s="alter table BILL add %s float"%(d)
            mycursor.execute(s)
            con1.commit()
        else:
            print("Incorrect input")
    elif inp==2:
        d=input("\nEnter name of column to delete: ")
        s="alter table BILL drop column %s "%(d)
        mycursor.execute(s)
        con1.commit()
    elif inp==3:
        print("\nWhat would you like to do? \n1.Add data \n2.Delete data \n3.Change data")
        data=int(input("Enter choice: "))
        if data==1:
            cid=int(input("\nEnter CID: "))
            pid=int(input("Enter PID: "))
            pname=input("Enter PName: ")
            quantity=int(input("Enter Quantity: "))
            total=input("Enter TotalAmount: ")
            s="insert into BILL values(%s, %s, %s, %s, %s) "
            t=(cid, pid, pname, quantity, total)
            mycursor.execute(s, t)
            con1.commit()
        elif data==2:
            cid=int(input("\nEnter CID: "))
            pid=int(input("Enter PID: "))
            s="delete from BILL where CID=%s and PID=%s"
            o=(cid, pid)
            mycursor.execute(s, o)
            con1.commit()
        elif data==3:
            print("\nWhat would you like to change? \n1.CID \n2.CName \n3.PID \n4.PName \n5.Quantity \n6.TotalAmount ")
            what=int(input("Enter choice: "))
            if what==1:
                t=int(input("\nEnter CID to change: "))
                p=int(input("Enter new CID: "))
                s="update BILL set CID=%s where CID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==2:
                t=int(input("\nEnter CID whose CName has to be changed: "))
                p=input("Enter new CName: ")
                s="update BILL set CName=%s where CID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==3:
                t=int(input("\nEnter PID to change: "))
                p=input("Enter new PID: ")
                s="update BILL set PID=%s where PID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==4:
                t=input("\nEnter PID whose PName has to be changed: ")
                p=input("Enter new PName: ")
                s="update BILL set PName=%s where PID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==5:
                t=int(input("\nEnter PID whose Quantity has to be changed: "))
                p=input("Enter new Quantity: ")
                s="update BILL set Quantity=%s where PID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==6:
                t=int(input("\nEnter PID whose TotalAmount has to be changed: "))
                p=input("Enter new TotalAmount: ")
                s="update BILL set Total_Amount=%s where PID=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()

def admininvoice():
    print("\nWhat would you like to do? \n1.Add a column \n2.Remove a column \n3.Update data")
    inp=int(input("Enter your choice: "))
    if inp==1:
        d=input("\nEnter name of column to add: ")
        typo=int(input("Data type of column-\n1.varchar \n2.int \n3.date \n4.float \n"))
        if typo==1:
            s="alter table invoice add %s varchar(40)"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==2:
            s="alter table invoice add %s int"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==3:
            s="alter table invoice add %s date"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==4:
            s="alter table invoice add %s float"%(d)
            mycursor.execute(s)
            con1.commit()
        else:
            print("Incorrect input")
    elif inp==2:
        d=input("\nEnter name of column to delete: ")
        s="alter table invoice drop column %s "%(d)
        mycursor.execute(s)
        con1.commit()
    elif inp==3:
        print("\nWhat would you like to do? \n1.Add data \n2.Delete data \n3.Change data")
        data=int(input("Enter choice: "))
        if data==1:
            invno=int(input("Enter InvoiceNo: "))
            cid=int(input("Enter CID: "))
            s="insert into user values(%s, %s) "
            t=(invno, cid)
            mycursor.execute(s, t)
            con1.commit()
        elif data==2:
            invno=int(input("Enter InvoiceNo: "))
            s="delete from invoice where InvoiceNo=%s"%(InvoiceNo)
            mycursor.execute(s)
            con1.commit()
        elif dataa==3:
            print("\nWhat would you like to change? \n1.InvoiceNo \n2.CID")
            what=int(input("Enter choice: "))
            if what==1:
                t=int(input("\nEnter InvoiceNo to change: "))
                p=int(input("Enter new InvoiceNo: "))
                s="update invoice set InvoiceNo=%s where Invoice=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==2:
                t=int(input("\nEnter InvoiceNo whose CID has to be changed: "))
                p=int(input("Enter new CID: "))
                s="update invoice set CID=%s where InvoiceNo=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            
def adminuser():
    print("\nWhat would you like to do? \n1.Add a column \n2.Remove a column \n3.Update data")
    inp=int(input("Enter your choice: "))
    if inp==1:
        d=input("\nEnter name of column to add: ")
        typo=int(input("Data type of column-\n1.varchar \n2.int \n3.date \n4.float \n"))
        if typo==1:
            s="alter table user add %s varchar(40)"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==2:
            s="alter table user add %s int"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==3:
            s="alter table user add %s date"%(d)
            mycursor.execute(s)
            con1.commit()
        elif typo==4:
            s="alter table user add %s float"%(d)
            mycursor.execute(s)
            con1.commit()
        else:
            print("Incorrect input")
    elif inp==2:
        d=input("\nEnter name of column to delete: ")
        s="alter table user drop column %s "%(d)
        mycursor.execute(s)
        con1.commit()
    elif inp==3:
        print("\nWhat would you like to do? \n1.Add user \n2.Delete user \n3.Change data")
        data=int(input("Enter choice: "))
        if data==1:
            username=input("Enter Username: ")
            passwd=input("Enter Password: ")
            status=input("Enter Status: ")
            s="insert into user values(%s, %s, %s) "
            t=(username, passwd, status)
            mycursor.execute(s, t)
            con1.commit()
        elif data==2:
            use=input("\nEnter Username: ")
            s="delete from user where Username='%s'"%(use)
            mycursor.execute(s)
            con1.commit()
        elif data==3:
            print("\nWhat would you like to change? \n1.Username \n2.Password \n3.Status ")
            what=int(input("Enter choice: "))
            if what==1:
                t=input("\nEnter Username to change: ")
                p=input("Enter new Username: ")
                s="update user set Username=%s where Username=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==2:
                t=input("\nEnter Username whose Password has to be changed: ")
                p=input("Enter new Password: ")
                s="update user set Password=%s where Username=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()
            elif what==3:
                t=input("\nEnter Username whose Status has to be changed: ")
                p=input("Enter new Status: ")
                s="update user set Status=%s where Username=%s"
                x=(p, t)
                mycursor.execute(s, x)
                con1.commit()

def adminlogedin():
    print("\nWhat would you like to do? \n1.View all the tables \n2.Make changes to user \n3.Make changes to Stock \n4.Make changes to Bill \n5.Make changes to invoice \n6.Make changes to customer \n7.Log out")
    ch=int(input("Enter choice: "))
    if ch==1:
        mycursor.execute("show tables;")
        a=mycursor.fetchall()
        print("\nThe tables are:-" )
        for i in a:
            print(i)
        adminlogedin()            
    elif ch==2:
        adminuser()
        adminlogedin()
    elif ch==3:
        adminstock()
        adminlogedin()
    elif ch==4:
        adminbilling()
        adminlogedin()
    elif ch==5:
        admininvoice()
        adminlogedin()
    elif ch==6:
        admincustomer()
        adminlogedin()
    elif ch==7:
        print("\nSuccessfully logged out")

###STAFF###

def insertincust():    
    mycursor.execute("insert into customer values({},'{}',{},'{}')".format(+c,name,+c,add))
    con1.commit()

def Women():    
    cn=mycursor.execute("select Pname from stock where category='F'")
    n=mycursor.fetchall()
    for i in n:
        f=list(i)
        print(*f,sep = "\n")
    ch=input("Enter your choice name:")
    lst=[]
    cmd=mycursor.execute("Select PID,Pname,Price from stock where Pname='{}'".format(ch.lower()))
    r=mycursor.fetchall()
    print("\nPname              Cost       ")
    for i in r:
        list(i)
        print(i[1],"     ",i[2])
        lst.append(i)
    x=input("Do you want to buy it?")
    if x=="yes":
        qty=int(input("Enter quantity:"))
        mycursor.execute("select Quantity from stock where Pname='{}'".format(ch.lower()))
        p=mycursor.fetchall()
        for s in p:
            list(s)
            if qty <= s[0]:
                m=(s[0]- qty)
                mycursor.execute("update stock set Quantity = {} where Pname='{}'".format(m,ch.lower()))
                cmd=mycursor.execute("insert into bill values({},{},'{}',{},{})".format(+c,i[0],i[1],qty,qty*i[2]))
                con1.commit()
                print("Added to your bill")
            else:
                print("out of stock")
    
def Men():    
    cn=mycursor.execute("select Pname from stock where category='M'")
    n=mycursor.fetchall()
    for i in n:
        f=list(i)
        print(*f,sep = "\n")
    ch=input("Enter your choice name:")
    lst=[]
    cmd=mycursor.execute("Select PID,Pname,Price from stock where Pname='{}'".format(ch.lower()))
    r=mycursor.fetchall()
    print("\nPname              Cost       ")
    for i in r:
        list(i)
        print(i[1],"     ",i[2])
        lst.append(i)
    x=input("Do you want to buy it?")
    if x=="yes":
        qty=int(input("Enter quantity:"))
        mycursor.execute("select Quantity from stock where Pname='{}'".format(ch.lower()))
        p=mycursor.fetchall()
        for s in p:
            list(s)
            if qty < s[0]:
                m=(s[0]- qty)
                mycursor.execute("update stock set Quantity = {} where Pname='{}'".format(m,ch.lower()))
                cmd=mycursor.execute("insert into bill values({},{},'{}',{},{})".format(+c,i[0],i[1],qty,qty*i[2]))
                con1.commit()
                print("Added to your bill")
            else:
                print("out of stock")
                
def itemlist():
    print("Pname           Quantity     TotalCost")
    cmd=mycursor.execute("Select *from bill where CID=({})".format(+c))
    m=mycursor.fetchall()
    for i in m:
        list(i)
        print(i[2],"          ",i[3],"           ",i[4])

def bill():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    mycursor.execute("select sum(Total_Amount) from bill where CID=({})".format(+c))
    s=mycursor.fetchall()
    for i in s:
        list(i)
    print("\n")
    print("-"*102)
    print("Fashion Mart".center(102))
    print("-"*100)
    print("Name:",name )
    print("Contact no:",+c)
    print("invoice time :", current_time)
    print("invoice date:", today)
    print("-"*102)
    itemlist()
    print("\nTotal Price:", i[0], "Rs/-" )
    print("-"*102)
    print("Thank you for shopping with us!")
    print("Customer care number: 9871xxxxxx")
    print("Email: fashionmart@abc.com")
    print("Corporate office: N-32,Lodhi Road,New Delhi")
    print("-"*102)

def Catalogue():
    print("\nWhat would you like to view? ")
    print("1.Men section")
    print("2.Women Section")
    print("3.Show bill")
    print("4.Exit")
    c=int(input("Enter your choice:"))
    if c==1:
        Men()
        Catalogue()
    elif c==2:
        Women()
        Catalogue()
    elif c==3:
        bill()
    elif c==4:
        print("Thank you for using Fashion Portal".center(102))
    else:
        mainmenu()
        
def mainmenu():
    print("\n")
    print("-"*102)
    print("Main Menu".center(102))
    print("1.Catalogue".center(102))
    print("2.Bill".center(102))
    print("3.Exit".center(102))
    print("-"*102)
    ch=int(input("Enter your choice:"))
    if ch==1:
        Catalogue()
    elif ch==2:
        bill()
    elif ch==3:
        print("Thank you for using Fashion Portal".center(102))
              
print("\n!!!!WELCOME TO FASHION MART!!!!")
user=int(input("\nPlease login to continue:-\n1.Admin \n2.Staff \nEnter:"))
if user==1:
    u=input("\nEnter username: ")
    p=input("Enter password: ")
    if u=="admin" and p=="admin":
        print("\nWelcome Admin!")
        adminlogedin()

elif user==2:
    u=input("\nEnter username: ")
    p=input("Enter password: ")
    s="select Password from user"
    t=mycursor.execute(s)
    for i in t:
        if i==p:
            print("Fashion Mart".center(102))
            print("\n1. Stock changes \n2.Customer billing \n3.Log out")
            ch=int(input("Enter Choice:"))
            if ch==1:
                staffstock()
                stafflog()
            elif ch==2:
                c=int(input("Enter phone no:"))
                name=input("enter name:")
                add=input("enter address:")
                insertincust()
                mainmenu()
            elif ch==3:
                print("Successfully logged out")
                




        
        
    
    




