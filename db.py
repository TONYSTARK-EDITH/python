import  sqlite3
md=sqlite3.connect("md.db")
cur=md.cursor()
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES (1,'TONYSTARK',01,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES (2,'pushpa',0,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES (3,'sankar',02,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES ( 4,'peper',03,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES (5,'ironman',04,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES (6,'Thor',05,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES (7,'captainamerica',07,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES ( 8,'blackwidow',06,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES (9,'hawkeye',8,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES (10,'loki',09,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES (11,'hulk',10,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES ( 12,'spiderman',11,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES (13,'john wick',12,'INDIA');")
cur.execute("INSERT INTO stu (ID, name,RANK,COUNTRY) VALUES (14,'groot',13,'INDIA');")
n=int(input("enter the no. of students\n"))
for i in range(n):
    a=int(input("enter the id\n"))
    b=input("enter the name\n")
    c=int(input("enter the rank\n"))
    try:
        cur.execute("INSERT INTO stu (I, name,RANK,COUNTRY) VALUES (?,?,?,'INDIA');", (a,b,c))
        md.commit()
        print("\nTHE STUDENT {} WITH THE ID {} HAS BEEN ADDED SUCCESSFULLY\n".format(b, a))
        
    except:
        print("\n ERROR IN  OPERATION ")
        md.rollback()
        break
md.commit()
