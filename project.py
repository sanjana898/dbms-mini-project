from cmath import rect
from tkinter import *
from tkinter import messagebox as ms
from tkinter import ttk
import mysql.connector
from nextpy import button

# Database 
def get_db_connection():
    
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="tcdav",
    database="courier_management_services"
    )
  


class main:
    def __init__(self,master): 
  
        self.master = master
        
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.n_reg=StringVar()
        self.n_mobile=StringVar()
        self.n_email=StringVar()
        self.consignment_id = StringVar() # Added consignment_no variable
        self.widgets()


    
    def login(self):
        db=get_db_connection()
        c=db.cursor()
        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = %s and password = %s')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        
        if result:
            self.track()
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
        db = get_db_connection()
        c = db.cursor()
        if self.n_username.get() != '' and self.n_password.get() != '' and self.n_mobile.get() != '' and self.n_email.get() != '' and "@" in self.n_email.get() and len(self.n_mobile.get()) == 10:
            find_user = "SELECT * FROM user WHERE username = %s"
            c.execute(find_user, (self.n_username.get(),))
            if c.fetchall():
                ms.showerror('Error!', 'Username Taken. Try a Different One.')
            else:
                insert = "INSERT INTO user (username, password, mobile, email) VALUES (%s, %s, %s, %s)"
                c.execute(insert, (self.n_username.get(), self.n_password.get(), self.n_mobile.get(), self.n_email.get()))
                db.commit()
                ms.showinfo('Success!', 'Account Created!')
                self.log()
        else:
            ms.showerror('Error!', 'Please Enter the Details Correctly.')
        c.close()
        db.close()
        
     
        
    def consignment(self):
        
       
        try:
            db = get_db_connection()
            c = db.cursor()
            # Fetch consignment details from the database based on the consignment number
            consignment_query = "SELECT * FROM consignment WHERE consignment_id = %s"
            c.execute(consignment_query, (self.consignment_id.get(),))
            consignment_details = c.fetchone()

            if consignment_details:
                # Display the consignment details
                self.track()
                self.crff.pack_forget()
                self.head['text'] = self.username.get() + '\n Your Product Details'
                self.consi.pack()

                # Update the labels with the fetched data
                self.consi.children['!label'].configure(text=f'Username : {consignment_details[1]}')
                self.consi.children['!label2'].configure(text=f'Product name: {consignment_details[2]}')
                self.consi.children['!label3'].configure(text=f'Product Status: {consignment_details[3]}')

            else:
                ms.showerror('Oops!', 'No consignment found for this consignment number.')
        except:
                ms.showerror('Oops!', 'Consignment Number Not Found.')
        finally:
                c.close()
                db.close()
                
    
   
    def track1(self):
        self.consi.pack_forget()
        self.head['text'] = self.username.get() + '\n Track your Product'
        self.crff.pack()
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Login'
        self.logf.pack()
        
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    def track(self):
        self.logf.pack_forget()
        self.head['text'] = self.username.get() + '\n Track your Product'
        self.crff.pack()
           

  
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',20),pady = 10)
        self.head.pack()
        
    
        self.logf = Frame(self.master,padx =10,pady = 10)
        
        self.logf.configure(background='lightblue')
        #PhotoImage(self.logf,file = 'lpu_logo.png')
        Label(self.logf,text = 'Username: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 3,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 3,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',background='lightgrey',bd = 2 ,font = ('',13),padx=6,pady=6,command=self.login).grid(row=8,column=0)
        Button(self.logf,text = ' New user ',background='lightgrey',bd = 2 ,font = ('',13),padx=6,pady=6,command=self.cr).grid(row=8,column=1)
       
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 3,font = ('',15)).grid(row=0,column=1)
        
        Label(self.crf,text = 'Password: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 3,font = ('',15),show = '*').grid(row=1,column=1)
        
        # Label(self.crf,text = 'Reg No.: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        # Entry(self.crf,textvariable = self.n_reg,bd = 3,font = ('',15)).grid(row=2,column=1)
        Label(self.crf,text = 'Gender: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        var = IntVar()
        R1 = Radiobutton(self.crf, text="Male", variable=var, value=1).grid(sticky=W)
        
        R2 = Radiobutton(self.crf, text="Female", variable=var, value=2 ).grid(row=4,column=1)
        Label(self.crf,text = 'Mobile No.: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_mobile,bd = 3,font = ('',15)).grid(row=5,column=1)
        
        Label(self.crf,text = 'Email Id: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_email,bd = 3,font = ('',15)).grid(row=6,column=1)
        
        
        
        Button(self.crf,text = 'Create Account',background='lightgrey',bd = 2,font = ('',13),padx=6,pady=6,command=self.new_user).grid(row=11,column=0)
        Button(self.crf,text = 'Go to Login',background='lightgrey',bd = 2,font = ('',13),padx=6,pady=6,command=self.log).grid(row=11,column=1)

    

        self.crff = Frame(self.master,padx =10,pady = 10)
        
      

        Label(self.crff,text = 'Consignment No: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crff,textvariable = self.consignment_id, bd = 3,font = ('',15)).grid(row=0,column=1)
        
        # Removed Mobile number field
        # Label(self.crff,text = 'Mobile no:',font = ('',15),pady=5,padx=5).grid(sticky = W)
        # Entry(self.crff,bd = 3,textvariable = self.mobile11,font = ('',15)).grid(row=1,column=1)
        Button(self.crff,text = 'Track',background='lightgrey',bd = 2,font = ('',13),padx=6,pady=6,command=self.consignment).grid(row=4,column=0)

        self.consi = Frame(self.master,padx =10,pady = 10)
        
        Label(self.consi,text = ' Product ID:',font = ('',15),pady=5,padx=5).grid(sticky = W, row=0, column=0)
        Label(self.consi,text ='' ,font = ('',13),pady=5,padx=5).grid(row=0,column=1, sticky=W)
        Label(self.consi,text = 'Product name: ',font = ('',15),pady=5,padx=5).grid(sticky = W, row=1, column=0)
        Label(self.consi,text ='' ,font = ('',13),pady=5,padx=5).grid(row=1,column=1, sticky=W)
        # Label(self.consi,text = 'Product Status: ',font = ('',15),pady=5,padx=5).grid(sticky = W, row=2, column=0)
        Label(self.consi,text ='' ,font = ('',13),pady=5,padx=5).grid(row=2,column=1, sticky=W)
        Label(self.consi,font = ('',13), text = 'Thanks for Exploring!').grid(row = 4, column = 0)
       
        Entry(self.consi,bd = 3,font = ('',15)).grid(row=5,column=1)

        Button(self.consi,text = 'Back',background='lightgrey',bd = 2,font = ('',13),padx=6,pady=6,command=self.track1).grid(row=6,column=0)
    
        
        
        
        

if __name__ == '__main__':

    root = Tk()
    root.title('Track Consignment')
    root.geometry('800x750+300+300')
    main(root)
    
    canvas = Canvas(root)
    canvas.pack()
    canvas.config(width = 640, height = 380)

    line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)
    canvas.itemconfigure(line, fill = '#1abc9c')
    print(canvas.coords(line))
    canvas.coords(line, 0, 0, 320, 240, 640, 0)

    canvas.itemconfigure(line, smooth = True)
    canvas.itemconfigure(line, splinesteps = 5)
    canvas.itemconfigure(line, splinesteps = 100)
    canvas.delete(line)

    # rect = canvas.create_rectangle(160, 120, 480, 360)
    # canvas.itemconfigure(rect, fill = '#3498db')
    # oval = canvas.create_oval(160, 120, 480, 360)
    # arc = canvas.create_arc(160, 1, 480, 240)
    # canvas.itemconfigure(arc, start = 0, extent = 180, fill = '#1abc9c')
    # poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = '#95a5a6')
    text = canvas.create_text(320, 240, font = ('Courier', 32, 'bold'))

    logo = PhotoImage(file = 'Courier-management-system-in-python--master\photo.png') 
    image = canvas.create_image(320, 240, image = logo)

    canvas.lift(text)
    canvas.lower(image)
    canvas.lower(image, text)
    canvas.itemconfigure(rect, tags = ('shape'))
    canvas.itemconfigure('shape', fill = 'grey')
    root.mainloop()
