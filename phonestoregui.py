#from curses.ascii import isascii
from email.utils import encode_rfc2231
from logging import root
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import edit_phone_data
import treeview


font=('Tahoma',15)
bg='#6B395F'
fg='#ffffff'
fgbl='black'
wind =Tk()
logo =PhotoImage(file='icon.gif')
wind.title("welcome")
wind.geometry("500x400")
wind.resizable(False,False)
wind.iconphoto(False,logo)
def exit_event():
    result=messagebox.askyesno('Exit','Are you sure you want to Exit?')
    if result==True:
        wind.destroy() 

def centerWindow(wind,width,height):
    screenwidth=wind.winfo_screenwidth()
    screenheight=wind.winfo_screenheight()
    x=int((screenwidth-width)/2)
    y=int((screenheight-height)/2)
    wind.geometry(f"{width}x{height}+{x}+{y}")
centerWindow(wind,500,400)

number=IntVar


def tab1():
    def tab4():
        l1.destroy()
        f1.destroy()
        btn1.destroy()
        btn2.destroy()
        #tab4['bg']='grey'
        l5=Label(wind, text="Password",fg=fgbl,font=("Arial ", 20),height=2)
        l5.place(x=70,y=95)
        e1_v=StringVar()
        e6=Entry(wind,show="*",font=font,width=15,textvariable=e1_v)
        e6.place(x=250,y=120)
        c_v=IntVar(value=0)
        def show ():
            if (c_v.get()==1):
                e6.config(show='')
            else:
                e6.config(show='*')
        ch=Checkbutton(wind,text="show password",command=show,variable=c_v,onvalue=1,offvalue=0)
        ch.place(x=280,y=160)
        def login ():
            password=e6.get()
            if (password==""):
                messagebox.showinfo("","Blank Not Allowed")

            elif(password=="admin"):
                    e6.destroy()
                    l5.destroy()
                    ch.destroy()
                    btn7.destroy()
                    btn8.destroy()
                    
                    def edit ():
                        treeview.showtree(wind)
                        edit_phone_data.phone_table()
                        btn9.destroy()
                        btn10.destroy()
                        btn11.destroy()
                        l11=Label(wind ,text="Id",fg=fgbl,font=font)
                        l11.place(x=20,y=120)
                        l22=Label(wind ,text="Name",fg=fgbl,font=font)
                        l22.place(x=20,y=150)
                        l33=Label(wind ,text="Type",fg=fgbl,font=font)
                        l33.place(x=20,y=180)
                        l44=Label(wind ,text="Storage",fg=fgbl,font=font)
                        l44.place (x=20,y=210)
                        l55=Label(wind ,text="Memory",fg=fgbl,font=font)
                        l55.place(x=20,y=240)
                        l66=Label(wind ,text="Color",fg=fgbl,font=font)
                        l66.place(x=20,y=270)
                        l77=Label(wind ,text="Price",fg=fgbl,font=font)
                        l77.place(x=20,y=300)
                        e11=Entry(wind,font=font,width=7)
                        e11.place(x=170,y=120)
                        e22=Entry(wind,font=font,width=13)
                        e22.place(x=170,y=150)
                        e33=Entry(wind,font=font,width=13)
                        e33.place(x=170,y=180)
                        e44=Entry(wind,font=font,width=13)
                        e44.place (x=170,y=210)
                        e55=Entry(wind,font=font,width=13)
                        e55.place(x=170,y=240)
                        e66=Entry(wind,font=font,width=13)
                        e66.place(x=170,y=270)
                        e77=Entry(wind,font=font,width=13)
                        e77.place(x=170,y=300)
                        btn66=Button(wind,text="Insert",background=bg,fg=fg,activebackground="grey",font=font)
                        btn66.place(x=20,y=340)
                        btn22=Button(wind,text="Update",background=bg,fg=fg,activebackground="grey",font=font)
                        btn22.place(x=100,y=340)
                        btn33=Button(wind,text="Delete",background=bg,fg=fg,activebackground="grey",font=font)
                        btn33.place(x=190,y=340)
                        btn44=Button(wind,text="Show all data",background=bg,fg=fg,activebackground="grey",font=font)
                        btn44.place(x=275,y=340)
                        ###########################################################3
                        
                        #########################################################@@

                        def back99():
                            l11.destroy()
                            l22.destroy()
                            l33.destroy()
                            l44.destroy()
                            l55.destroy()
                            l66.destroy()
                            l77.destroy()
                            btn66.destroy()
                            btn22.destroy()
                            btn33.destroy()
                            btn44.destroy()
                            btn55.destroy()
                            e11.destroy()
                            e22.destroy()
                            e33.destroy()
                            e44.destroy()
                            e55.destroy()
                            e66.destroy()
                            e77.destroy()
                            tab4()

                        btn55=Button(wind,text="Back",background=bg,activebackground="grey",fg=fg,font=font,command=back99)
                        btn55.place(x=420,y=340)
                    btn9=Button(wind,text="Edit phone data",font = font,background=bg,activebackground="grey",fg=fg,command=edit)
                    btn9.place(x=50,y=180)


                    def show ():
                        #login as custom
                        btn9.destroy()
                        btn10.destroy()
                        btn11.destroy()
                        l88=Label(wind ,text="phone Number",fg=fgbl,font=("arial",15))
                        l88.place(x=20,y=180)
                        l99=Label(wind ,text="Customer Name",fg=fgbl,font=("arial",15))
                        l99.place(x=20,y=260)
                        e88=Entry(wind,font=("arial",17),width=18)
                        e88.place(x=180,y=180)
                    
                        e99=Entry(wind,font=("arial",17),width=18)
                        e99.place(x=180,y=260)

                        def back88():
                            bt1.destroy()
                            bt2.destroy()
                            l99.destroy()
                            l88.destroy()
                            e88.destroy()
                            e99.destroy()
                            tab4()

                        bt1=Button(wind,text="Back",fg=fg,background=bg,activebackground="grey",font=("arial",15),command=back88)
                        bt1.place(x=420,y=340)
                        bt2=Button(wind,text="Show all data",fg=fg,background=bg,activebackground="grey",font=("arial",15))
                        bt2.place(x=20,y=340)
                        
                    btn10=Button(wind,text="Show customer data",font = font,bg=bg,activebackground="grey",fg=fg,command=show)
                    btn10.place(x=250,y=180)

                    def back5 ():
                        btn9.destroy()
                        btn10.destroy()
                        btn11.destroy()
                        tab4()
                    btn11=Button(wind , text="Back",font= ("arial",12),fg=fg,background=bg,activebackground="grey",command=back5,width=5)
                    btn11.place(x=400,y=340)

            else :
                messagebox.showinfo("","incorrect password")
        btn7=Button(wind,font=("Arial ", 15),text="Login",background=bg,fg=fg,command=login)
        btn7.place(x=220,y=250)
        def back3():
            btn7.destroy()
            btn8.destroy()
            ch.destroy()
            l5.destroy()
            e6.destroy()
            tab1()
        btn8=Button(wind,text="Back",background=bg,font=("Arial",12),fg=fg,command=back3,activebackground="grey")
        btn8.place(x=400,y=340)
        

    def tab2():
        #buy
        def tab3 ():
            
            e1.destroy()
            e2.destroy()
            l0.destroy()
            l2.destroy()
            l3.destroy()
            btn3.destroy()
            btn4.destroy()
            def back2 ():
                btn5.destroy()
                btn6.destroy()
                l4.destroy()
                e3.destroy()
                tab2()
            def buy ():
                messagebox.showinfo(title="Done",message="Thank You")
            btn5=Button(wind,text="Back",background=bg,fg=fg,font=font,
                activebackground="grey",command=back2)
            btn5.place(x=390,y=340)
            btn6=Button(wind,text="Buy it",background="#33FF33",font=font,
                activebackground="grey",command=buy)
            btn6.place(x=200,y=280)
            l4=Label(wind , text="Please enter your \n credit card number",font=font,
                fg=fgbl,height=2)
            l4.place(x=40,y=200)
            e3=Entry(wind,font=("Arial ", 17),width=18)
            e3.place(x=240,y=210)
        l1.destroy()
        f1.destroy()
        btn1.destroy()
        btn2.destroy()
        e1=Entry(wind,font=font,width=15)
        e2=Entry(wind,font=font,width=15)
        e1.place(x=260,y=160)
        e2.place(x=260,y=220)

        l0=Label(wind , text="Welcome",font=("Arial ", 25),bg=bg,fg=fg,height=3)
        l0.pack(fill=X)
        l2=Label(wind , text="Username ",font=font,fg=fgbl,height=2)
        l2.place(x=90,y=140)
        l3=Label(wind , text="Phone number",font=font,fg=fgbl,height=2)
        l3.place(x=90,y=200)

        def back ():
            e1.destroy()
            e2.destroy()
            l0.destroy()
            l2.destroy()
            l3.destroy()
            btn3.destroy()
            btn4.destroy()
            tab1()

        def sub ():
            phone =e1.get()
            us_name =e2.get()
            if phone == "" and us_name == "":
                messagebox.showinfo("","Blank Not Allowed")
            # elif phone.isascii:
            #     messagebox.showerror("Error","please Enter a phone Number!")
            elif (phone=="") or (us_name ==""):
                messagebox.showinfo("","please Enter user name and phone") 
            else:
                tab3()


        btn3=Button(wind,text="Submit",background=bg,fg=fg,font=font,
                activebackground="grey",command=sub)
        btn3.place(x=200,y=300,)
        btn4=Button(wind,text="Back",background=bg,fg=fg,font=font,
                activebackground="grey",command=back)
        btn4.place(x=390,y=340)
      
    l1=Label(wind , text="Phone Store",font=("Tahoma", 40),background=bg,fg=fg,height=2)
    l1.pack(fill=X)
    f1=Frame(wind,width=500,height=260)
    f1.place(x=0,y=130)
    btn1=Button(f1,text="login as admin",borderwidth=5,background=bg,fg=fg,
            font=("Arial ", 15),activebackground="grey",command=tab4)
    btn1.place(x=60,y=100)
    btn2=Button(f1,text="login as customer",borderwidth=5,background=bg,fg=fg,font=font,
            activebackground="grey",command=tab2)
    btn2.place(x=280,y=100)
    b_tn=Button(f1,text="Exit",background=bg,fg=fg,borderwidth=5,activebackground="grey",font=font,command=exit_event)
    b_tn.place(x=210,y=170)
