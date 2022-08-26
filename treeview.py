from tkinter import *
from tkinter.ttk import *
phones=[(1,'Iphone7','Iphone',64,4,'white',210),
            (2,'Redmi9','shawme',128,8,'white',2000),
            (3,'Iphone7','shawme',128,8,'blue',230),
            (4,'Iphone7','OPPO',642,3,'white',230),
            (5,'sanmsung Galaxy A73 5G','sanmsung',80,4,'red',230)]
root=Tk()
logo =PhotoImage(file='image\icon.gif')
columns=['id','name','type','storage','memmory','colour','price']
tree=Treeview(root,columns=columns,show='headings',height=3)
tree.column('id',width=80,anchor='center')
tree.column('name',width=80,anchor='center')
tree.column('type',width=80,anchor='center')
tree.column('storage',width=80,anchor='center')
tree.column('memmory',width=80,anchor='center')
tree.column('colour',width=80,anchor='center')
tree.column('price',width=80,anchor='center')
tree.heading('id',text='idphone')
tree.heading('name',text='name')
tree.heading('type',text='type')
tree.heading('storage',text='storage')
tree.heading('memmory',text='Memory')
tree.heading('colour',text='colour')
tree.heading('price',text='price')

for phone in phones:
    tree.insert('','end',iid=phone[0],values=phone)#insert('parent',index,id ,data)

def get_selected():
    for selection in tree.selection():
        print(tree.item(selection)['values'])
    
btn=Button(root,text="click",command=get_selected)
scrollbar=Scrollbar(root,orient='vertical',command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0,column=1,sticky='ns')
tree.grid(row=0,column=0)
btn.grid(row=1,column=0)
style=Style()
style.configure('Treeview',font=('arial',12),rowheight=30,fg='black',bg='white')
style.map('Treeview',foreground=[('selected','#011936')],background=[('selected','#c2eabd')])
style.configure('Treeview.Heading',font=('Tahoma',14))
root.iconphoto(False,logo)
root.mainloop()