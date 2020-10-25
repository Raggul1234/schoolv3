from tkinter import *
from tkinter import ttk
import tkinter as tk
import pyodbc


#ConnectingDatabase#

from tkinter import messagebox
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MUTHUCOMPUTER;'
                      'Database=Class4c v3;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


#Adding new record#

def save():
    Names=   (Name.get())
    Ages=    (Age.get())
    Heights= (height.get())
    Weights= (weight.get())
    Rollnos= (StudentId.get())
    Activitytypes=(Activitytype.get())
    Activities=(Activity.get())
    Extras=(Extra.get())
#validation
    Validate(Names,Ages,Heights,Weights,Rollnos,Activitytypes,Activities,Extras)   
                






               
#function to Validate entries
def Validate(Names,Ages,Heights,Weights,Rollnos,Activitytypes,Activities,Extras):

    while True:
        
            if len(Names)==0:
                messagebox.showinfo("Tkinter", "Name cannot be empty")
                break
            elif len(Ages)==0:
                messagebox.showinfo("Tkinter", "Age cannot be empty")
                break
            elif (M.get() == 0) and (F.get() == 0):
                messagebox.showinfo("Tkinter", "Genders cannot be empty")
                break
            elif len(Rollnos)==0:
                messagebox.showinfo("Tkinter", "StudentId cannot be empty")
                break
            elif len(Names)==0 and len(Ages)==0 and len(Gender)==0 and len(Rollnos):
                messagebox.showinfo("Tkinter", "Atleast Name,Age,Gender and StudentId must be given!!")
                break
            
            try:
            
                int(Names)
                messagebox.showinfo("Tkinter", "Name must be string")
                break
            except ValueError:
                
                    if (M.get() == 1) and (F.get() == 0):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'M',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    elif (M.get() == 0) and (F.get() == 1):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'F',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                
            try:
                int(Ages)
                break
            except ValueError:
                messagebox.showinfo("Tkinter", "Age must be integer")
                break
            else:
                
                    if (M.get() == 1) and (F.get() == 0):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'M',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    
             
            try:
            
                if (M.get() == 1) and (F.get() == 0):
                    
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'M',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    
                elif (M.get() == 0) and (F.get() == 1):
                    
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'F',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
            except pyodbc.IntegrityError:
                        messagebox.showinfo("Tkinter", "StudentId already exists")
                        break        
            try:
            
                int(Heights)
                break
            except ValueError:
                messagebox.showinfo("Tkinter", "Height must be integer")
                break
            else:
               
                    if (M.get() == 1) and (F.get() == 0):
                            pass  
                            cursor.execute("""
                            INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                            VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'M',Heights,Weights))
                            conn.commit()
                            cursor.execute("""
                            INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                            VALUES (?,?,?,?,?)
                            """,(Rollnos,Names,Activitytypes,Activities,Extras))
                            conn.commit()
                            clearfields()
                            
                            messagebox.showinfo("Tkinter", "Saved successfully!")
                            break
                    elif (M.get() == 0) and (F.get() == 1):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'F',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break


            try:
            
                int(Weights)
                break
            except ValueError:
                messagebox.showinfo("Tkinter", "Weight must be integer")
                break
            else:
                
                    if (M.get() == 1) and (F.get() == 0):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'M',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    if (M.get() == 0) and (F.get() == 1):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'F',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    

            try:
            
                int(Rollnos)
                break
            except ValueError:
                messagebox.showinfo("Tkinter", "StudentId must be integer")
                break
            else:
                
                    if (M.get() == 1) and (F.get() == 0):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'M',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    elif (M.get() == 0) and (F.get() == 1):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'F',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                
            try:
            
                int(Activitytypes)
                messagebox.showinfo("Tkinter", "Activitytype must be string")
                break
            except ValueError:
                
                    if (M.get() == 1) and (F.get() == 0):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'M',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    elif (M.get() == 0) and (F.get() == 1):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'F',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    
                    

            try:
            
                int(Activities)
                messagebox.showinfo("Tkinter", "Activity must be string")
                break
            except ValueError:
                
                    if (M.get() == 1) and (F.get() == 0):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'M',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    if (M.get() == 0) and (F.get() == 1):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'F',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break

            try:
            
                int(Extras)
                messagebox.showinfo("Tkinter", "Extra must be string")
                break
            except ValueError:
                
                    if (M.get() == 1) and (F.get() == 0):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'M',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    elif (M.get() == 0) and (F.get() == 1):
                        pass  
                        cursor.execute("""
                        INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                        VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,'F',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activity(StudentId,Name,Activitytype,Activity,ExtraActivity)
                        VALUES (?,?,?,?,?)
                        """,(Rollnos,Names,Activitytypes,Activities,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    
                    messagebox.showinfo("Tkinter", "Saved successfully!")
                    break










                

#function to clear all entries
def clearfields():
    Name.delete(0 ,tk.END)
    Age.delete(0 ,tk.END)
    G1.deselect()
    G2.deselect()
    height.delete(0 ,tk.END)
    weight.delete(0 ,tk.END)
    StudentId.delete(0 ,tk.END)
    Activitytype.delete(0 ,tk.END)
    Activity.delete(0 ,tk.END)
    Extra.delete(0 ,tk.END)













def Search():
     
            Names= Name.get()
            Ages= Age.get()
            Heights= height.get()
            Weights= weight.get()
            StudentIds= StudentId.get()
            Activitytypes=Activitytype.get()
            Activities=Activity.get()
            Extras=Extra.get()

            

    # clearing the tree
           
            t=tree.get_children()
            for f in t:
                tree.delete(f)
            

    #Search starts
                

            if len(Names)!=0:
                cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
                from Students A inner join Activity B on A.StudentId=B.StudentId where A.Name like(?)""",(Names))
                records=cursor.fetchall()
                for row in records:
                    tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                    tree.pack(side=tk.TOP,fill=tk.X)
                        
                    
            elif  len(Ages)!=0:
                cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
                from Students A inner join Activity B on A.StudentId=B.StudentId where A.Age like(?)""",(Ages))
                records=cursor.fetchall()
                for row in records:
                    tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                    tree.pack(side=tk.TOP,fill=tk.X)


            elif  (M.get() == 0) and (F.get() == 1):
                cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
                from Students A inner join Activity B on A.StudentId=B.StudentId where A.Gender like 'F'""")
                records=cursor.fetchall()
                for row in records:
                    tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                    tree.pack(side=tk.TOP,fill=tk.X)

                    
            elif  (M.get() == 1) and (F.get() == 0):
                cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
                from Students A inner join Activity B on A.StudentId=B.StudentId where A.Gender like 'M'""")
                records=cursor.fetchall()
                for row in records:
                    tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                    tree.pack(side=tk.TOP,fill=tk.X)


            elif  len(Heights)!=0:
                cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
                from Students A inner join Activity B on A.StudentId=B.StudentId where A.Height like(?)""",(Heights))
                records=cursor.fetchall()
                for row in records:
                    tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                    tree.pack(side=tk.TOP,fill=tk.X)          


            elif  len(Weights)!=0:
                cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
                from Students A inner join Activity B on A.StudentId=B.StudentId where A._Weight like(?)""",(Weights))
                records=cursor.fetchall()
                for row in records:
                    tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                    tree.pack(side=tk.TOP,fill=tk.X)


            elif  len(StudentId)!=0:
                cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
                from Students A inner join Sports B on A.StudentId=B.StudentId where A.StudentId like(?)""",(StudentId))
                records=cursor.fetchall()
                for row in records:
                    tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                    tree.pack(side=tk.TOP,fill=tk.X)


            elif  len(Activitytypes)!=0:
                cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
                from Students A inner join Activity B on A.StudentId=B.StudentId where B.Activitytypes like(?)""",(Activitytypes))
                records=cursor.fetchall()
                for row in records:
                    tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                    tree.pack(side=tk.TOP,fill=tk.X)

                    
            elif  len(Activities)!=0:
                cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
                from Students A inner join Activity B on A.StudentId=B.StudentId where B.Activity like(?)""",(Activities))
                records=cursor.fetchall()
                for row in records:
                    tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                    tree.pack(side=tk.TOP,fill=tk.X)
                    

            elif  len(Extra)!=0:
                cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
                from Students A inner join Activity B on A.StudentId=B.StudentId where B.Extra like(?)""",(estras))
                records=cursor.fetchall()
                for row in records:
                    tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                    tree.pack(side=tk.TOP,fill=tk.X)

            else:
                
                messagebox.showinfo("Tkinter", "Atleast one search criteria must be given!")





            



#function to delete record

def delete():
        x=StudentId.get()
        cursor.execute("""
        DELETE FROM Students
        WHERE StudentId = (?)""",(x))
        conn.commit()
        cursor.execute("""
        DELETE FROM Activity
        WHERE StudentId = (?)""",(x))
        conn.commit()
        clearfields()
        messagebox.showinfo("Tkinter", "Deleted successfully!")


def getallrecords():
    t=tree.get_children()
    for f in t:
        tree.delete(f)
    cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
    from Students A inner join Activity B on A.StudentId=B.StudentId""")
    records=cursor.fetchall()
    for row in records:
        tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
        tree.pack(side=tk.TOP,fill=tk.X)