tab1()

#db=edit_phone_data()
# def BuSAVEData():
#     print("ID:{}",format(tab1().e11.get()))
#     print("name:{}",format(tab1().e22.get()))
#     print("type:{}",format(tab1().e33.get()))
#     print("storage:{}",format(tab1().e44.get()))
#     print("memory:{}",format(tab1().e55.get()))
#     print("color:{}",format(tab1().e66.get()))
#     print("price:{}",format(tab1().e77.get()))
#     ID=tab1().e11.get()
#     name=tab1().e22.get()
#     type=tab1().e33.get()
#     storage=tab1().e44.get()
#     memory=tab1().e55.get()
#     color=tab1().e66.get()
#     price=tab1().e77.get()
#     msg=edit_phone_data.insert(ID,name,type,storage,memory,color,price)
#     messagebox.showinfo(title="Add info",message=msg)
#     ID.delete(0,'end')
#     name.delete(0,'end')
#     type.delete(0,'end')
#     storage.delete(0,'end')
#     memory.delete(0,'end')
#     price.delete(0,'end')
#     color.delete(0,'end')
# def BuListData():
#     #TODO: show orders

#     print('not implemented yet')

# tab1().btn66.config(command=BuSAVEData)
# tab1().config(command=BuListData) 
wind.mainloop()
