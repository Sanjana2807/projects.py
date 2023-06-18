def exp_date(): # expiry window open-----------------------------------------------------------------------------EXPIRY
    global exp, s,c, cur, flag, apt, flags
    apt.destroy()
    flag='exp'
    from datetime import date
    now=time.localtime()
    n=[]
    cur.execute("select *from med")
    for i in cur:
        n.append(i[1])
    c.commit()
    exp=Tk()
    exp.title('EXPIRY CHECK')
    Label(exp,text='Today : '+str(now[2])+'/'+str(now[1])+'/'+str(now[0])).grid(row=0, column=0, columnspan=3)
    Label(exp,text='Selling Expired Medicines and Drugs is Illegal').grid(row=1, column=0,columnspan=3)
    Label(exp,text='-'*80).grid(row=2, column=0,columnspan=3)
    s=Spinbox(exp,values=n)
    s.grid(row=3, column=0)
    Button(exp,text='Check Expiry date', bg='red', fg='white', command=s_exp).grid(row=3, column=1)
    Label(exp,text='-'*80).grid(row=4, column=0,columnspan=3)
    if flags=='apt1':
        Button(exp,text='Main Menu', bg='green', fg='white', command=main_cus).grid(row=5, column=2)
    else:
        Button(exp,width=20,text='Check Products expiring', bg='red', fg='white', command=exp_dt).grid(row=5, column=0)
        Button(exp,text='Main Menu', bg='green', fg='white', command=main_menu).grid(row=5, column=2)
    exp.mainloop()