# defining the canvas

root= tk.Tk()
root.title("Class4c")
canvas1 = tk.Canvas(root, width = 900, height = 300)
canvas1.pack()



# Defining the fields and labels and validating

Name = tk.Entry (root)
canvas1.create_window(300, 10, window=Name)
label1 = tk.Label(root, text='Name:')
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 10, window=label1)


Age = tk.Entry (root)
canvas1.create_window(300, 40, window=Age)
label2 = tk.Label(root, text='Age:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 40, window=label2)



label3 = tk.Label(root, text='Gender:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 70, window=label3)


M = IntVar()
G1 = Checkbutton(
    root, text="M", variable=M,
    onvalue=1, offvalue=0)

F = IntVar()
G2 = Checkbutton(
    root, text="F", variable=F,
    onvalue=1, offvalue=0)

canvas1.create_window(350, 70, window=G1)
canvas1.create_window(250, 70, window=G2)


height = tk.Entry (root)
canvas1.create_window(300, 100, window=height)
label4 = tk.Label(root, text='height in cm:')
label4.config(font=('helvetica', 10))
canvas1.create_window(195, 100, window=label4)

weight = tk.Entry (root)
canvas1.create_window(300, 130, window=weight)
label5 = tk.Label(root, text='weight in kg:')
label5.config(font=('helvetica', 10))
canvas1.create_window(195, 130, window=label5)

StudentId = tk.Entry (root)
canvas1.create_window(300, 160, window=StudentId)
label6 = tk.Label(root, text='StudentId:')
label6.config(font=('helvetica', 10))
canvas1.create_window(200, 160, window=label6)

Activitytype = tk.Entry (root)
canvas1.create_window(300, 190, window=Activitytype)
label7 = tk.Label(root, text='Activitytype:')
label7.config(font=('helvetica', 10))
canvas1.create_window(200, 190, window=label7)


Activity = tk.Entry (root)
canvas1.create_window(500, 10, window=Activity)
label8 = tk.Label(root, text='Activity:')
label8.config(font=('helvetica', 10))
canvas1.create_window(400, 10, window=label8)

Extra = tk.Entry (root)
canvas1.create_window(500, 40, window=Extra)
label9 = tk.Label(root, text='Extra:')
label9.config(font=('helvetica', 10))
canvas1.create_window(400, 40, window=label9)





# Defining the buttons

button1 = tk.Button(text='Save',command = save)
canvas1.create_window(500, 250, window=button1)

button2 = tk.Button(text='Search',command=Search)
canvas1.create_window(400, 250, window=button2)

button3 = tk.Button(text='Delete',command=delete)
canvas1.create_window(450, 250, window=button3)

button4 = tk.Button(text='Get all records',command=getallrecords)
canvas1.create_window(330, 250, window=button4)



# Defining the tree

tree=ttk.Treeview(root)
tree["columns"]=("one","two","three","four","five","six")
tree.column("#0", width=130, minwidth=270, stretch=tk.NO)
tree.column("one", width=100, minwidth=150, stretch=tk.NO)
tree.column("two", width=100, minwidth=100)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("one", text="Age",anchor=tk.W)
tree.heading("two", text="Gender",anchor=tk.W)
tree.heading("three", text="Height",anchor=tk.W)
tree.heading("four", text="Weight",anchor=tk.W)
tree.heading("five", text="StudentId",anchor=tk.W)
tree.heading("six", text="Activity",anchor=tk.W)
tree.pack()



root.mainloop()
