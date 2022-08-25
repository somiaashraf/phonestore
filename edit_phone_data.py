import sqlite3
def phone_table():
    db=sqlite3.connect('phonedata.db')
    cr=db.cursor()
    cr.execute("""create table if not exists phone1
                (
                id integer NOT NULL PRIMARY KEY,
                name text,
                type text,
                storage integer,
                memmory integer,
                colour text,
                price integer
            

                )""")
    cr.commit()
    cr.close()
#cr.execute("delete from Students")

# cr.execute("""insert into phone1(id,name,type,storage,memmory,colour,price)
#                             values(1,'Iphone7','Iphone','64','4','white',210)""")
# cr.execute("""insert into phone1(id,name,type,storage,memmory,colour,price)
#                             values(2,'Redmi9','shawme','128','8','white',2000)""")
# cr.execute("""insert into phone1(id,name,type,storage,memmory,colour,price)
#                             values(3,'Iphone7','shawme','128','8','blue',230)""")
# cr.execute("""insert into phone1(id,name,type,storage,memmory,colour,price)
#                             values(4,'Iphone7','OPPO','642','3','white',230)""")
# cr.execute("""insert into phone1(id,name,type,storage,memmory,colour,price)
#                             values(5,'sanmsung Galaxy A73 5G','sanmsung','80','4','red',230)""")

# student_id=1
# db.commit()
# db.execute("""
# DELETE FROM Students
# WHERE id=?
# """,(student_id,))

           
# 
#cr.execute("""insert into Students(id,fname,lname,age,address,mobile)
#                             #values(2,'hussam','aya','14','14street','123')""")
# cr.execute("""
#            UPDATE Students 
#            SET fname='henedy'
#            WHERE id=2
#            """)
def insert(id,name,type,storage,memmory,colour,price):
    db=sqlite3.connect('phonedata.db')
    cr=db.cursor()
    cr.execute('insert into phone1 values (?,?,?,?,?,?,?)',(id,name,type,storage,memmory,colour,price))
    db.commit()
    db.close()
    return "the phone data has been added"
def Update(id,name,type,storage,memmory,colour,price):
    db=sqlite3.connect('phonedata.db')
    cr=db.cursor()
    cr.execute('update phonedata set id=? ,name=?,type=?,storage=?,memmory=?,colour=?,price=?')
    db.commit()
    db.close()
def delete(id,name,type,storage,memmory,colour,price):
    db=sqlite3.connect('phonedata.db')
    cr=db.cursor()
    cr.execute(f'delete from phone1 where id={id},name={name},type={type},storage={storage},memmory={memmory},colour={colour},price={price}')
    db.commit()
    db.close()
def show_all_data():
    db=sqlite3.connect('phonedata.db')
    cr=db.cursor()
    cr.execute("select * from phone1")
    rows=cr.fetchall()
    for row in rows:
         print(row)

    db.commit()
    db.close()


        
        

