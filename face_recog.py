from tkinter import *
from tkinter import font, ttk, messagebox, simpledialog
from PIL import ImageTk, Image 
import time
import customtkinter
import os
import sqlite3
from time import strftime
import calendar
import pandas as pd
import csv
from tkinter import filedialog
import collections
from collections import defaultdict
import shutil
import datetime
attemptadmin = 0
attempuser= 0
sched_id = 0

w=Tk()

#Using piece of code from old splash screen
width_of_window = 1000
height_of_window = 500
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar



Frame(w, width=1000, height=500).place(x=0,y=0)
img= (Image.open("pic/1.png"))
resized_image_splash= img.resize((1000,500))
photo= ImageTk.PhotoImage(resized_image_splash)
# label = Label(w, image = photo)
# label.pack()

# label2=Label(w, text='Loading', fg='white', bg='#dab015') #decorate it 
# label2.configure(font=("Calibri", 17))
# label2.place(x=10,y=465)

#making animation

image_a=ImageTk.PhotoImage(Image.open('pic/dot2.png'))
image_b=ImageTk.PhotoImage(Image.open('pic/dot1.png'))


# for i in range(5):
#     # loading text
#     label2=Label(w, text='Loading', fg='white', bg='#dab015') #decorate it 
#     label2.configure(font=("Calibri", 17))
#     label2.place(x=10,y=465)
#     # background image
#     label = Label(w, image = photo)
#     label.pack()
#     # loading dot animation
#     l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=90, y=480)
#     l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=110, y=480)
#     l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=130, y=480)
#     l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=150, y=480)
#     w.update_idletasks()
#     time.sleep(0.5)

#     # loading text
#     label2=Label(w, text='Loading', fg='white', bg='#dab015') #decorate it 
#     label2.configure(font=("Calibri", 17))
#     label2.place(x=10,y=465)
#     # background image
#     label = Label(w, image = photo)
#     label.pack()
#     # loading dot animation
#     l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=90, y=480)
#     l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=110, y=480)
#     l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=130, y=480)
#     l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=150, y=480)
#     w.update_idletasks()
#     time.sleep(0.5)

#     # loading text
#     label2=Label(w, text='Loading', fg='white', bg='#dab015') #decorate it 
#     label2.configure(font=("Calibri", 17))
#     label2.place(x=10,y=465)
#     # background image
#     label = Label(w, image = photo)
#     label.pack()
#     # loading dot animation
#     l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=90, y=480)
#     l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=110, y=480)
#     l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=130, y=480)
#     l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=150, y=480)
#     w.update_idletasks()
#     time.sleep(0.5)

#     # loading text
#     label2=Label(w, text='Loading', fg='white', bg='#dab015') #decorate it 
#     label2.configure(font=("Calibri", 17))
#     label2.place(x=10,y=465)
#     # background image
#     label = Label(w, image = photo)
#     label.pack()
#     # loading dot animation
#     l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=90, y=480)
#     l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=110, y=480)
#     l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=130, y=480)
#     l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=150, y=480)
#     w.update_idletasks()
#     time.sleep(0.5)

#new window to open
def new_win():

    customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

    main_window=customtkinter.CTk()
    main_window.title('main window')
    # main_window.geometry('1000x500')
    main_window.state('zoomed')
    main_window.resizable(False,False)
    # main_window.rowconfigure(0, weight=2)
    # main_window.columnconfigure(1, weight=1)
    
    page1 = Frame(main_window)
    page2 = Frame(main_window)
    page3 = Frame(main_window)
    page4 = Frame(main_window)
    attendance_record = Frame(main_window)
    faculty_information = Frame(main_window)
    mathematics_att_record = Frame(main_window)
    employee_login = Frame(main_window)
    attendance_monitoring = Frame(main_window)
    developers = Frame(main_window)
    about = Frame(main_window)
    about_clg_goal = Frame(main_window)
    about_program= Frame(main_window)
    psychology_att_record = Frame(main_window)
    applied_physics_att_record = Frame(main_window)
    ite_att_record = Frame(main_window)
    activity_log = Frame(main_window)
    

    for frame in (page1, page2, page3, page4, attendance_record,faculty_information,mathematics_att_record,employee_login,attendance_monitoring,developers,about,about_clg_goal,about_program,psychology_att_record,applied_physics_att_record,ite_att_record,activity_log):
        frame.grid(row=0, column=0, sticky='nsew')

    def show_frame(frame):
        frame.tkraise()

    show_frame(faculty_information)

    # ============= Page 1 Frame =========================================================================================================================================

        # open background image
    page1.pg1_image = Image.open('pic/2.png')
    page1.pg1_resize_image = page1.pg1_image.resize((1362, 692))
    page1.photo = ImageTk.PhotoImage(page1.pg1_resize_image)
    page1.pg1_bg_img_lb = Label(page1, image = page1.photo)
    page1.pg1_bg_img_lb.pack()
    
        # Login Button
    pg1_login_img_btn = PhotoImage(file = "pic/btn_login.png")
    pg1_button_admin = Button(page1,image=pg1_login_img_btn, borderwidth=0, bg='#1f2a76',command=lambda: show_frame(page2))
    pg1_button_admin.place(x=99, y=422)

        # Biomettric Button
    biometric_img_btn = PhotoImage(file = "pic/bttn_biometric.png")
    pg1_button_bio = Button(page1,image=biometric_img_btn, borderwidth=0,bg='#1f2a76', command=lambda: show_frame(page2))
    pg1_button_bio.place(x=99, y=256)

    # ============= Page 2 Frame =======================================================================================================================================

        # open background image
    page2.pg2_image = Image.open('pic/3.png')
    page2.pg2_resize_image = page2.pg2_image.resize((1362, 692))
    page2.photo = ImageTk.PhotoImage(page2.pg2_resize_image)
    page2.pg2_bg_img_lb = Label(page2, image = page2.photo)
    page2.pg2_bg_img_lb.pack()

        # Employee Button
    employee_img_btn = PhotoImage(file = "pic/btn_employee.png")
    pg2_button_employee = Button(page2,image=employee_img_btn, borderwidth=0,bg='#1f2a76', command=lambda: show_frame(employee_login))
    pg2_button_employee.place(x=99, y=256)

        # Admin Button
    admin_img_btn = PhotoImage(file = "pic/bttn_admin.png")
    pg2_button_admin = Button(page2,image=admin_img_btn, borderwidth=0, bg='#1f2a76',command=lambda: show_frame(page3))
    pg2_button_admin.place(x=99, y=422)

        # Back Button
    pg2_back = PhotoImage(file = "pic/btn_back_log.png")
    pg2_button_back = customtkinter.CTkButton(master=page2,image=pg2_back, text="" ,
                                                corner_radius=5,bg_color='#e4b50b', fg_color="#e4b50b",hover_color="#006699", command=lambda: show_frame(page1))
    pg2_button_back.place(x=5, y=5, height=40,width=70)
    
    # ============= Employee Sign In Frame ============================================================================================================================

        # open background image
    employee_login.empl_log_image = Image.open('pic/5.png')
    employee_login.empl_log_resize_image = employee_login.empl_log_image.resize((1362, 692))
    employee_login.photo = ImageTk.PhotoImage(employee_login.empl_log_resize_image)
    employee_login.empl_log_bg_img_lb = Label(employee_login, image = employee_login.photo)
    employee_login.empl_log_bg_img_lb.pack()

        # Text Box Username and Password
    username_lbl_empl_log= Label(employee_login, text='Username', fg='Black', bg ='#1f2a76', font = "Heltvetica 27 bold")
    username_lbl_empl_log.place(x=116, y=207)
    empl_log_txtbox_username = Entry(employee_login, borderwidth=0, width=16, font=('Arial',30))
    empl_log_txtbox_username.place(x=116, y=256, height=92)

    password_lbl_empl_log = Label(employee_login, text='Password', fg='Black', bg ='#1f2a76', font = "Heltvetica 27 bold")
    password_lbl_empl_log.place(x=116, y=370)
    empl_log_txtbox_pass = Entry(employee_login, borderwidth=0, width=16, font=('Arial', 30), show='*')
    empl_log_txtbox_pass.place(x=116, y=422, height=90)

    def refreshTable_log():

        for data_log in data_table_act.get_children():
            data_table_act.delete(data_log)

        for results_log in reverse(log_read()):
            data_table_act.insert(parent='', index='end', iid=results_log, text="", values=(results_log), tag="orow")
        data_table_act.tag_configure('orow', background='#EEEEEE')

    def check_duplicate_Username_emp():
        Username = empl_log_txtbox_username.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(Username) + "'")
        records = cursor.fetchone()

        if records is not None:
            return True
        else:
            return False

        conn.commit()

    def check_duplicate_Pass_emp():
        Password = empl_log_txtbox_pass.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM faculty_data WHERE Password = '" + str(Password) + "'")
        records = cursor.fetchone()

        if records is not None:
            return True
        else:
            return False

        conn.commit() 

        # Account verification
    def verify():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # cursor.execute("""CREATE TABLE IF NOT EXISTS 
        #     user_login(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Username TEXT, Password TEXT, Position TEXt)""")

        # cursor.execute("INSERT INTO user_login (Username,Password) VALUES ('admin', '123' , 'admin')")

        global attempuser
        uname = empl_log_txtbox_username.get()
        pwd = empl_log_txtbox_pass.get()
        emply = "Employee"

        cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(uname) + "' AND  Password = '" + str(pwd) + "' AND  Position = '" + str(emply) + "' AND Status ='Deactivated'")
        inactive = cursor.fetchone()

        if uname=='' or pwd=='':
            messagebox.showinfo("Error", "Please Fill The Empty Field!!")
        elif attempuser >=0 and attempuser <=2:
            cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(uname) + "' AND  Password = '" + str(pwd) + "' AND  Position = '" + str(emply) + "' AND Status='Activated'")
            if cursor.fetchone():
                cursor.execute("SELECT Employee_Name FROM faculty_data WHERE Username like '"+ str(uname)+"' AND Password like '"+ str(pwd)+"'")
                get_Name = cursor.fetchone()
                cursor.execute("SELECT College_Department FROM faculty_data WHERE Username like '"+ str(uname)+"' AND Password like '"+ str(pwd)+"'")
                get_Department = cursor.fetchone()
                cursor.execute("SELECT Employee_No FROM faculty_data WHERE Username like '"+ str(uname)+"' AND Password like '"+ str(pwd)+"'")
                get_ID_Number = cursor.fetchone()
                cursor.execute("SELECT Email FROM faculty_data WHERE Username like '"+ str(uname)+"' AND Password like '"+ str(pwd)+"'")
                get_Email = cursor.fetchone()
                cursor.execute("SELECT Contact_Number FROM faculty_data WHERE Username like '"+ str(uname)+"' AND Password like '"+ str(pwd)+"'")
                get_Phone = cursor.fetchone()

                att_mon_lb_name.configure(text = get_Name)
                att_mon_lb_dept.configure(text = get_Department)
                att_mon_lb_empnum.configure(text = get_ID_Number)
                att_mon_lb_eml.configure(text = get_Email)
                att_mon_lb_cont.configure(text = get_Phone)

                hidetext.configure(state='normal')
                hidetext.insert(0,get_Name)
                text = hidetext.get()
                hidename.configure(text = text)
                hidetext.configure(state='disabled')
                refreshTable_attrec()

                show_frame(attendance_monitoring)
                messagebox.showinfo("Messgae", "WELCOME USER" )

                empl_log_txtbox_username.delete(0, END)
                empl_log_txtbox_pass.delete(0, END)
                check_button_empl_log.deselect()

                currentDateTime = datetime.datetime.now()

                cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    activity_log(
                                "ID"    INTEGER,
                                "Name"  TEXT,
                                "Activity"  TEXT,
                                "Department"    TEXT,
                                "Date_Time" TIMESTAMP,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                                )""")

                eName = att_mon_lb_empnum.cget("text")
                eDepartment = att_mon_lb_dept.cget("text")

                insetdata = (eName,'login',eDepartment,currentDateTime)
                cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                    VAlUES(?,?,?,?);""", insetdata)
                refreshTable_log()
            elif inactive:
                messagebox.showinfo("Messgae", "Please inform the Admin to Activate your account!!\nThank You!! ")

            elif check_duplicate_Username_emp()==False:
                # messagebox.showinfo("Error", "Username Is Incorrect!!")
                attempuser += 1
                count = 3 - attempuser
                messagebox.showinfo("Messge", "Username Is Incorrect!!\n\nReamaining Attempt: "+ str(count))
                empl_log_txtbox_username.delete(0, END)
                empl_log_txtbox_pass.delete(0, END)
                check_button_empl_log.deselect()
                return
            elif check_duplicate_Pass_emp()==False:
                # messagebox.showinfo("Error", "Password Is Incorrect!!")
                attempuser += 1
                count = 3 - attempuser
                messagebox.showinfo("Messge", "Password Is Incorrect!!\n\nReamaining Attempt: "+ str(count))
                empl_log_txtbox_username.delete(0, END)
                empl_log_txtbox_pass.delete(0, END)
                check_button_empl_log.deselect()
                return
            else:
                attempuser += 1
                count = 3 - attempuser
                messagebox.showinfo("Messge", "Please provide correct Username and Password!!\n\nReamaining Attempt: "+ str(count))
                empl_log_txtbox_username.delete(0, END)
                empl_log_txtbox_pass.delete(0, END)
                check_button_empl_log.deselect()
        else:
            cursor.execute("UPDATE faculty_data SET Status='Deactivated' WHERE (Username = '" + str(uname) + "' or  Password = '" + str(pwd) + "') AND  Position = '" + str(emply) + "'")
            messagebox.showinfo("Error", "Access denied, Out of try!!\n\nYour Account has Deactivate!!\n\nPlease contact your Admin!!")
            empl_log_txtbox_username.delete(0, END)
            empl_log_txtbox_pass.delete(0, END)
            check_button_empl_log.deselect()
            attempuser = attempuser - 3

        conn.commit()

        # Login Button
    login_img_btn1 = PhotoImage(file = "pic/login.png")
    empl_log_button = Button(employee_login, image=login_img_btn1, borderwidth=0, bg='#1f2a76', command=verify)
    empl_log_button.place(x=180, y=557)

        # show and hide Password
    def show_password_Employee():
        if  empl_log_txtbox_pass.cget('show') =='*':
            empl_log_txtbox_pass.configure(show='')
        else:
            empl_log_txtbox_pass.configure(show='*')
    check_button_empl_log = Checkbutton(employee_login, text="show password",bg="#1f2a76", command=show_password_Employee, font="Arial", activebackground="#1f2a76",)
    check_button_empl_log.place(x=116,y=520)

        # Back Button
    empl_log_back = PhotoImage(file = "pic/btn_back_log.png")
    empl_log_button_back = customtkinter.CTkButton(master=employee_login,image=empl_log_back, text="" ,
                                                corner_radius=5,bg_color='#e4b50b', fg_color="#e4b50b",hover_color="#006699", command=lambda: show_frame(page2))
    empl_log_button_back.place(x=5, y=5, height=40,width=70)

    # ============= Schedule ========================================================================================================================

    def Schedule_Employee():
        popupwindow_sched_emp = Toplevel(main_window)
        popupwindow_sched_emp.title("Schedule")
        popupwindow_sched_emp.geometry('1020x670')
        popupwindow_sched_emp.grab_set()
        popupwindow_sched_emp.resizable(False,False)

            # open background image
        popupwindow_sched_emp.sched_image = Image.open('pic/12.png')
        popupwindow_sched_emp.sched_resize_image = popupwindow_sched_emp.sched_image.resize((1020,670))
        popupwindow_sched_emp.photo = ImageTk.PhotoImage(popupwindow_sched_emp.sched_resize_image)
        popupwindow_sched_emp.sched_bg_img_lb = Label(popupwindow_sched_emp, image = popupwindow_sched_emp.photo)
        popupwindow_sched_emp.sched_bg_img_lb.pack()

        name_emp = att_mon_lb_name.cget("text")
        depart = att_mon_lb_dept.cget("text")

        def sched_read():
            # sched_name.configure(state='normal')
            # sched_department_combobox.configure(state='normal')

            # nm = sched_name.get()
            # dpt = sched_department_combobox.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Monday'")
            results_sched = cursor.fetchall()
            conn.commit()
            return results_sched

        def refreshTable_sched_emp():
            for data_sched in data_table_sched_emp.get_children():
                data_table_sched_emp.delete(data_sched)

            for results_sched in reverse(sched_read()):
                data_table_sched_emp.insert(parent='', index='end', iid=results_sched, text="", values=(results_sched), tag="orow")
            data_table_sched_emp.tag_configure('orow', background='#EEEEEE')

        def select_row_sched_emp(e):

            selected = data_table_sched_emp.focus()
            values = data_table_sched_emp.item(selected, 'values')

            if values:
                conn = sqlite3.connect("data/data.db")
                cursor = conn.cursor()

                day_sched_emp.configure(state='normal')
                hr_strttime_sched_emp.configure(state='normal')
                min_strttime_sched_emp.configure(state='normal')
                sec_strttime_sched_emp.configure(state='normal')
                p_strttime_sched_emp.configure(state='normal')
                hr_endtime_sched_emp.configure(state='normal')
                min_endtime_sched_emp.configure(state='normal')
                sec_endtime_sched_emp.configure(state='normal')
                p_endtime_sched_emp.configure(state='normal')

                sub_sched_emp.configure(state='normal')
                room_sched_emp.configure(state='normal')
                section_sched_emp.configure(state='normal')

                day_sched_emp.delete(0,END)
                sub_sched_emp.delete(0,END)
                room_sched_emp.delete(0,END)
                section_sched_emp.delete(0,END)
                p_strttime_sched_emp.delete(0,END)
                p_endtime_sched_emp.delete(0,END)
                
                sub_sched_emp.insert(0,values[2])
                room_sched_emp.insert(0,values[3])
                section_sched_emp.insert(0,values[4])

                subject = sub_sched_emp.get()

                cursor.execute("SELECT Day FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                day = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(Start_Time,1,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                hr_strttime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(Start_Time,4,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                min_strttime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(Start_Time,7,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                sec_strttime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(Start_Time,10,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                p_strttime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(End_Time,1,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                hr_endtime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(End_Time,4,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                min_endtime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(End_Time,7,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                sec_endtime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(End_Time,10,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                p_endtime = cursor.fetchone()

                HR_strttime_emp = IntVar()
                HR_strttime_emp.set(hr_strttime)
                MIN_strttime_emp = IntVar()
                MIN_strttime_emp.set(min_strttime)
                SEC_strttime_emp = IntVar()
                SEC_strttime_emp.set(sec_strttime)
                hr_strttime_sched_emp.configure(textvariable=HR_strttime_emp)
                min_strttime_sched_emp.configure(textvariable=MIN_strttime_emp)
                sec_strttime_sched_emp.configure(textvariable=SEC_strttime_emp)
                p_strttime_sched_emp.insert(0,p_strttime)

                HR_endtime_emp = IntVar()
                HR_endtime_emp.set(hr_endtime)
                MIN_endtime_emp = IntVar()
                MIN_endtime_emp.set(min_endtime)
                SEC_endtime_emp = IntVar()
                SEC_endtime_emp.set(sec_endtime)
                hr_endtime_sched_emp.configure(textvariable=HR_endtime_emp)
                min_endtime_sched_emp.configure(textvariable=MIN_endtime_emp)
                sec_endtime_sched_emp.configure(textvariable=SEC_endtime_emp)
                p_endtime_sched_emp.insert(0,p_strttime)
                
                day_sched_emp.insert(0,day)

                sub_sched_lb_emp.configure(text=subject)

                day_sched_emp.configure(state='disabled')
                hr_strttime_sched_emp.configure(state='disabled')
                min_strttime_sched_emp.configure(state='disabled')
                sec_strttime_sched_emp.configure(state='disabled')
                p_strttime_sched_emp.configure(state='disabled')
                hr_endtime_sched_emp.configure(state='disabled')
                min_endtime_sched_emp.configure(state='disabled')
                sec_endtime_sched_emp.configure(state='disabled')
                p_endtime_sched_emp.configure(state='disabled')

                sub_sched_emp.configure(state='disabled')
                room_sched_emp.configure(state='disabled')
                section_sched_emp.configure(state='disabled')

                conn.commit()
                conn.close()

            else:
                messagebox.showinfo("Error", "There is no data on the table !!")

        def clear_sched_emp():
            day_sched_emp.configure(state='normal')
            hr_strttime_sched_emp.configure(state='normal')
            min_strttime_sched_emp.configure(state='normal')
            sec_strttime_sched_emp.configure(state='normal')
            p_strttime_sched_emp.configure(state='normal')
            hr_endtime_sched_emp.configure(state='normal')
            min_endtime_sched_emp.configure(state='normal')
            sec_endtime_sched_emp.configure(state='normal')
            p_endtime_sched_emp.configure(state='normal')

            sub_sched_emp.configure(state='normal')
            room_sched_emp.configure(state='normal')
            section_sched_emp.configure(state='normal')

            day_sched_emp.delete(0,END)
            sub_sched_emp.delete(0,END)
            room_sched_emp.delete(0,END)
            section_sched_emp.delete(0,END)
            p_strttime_sched_emp.delete(0,END)
            p_endtime_sched_emp.delete(0,END)
            p_strttime_sched_emp.insert(0,"AM")
            p_endtime_sched_emp.insert(0,"AM")

            zero= "00"
            HR_strttime = IntVar()
            HR_strttime.set(zero)
            MIN_strttime = IntVar()
            MIN_strttime.set(zero)
            SEC_strttime = IntVar()
            SEC_strttime.set(zero)
            hr_strttime_sched_emp.configure(textvariable=HR_strttime)
            min_strttime_sched_emp.configure(textvariable=MIN_strttime)
            sec_strttime_sched_emp.configure(textvariable=SEC_strttime)
            HR_endtime = IntVar()
            HR_endtime.set(zero)
            MIN_endtime = IntVar()
            MIN_endtime.set(zero)
            SEC_endtime = IntVar()
            SEC_endtime.set(zero)
            hr_endtime_sched_emp.configure(textvariable=HR_endtime)
            min_endtime_sched_emp.configure(textvariable=MIN_endtime)
            sec_endtime_sched_emp.configure(textvariable=SEC_endtime)

            day_sched_emp.configure(state='disabled')
            hr_strttime_sched_emp.configure(state='disabled')
            min_strttime_sched_emp.configure(state='disabled')
            sec_strttime_sched_emp.configure(state='disabled')
            p_strttime_sched_emp.configure(state='disabled')
            hr_endtime_sched_emp.configure(state='disabled')
            min_endtime_sched_emp.configure(state='disabled')
            sec_endtime_sched_emp.configure(state='disabled')
            p_endtime_sched_emp.configure(state='disabled')

            sub_sched_emp.configure(state='disabled')
            room_sched_emp.configure(state='disabled')
            section_sched_emp.configure(state='disabled')

        def Monday_emp():
            btn_mon_sched_emp.configure(fg_color="#00436e")
            btn_tue_sched_emp.configure(fg_color="#ffb000")
            btn_wed_sched_emp.configure(fg_color="#ffb000")
            btn_thur_sched_emp.configure(fg_color="#ffb000")
            btn_fri_sched_emp.configure(fg_color="#ffb000")
            btn_sat_sched_emp.configure(fg_color="#ffb000")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched_emp.get_children():
                data_table_sched_emp.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Monday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched_emp.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched_emp.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

        def Tuesday_emp():
            btn_mon_sched_emp.configure(fg_color="#ffb000")
            btn_tue_sched_emp.configure(fg_color="#00436e")
            btn_wed_sched_emp.configure(fg_color="#ffb000")
            btn_thur_sched_emp.configure(fg_color="#ffb000")
            btn_fri_sched_emp.configure(fg_color="#ffb000")
            btn_sat_sched_emp.configure(fg_color="#ffb000")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched_emp.get_children():
                data_table_sched_emp.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Tuesday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched_emp.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched_emp.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

        def Wednesday_emp():
            btn_mon_sched_emp.configure(fg_color="#ffb000")
            btn_tue_sched_emp.configure(fg_color="#ffb000")
            btn_wed_sched_emp.configure(fg_color="#00436e")
            btn_thur_sched_emp.configure(fg_color="#ffb000")
            btn_fri_sched_emp.configure(fg_color="#ffb000")
            btn_sat_sched_emp.configure(fg_color="#ffb000")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched_emp.get_children():
                data_table_sched_emp.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Wednesday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched_emp.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched_emp.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

        def Thursday_emp():
            btn_mon_sched_emp.configure(fg_color="#ffb000")
            btn_tue_sched_emp.configure(fg_color="#ffb000")
            btn_wed_sched_emp.configure(fg_color="#ffb000")
            btn_thur_sched_emp.configure(fg_color="#00436e")
            btn_fri_sched_emp.configure(fg_color="#ffb000")
            btn_sat_sched_emp.configure(fg_color="#ffb000")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched_emp.get_children():
                data_table_sched_emp.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Thursday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched_emp.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched_emp.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

        def Friday_emp():
            btn_mon_sched_emp.configure(fg_color="#ffb000")
            btn_tue_sched_emp.configure(fg_color="#ffb000")
            btn_wed_sched_emp.configure(fg_color="#ffb000")
            btn_thur_sched_emp.configure(fg_color="#ffb000")
            btn_fri_sched_emp.configure(fg_color="#00436e")
            btn_sat_sched_emp.configure(fg_color="#ffb000")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched_emp.get_children():
                data_table_sched_emp.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Friday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched_emp.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched_emp.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

        def Saturday_emp():
            btn_mon_sched_emp.configure(fg_color="#ffb000")
            btn_tue_sched_emp.configure(fg_color="#ffb000")
            btn_wed_sched_emp.configure(fg_color="#ffb000")
            btn_thur_sched_emp.configure(fg_color="#ffb000")
            btn_fri_sched_emp.configure(fg_color="#ffb000")
            btn_sat_sched_emp.configure(fg_color="#00436e")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched_emp.get_children():
                data_table_sched_emp.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Saturday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched_emp.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched_emp.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched_emp.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

            # Data Table "TreeView"
        scrollbary_sched_emp = Scrollbar(popupwindow_sched_emp, orient=VERTICAL)
        scrollbary_sched_emp.place(x=1030, y=230, height=350)

        # style = ttk.Style()
        # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

        data_table_sched_emp = ttk.Treeview(popupwindow_sched_emp)
        data_table_sched_emp.place(x=145, y=415, width=740, height=215)
        data_table_sched_emp.configure(yscrollcommand=scrollbary_sched_emp.set)

        scrollbary_sched_emp.configure(command=data_table_sched_emp.yview)

        data_table_sched_emp['columns'] = ("Start Time","End Time","Subject","Room","Section")
        # Format Columns
        data_table_sched_emp.column("#0", width=0, stretch=NO)
        data_table_sched_emp.column("Start Time", anchor=CENTER,width=0)
        data_table_sched_emp.column("End Time", anchor=CENTER, width=50)
        data_table_sched_emp.column("Subject", anchor=CENTER, width=50)
        data_table_sched_emp.column("Room", anchor=CENTER, width=50)
        data_table_sched_emp.column("Section", anchor=CENTER, width=50)

        # Create Headings
        data_table_sched_emp.heading("Start Time", text="Start Time", anchor=CENTER)
        data_table_sched_emp.heading("End Time", text="End Time", anchor=CENTER)
        data_table_sched_emp.heading("Subject", text="Subject", anchor=CENTER)
        data_table_sched_emp.heading("Room", text="Room", anchor=CENTER)
        data_table_sched_emp.heading("Section", text="Section", anchor=CENTER)

        data_table_sched_emp.bind("<ButtonRelease-1>", select_row_sched_emp)

        refreshTable_sched_emp()

            # Entry Employee Name
        sched_name_emp = Entry(popupwindow_sched_emp, state='disabled')
        sched_name_emp.place(x=180, y=172, width=150)

            # Entry Day
        day_sched_emp = ttk.Combobox(popupwindow_sched_emp, state='disabled', values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        day_sched_emp.place(x=180, y=209, width=150)

            # Subject Label
        sub_sched_lb_emp = Label(popupwindow_sched_emp, fg='#f0f0f0', font = "Heltvetica 9")
        sub_sched_lb_emp.place(x=180, y=235)

            # Entry Subject
        sub_sched_emp = Entry(popupwindow_sched_emp, state='disabled')
        sub_sched_emp.place(x=180, y=258, width=150)

            # ComboBox College Department
        sched_department_combobox_emp = ttk.Combobox(popupwindow_sched_emp, state='disabled', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
        sched_department_combobox_emp.place(x=545, y=172, width=150)
        
        #     # Entry Start Time
        # strttime_sched= Entry(popupwindow_sched,textvariable=time_format)
        # strttime_sched.place(x=545, y=209, width=150)

            # Entry Start Time Hour
        var_hr_strt_emp = IntVar()
        var_hr_strt_emp.set(00)
        hr_strttime_sched_emp = Spinbox(popupwindow_sched_emp, state='disabled', from_=00, to=12, format="%02.0f",textvariable=var_hr_strt_emp)
        hr_strttime_sched_emp.place(x=545, y=209, width=35)

            # Entry Start Time Minute
        var_min_strt_emp = IntVar()
        var_min_strt_emp.set(00)
        min_strttime_sched_emp = Spinbox(popupwindow_sched_emp, state='disabled', from_=00, to=59, format="%02.0f",textvariable=var_min_strt_emp)
        min_strttime_sched_emp.place(x=585, y=209, width=35)

            # Entry Start Time Second
        var_sec_strt_emp = IntVar()
        var_sec_strt_emp.set(00)
        sec_strttime_sched_emp = Spinbox(popupwindow_sched_emp, state='disabled', from_=00, to=59, format="%02.0f",textvariable=var_sec_strt_emp)
        sec_strttime_sched_emp.place(x=625, y=209, width=35)

            # ComboBox College Department
        p_strttime_sched_emp = ttk.Combobox(popupwindow_sched_emp, state='disabled', values=["AM", "PM",])
        p_strttime_sched_emp.set("AM")
        p_strttime_sched_emp.place(x=665, y=209, width=45)

            # Entry Room
        room_sched_emp = Entry(popupwindow_sched_emp, state='disabled')
        room_sched_emp.place(x=545, y=258, width=150)

        #     # Entry End Time
        # endtime_sched = Entry(popupwindow_sched)
        # endtime_sched.place(x=810, y=209, width=150)

            # Entry End Time Hour
        var_hr_end_emp = IntVar()
        var_hr_end_emp.set(00)
        hr_endtime_sched_emp = Spinbox(popupwindow_sched_emp, state='disabled', from_=00, to=12, format="%02.0f",textvariable=var_hr_end_emp)
        hr_endtime_sched_emp.place(x=810, y=209, width=35)

            # Entry End Time Minute
        var_min_end_emp = IntVar()
        var_min_end_emp.set(00)
        min_endtime_sched_emp = Spinbox(popupwindow_sched_emp, state='disabled', from_=00, to=59, format="%02.0f",textvariable=var_min_end_emp)
        min_endtime_sched_emp.place(x=850, y=209, width=35)

            # Entry End Time Second
        var_sec_end_emp = IntVar()
        var_sec_end_emp.set(00)
        sec_endtime_sched_emp = Spinbox(popupwindow_sched_emp, state='disabled', from_=00, to=59, format="%02.0f",textvariable=var_sec_end_emp)
        sec_endtime_sched_emp.place(x=890, y=209, width=35)

            # ComboBox College Department
        p_endtime_sched_emp = ttk.Combobox(popupwindow_sched_emp, state='disabled', values=["AM", "PM",])
        p_endtime_sched_emp.set("AM")
        p_endtime_sched_emp.place(x=930, y=209, width=45)

            # Entry Section
        section_sched_emp = Entry(popupwindow_sched_emp, state='disabled')
        section_sched_emp.place(x=810, y=258, width=150)

        sched_name_emp.configure(state='normal')
        sched_department_combobox_emp.configure(state='normal')
        sched_name_emp.insert(0, name_emp)
        sched_department_combobox_emp.insert(0, depart)
        sched_name_emp.configure(state='disabled')
        sched_department_combobox_emp.configure(state='disabled')

        #     # Save Data Button
        # save_pic_emp = PhotoImage(file = "pic/btn_save.png")
        # save_button_sched_emp = customtkinter.CTkButton(master=popupwindow_sched_emp,image=save_pic_emp, text="" ,
        #                                             corner_radius=6, fg_color="#00436e",hover_color="#006699", command='save_sched')
        # save_button_sched_emp.place(x=315, y=290, height=32,width=131)

        #     # Updated Button
        # update_pic_emp = PhotoImage(file = "pic/btn_update.png")
        # button_update_sched_emp = customtkinter.CTkButton(master=popupwindow_sched_emp,state='disabled',image=update_pic_emp, text="" ,
        #                                             corner_radius=6, fg_color="#00436e",hover_color="#006699", command='update_sched')
        # button_update_sched_emp.place(x=460, y=290, height=32,width=131)

            # Reset Button
        reset_btnsched_emp = PhotoImage(file = "pic/btn_reset.png")
        button_resetsched_emp = customtkinter.CTkButton(master=popupwindow_sched_emp,image=reset_btnsched_emp, text="" ,
                                                    corner_radius=6, fg_color="#00436e",hover_color="#006699", command=clear_sched_emp)
        button_resetsched_emp.place(x=460, y=290, height=32,width=131)

            # Moday Button
        mon_btn_emp = PhotoImage(file = "pic/btn_mon.png")
        btn_mon_sched_emp = customtkinter.CTkButton(master=popupwindow_sched_emp,image=mon_btn_emp, text="" ,
                                                    corner_radius=6, fg_color="#00436e",hover_color="#006699", command=Monday_emp)
        btn_mon_sched_emp.place(x=90, y=373, height=28,width=131)

            # Tuesday Button
        tue_btn_emp = PhotoImage(file = "pic/btn_tue.png")
        btn_tue_sched_emp = customtkinter.CTkButton(master=popupwindow_sched_emp,image=tue_btn_emp, text="" ,
                                                    corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Tuesday_emp)
        btn_tue_sched_emp.place(x=235, y=373, height=28,width=131)

             # Wednesday Button
        wed_btn_emp = PhotoImage(file = "pic/btn_wed.png")
        btn_wed_sched_emp = customtkinter.CTkButton(master=popupwindow_sched_emp,image=wed_btn_emp, text="" ,
                                                    corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Wednesday_emp)
        btn_wed_sched_emp.place(x=380, y=373, height=28,width=131)

             # Thursday Button
        thur_btn_emp = PhotoImage(file = "pic/btn_thu.png")
        btn_thur_sched_emp = customtkinter.CTkButton(master=popupwindow_sched_emp,image=thur_btn_emp, text="" ,
                                                    corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Thursday_emp)
        btn_thur_sched_emp.place(x=525, y=373, height=28,width=131)

             # Friday Button
        fri_btn_emp = PhotoImage(file = "pic/btn_fri.png")
        btn_fri_sched_emp = customtkinter.CTkButton(master=popupwindow_sched_emp,image=fri_btn_emp, text="" ,
                                                    corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Friday_emp)
        btn_fri_sched_emp.place(x=670, y=373, height=28,width=131)

             # Saturday Button
        sat_btn_emp = PhotoImage(file = "pic/btn_sat.png")
        btn_sat_sched_emp = customtkinter.CTkButton(master=popupwindow_sched_emp,image=sat_btn_emp, text="" ,
                                                    corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Saturday_emp)
        btn_sat_sched_emp.place(x=815, y=373, height=28,width=131)

    # ============= Employee Attendance Record In Frame ========================================================================================================================

        # open background image
    attendance_monitoring.att_mon_image = Image.open('pic/6.png')
    attendance_monitoring.att_mon_resize_image = attendance_monitoring.att_mon_image.resize((1362, 692))
    attendance_monitoring.photo = ImageTk.PhotoImage(attendance_monitoring.att_mon_resize_image)
    attendance_monitoring.att_mon_bg_img_lb = Label(attendance_monitoring, image = attendance_monitoring.photo)
    attendance_monitoring.att_mon_bg_img_lb.pack()

    def reverse(tuples):
        new_tup = tuples[::-1]
        return new_tup

        # Get And Disply the data in the table
    def attrec_read():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        set_name = hidename.cget("text")

        cursor.execute("SELECT Time_in,Time_out,_Date,Status FROM attendance_record WHERE Name='"+ str(set_name) +"' AND Department='Psychology'")
        results_user = cursor.fetchall()
        conn.commit()
        return results_user

        # Refresh the tabble on Treeview
    def refreshTable_attrec():

        for data_attrec in data_table_emp_att_rec.get_children():
            data_table_emp_att_rec.delete(data_attrec)

        for results_attrec in reverse(attrec_read()):
            data_table_emp_att_rec.insert(parent='', index='end', iid=results_attrec, text="", values=(results_attrec), tag="orow")
        data_table_emp_att_rec.tag_configure('orow', background='#EEEEEE')

    hidetext = Entry(attendance_monitoring,borderwidth=0,fg='#ffffff',bg='#ffffff',state='disabled')
    hidetext.place(x=500, y=350 )

         # Data Table "TreeView"
    scrollbary_emp_att_rec = Scrollbar(attendance_monitoring, orient=VERTICAL)
    scrollbary_emp_att_rec.place(x=1090, y=300, height=335)

    # style = ttk.Style()
    # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table_emp_att_rec = ttk.Treeview(attendance_monitoring)
    data_table_emp_att_rec.place(x=340, y=300, width=750, height=335)
    data_table_emp_att_rec.configure(yscrollcommand=scrollbary_emp_att_rec.set)

    scrollbary_emp_att_rec.configure(command=data_table_emp_att_rec.yview)

    data_table_emp_att_rec['columns'] = ("Time in","Time out","Date","Status")
    # Format Columns
    data_table_emp_att_rec.column("#0", width=0, stretch=NO)
    data_table_emp_att_rec.column("Time in", anchor=CENTER, width=50)
    data_table_emp_att_rec.column("Time out", anchor=CENTER, width=50)
    data_table_emp_att_rec.column("Date", anchor=CENTER, width=50)
    data_table_emp_att_rec.column("Status", anchor=CENTER, width=50)

    # Create Headings
    data_table_emp_att_rec.heading("Time in", text="Time in", anchor=CENTER)
    data_table_emp_att_rec.heading("Time out", text="Time out", anchor=CENTER)
    data_table_emp_att_rec.heading("Date", text="Date", anchor=CENTER)
    data_table_emp_att_rec.heading("Status", text="Status", anchor=CENTER)

    hidename = Label(attendance_monitoring, bg ='#ffffff',fg='#ffffff')
    hidename.place(x=50, y=400)

        # Employee Name Label
    att_mon_lb_name = Label(attendance_monitoring, bg ='#ffd636', font = "Heltvetica 30 bold")
    att_mon_lb_name.place(x=300, y=40)

        # Employee Number Label
    att_mon_lb_empnum = Label(attendance_monitoring, bg ='#ffd636', font = "Heltvetica 17 bold")
    att_mon_lb_empnum.place(x=300, y=100)

        # Employee Department Label
    att_mon_lb_dept = Label(attendance_monitoring, bg ='#ffd636', font = "Heltvetica 17 bold")
    att_mon_lb_dept.place(x=300, y=140)

        # Employee Email Label
    att_mon_lb_eml = Label(attendance_monitoring, bg ='#ffd636', font = "Heltvetica 17 bold")
    att_mon_lb_eml.place(x=660, y=100)

        # Employee Phone Number Label
    att_mon_lb_cont = Label(attendance_monitoring, bg ='#ffd636', font = "Heltvetica 17 bold")
    att_mon_lb_cont.place(x=660, y=140)

        # Search Entry
    search_entry_att_mon = StringVar()
    search_att_mon = Entry(attendance_monitoring, textvariable = search_entry_att_mon)
    search_att_mon.place(x=590, y=237, width=210)

        # Search Button
    search_btn_att_mon = PhotoImage(file = "pic/btn_search.png")
    att_mon_button_search = customtkinter.CTkButton(master=attendance_monitoring,image=search_btn_att_mon, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command= "")
    att_mon_button_search.place(x=820, y=235, height=20,width=90)

        # Show All Button
    showall_btn_att_mon = PhotoImage(file = "pic/btn_showall.png")
    att_mon_button_showall = customtkinter.CTkButton(master=attendance_monitoring,image=showall_btn_att_mon, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_attrec)
    att_mon_button_showall.place(x=680, y=655, height=27,width=110)

        # Schedule Button
    textsched_btn = PhotoImage(file = "pic/btn_schedule.png")
    sched_btn = customtkinter.CTkButton(master=attendance_monitoring,image=textsched_btn, text="" ,
                                                corner_radius=6, bg_color="#ffd636", fg_color="#00436e",hover_color="#006699", command=Schedule_Employee)
    sched_btn.place(x=960, y=100, height=40,width=210)

    def logout_employee():
        show_frame(employee_login)
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        currentDateTime = datetime.datetime.now()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            activity_log(
                        "ID"    INTEGER,
                        "Name"  TEXT,
                        "Activity"  TEXT,
                        "Department"    TEXT,
                        "Date_Time" TIMESTAMP,
                        PRIMARY KEY("ID" AUTOINCREMENT)
                        )""")

        eName = att_mon_lb_empnum.cget("text")
        eDepartment = att_mon_lb_dept.cget("text")

        insetdata = (eName,'Logout',eDepartment,currentDateTime)
        cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                            VAlUES(?,?,?,?);""", insetdata)
        conn.commit()
        conn.close()
        refreshTable_log()


        # Logout Button
    att_mon_logout = PhotoImage(file = "pic/btn_logout.png")
    att_mon_button_logout = customtkinter.CTkButton(master=attendance_monitoring,image=att_mon_logout, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#ffffff",hover_color="#6699cc", command=logout_employee)
    att_mon_button_logout.place(x=30, y=565, height=100,width=100)

    refreshTable_attrec()

    #     # Attendace Record Button
    # record_btn_att_mon = PhotoImage(file = "pic/btn_attendace_rec.png")
    # att_mon_button_record = customtkinter.CTkButton(master=attendance_monitoring,image=record_btn_att_mon, text="" ,
    #                                             corner_radius=20,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(employee_login))
    # att_mon_button_record.place(x=773, y=319, height=100,width=412)

    #     # Personal Information Button
    # info_btn_att_mon = PhotoImage(file = "pic/btn_personal_info.png")
    # att_mon_button_info = customtkinter.CTkButton(master=attendance_monitoring,image=info_btn_att_mon, text="" ,
    #                                             corner_radius=20,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(employee_login))
    # att_mon_button_info.place(x=296, y=319, height=100,width=412)

    # ======== Page 3 Admin Sign In Frame ====================================================================================================================================

        # open background image
    page3.pg3_image = Image.open('pic/4.png')
    page3.pg3_resize_image = page3.pg3_image.resize((1362, 692))
    page3.photo = ImageTk.PhotoImage(page3.pg3_resize_image)
    page3.pg3_bg_img_lb = Label(page3, image = page3.photo)
    page3.pg3_bg_img_lb.pack() 

        # Text Box Username and Password
    username_lbl_pg3 = Label(page3, text='Username', fg='Black', bg ='#1f2a76', font = "Heltvetica 27 bold")
    username_lbl_pg3.place(x=116, y=207)
    pg3_txtbox_username = Entry(page3, borderwidth=0, width=16, font=('Arial',30))
    # pg3_txtbox_username.insert(0,"Username")
    pg3_txtbox_username.place(x=116, y=256, height=92)

    password_lbl_pg3 = Label(page3, text='Password', fg='Black', bg ='#1f2a76', font = "Heltvetica 27 bold")
    password_lbl_pg3.place(x=116, y=370)
    pg3_txtbox_pass = Entry(page3, borderwidth=0, width=16, font=('Arial', 30), show='*')
    # pg3_txtbox_pass.insert(0,"Password")
    pg3_txtbox_pass.place(x=116, y=422, height=90)

    def check_duplicate_Username_admin():
        Username = pg3_txtbox_username.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(Username) + "'")
        records = cursor.fetchone()

        if records is not None:
            return True
        else:
            return False

        conn.commit()

    def check_duplicate_Pass_admin():
        Password = pg3_txtbox_pass.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM faculty_data WHERE Password = '" + str(Password) + "'")
        records = cursor.fetchone()

        if records is not None:
            return True
        else:
            return False

        conn.commit()
 
        # Account verification
    def verify_admin():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # cursor.execute("""CREATE TABLE IF NOT EXISTS 
        #     user_login(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Username TEXT, Password TEXT, Position TEXt)""")

        # cursor.execute("INSERT INTO user_login (Username,Password) VALUES ('admin', '123' , 'admin')")
        
        global attemptadmin 
        uname = pg3_txtbox_username.get()
        pwd = pg3_txtbox_pass.get()
        adm = "Admin"
        state = "Activated"

        cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(uname) + "' AND  Password = '" + str(pwd) + "' AND  Position = '" + str(adm) + "' AND Status ='Deactivated'")
        inactive = cursor.fetchone()

        if uname=='' or pwd=='':
            messagebox.showinfo("Error", "Please Fill The Empty Field!!")
        elif attemptadmin >=0 and attemptadmin <=2:
            cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(uname) + "' AND  Password = '" + str(pwd) + "' AND  Position = '" + str(adm) + "' AND Status ='" + str(state) + "'")
            if cursor.fetchone():
                cursor.execute("SELECT Employee_No FROM faculty_data WHERE Username = '"+ str(uname)+"' AND Password = '"+ str(pwd)+"'")
                get_Name = cursor.fetchone()
                cursor.execute("SELECT College_Department FROM faculty_data WHERE Username = '"+ str(uname)+"' AND Password = '"+ str(pwd)+"'")
                get_Department = cursor.fetchone()

                show_frame(page4)
                messagebox.showinfo("Messgae", "WELCOME USER")

                pg3_txtbox_username.delete(0, END)
                pg3_txtbox_pass.delete(0, END)
                check_button.deselect()

                pg4_lb_name.configure(text = get_Name)
                pg4_lb_dept.configure(text = get_Department)

                currentDateTime = datetime.datetime.now()

                cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    activity_log(
                                "ID"    INTEGER,
                                "Name"  TEXT,
                                "Activity"  TEXT,
                                "Department"    TEXT,
                                "Date_Time" TIMESTAMP,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                                )""")

                eName = pg4_lb_name.cget("text")
                eDepartment = pg4_lb_dept.cget("text")

                insetdata = str(eName),'login',str(eDepartment),currentDateTime
                cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                    VAlUES(?,?,?,?)""", insetdata)
                refreshTable_log()

            elif inactive:
                messagebox.showinfo("Messgae", "Please inform the  Co-Admin to Activate your Account!!\nThank You!! ")
            elif check_duplicate_Username_admin()==False:
                # messagebox.showinfo("Error", "Username Is Incorrect!!")
                attemptadmin += 1
                count = 3 - attemptadmin
                messagebox.showinfo("Messge", "Username Is Incorrect!!\n\nReamaining Attempt: "+ str(count))
                pg3_txtbox_username.delete(0, END)
                pg3_txtbox_pass.delete(0, END)
                check_button.deselect()
                return
            elif check_duplicate_Pass_admin()==False:
                # messagebox.showinfo("Error", "Password Is Incorrect!!")
                attemptadmin += 1
                count = 3 - attemptadmin
                messagebox.showinfo("Messge", "Password Is Incorrect!!\n\nReamaining Attempt: "+ str(count))
                pg3_txtbox_username.delete(0, END)
                pg3_txtbox_pass.delete(0, END)
                check_button.deselect()
                return
            else:
                attemptadmin += 1
                count = 3 - attemptadmin
                messagebox.showinfo("Messge", "Please provide correct Username and Password!!\n\nReamaining Attempt: "+ str(count))
                pg3_txtbox_username.delete(0, END)
                pg3_txtbox_pass.delete(0, END)
                check_button.deselect()
            
        else:
            cursor.execute("UPDATE faculty_data SET Status='Deactivated' WHERE (Username = '" + str(uname) + "' or  Password = '" + str(pwd) + "') AND  Position = '" + str(adm) + "'")
            messagebox.showinfo("Error", "Access denied, Out of try!!\n\nYour Account has Deactivate!!\n\nPlease contact your Co-Admin!!")
            pg3_txtbox_username.delete(0, END)
            pg3_txtbox_pass.delete(0, END)
            check_button.deselect()
            attemptadmin = attemptadmin - 3
            

        conn.commit()
        conn.close()

        # Login Button
    login_img_btn = PhotoImage(file = "pic/login.png")
    pg3_button = Button(page3, image=login_img_btn, borderwidth=0, bg='#1f2a76', command=verify_admin)
    pg3_button.place(x=180, y=557)

        # show and hide Password
    def show_password():
        if  pg3_txtbox_pass.cget('show') =='*':
            pg3_txtbox_pass.configure(show='')
        else:
            pg3_txtbox_pass.configure(show='*')
    check_button = Checkbutton(page3, text="show password",bg="#1f2a76", command=show_password, font="Arial", activebackground="#1f2a76",)
    check_button.place(x=116,y=520)

        # Back Button
    pg3_back = PhotoImage(file = "pic/btn_back_log.png")
    pg3_button_back = customtkinter.CTkButton(master=page3,image=pg3_back, text="" ,
                                                corner_radius=5,bg_color='#e4b50b', fg_color="#e4b50b",hover_color="#006699", command=lambda: show_frame(page2))
    pg3_button_back.place(x=5, y=5, height=40,width=70)

    # ============= Page 4 Home  Frame ====================================================================================================================

        # open background image
    page4.pg4_image = Image.open('pic/7.png')
    page4.pg4_resize_image = page4.pg4_image.resize((1362, 692))
    page4.photo = ImageTk.PhotoImage(page4.pg4_resize_image)
    page4.pg4_bg_img_lb = Label(page4, image = page4.photo)
    page4.pg4_bg_img_lb.pack()

        # Admin Name Label
    pg4_lb_name = Label(page4, bg ='#ffffff', fg='#ffffff', font = "Heltvetica 9")
    pg4_lb_name.place(x=540, y=10)

        # Admin Department Label
    pg4_lb_dept = Label(page4, bg ='#ffffff', fg='#ffffff', font = "Heltvetica 9")
    pg4_lb_dept.place(x=640, y=10)

        # Faculty Information Button
    faculty_info_btn = PhotoImage(file = "pic/faculty_info.png")
    pg4_button_faculty = customtkinter.CTkButton(master=page4,image=faculty_info_btn, text="" ,
                                                corner_radius=30,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(faculty_information))
    pg4_button_faculty.place(x=100, y=314, height=134,width=562)

        # Activity Log Button
    att_rec_btn = PhotoImage(file = "pic/act_log.png")
    pg4_button_att_rec = customtkinter.CTkButton(master=page4,image=att_rec_btn, text="" ,
                                                corner_radius=30,bg_color='#ffffff', fg_color="#cc9900",hover_color="#fdca34", command=lambda: show_frame(activity_log))
    pg4_button_att_rec.place(x=100, y=469, height=178,width=330)

        # About Button
    about_btn = PhotoImage(file = "pic/about.png")
    pg4_button_photo = customtkinter.CTkButton(master=page4,image=about_btn, text="" ,
                                                corner_radius=30,bg_color='#ffffff', fg_color="#cc9900",hover_color="#fdca34", command=lambda: show_frame(about))
    pg4_button_photo.place(x=456, y=469, height=178,width=197)

        # Attendace Record Button
    photo_btn = PhotoImage(file = "pic/attendance_rec.png")
    pg4_button_train_img = customtkinter.CTkButton(master=page4,image=photo_btn, text="" ,
                                                corner_radius=30,bg_color='#ffffff', fg_color="#cc9900",hover_color="#fdca34", command=lambda:show_frame(attendance_record))
    pg4_button_train_img.place(x=683, y=315, height=333,width=348)

        # Developers Button
    developers_btn = PhotoImage(file = "pic/developers.png")
    pg4_button_developers = customtkinter.CTkButton(master=page4,image=developers_btn, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(developers))
    pg4_button_developers.place(x=1048, y=314, height=134,width=246)

    def logout():
        show_frame(page3)
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        currentDateTime = datetime.datetime.now()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            activity_log(
                        "ID"    INTEGER,
                        "Name"  TEXT,
                        "Activity"  TEXT,
                        "Department"    TEXT,
                        "Date_Time" TIMESTAMP,
                        PRIMARY KEY("ID" AUTOINCREMENT)
                        )""")

        eName = pg4_lb_name.cget("text")
        eDepartment = pg4_lb_dept.cget("text")

        insetdata = str(eName),'Logout',str(eDepartment),currentDateTime
        cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                            VAlUES(?,?,?,?)""", insetdata)
        conn.commit()
        conn.close()
        refreshTable_log()

        # Logout Button
    logout_btn = PhotoImage(file = "pic/logout.png")
    pg4_button_logout = customtkinter.CTkButton(master=page4,image=logout_btn, text="" ,
                                                corner_radius=30,bg_color='#ffffff', fg_color="#ffffff",hover_color="#6699cc", command=logout)
    pg4_button_logout.place(x=1075, y=469, height=178,width=197)

    # ============= Developers Frame ========================================================================================================================================

        # open background image
    developers.dev_image = Image.open('pic/8a.png')
    developers.dev_resize_image = developers.dev_image.resize((1362, 692))
    developers.photo = ImageTk.PhotoImage(developers.dev_resize_image)
    developers.dev_bg_img_lb = Label(developers, image = developers.photo)
    developers.dev_bg_img_lb.pack()

        # Back Button
    dev_back = PhotoImage(file = "pic/btn_back_page.png")
    dev_button_back = customtkinter.CTkButton(master=developers,image=dev_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
    dev_button_back.place(x=45, y=595, height=50,width=140)

    # ============= About(the Collage) Frame ================================================================================================================================
# #fcd24f
        # open background image
    about.abt_image = Image.open('pic/9a.png')
    about.abt_resize_image = about.abt_image.resize((1362, 692))
    about.photo = ImageTk.PhotoImage(about.abt_resize_image)
    about.abt_bg_img_lb = Label(about, image = about.photo)
    about.abt_bg_img_lb.pack()

        # Next Button
    next_btn = PhotoImage(file = "pic/btn_forward.png")
    button_next = customtkinter.CTkButton(master=about,image=next_btn, text="" ,
                                                corner_radius=6,fg_color="#ffffff",hover_color="#006699", command=lambda: show_frame(about_clg_goal))
    button_next.place(x=1250, y=320, height=100,width=100)

        # Back Button
    abt_back = PhotoImage(file = "pic/btn_back_page.png")
    abt_button_back = customtkinter.CTkButton(master=about,image=abt_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
    abt_button_back.place(x=20, y=595, height=50,width=140)

    # ============= About(Collage Goals) Frame ================================================================================================================================

        # open background image
    about_clg_goal.abt_clg_goal_image = Image.open('pic/9b.png')
    about_clg_goal.abt_clg_goal_resize_image = about_clg_goal.abt_clg_goal_image.resize((1362, 692))
    about_clg_goal.abt_clg_goal_photo = ImageTk.PhotoImage(about_clg_goal.abt_clg_goal_resize_image)
    about_clg_goal.abt_clg_goal_bg_img_lb = Label(about_clg_goal, image = about_clg_goal.abt_clg_goal_photo)
    about_clg_goal.abt_clg_goal_bg_img_lb.pack()

        # Next Button
    next_btn_abt_clg_goal = PhotoImage(file = "pic/btn_forward.png")
    abt_clg_goal_button_next = customtkinter.CTkButton(master=about_clg_goal,image=next_btn_abt_clg_goal, text="" ,
                                                corner_radius=6,fg_color="#ffffff",hover_color="#006699", command=lambda: show_frame(about_program))
    abt_clg_goal_button_next.place(x=1250, y=320, height=100,width=100)

        # Back Button
    abt_clg_goal_back_btn = PhotoImage(file = "pic/btn_back.png")
    abt_clg_goal_button_back = customtkinter.CTkButton(master=about_clg_goal,image=abt_clg_goal_back_btn, text="" ,
                                                corner_radius=6,fg_color="#ffffff",hover_color="#006699", command=lambda: show_frame(about))
    abt_clg_goal_button_back.place(x=20, y=320, height=100,width=100)

        # Back Button
    abt_clg_goal_back = PhotoImage(file = "pic/btn_back_page.png")
    abt_clg_goal_button_back = customtkinter.CTkButton(master=about_clg_goal,image=abt_clg_goal_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
    abt_clg_goal_button_back.place(x=20, y=595, height=50,width=140)

    # ============= About(Collage Goals) Frame =================================================================================================================================

        # open background image
    about_program.abt_prog_image = Image.open('pic/9c.png')
    about_program.abt_prog_resize_image = about_program.abt_prog_image.resize((1362, 692))
    about_program.abt_prog_photo = ImageTk.PhotoImage(about_program.abt_prog_resize_image)
    about_program.abt_prog_bg_img_lb = Label(about_program, image = about_program.abt_prog_photo)
    about_program.abt_prog_bg_img_lb.pack()

        # Back Button
    abt_prog_back_btn = PhotoImage(file = "pic/btn_back.png")
    abt_prog_button_back = customtkinter.CTkButton(master=about_program,image=abt_prog_back_btn, text="" ,
                                                corner_radius=6,fg_color="#ffffff",hover_color="#006699", command=lambda: show_frame(about_clg_goal))
    abt_prog_button_back.place(x=20, y=320, height=100,width=100)

        # Back Button
    abt_prog_back = PhotoImage(file = "pic/btn_back_page.png")
    abt_prog_button_back = customtkinter.CTkButton(master=about_program,image=abt_prog_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
    abt_prog_button_back.place(x=20, y=595, height=50,width=140)

    # ============= Attendace Record Frame ======================================================================================================================================

        # open background image
    attendance_record.att_rec_image = Image.open('pic/8.png')
    attendance_record.att_rec_resize_image = attendance_record.att_rec_image.resize((1362, 692))
    attendance_record.photo = ImageTk.PhotoImage(attendance_record.att_rec_resize_image)
    attendance_record.att_rec_bg_img_lb = Label(attendance_record, image = attendance_record.photo)
    attendance_record.att_rec_bg_img_lb.pack()

        # Mathematics Faculty Button
    math_fac_btn = PhotoImage(file = "pic/math_faculty.png")
    att_rec_button_math_fac = customtkinter.CTkButton(master=attendance_record,image=math_fac_btn, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(mathematics_att_record))
    att_rec_button_math_fac.place(x=254, y=254, height=99,width=413)

        # Psychology Faculty Button
    psyc_fac_btn = PhotoImage(file = "pic/psyc_faculty.png")
    att_rec_button_psyc_fac = customtkinter.CTkButton(master=attendance_record,image=psyc_fac_btn, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(psychology_att_record))
    att_rec_button_psyc_fac.place(x=731, y=254, height=99,width=413)

        # ITE Faculty Button
    ite_fac_btn = PhotoImage(file = "pic/ite_faculty.png")
    att_rec_button_ite_fac = customtkinter.CTkButton(master=attendance_record,image=ite_fac_btn, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(ite_att_record))
    att_rec_button_ite_fac.place(x=254, y=394, height=99,width=413)

        # Applied Psychology Faculty Button
    app_psyc_fac_btn = PhotoImage(file = "pic/applied_psyc_faculty.png")
    att_rec_button_app_psyc_fac = customtkinter.CTkButton(master=attendance_record,image=app_psyc_fac_btn, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(applied_physics_att_record))
    att_rec_button_app_psyc_fac.place(x=731, y=394, height=99,width=413)

        # Back Button
    att_rec_back = PhotoImage(file = "pic/btn_back_page.png")
    att_rec_button_back = customtkinter.CTkButton(master=attendance_record,image=att_rec_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
    att_rec_button_back.place(x=45, y=595, height=50,width=140)

     # ============= Schedule ========================================================================================================================

    def Schedule():
        popupwindow_sched = Toplevel(main_window)
        popupwindow_sched.title("Schedule")
        popupwindow_sched.geometry('1020x670')
        popupwindow_sched.grab_set()
        popupwindow_sched.resizable(False,False)

            # open background image
        popupwindow_sched.sched_image = Image.open('pic/12.png')
        popupwindow_sched.sched_resize_image = popupwindow_sched.sched_image.resize((1020,670))
        popupwindow_sched.photo = ImageTk.PhotoImage(popupwindow_sched.sched_resize_image)
        popupwindow_sched.sched_bg_img_lb = Label(popupwindow_sched, image = popupwindow_sched.photo)
        popupwindow_sched.sched_bg_img_lb.pack()

        name_emp = employee_name_fac_inf.get()
        depart = department_combobox.get()

        def save_sched():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            currentDateTime = datetime.datetime.now()

            cursor.execute("""CREATE TABLE IF NOT EXISTS 
                schedule(
                            "ID" INTEGER,
                            "Name" TEXT,
                            "Department" TEXT,
                            "Day" TEXT,
                            "Start_Time" TEXT,
                            "End_Time" TEXT,
                            "Subject" TEXT,
                            "Room" TEXT,
                            "Section" TEXT,
                            PRIMARY KEY("ID" AUTOINCREMENT)
                            )""")

            sched_name.configure(state='normal')
            sched_department_combobox.configure(state='normal')
            hr_strttime_sched.configure(state='normal')
            min_strttime_sched.configure(state='normal')
            sec_strttime_sched.configure(state='normal')
            p_strttime_sched.configure(state='normal')
            hr_endtime_sched.configure(state='normal')
            min_endtime_sched.configure(state='normal')
            sec_endtime_sched.configure(state='normal')
            p_endtime_sched.configure(state='normal')
            day_sched.configure(state='normal')

            Hour_Start=hr_strttime_sched.get()
            Min_Start=min_strttime_sched.get()
            Sec_Start=sec_strttime_sched.get()
            P_Start=p_strttime_sched.get()

            Hour_End=hr_endtime_sched.get()
            Min_End=min_endtime_sched.get()
            Sec_End=sec_endtime_sched.get()
            P_End=p_endtime_sched.get()

            Name=sched_name.get()
            Department=sched_department_combobox.get()
            Day=day_sched.get()
            Start_time= Hour_Start + ':' + Min_Start + ':' + Sec_Start + ' ' + P_Start
            End_time= Hour_End + ':' + Min_End + ':' + Sec_End + ' ' + P_End
            Subject=sub_sched.get()
            Room=room_sched.get()
            Section=section_sched.get()

            if Name == " " or Department == " " or Day == " " or Start_time == " " or End_time == " " or Subject == " " or Room == " " or Section == " ":
                messagebox.showinfo("Error", "Please fill up the blank entry!!")
            else:
                insertdata = str(Name),str(Department),str(Day),str(Start_time),str(End_time),str(Subject),str(Room),str(Section)
                cursor.execute("""INSERT INTO schedule (Name,Department,Day,Start_Time,End_Time,Subject,Room,Section) 
                                    VAlUES(?,?,?,?,?,?,?,?)""", insertdata)
                
                day_sched.delete(0,END)
                sub_sched.delete(0,END)
                room_sched.delete(0,END)
                section_sched.delete(0,END)

                # var = IntVar(popupwindow_sched)
                # var.set(00)
                # hr_strttime_sched.configure(textvariable=var)
                # min_strttime_sched.configure(textvariable=var)
                # sec_strttime_sched.configure(textvariable=var)
                # p_strttime_sched.configure(state='readonly')
                # hr_endtime_sched.configure(textvariable=var)
                # min_endtime_sched.configure(textvariable=var)
                # sec_endtime_sched.configure(textvariable=var)
                # p_endtime_sched.configure(state='readonly')
                
                day_sched.configure(state='readonly')
                sched_name.configure(state='disabled')
                sched_department_combobox.configure(state='disabled')
                hr_strttime_sched.configure(state='readonly')
                min_strttime_sched.configure(state='readonly')
                sec_strttime_sched.configure(state='readonly')
                p_strttime_sched.configure(state='readonly')
                hr_endtime_sched.configure(state='readonly')
                min_endtime_sched.configure(state='readonly')
                sec_endtime_sched.configure(state='readonly')
                p_endtime_sched.configure(state='readonly')

            day_sched.configure(state='readonly')
            sched_name.configure(state='disabled')
            sched_department_combobox.configure(state='disabled')
            hr_strttime_sched.configure(state='readonly')
            min_strttime_sched.configure(state='readonly')
            sec_strttime_sched.configure(state='readonly')
            p_strttime_sched.configure(state='readonly')
            hr_endtime_sched.configure(state='readonly')
            min_endtime_sched.configure(state='readonly')
            sec_endtime_sched.configure(state='readonly')
            p_endtime_sched.configure(state='readonly')
            conn.commit()
            conn.close()

        def sched_read():
            # sched_name.configure(state='normal')
            # sched_department_combobox.configure(state='normal')

            # nm = sched_name.get()
            # dpt = sched_department_combobox.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Monday'")
            results_sched = cursor.fetchall()
            conn.commit()
            return results_sched

        def refreshTable_sched():
            for data_sched in data_table_sched.get_children():
                data_table_sched.delete(data_sched)

            for results_sched in reverse(sched_read()):
                data_table_sched.insert(parent='', index='end', iid=results_sched, text="", values=(results_sched), tag="orow")
            data_table_sched.tag_configure('orow', background='#EEEEEE')

        def Monday():
            btn_mon_sched.configure(fg_color="#00436e")
            btn_tue_sched.configure(fg_color="#ffb000")
            btn_wed_sched.configure(fg_color="#ffb000")
            btn_thur_sched.configure(fg_color="#ffb000")
            btn_fri_sched.configure(fg_color="#ffb000")
            btn_sat_sched.configure(fg_color="#ffb000")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched.get_children():
                data_table_sched.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Monday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

        def Tuesday():
            btn_mon_sched.configure(fg_color="#ffb000")
            btn_tue_sched.configure(fg_color="#00436e")
            btn_wed_sched.configure(fg_color="#ffb000")
            btn_thur_sched.configure(fg_color="#ffb000")
            btn_fri_sched.configure(fg_color="#ffb000")
            btn_sat_sched.configure(fg_color="#ffb000")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched.get_children():
                data_table_sched.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Tuesday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

        def Wednesday():
            btn_mon_sched.configure(fg_color="#ffb000")
            btn_tue_sched.configure(fg_color="#ffb000")
            btn_wed_sched.configure(fg_color="#00436e")
            btn_thur_sched.configure(fg_color="#ffb000")
            btn_fri_sched.configure(fg_color="#ffb000")
            btn_sat_sched.configure(fg_color="#ffb000")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched.get_children():
                data_table_sched.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Wednesday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

        def Thursday():
            btn_mon_sched.configure(fg_color="#ffb000")
            btn_tue_sched.configure(fg_color="#ffb000")
            btn_wed_sched.configure(fg_color="#ffb000")
            btn_thur_sched.configure(fg_color="#00436e")
            btn_fri_sched.configure(fg_color="#ffb000")
            btn_sat_sched.configure(fg_color="#ffb000")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched.get_children():
                data_table_sched.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Thursday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

        def Friday():
            btn_mon_sched.configure(fg_color="#ffb000")
            btn_tue_sched.configure(fg_color="#ffb000")
            btn_wed_sched.configure(fg_color="#ffb000")
            btn_thur_sched.configure(fg_color="#ffb000")
            btn_fri_sched.configure(fg_color="#00436e")
            btn_sat_sched.configure(fg_color="#ffb000")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched.get_children():
                data_table_sched.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Friday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

        def Saturday():
            btn_mon_sched.configure(fg_color="#ffb000")
            btn_tue_sched.configure(fg_color="#ffb000")
            btn_wed_sched.configure(fg_color="#ffb000")
            btn_thur_sched.configure(fg_color="#ffb000")
            btn_fri_sched.configure(fg_color="#ffb000")
            btn_sat_sched.configure(fg_color="#00436e")

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_sched.get_children():
                data_table_sched.delete(record)
            
            cursor.execute("SELECT Start_Time,End_Time,Subject,Room,Section FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Day='Saturday'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_sched.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_sched.tag_configure('evenrow', background='#EEEEEE')
                data_table_sched.tag_configure('oddrow', background='#EEEEEE')

            conn.commit()
            conn.close()

        def select_row_sched(e):

            selected = data_table_sched.focus()
            values = data_table_sched.item(selected, 'values')

            if values:
                conn = sqlite3.connect("data/data.db")
                cursor = conn.cursor()

                day_sched.configure(state='normal')
                hr_strttime_sched.configure(state='normal')
                min_strttime_sched.configure(state='normal')
                sec_strttime_sched.configure(state='normal')
                p_strttime_sched.configure(state='normal')
                hr_endtime_sched.configure(state='normal')
                min_endtime_sched.configure(state='normal')
                sec_endtime_sched.configure(state='normal')
                p_endtime_sched.configure(state='normal')

                day_sched.delete(0,END)
                sub_sched.delete(0,END)
                room_sched.delete(0,END)
                section_sched.delete(0,END)
                p_strttime_sched.delete(0,END)
                p_endtime_sched.delete(0,END)
                
                sub_sched.insert(0,values[2])
                room_sched.insert(0,values[3])
                section_sched.insert(0,values[4])

                subject = sub_sched.get()

                cursor.execute("SELECT Day FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                day = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(Start_Time,1,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                hr_strttime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(Start_Time,4,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                min_strttime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(Start_Time,7,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                sec_strttime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(Start_Time,10,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                p_strttime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(End_Time,1,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                hr_endtime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(End_Time,4,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                min_endtime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(End_Time,7,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                sec_endtime = cursor.fetchone()

                cursor.execute("SELECT DISTINCT SUBSTR(End_Time,10,2) FROM schedule WHERE Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subject) +"'")
                p_endtime = cursor.fetchone()

                HR_strttime = IntVar()
                HR_strttime.set(hr_strttime)
                MIN_strttime = IntVar()
                MIN_strttime.set(min_strttime)
                SEC_strttime = IntVar()
                SEC_strttime.set(sec_strttime)
                hr_strttime_sched.configure(textvariable=HR_strttime)
                min_strttime_sched.configure(textvariable=MIN_strttime)
                sec_strttime_sched.configure(textvariable=SEC_strttime)
                p_strttime_sched.insert(0,p_strttime)

                HR_endtime = IntVar()
                HR_endtime.set(hr_endtime)
                MIN_endtime = IntVar()
                MIN_endtime.set(min_endtime)
                SEC_endtime = IntVar()
                SEC_endtime.set(sec_endtime)
                hr_endtime_sched.configure(textvariable=HR_endtime)
                min_endtime_sched.configure(textvariable=MIN_endtime)
                sec_endtime_sched.configure(textvariable=SEC_endtime)
                p_endtime_sched.insert(0,p_strttime)
                
                day_sched.insert(0,day)

                sub_sched_lb.configure(text=subject)

                day_sched.configure(state='readonly')
                hr_strttime_sched.configure(state='readonly')
                min_strttime_sched.configure(state='readonly')
                sec_strttime_sched.configure(state='readonly')
                p_strttime_sched.configure(state='readonly')
                hr_endtime_sched.configure(state='readonly')
                min_endtime_sched.configure(state='readonly')
                sec_endtime_sched.configure(state='readonly')
                p_endtime_sched.configure(state='readonly')

                conn.commit()
                conn.close()

                button_update_sched.configure(state='normal')
            else:
                messagebox.showinfo("Error", "There is no data on the table !!")

        def update_sched():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            day_sched.configure(state='normal')
            hr_strttime_sched.configure(state='normal')
            min_strttime_sched.configure(state='normal')
            sec_strttime_sched.configure(state='normal')
            p_strttime_sched.configure(state='normal')
            hr_endtime_sched.configure(state='normal')
            min_endtime_sched.configure(state='normal')
            sec_endtime_sched.configure(state='normal')
            p_endtime_sched.configure(state='normal')

            Hour_Start=hr_strttime_sched.get()
            Min_Start=min_strttime_sched.get()
            Sec_Start=sec_strttime_sched.get()
            P_Start=p_strttime_sched.get()

            Hour_End=hr_endtime_sched.get()
            Min_End=min_endtime_sched.get()
            Sec_End=sec_endtime_sched.get()
            P_End=p_endtime_sched.get()

            subj = sub_sched_lb.cget("text")

            Day=day_sched.get()
            Start_time= Hour_Start + ':' + Min_Start + ':' + Sec_Start + ' ' + P_Start
            End_time= Hour_End + ':' + Min_End + ':' + Sec_End + ' ' + P_End
            Subject=sub_sched.get()
            Room=room_sched.get()
            Section=section_sched.get()

            cursor.execute("UPDATE schedule SET Day='"+ str(Day) +"',Start_Time='"+ str(Start_time) +"',End_Time='"+ str(End_time) +"',Subject='"+ str(Subject) +"',Room='"+ str(Room) +"',Section='"+ str(Section) +"' WHERE  Name='"+ str(name_emp) +"' AND Department='"+ str(depart) +"' AND Subject='"+ str(subj) +"'")
            
            day_sched.delete(0,END)
            sub_sched.delete(0,END)
            room_sched.delete(0,END)
            section_sched.delete(0,END)
            p_strttime_sched.delete(0,END)
            p_endtime_sched.delete(0,END)
            p_strttime_sched.insert(0,"AM")
            p_endtime_sched.insert(0,"AM")

            zero= "00"
            HR_strttime = IntVar()
            HR_strttime.set(zero)
            MIN_strttime = IntVar()
            MIN_strttime.set(zero)
            SEC_strttime = IntVar()
            SEC_strttime.set(zero)
            hr_strttime_sched.configure(textvariable=HR_strttime)
            min_strttime_sched.configure(textvariable=MIN_strttime)
            sec_strttime_sched.configure(textvariable=SEC_strttime)
            HR_endtime = IntVar()
            HR_endtime.set(zero)
            MIN_endtime = IntVar()
            MIN_endtime.set(zero)
            SEC_endtime = IntVar()
            SEC_endtime.set(zero)
            hr_endtime_sched.configure(textvariable=HR_endtime)
            min_endtime_sched.configure(textvariable=MIN_endtime)
            sec_endtime_sched.configure(textvariable=SEC_endtime)

            day_sched.configure(state='readonly')
            hr_strttime_sched.configure(state='readonly')
            min_strttime_sched.configure(state='readonly')
            sec_strttime_sched.configure(state='readonly')
            p_strttime_sched.configure(state='readonly')
            hr_endtime_sched.configure(state='readonly')
            min_endtime_sched.configure(state='readonly')
            sec_endtime_sched.configure(state='readonly')
            p_endtime_sched.configure(state='readonly')

            button_update_sched.configure(state='disabled')

            conn.commit()
            conn.close()
        def clear_sched():
            day_sched.configure(state='normal')
            hr_strttime_sched.configure(state='normal')
            min_strttime_sched.configure(state='normal')
            sec_strttime_sched.configure(state='normal')
            p_strttime_sched.configure(state='normal')
            hr_endtime_sched.configure(state='normal')
            min_endtime_sched.configure(state='normal')
            sec_endtime_sched.configure(state='normal')
            p_endtime_sched.configure(state='normal')

            day_sched.delete(0,END)
            sub_sched.delete(0,END)
            room_sched.delete(0,END)
            section_sched.delete(0,END)
            p_strttime_sched.delete(0,END)
            p_endtime_sched.delete(0,END)
            p_strttime_sched.insert(0,"AM")
            p_endtime_sched.insert(0,"AM")

            zero= "00"
            HR_strttime = IntVar()
            HR_strttime.set(zero)
            MIN_strttime = IntVar()
            MIN_strttime.set(zero)
            SEC_strttime = IntVar()
            SEC_strttime.set(zero)
            hr_strttime_sched.configure(textvariable=HR_strttime)
            min_strttime_sched.configure(textvariable=MIN_strttime)
            sec_strttime_sched.configure(textvariable=SEC_strttime)
            HR_endtime = IntVar()
            HR_endtime.set(zero)
            MIN_endtime = IntVar()
            MIN_endtime.set(zero)
            SEC_endtime = IntVar()
            SEC_endtime.set(zero)
            hr_endtime_sched.configure(textvariable=HR_endtime)
            min_endtime_sched.configure(textvariable=MIN_endtime)
            sec_endtime_sched.configure(textvariable=SEC_endtime)

            day_sched.configure(state='readonly')
            hr_strttime_sched.configure(state='readonly')
            min_strttime_sched.configure(state='readonly')
            sec_strttime_sched.configure(state='readonly')
            p_strttime_sched.configure(state='readonly')
            hr_endtime_sched.configure(state='readonly')
            min_endtime_sched.configure(state='readonly')
            sec_endtime_sched.configure(state='readonly')
            p_endtime_sched.configure(state='readonly')

            # Data Table "TreeView"
        scrollbary_sched = Scrollbar(popupwindow_sched, orient=VERTICAL)
        scrollbary_sched.place(x=1030, y=230, height=350)

        # style = ttk.Style()
        # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

        data_table_sched = ttk.Treeview(popupwindow_sched)
        data_table_sched.place(x=145, y=415, width=740, height=215)
        data_table_sched.configure(yscrollcommand=scrollbary_sched.set)

        scrollbary_sched.configure(command=data_table_sched.yview)

        data_table_sched['columns'] = ("Start Time","End Time","Subject","Room","Section")
        # Format Columns
        data_table_sched.column("#0", width=0, stretch=NO)
        data_table_sched.column("Start Time", anchor=CENTER,width=0)
        data_table_sched.column("End Time", anchor=CENTER, width=50)
        data_table_sched.column("Subject", anchor=CENTER, width=50)
        data_table_sched.column("Room", anchor=CENTER, width=50)
        data_table_sched.column("Section", anchor=CENTER, width=50)

        # Create Headings
        data_table_sched.heading("Start Time", text="Start Time", anchor=CENTER)
        data_table_sched.heading("End Time", text="End Time", anchor=CENTER)
        data_table_sched.heading("Subject", text="Subject", anchor=CENTER)
        data_table_sched.heading("Room", text="Room", anchor=CENTER)
        data_table_sched.heading("Section", text="Section", anchor=CENTER)

        data_table_sched.bind("<ButtonRelease-1>", select_row_sched)

        refreshTable_sched()

            # Entry Employee Name
        sched_name = Entry(popupwindow_sched, state='disabled')
        sched_name.place(x=180, y=172, width=150)

            # Entry Day
        day_sched = ttk.Combobox(popupwindow_sched,  state='readonly', values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        day_sched.place(x=180, y=209, width=150)

            # Subject Label
        sub_sched_lb = Label(popupwindow_sched, fg='#f0f0f0', font = "Heltvetica 9")
        sub_sched_lb.place(x=180, y=235)

            # Entry Subject
        sub_sched = Entry(popupwindow_sched)
        sub_sched.place(x=180, y=258, width=150)

            # ComboBox College Department
        sched_department_combobox = ttk.Combobox(popupwindow_sched, state='disabled', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
        sched_department_combobox.place(x=545, y=172, width=150)
        
        #     # Entry Start Time
        # strttime_sched= Entry(popupwindow_sched,textvariable=time_format)
        # strttime_sched.place(x=545, y=209, width=150)

            # Entry Start Time Hour
        var_hr_strt = IntVar()
        var_hr_strt.set(00)
        hr_strttime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=12, format="%02.0f",textvariable=var_hr_strt)
        hr_strttime_sched.place(x=545, y=209, width=35)

            # Entry Start Time Minute
        var_min_strt = IntVar()
        var_min_strt.set(00)
        min_strttime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=59, format="%02.0f",textvariable=var_min_strt)
        min_strttime_sched.place(x=585, y=209, width=35)

            # Entry Start Time Second
        var_sec_strt = IntVar()
        var_sec_strt.set(00)
        sec_strttime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=59, format="%02.0f",textvariable=var_sec_strt)
        sec_strttime_sched.place(x=625, y=209, width=35)

            # ComboBox College Department
        p_strttime_sched = ttk.Combobox(popupwindow_sched, state='readonly', values=["AM", "PM",])
        p_strttime_sched.set("AM")
        p_strttime_sched.place(x=665, y=209, width=45)

            # Entry Room
        room_sched = Entry(popupwindow_sched)
        room_sched.place(x=545, y=258, width=150)

        #     # Entry End Time
        # endtime_sched = Entry(popupwindow_sched)
        # endtime_sched.place(x=810, y=209, width=150)

            # Entry End Time Hour
        var_hr_end = IntVar()
        var_hr_end.set(00)
        hr_endtime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=12, format="%02.0f",textvariable=var_hr_end)
        hr_endtime_sched.place(x=810, y=209, width=35)

            # Entry End Time Minute
        var_min_end = IntVar()
        var_min_end.set(00)
        min_endtime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=59, format="%02.0f",textvariable=var_min_end)
        min_endtime_sched.place(x=850, y=209, width=35)

            # Entry End Time Second
        var_sec_end = IntVar()
        var_sec_end.set(00)
        sec_endtime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=59, format="%02.0f",textvariable=var_sec_end)
        sec_endtime_sched.place(x=890, y=209, width=35)

            # ComboBox College Department
        p_endtime_sched = ttk.Combobox(popupwindow_sched, state='readonly', values=["AM", "PM",])
        p_endtime_sched.set("AM")
        p_endtime_sched.place(x=930, y=209, width=45)

            # Entry Section
        section_sched = Entry(popupwindow_sched)
        section_sched.place(x=810, y=258, width=150)

        sched_name.configure(state='normal')
        sched_department_combobox.configure(state='normal')
        sched_name.insert(0, name_emp)
        sched_department_combobox.insert(0, depart)
        sched_name.configure(state='disabled')
        sched_department_combobox.configure(state='disabled')

            # Save Data Button
        save_pic = PhotoImage(file = "pic/btn_save.png")
        save_button_sched = customtkinter.CTkButton(master=popupwindow_sched,image=save_pic, text="" ,
                                                    corner_radius=6, fg_color="#00436e",hover_color="#006699", command=save_sched)
        save_button_sched.place(x=315, y=290, height=32,width=131)

            # Updated Button
        update_pic = PhotoImage(file = "pic/btn_update.png")
        button_update_sched = customtkinter.CTkButton(master=popupwindow_sched,state='disabled',image=update_pic, text="" ,
                                                    corner_radius=6, fg_color="#00436e",hover_color="#006699", command=update_sched)
        button_update_sched.place(x=460, y=290, height=32,width=131)

            # Reset Button
        reset_btnsched = PhotoImage(file = "pic/btn_reset.png")
        button_resetsched = customtkinter.CTkButton(master=popupwindow_sched,image=reset_btnsched, text="" ,
                                                    corner_radius=6, fg_color="#00436e",hover_color="#006699", command=clear_sched)
        button_resetsched.place(x=605, y=290, height=32,width=131)

            # Moday Button
        mon_btn = PhotoImage(file = "pic/btn_mon.png")
        btn_mon_sched = customtkinter.CTkButton(master=popupwindow_sched,image=mon_btn, text="" ,
                                                    corner_radius=6, fg_color="#00436e",hover_color="#006699", command=Monday)
        btn_mon_sched.place(x=90, y=373, height=28,width=131)

            # Tuesday Button
        tue_btn = PhotoImage(file = "pic/btn_tue.png")
        btn_tue_sched = customtkinter.CTkButton(master=popupwindow_sched,image=tue_btn, text="" ,
                                                    corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Tuesday)
        btn_tue_sched.place(x=235, y=373, height=28,width=131)

             # Wednesday Button
        wed_btn = PhotoImage(file = "pic/btn_wed.png")
        btn_wed_sched = customtkinter.CTkButton(master=popupwindow_sched,image=wed_btn, text="" ,
                                                    corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Wednesday)
        btn_wed_sched.place(x=380, y=373, height=28,width=131)

             # Thursday Button
        thur_btn = PhotoImage(file = "pic/btn_thu.png")
        btn_thur_sched = customtkinter.CTkButton(master=popupwindow_sched,image=thur_btn, text="" ,
                                                    corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Thursday)
        btn_thur_sched.place(x=525, y=373, height=28,width=131)

             # Friday Button
        fri_btn = PhotoImage(file = "pic/btn_fri.png")
        btn_fri_sched = customtkinter.CTkButton(master=popupwindow_sched,image=fri_btn, text="" ,
                                                    corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Friday)
        btn_fri_sched.place(x=670, y=373, height=28,width=131)

             # Saturday Button
        sat_btn = PhotoImage(file = "pic/btn_sat.png")
        btn_sat_sched = customtkinter.CTkButton(master=popupwindow_sched,image=sat_btn, text="" ,
                                                    corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Saturday)
        btn_sat_sched.place(x=815, y=373, height=28,width=131)

    # ============= Faculty Information Frame ===================================================================================================================================================

        # open background image
    faculty_information.fac_inf_image = Image.open('pic/10.png')
    faculty_information.fac_inf_resize_image = faculty_information.fac_inf_image.resize((1362, 692))
    faculty_information.photo = ImageTk.PhotoImage(faculty_information.fac_inf_resize_image)
    faculty_information.fac_inf_bg_img_lb = Label(faculty_information, image = faculty_information.photo)
    faculty_information.fac_inf_bg_img_lb.pack()

        # Clear Text Field
    def clear():
        button_update.configure(state='disabled')
        
        department_combobox.configure(state='normal')
        gender_combobox_fac_inf.configure(state='normal')
        status_combobox_fac_inf.configure(state='normal')
        position_fac_inf.configure(state='normal')
        password_fac_inf.configure(state='normal')
        username_fac_inf.configure(state='normal')

        department_combobox.delete(0, END)
        employee_num_fac_inf.delete(0, END)
        gender_combobox_fac_inf.delete(0, END)
        email_fac_inf.delete(0, END)
        address_fac_inf.delete(0, END)
        employee_name_fac_inf.delete(0, END)
        age_fac_inf.delete(0, END)
        con_num_fac_inf.delete(0, END)
        status_combobox_fac_inf.delete(0,END)
        position_fac_inf.delete(0, END)
        username_fac_inf.delete(0, END)
        password_fac_inf.delete(0, END)
        # check_button_fac_inf.deselect()
        # retype_password_fac_inf.delete(0, END)
        department_combobox.configure(state='readonly')
        gender_combobox_fac_inf.configure(state='readonly')
        status_combobox_fac_inf.configure(state='disabled')
        position_fac_inf.configure(state='readonly')
        loads_button_fac_inf.configure(state='disabled')


    def search_data():
        lookup_record = search_fac_inf.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for record in data_table.get_children():
            data_table.delete(record)

        cursor.execute("SELECT * FROM faculty_data WHERE Employee_No = '" + str(lookup_record) + "' or  Email = '" + str(lookup_record) + "' or  Employee_Name = '" + str(lookup_record) + "' or Gender = '" + str(lookup_record) + "' or Age = '" + str(lookup_record) + "' or Contact_Number = '" + str(lookup_record) + "' or Address = '" + str(lookup_record) + "' or College_Department = '" + str(lookup_record) + "' or Status = '" + str(lookup_record) + "'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]), tag="evenrow")
            else:
                data_table.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]), tag="oddrow")
            count += 1
            data_table.tag_configure('evenrow', background='#EEEEEE')
            data_table.tag_configure('oddrow', background='#EEEEEE')
            search_fac_inf.delete(0, END)

        conn.commit()
        conn.close()

    def refreshTable():
        for data in data_table.get_children():
            data_table.delete(data)

        for result in reverse(read()):
            data_table.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")
        data_table.tag_configure('orow', background='#EEEEEE')


    def reverse(tuples):
        new_tup = tuples[::-1]
        return new_tup

        # Insert Data
    def insert(Employee_No,Email,Employee_Name,Gender,Age,Contact_Number,Address,College_Department,Username,Password,Position,Status):
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            faculty_data(Employee_No TEXT, Email TEXT, Employee_Name TEXT,
            Gender TEXT,Age TEXT,Contact_Number TEXT,Address TEXT,College_Department TEXT,
            Username TEXT, Password TEXT, Position TEXT, Status TEXT)""")
        
        cursor.execute("INSERT INTO faculty_data VALUES ('" + str(Employee_No) + "','" + str(Email) + "','" + str(Employee_Name) + "','" + str(Gender) + "','" + str(Age) + "','" + str(Contact_Number) + "','" + str(Address) + "','" + str(College_Department) + "','" + str(Username) + "','" + str(Password) + "','" + str(Position) + "','" + str(Status) + "')")
        conn.commit()

        # Read Data on the sql
    def read():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            faculty_data(Employee_No TEXT, Email TEXT, Employee_Name TEXT,
            Gender TEXT,Age TEXT,Contact_Number TEXT,Address TEXT,College_Department TEXT,
            Username TEXT, Password TEXT, Position TEXT,Status TEXT)""")

        cursor.execute("SELECT * FROM faculty_data")
        results = cursor.fetchall()
        conn.commit()
        return results

    def delete(data):
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            faculty_data(Employee_No TEXT, Email TEXT, Employee_Name TEXT,
            Gender TEXT,Age TEXT,Contact_Number TEXT,Address TEXT,College_Department TEXT,
            Username TEXT, Password TEXT, Position TEXT,Status TEXT)""")

        cursor.execute("DELETE FROM faculty_data WHERE Employee_No ='" + srt(data) + "'")
        conn.commit()

        # Update data sql
    def update(Employee_No,Email,Employee_Name,Gender,Age,Contact_Number,Address,College_Department,Username,Password,Position,idEmployee_No):
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            faculty_data(Employee_No TEXT, Email TEXT, Employee_Name TEXT,
            Gender TEXT,Age TEXT,Contact_Number TEXT,Address TEXT,College_Department TEXT,
            Username TEXT, Password TEXT, Position TEXT, Status TEXT)""")

        cursor.execute("UPDATE faculty_data SET Employee_No = '" + str(Employee_No) + "', Email = '" + str(Email) + "', Employee_Name = '" + str(Employee_Name) + "', Gender = '" + str(Gender) + "', Age = '" + str(Age) + "', Contact_Number = '" + str(Contact_Number) + "', Address = '" + str(Address) + "', College_Department = '" + str(College_Department) + "', Username = '" + str(Username) + "', Password = '" + str(Password) + "', Position = '" + str(Position) + "' WHERE Employee_No = '"+ str(idEmployee_No)+"'")
        conn.commit()

    def check_duplicate():
        Employee_No = employee_num_fac_inf.get()
        # Email = email_fac_inf.get()
        # Contact_Number = con_num_fac_inf.get()
        # Username = username_fac_inf.get()
        # Password = password_fac_inf.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM faculty_data WHERE Employee_No = '" + str(Employee_No) + "'")
        records = cursor.fetchone()

        if records is not None:
            return True
        else:
            return False

        conn.commit()

    def check_duplicate_Email():
        # Employee_No = employee_num_fac_inf.get()
        Email = email_fac_inf.get()
        # Contact_Number = con_num_fac_inf.get()
        # Username = username_fac_inf.get()
        # Password = password_fac_inf.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM faculty_data WHERE Email = '" + str(Email) + "'")
        records = cursor.fetchone()

        if records is not None:
            return True
        else:
            return False

        conn.commit()

    def check_duplicate_Con():
        # Employee_No = employee_num_fac_inf.get()
        # Email = email_fac_inf.get()
        Contact_Number = con_num_fac_inf.get()
        # Username = username_fac_inf.get()
        # Password = password_fac_inf.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM faculty_data WHERE Contact_Number = '" + str(Contact_Number) + "'")
        records = cursor.fetchone()

        if records is not None:
            return True
        else:
            return False

        conn.commit()

    def check_duplicate_Username():
        # Employee_No = employee_num_fac_inf.get()
        # Email = email_fac_inf.get()
        # Contact_Number = con_num_fac_inf.get()
        Username = username_fac_inf.get()
        # Password = password_fac_inf.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(Username) + "'")
        records = cursor.fetchone()

        if records is not None:
            return True
        else:
            return False

        conn.commit()

    def check_duplicate_Pass():
        # Employee_No = employee_num_fac_inf.get()
        # Email = email_fac_inf.get()
        # Contact_Number = con_num_fac_inf.get()
        # Username = username_fac_inf.get()
        Password = password_fac_inf.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM faculty_data WHERE Password = '" + str(Password) + "'")
        records = cursor.fetchone()

        if records is not None:
            return True
        else:
            return False

        conn.commit()

        # Add Faculty 
    def Save_Data():
        department_combobox.configure(state='normal')
        gender_combobox_fac_inf.configure(state='normal')
        # status_combobox_fac_inf.configure(state='normal')
        position_fac_inf.configure(state='normal')

        save_employee_number = employee_num_fac_inf.get()
        save_email = email_fac_inf.get()
        save_employee_name = employee_name_fac_inf.get()
        save_gender = gender_combobox_fac_inf.get()
        save_age = age_fac_inf.get()
        save_contact_number = con_num_fac_inf.get()
        save_address = address_fac_inf.get()
        save_college_department = department_combobox.get()
        save_username = username_fac_inf.get()
        save_password = password_fac_inf.get()
        save_position = position_fac_inf.get()
        # save_status = status_combobox_fac_inf.get()
        save_status = 'Activated'

        if save_employee_number == "" or save_email == "" or save_employee_name == "" or save_gender == "" or save_age == "" or save_contact_number == "" or save_address == "" or save_college_department == "" or save_username == "" or save_password == "" or save_position == "":
            messagebox.showinfo("Error", "Please fill up the blank entry!!")
            return
        else:
            if check_duplicate() == True:
                messagebox.showinfo("Error", "Employee Number Already Exist!!")
                return
            elif check_duplicate_Email()== True:
                messagebox.showinfo("Error", "Email Already Exist!!")
                return
            elif check_duplicate_Con()== True:
                messagebox.showinfo("Error", "Contact Number Already Exist!!")
                return
            elif check_duplicate_Username()== True:
                messagebox.showinfo("Error", "Username Already Exist!!")
                return
            elif check_duplicate_Pass()== True:
                messagebox.showinfo("Error", "Password Already Exist!!")
                return
            elif '@' not in save_email or '.com' not in save_email:
                messagebox.showinfo("Error","Not a valid Email Address, Enter a valid Email Address!!")
                return
            elif not save_contact_number.isdigit():
                messagebox.showinfo("Error","Not a valid Contact Number, Please enter numbers only!!")
                return
            elif len(save_contact_number) > 11:
                messagebox.showinfo("Error","Not a valid Contact Number, Please enter 11 numbers only!!")
                return
            elif not employee_num_fac_inf.isdigit():
                messagebox.showinfo("Error","Not a valid Employee Number, Please enter numbers only!!")
                return
            elif not any(ch.isupper() for ch in save_password):
                messagebox.showinfo("Error","Password Atleast 1 uppercase character required!")
                return
            elif not any(ch.islower() for ch in save_password):
                messagebox.showinfo("Error","Password Atleast 1 lowercase character required!")
                return
            elif not any(ch.isdigit() for ch in save_password):
                messagebox.showinfo("Error","Password Atleast 1 number required!")
                return
            elif len(save_password) < 8:
                messagebox.showinfo("Error","Password must be minimum of 8 characters!")
                return
            else:
                messagebox.showinfo("Messgae", "Data Added!!")
                insert(str(save_employee_number),str(save_email),str(save_employee_name),str(save_gender),str(save_age),str(save_contact_number),str(save_address),str(save_college_department),str(save_username),str(save_password),str(save_position),str(save_status)) 
                
                department_combobox.configure(state='readonly')
                gender_combobox_fac_inf.configure(state='readonly')
                # status_combobox_fac_inf.configure(state='readonly')
                position_fac_inf.configure(state='readonly')
                clear() 

                conn = sqlite3.connect("data/data.db")
                cursor = conn.cursor()

                currentDateTime = datetime.datetime.now()

                cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    activity_log(
                                "ID"    INTEGER,
                                "Name"  TEXT,
                                "Activity"  TEXT,
                                "Department"    TEXT,
                                "Date_Time" TIMESTAMP,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                                )""")

                eName = pg4_lb_name.cget("text")
                eDepartment = pg4_lb_dept.cget("text")

                insetdata = str(eName),'Add Faculty',str(eDepartment),currentDateTime
                cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                    VAlUES(?,?,?,?)""", insetdata)
                conn.commit()
                conn.close()
                loads_button_fac_inf.configure(state='disabled')
                refreshTable_log()
            
        refreshTable()

    def select_row(e):
        clear()

        selected = data_table.focus()
        values = data_table.item(selected, 'values')

        if values:
            button_update.configure(state='normal')

            department_combobox.configure(state='normal')
            gender_combobox_fac_inf.configure(state='normal')
            status_combobox_fac_inf.configure(state='normal')
            position_fac_inf.configure(state='normal')
            password_fac_inf.configure(state='normal')
            username_fac_inf.configure(state='normal')

            password_fac_inf.delete(0,END)
            username_fac_inf.delete(0,END)

            employee_num_fac_inf.insert(0, values[0])
            email_fac_inf.insert(0, values[1])
            employee_name_fac_inf.insert(0, values[2])
            gender_combobox_fac_inf.insert(0, values[3])
            age_fac_inf.insert(0, values[4])
            con_num_fac_inf.insert(0, values[5])
            address_fac_inf.insert(0, values[6])
            department_combobox.insert(0, values[7])
            username_fac_inf.insert(0, values[8])
            password_fac_inf.insert(0, values[9])
            position_fac_inf.insert(0, values[10])
            status_combobox_fac_inf.insert(0,values[11])

            department_combobox.configure(state='readonly')
            gender_combobox_fac_inf.configure(state='readonly')
            status_combobox_fac_inf.configure(state='readonly')
            position_fac_inf.configure(state='readonly')
            loads_button_fac_inf.configure(state='normal')
            password_fac_inf.configure(state='disabled')
            username_fac_inf.configure(state='disabled')
        else:
            messagebox.showinfo("Error", "There is no data on the table !!")
        

        # Updating Selected Data
    def Update_Data():
        department_combobox.configure(state='normal')
        gender_combobox_fac_inf.configure(state='normal')
        status_combobox_fac_inf.configure(state='normal')
        position_fac_inf.configure(state='normal')

        save_employee_number = employee_num_fac_inf.get()
        save_email = email_fac_inf.get()
        save_employee_name = employee_name_fac_inf.get()
        save_gender = gender_combobox_fac_inf.get()
        save_age = age_fac_inf.get()
        save_contact_number = con_num_fac_inf.get()
        save_address = address_fac_inf.get()
        save_college_department = department_combobox.get()
        save_username = username_fac_inf.get()
        save_password = password_fac_inf.get()
        save_position = position_fac_inf.get()
        save_status = status_combobox_fac_inf.get()

        selected_item = data_table.selection()[0]
        update_name = str(data_table.item(selected_item)['values'][0])
        if save_status == "" or save_employee_number == "" or save_email == "" or save_employee_name == "" or save_gender == "" or save_age == "" or save_contact_number == "" or save_address == "" or save_college_department == "" or save_username == "" or save_password == "" or save_position == "":
            messagebox.showinfo("Error", "Please fill up the blank entry!!")
            return
        elif '@' not in save_email or '.com' not in save_email:
            messagebox.showinfo("Error","Not a valid Email Address, Enter a valid Email Address!!")
            return
        elif not save_contact_number.isdigit():
            messagebox.showinfo("Error","Not a valid Contact Number, Please enter numbers only!!")
            return
        elif len(save_contact_number) > 11:
            messagebox.showinfo("Error","Not a valid Contact Number, Please enter 11 numbers only!!")
            return
        # elif not any(ch.isupper() for ch in save_password):
        #     messagebox.showinfo("Error","Password Atleast 1 uppercase character required!")
        #     return
        # elif not any(ch.islower() for ch in save_password):
        #     messagebox.showinfo("Error","Password Atleast 1 lowercase character required!")
        #     return
        # elif not any(ch.isdigit() for ch in save_password):
        #     messagebox.showinfo("Error","Password Atleast 1 number required!")
        #     return
        # elif len(save_password) < 8:
        #     messagebox.showinfo("Error","Password must be minimum of 8 characters!")
        #     return
        else:
            messagebox.showinfo("Messgae", "Data Updated!!")
            update(save_employee_number,save_email,save_employee_name,save_gender,save_age,save_contact_number,save_address,save_college_department,save_username,save_password,save_position,update_name)
            
            # conn = sqlite3.connect("data/data.db")
            # cursor = conn.cursor()

            # cursor.execute("UPDATE faculty_data SET  Status = '" + str(save_status) + "' WHERE Employee_No = '"+ str(save_employee_number)+"'")
            # conn.commit()
            # conn.close()

            department_combobox.configure(state='readonly')
            gender_combobox_fac_inf.configure(state='readonly')
            status_combobox_fac_inf.configure(state='readonly')
            position_fac_inf.configure(state='readonly')
            clear()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            currentDateTime = datetime.datetime.now()

            cursor.execute("""CREATE TABLE IF NOT EXISTS 
                activity_log(
                            "ID"    INTEGER,
                            "Name"  TEXT,
                            "Activity"  TEXT,
                            "Department"    TEXT,
                            "Date_Time" TIMESTAMP,
                            PRIMARY KEY("ID" AUTOINCREMENT)
                            )""")     

            eName = pg4_lb_name.cget("text")
            eDepartment = pg4_lb_dept.cget("text")

            insetdata = str(eName),'Update',str(eDepartment),currentDateTime
            cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                VAlUES(?,?,?,?)""", insetdata)

            conn.commit()
            conn.close()
            loads_button_fac_inf.configure(state='disabled')
            button_update.configure(state='disabled')
            refreshTable_log()


        refreshTable()
    def combobox_event(event):
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        save_status = status_combobox_fac_inf.get()
        save_employee_number = employee_num_fac_inf.get()
        
        cursor.execute("UPDATE faculty_data SET  Status = '" + str(save_status) + "' WHERE Employee_No = '"+ str(save_employee_number)+"'")
        
        currentDateTime = datetime.datetime.now()
        eName = pg4_lb_name.cget("text")
        eDepartment = pg4_lb_dept.cget("text")
        
        if save_status == 'Activated':
            construct_1 = '#'+ save_employee_number + ' Account Activated'
            insetdata_2 = str(eName),str(construct_1),str(eDepartment),currentDateTime
            cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                            VAlUES(?,?,?,?)""", insetdata_2)
            messagebox.showinfo("Messgae", "Status Activated!!")
            refreshTable_log()
        elif save_status == 'Deactivated':
            construct = '#' + save_employee_number + ' Account Deactivated'
            insetdata_1 = str(eName),str(construct),str(eDepartment),currentDateTime
            cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                            VAlUES(?,?,?,?)""", insetdata_1)
            messagebox.showinfo("Messgae", "Status Deactivated!!")
            refreshTable_log()
        refreshTable_log()
        conn.commit()
        conn.close()

         # Data Table "TreeView"
    scrollbarx = Scrollbar(faculty_information, orient=HORIZONTAL)
    scrollbarx.place(x=730, y=584, width=465)
    scrollbary = Scrollbar(faculty_information, orient=VERTICAL)
    scrollbary.place(x=1180, y=284, height=300)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table = ttk.Treeview(faculty_information)
    data_table.place(x=730, y=284, width=450, height=300)
    data_table.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

    scrollbarx.configure(command=data_table.xview)
    scrollbary.configure(command=data_table.yview)

    data_table['columns'] = ("Employee No.","Email","Employee Name","Gender","Age","Contact Number","Address","College Department","Username","Password","Position","Status")
    # Format Columns
    data_table.column("#0", width=0, stretch=NO)
    data_table.column("Employee No.", anchor=CENTER, width=150)
    data_table.column("Email", anchor=CENTER, width=100)
    data_table.column("Employee Name", anchor=CENTER, width=200)
    data_table.column("Gender", anchor=CENTER, width=100)
    data_table.column("Age", anchor=CENTER, width=100)
    data_table.column("Contact Number", anchor=CENTER, width=200)
    data_table.column("Address", anchor=CENTER, width=300)
    data_table.column("College Department", anchor=CENTER, width=150)
    data_table.column("Username", anchor=CENTER, width=100)
    data_table.column("Password", anchor=CENTER, width=100)
    data_table.column("Position", anchor=CENTER, width=100)
    data_table.column("Status", anchor=CENTER, width=100)

    # Create Headings
    data_table.heading("Employee No.", text="Employee No.", anchor=CENTER)
    data_table.heading("Email", text="Email", anchor=CENTER)
    data_table.heading("Employee Name", text="Employee Name", anchor=CENTER)
    data_table.heading("Gender", text="Gender", anchor=CENTER)
    data_table.heading("Age", text="Age", anchor=CENTER)
    data_table.heading("Contact Number", text="Contact Number", anchor=CENTER)
    data_table.heading("Address", text="Address", anchor=CENTER)
    data_table.heading("College Department", text="College Department", anchor=CENTER)
    data_table.heading("Username", text="Username", anchor=CENTER)
    data_table.heading("Password", text="Password", anchor=CENTER)
    data_table.heading("Position", text="Position", anchor=CENTER)
    data_table.heading("Status", text="Status", anchor=CENTER)

    data_table.bind("<ButtonRelease-1>", select_row)

    refreshTable()

        # ComboBox College Department
    department_combobox = ttk.Combobox(faculty_information,state='readonly', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
    department_combobox.set('NONE')
    department_combobox.place(x=382, y=202, width=200)
    # state="readonly"
    
        # Entry Employee Number
    employee_num_fac_inf = Entry(faculty_information)
    employee_num_fac_inf.place(x=200, y=288, width=125)

        # Entry Employee Name
    employee_name_fac_inf = Entry(faculty_information)
    employee_name_fac_inf.place(x=385, y=288, width=125)

        # ComboBox Gender
    gender_combobox_fac_inf = ttk.Combobox(faculty_information,state='readonly', values=["Male", "Female"])
    gender_combobox_fac_inf.place(x=200, y=328, width=125)

        # Entry Age
    age_fac_inf = Entry(faculty_information)
    age_fac_inf.place(x=385, y=328, width=125)

        # Entry E-mail
    email_fac_inf = Entry(faculty_information)
    email_fac_inf.place(x=200, y=365, width=125)

        # Entry Contact Number
    con_num_fac_inf = Entry(faculty_information)
    con_num_fac_inf.place(x=385, y=365, width=125)

        # Entry Address
    address_fac_inf = Entry(faculty_information)
    address_fac_inf.place(x=200, y=405, width=125)

        # Label Status
    status_fac_lb = Label(faculty_information, text='Status:', fg='#043f6b', font="Heltvetica 8 bold")
    status_fac_lb.place(x=382, y=390)

        # Entry Status
    status_combobox_fac_inf = ttk.Combobox(faculty_information,state='disabled', values=["Activated", "Deactivated"])
    status_combobox_fac_inf.bind("<<ComboboxSelected>>", combobox_event)
    status_combobox_fac_inf.place(x=385, y=405, width=125)

        # Label Position
    position_fac_inf_lb = Label(faculty_information, text='Position:', fg='#043f6b', font="Heltvetica 8 bold")
    position_fac_inf_lb.place(x=560, y=272)

        # Label Username
    username_fac_inf_lb = Label(faculty_information, text='Username:', fg='#043f6b', font="Heltvetica 8 bold")
    username_fac_inf_lb.place(x=560, y=312)

        # Label Password
    password_fac_lb = Label(faculty_information, text='Password:', fg='#043f6b', font="Heltvetica 8 bold")
    password_fac_lb.place(x=560, y=350)

    #     # Label Retype Password
    # retype_password_fac_lb = Label(faculty_information, text='ReType Password:', fg='#043f6b', font="Heltvetica 8 bold")
    # retype_password_fac_lb.place(x=560, y=389)

        # Entry Position
    position_fac_inf = ttk.Combobox(faculty_information,state='readonly', values=["Admin", "Employee"])
    position_fac_inf.place(x=560, y=288, width=125)

        # Entry Username
    username_fac_inf = Entry(faculty_information)
    username_fac_inf.place(x=560, y=328, width=125)

        # Entry Password
    password_fac_inf = Entry(faculty_information, show='*')
    password_fac_inf.place(x=560, y=365, width=125)

    check_button_style = ttk.Style()
    check_button_style.configure('TCheckbutton', font = 7)

        # show and hide Password
    def show_entry_password():
        if  password_fac_inf.cget('show') =='*':
            password_fac_inf.configure(show='')
        else:
            password_fac_inf.configure(show='*')
    check_button_fac_inf = Checkbutton(faculty_information, text="show password", command=show_entry_password, font="Arial 7", )
    check_button_fac_inf.place(x=560, y=385)

    #     # Entry Retype Password
    # retype_password_fac_inf = Entry(faculty_information)
    # retype_password_fac_inf.place(x=560, y=405, width=125)

        # Search Entry
    search_ent_val = StringVar()
    search_fac_inf = Entry(faculty_information, textvariable = search_ent_val)
    search_fac_inf.place(x=850, y=205, width=200)

        # Employee Loads Button
    loads_fac_btn = PhotoImage(file = "pic/btn_employee_loads.png")
    loads_button_fac_inf = customtkinter.CTkButton(master=faculty_information,state='disabled',image=loads_fac_btn, text="" ,
                                                corner_radius=6, fg_color="#00436e",hover_color="#006699", command=Schedule)
    loads_button_fac_inf.place(x=383, y=430, height=25,width=128)

        # Add Faculty Button
    add_fac_btn = PhotoImage(file = "pic/btn_add_faculty.png")
    add_button_fac_inf = customtkinter.CTkButton(master=faculty_information,image=add_fac_btn, text="" ,
                                                corner_radius=6, fg_color="#00436e",hover_color="#006699", command= Save_Data)
    add_button_fac_inf.place(x=380, y=506, height=32,width=131)

        # Update Button
    # def Update():
    #     print("update")
    update_btn = PhotoImage(file = "pic/btn_update.png")
    button_update = customtkinter.CTkButton(master=faculty_information,image=update_btn, text="", state='disabled',
                                                corner_radius=6, fg_color="#00436e",hover_color="#006699", command= Update_Data)
    button_update.place(x=212, y=506, height=32,width=131)

        # Reset Button
    reset_btn = PhotoImage(file = "pic/btn_reset.png")
    button_reset = customtkinter.CTkButton(master=faculty_information,image=reset_btn, text="" ,
                                                corner_radius=6, fg_color="#00436e",hover_color="#006699", command= clear)
    button_reset.place(x=548, y=506, height=32,width=131)

        # Search Button
    search_btn = PhotoImage(file = "pic/btn_search.png")
    button_search = customtkinter.CTkButton(master=faculty_information,image=search_btn, text="" ,
                                                corner_radius=6, fg_color="#00436e",hover_color="#006699", command= search_data)
    button_search.place(x=1065, y=204, height=20,width=90)

        # Show All Button
    showall_btn = PhotoImage(file = "pic/btn_showall.png")
    button_showall = customtkinter.CTkButton(master=faculty_information,image=showall_btn, text="" ,
                                                corner_radius=6, fg_color="#00436e",hover_color="#006699", command= refreshTable)
    button_showall.place(x=923, y=603, height=28,width=110)

        # Back Button
    fac_inf_back = PhotoImage(file = "pic/btn_back_page.png")
    fac_inf_button_back = customtkinter.CTkButton(master=faculty_information,image=fac_inf_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
    fac_inf_button_back.place(x=20, y=595, height=50,width=140)

    # ============= Summary Report In Frame ========================================================================================================================

    def summary():
        popupwindow = Toplevel(main_window)
        popupwindow.title("Individual Summary Report")
        popupwindow.geometry('1020x650')
        popupwindow.grab_set()
        popupwindow.resizable(False,False)

            # open background image
        popupwindow.summary_image = Image.open('pic/16.png')
        popupwindow.summary_resize_image = popupwindow.summary_image.resize((1020,650))
        popupwindow.photo = ImageTk.PhotoImage(popupwindow.summary_resize_image)
        popupwindow.summary_bg_img_lb = Label(popupwindow, image = popupwindow.photo)
        popupwindow.summary_bg_img_lb.pack()

        emp_num = employee_num_math_rec.get()
        emp_name = employee_name_math_rec.get()

             # Get Current Time and Date
        def time_report():
            string_time = strftime('%I:%M:%S %p')
            time_lb_summary.configure(text = string_time)
            time_lb_summary.after(1000, time_report)

            string_date = strftime('%d-%m-20%y')
            date_lb_summary.configure(text = string_date)

        def display_info():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT Department FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            dept = cursor.fetchone()

            cursor.execute("SELECT Status FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            st = cursor.fetchone()

            cursor.execute("SELECT Time_in FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            Tmin = cursor.fetchone()

            cursor.execute("SELECT Time_out FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            Tmout = cursor.fetchone()

            cursor.execute("SELECT _Date FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            dt = cursor.fetchone()


            summary_department_combobox.configure(state='normal')
            employee_num_summary.configure(state='normal')
            employee_name_summary.configure(state='normal')
            att_status_summary.configure(state='normal')
            time_in_summary.configure(state='normal')
            time_out_summary.configure(state='normal')
            date_summary.configure(state='normal')

            summary_department_combobox.insert(0,dept)
            employee_num_summary.insert(0,emp_num)
            employee_name_summary.insert(0,emp_name)
            att_status_summary.insert(0,st)
            time_in_summary.insert(0,Tmin)
            time_out_summary.insert(0,Tmout)
            date_summary.insert(0,dt)

            summary_department_combobox.configure(state='disabled')
            employee_num_summary.configure(state='disabled')
            employee_name_summary.configure(state='disabled')
            att_status_summary.configure(state='disabled')
            time_in_summary.configure(state='disabled')
            time_out_summary.configure(state='disabled')
            date_summary.configure(state='disabled')

            conn.commit()
            conn.close()

        def count_data_report():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            date_mathematics = date_lb_summary.cget("text")

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE  Department='Mathematics' AND Status='Present' AND _Date='"+ str(date_mathematics) +"'")
            present_math = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE  Department='Mathematics' AND Status='Late' AND _Date='"+ str(date_mathematics) +"'")
            late_math = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Mathematics' AND Status='Absent' AND _Date='"+ str(date_mathematics) +"'")
            absent_math = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Mathematics' AND Status='Early Dismissal' AND _Date='"+ str(date_mathematics) +"'")
            earldis_math = cursor.fetchall()

            total_present_lb_summary.configure(text=present_math)
            total_late_lb_summary.configure(text=late_math)
            total_absent_lb_summary.configure(text=absent_math)
            total_earldis_lb_summary.configure(text=earldis_math)

            conn.commit()
            conn.close()

        def math_read_report():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            results_math_report = cursor.fetchall()
            conn.commit()
            return results_math_report

        def refreshTable_math_report():
            for data_math_report in data_table_summary.get_children():
                data_table_summary.delete(data_math_report)

            for results_math_rec_report in reverse(math_read_report()):
                data_table_summary.insert(parent='', index='end', iid=results_math_rec_report, text="", values=(results_math_rec_report), tag="orow")
            data_table_summary.tag_configure('orow', background='#EEEEEE')

        def search_present():
            date_mathematics = date_lb_summary.cget("text")
            employee_num_summary.configure(state='normal')
            emplno = employee_num_summary.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary.get_children():
                data_table_summary.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Mathematics' AND Status='Present' AND _Date='"+ str(date_mathematics) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary.configure(state='disabled')
                summary_button_print1.configure(state='disabled')
            employee_num_summary.configure(state='disabled')
            summary_button_print1.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_late():
            date_mathematics = date_lb_summary.cget("text")
            employee_num_summary.configure(state='normal')
            emplno = employee_num_summary.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary.get_children():
                data_table_summary.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Mathematics' AND Status='Late' AND _Date='"+ str(date_mathematics) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary.configure(state='disabled')
                summary_button_print1.configure(state='disabled')
            employee_num_summary.configure(state='disabled')
            summary_button_print1.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_absent():
            date_mathematics = date_lb_summary.cget("text")
            employee_num_summary.configure(state='normal')
            emplno = employee_num_summary.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary.get_children():
                data_table_summary.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Mathematics' AND Status='Absent' AND _Date='"+ str(date_mathematics) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary.configure(state='disabled')
                summary_button_print1.configure(state='disabled')
            employee_num_summary.configure(state='disabled')
            summary_button_print1.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_earlydismissal():
            date_mathematics = date_lb_summary.cget("text")
            employee_num_summary.configure(state='normal')
            emplno = employee_num_summary.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary.get_children():
                data_table_summary.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Mathematics' AND Status='Early Dismissal' AND _Date='"+ str(date_mathematics) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary.configure(state='disabled')
                summary_button_print1.configure(state='disabled')
            employee_num_summary.configure(state='disabled')
            summary_button_print1.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_date_math():
            date_mathematics = dtr_summary.get()
            employee_num_summary.configure(state='normal')
            emplno = employee_num_summary.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary.get_children():
                data_table_summary.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Mathematics' AND _Date='"+ str(date_mathematics) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary.tag_configure('oddrow', background='#EEEEEE')
                dtr_summary.delete(0,END)
                employee_num_summary.configure(state='disabled')
                summary_button_print1.configure(state='normal')
            employee_num_summary.configure(state='disabled')

            conn.commit()
            conn.close()

        def print_data_math_report():
            summary_department_combobox.configure(state='normal')
            employee_name_summary.configure(state='normal')
            employee_num_summary.configure(state='normal')

            dep = summary_department_combobox.get()
            name = employee_name_summary.get()
            num = employee_num_summary.get()

            file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

            cols = ['Date','Time in','Time out','Late','Early Dismissal']
            path = 'excelfile/read_data_employee_mathematics.csv'
            excel_name = 'excelfile/new_datasave.xlsx'
            lst = []
            with open(path,"w",newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=',')
                for row_id in data_table_summary.get_children():
                    row = data_table_summary.item(row_id,'values')
                    lst.append(row)
                lst = list(map(list,lst))
                lst.insert(0,cols)
                for row in lst:
                    csvwriter.writerow(row)

            writer = pd.ExcelWriter(excel_name)
            df = pd.read_csv(path)
            df.to_excel(writer,'sheet1', startrow = 3, index = False)
            
            workbook = writer.book
            worksheet = writer.sheets['sheet1']
            worksheet.write(0,0,'Departmet:  ' + dep, workbook.add_format({'bold': True}))
            worksheet.write(1,0,'Name:  ' + name, workbook.add_format({'bold': True}))
            worksheet.write(1,3,'Employee No:  ' + num, workbook.add_format({'bold': True}))

            writer.save()
            source = "excelfile/new_datasave.xlsx"
            if file:
                shutil.copy(source,file)
                conn = sqlite3.connect("data/data.db")
                cursor = conn.cursor()

                currentDateTime = datetime.datetime.now()

                cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    activity_log(
                                "ID"    INTEGER,
                                "Name"  TEXT,
                                "Activity"  TEXT,
                                "Department"    TEXT,
                                "Date_Time" TIMESTAMP,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                                )""")

                eName = pg4_lb_name.cget("text")
                eDepartment = pg4_lb_dept.cget("text")

                insetdata = str(eName),'Print',str(eDepartment),currentDateTime
                cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                    VAlUES(?,?,?,?)""", insetdata)
                conn.commit()
                conn.close()
                refreshTable_log()
                summary_button_print1.configure(state='disabled')
            else:
                messagebox.showinfo("Message", "You did not save the file!!")

            summary_department_combobox.configure(state='disabled')
            employee_name_summary.configure(state='disabled')
            employee_num_summary.configure(state='disabled')

                 # Data Table "TreeView"
        scrollbarx_summary = Scrollbar(popupwindow, orient=HORIZONTAL)
        scrollbarx_summary.place(x=500, y=584, width=367)
        scrollbary_summary = Scrollbar(popupwindow, orient=VERTICAL)
        scrollbary_summary.place(x=869, y=225, height=358)

        # style = ttk.Style()
        # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

        data_table_summary = ttk.Treeview(popupwindow)
        data_table_summary.place(x=500, y=225, width=368, height=358)
        data_table_summary.configure(yscrollcommand=scrollbary_summary.set, xscrollcommand=scrollbarx_summary.set)

        scrollbarx_summary.configure(command=data_table_summary.xview)
        scrollbary_summary.configure(command=data_table_summary.yview)

        data_table_summary['columns'] = ("Date","Time in","Time out","Late","Early Dismissal")
        # Format Columns
        data_table_summary.column("#0", width=0, stretch=NO)
        data_table_summary.column("Date", anchor=W, width=100)
        data_table_summary.column("Time in", anchor=W, width=100)
        data_table_summary.column("Time out", anchor=W, width=100)
        data_table_summary.column("Late", anchor=W, width=100)
        data_table_summary.column("Early Dismissal", anchor=W, width=100)

        # Create Headings
        data_table_summary.heading("Date", text="Date", anchor=CENTER)
        data_table_summary.heading("Time in", text="Time in", anchor=CENTER)
        data_table_summary.heading("Time out", text="Time out", anchor=CENTER)
        data_table_summary.heading("Late", text="Late", anchor=CENTER)
        data_table_summary.heading("Early Dismissal", text="Early Dismissal", anchor=CENTER)

        refreshTable_math_report()

                # Time Text
        time_lb = Label(popupwindow, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        time_lb.place(x=360, y=10)

            # date Text
        date_lb = Label(popupwindow, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        date_lb.place(x=530, y=10)

            # Time Label
        time_lb_summary = Label(popupwindow, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        time_lb_summary.place(x=410, y=10)

            # date Label
        date_lb_summary = Label(popupwindow, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        date_lb_summary.place(x=580, y=10)

            # ComboBox College Department
        summary_department_combobox = ttk.Combobox(popupwindow, state='disabled', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
        summary_department_combobox.place(x=253, y=245, width=175)

            # Entry Employee Number
        employee_num_summary = Entry(popupwindow, state='disabled')
        employee_num_summary.place(x=240, y=308, width=80)

            # Entry Employee Name
        employee_name_summary = Entry(popupwindow, state='disabled')
        employee_name_summary.place(x=240, y=330, width=80)

            # Entry Attendance Satatus
        att_status_summary = Entry(popupwindow, state='disabled')
        att_status_summary.place(x=240, y=352, width=80)

            # Entry Time In
        time_in_summary = Entry(popupwindow, state='disabled')
        time_in_summary.place(x=370, y=308, width=80)

            # Entry Time Out
        time_out_summary = Entry(popupwindow, state='disabled')
        time_out_summary.place(x=370, y=330, width=80)

            # Entry Date
        date_summary = Entry(popupwindow, state='disabled')
        date_summary.place(x=370, y=352, width=80)

           # Entry dtr
        dtr_summary = Entry(popupwindow)
        dtr_summary.place(x=152, y=470, width=80)

            # Button Present
        present_btn_summary = PhotoImage(file = "pic/btn_present.png")
        summary_button_present = customtkinter.CTkButton(master=popupwindow,image=present_btn_summary, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_present)
        summary_button_present.place(x=175, y=103, height=78,width=150)

            # Button Late
        late_btn_summary = PhotoImage(file = "pic/btn_late.png")
        summary_button_late = customtkinter.CTkButton(master=popupwindow,image=late_btn_summary, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_late)
        summary_button_late.place(x=355, y=103, height=78,width=150)

            # Button Absent
        absent_btn_summary = PhotoImage(file = "pic/btn_absent.png")
        summary_button_absent = customtkinter.CTkButton(master=popupwindow,image=absent_btn_summary, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_absent)
        summary_button_absent.place(x=525, y=103, height=78,width=150)

            # Button Early Dismisal
        ed_btn_summary = PhotoImage(file = "pic/btn_early_dis.png")
        summary_button_ed = customtkinter.CTkButton(master=popupwindow,image=ed_btn_summary, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_earlydismissal)
        summary_button_ed.place(x=705, y=103, height=78,width=150)

            # Total Present Label
        total_present_lb_summary = Label(popupwindow, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_present_lb_summary.place(x=225, y=136)

            # Total Late Label
        total_late_lb_summary = Label(popupwindow, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_late_lb_summary.place(x=405, y=136)

            # Total Absent Label
        total_absent_lb_summary = Label(popupwindow, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_absent_lb_summary.place(x=575, y=136)

            # Total Early Dismisal Label
        total_earldis_lb_summary = Label(popupwindow, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_earldis_lb_summary.place(x=755, y=136)

            # Print Button
        print_btn_summary = PhotoImage(file = "pic/btn_print.png")
        summary_button_print = customtkinter.CTkButton(master=popupwindow,image=print_btn_summary, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_data_math_report)
        summary_button_print.place(x=258, y=375, height=20,width=80)

            # Generate Button
        generate_btn_summary = PhotoImage(file = "pic/btn_generate.png")
        summary_button_generate = customtkinter.CTkButton(master=popupwindow,image=generate_btn_summary, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=search_date_math)
        summary_button_generate.place(x=258, y=468, height=20,width=80)

            # Print Button
        summary_button_print1 = customtkinter.CTkButton(master=popupwindow,state='disabled',image=print_btn_summary, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_data_math_report)
        summary_button_print1.place(x=358, y=468, height=20,width=80)

            # Show All Button
        showall_btn_summary = PhotoImage(file = "pic/btn_showall_small.png")
        summary_button_showall = customtkinter.CTkButton(master=popupwindow,image=showall_btn_summary, text="" ,
                                                    corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_math_report)
        summary_button_showall.place(x=650, y=598, height=20,width=90)

        display_info()
        time_report()
        count_data_report()

    # ============= Mathematics Attendance Record Frame =============================================================================

        # open background image
    mathematics_att_record.math_rec_image = Image.open('pic/15.png')
    mathematics_att_record.math_rec_resize_image = mathematics_att_record.math_rec_image.resize((1362, 692))
    mathematics_att_record.photo = ImageTk.PhotoImage(mathematics_att_record.math_rec_resize_image)
    mathematics_att_record.math_rec_bg_img_lb = Label(mathematics_att_record, image = mathematics_att_record.photo)
    mathematics_att_record.math_rec_bg_img_lb.pack()

         # Get Current Time and Date
    def time():
        string_time = strftime('%I:%M:%S %p')
        time_lb_math_rec.configure(text = string_time)
        time_lb_math_rec.after(1000, time)

        string_date = strftime('%d-%m-20%y')
        date_lb_math_rec.configure(text = string_date)

            # search Data
    def search_data_math():
        lookup_record = search_math_rec.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for record in data_table_math_rec.get_children():
            data_table_math_rec.delete(record)
        
        cursor.execute("SELECT Name,Department,Day,Subject,Room,Section,Time_in,Time_out,_Date,Status,Late,Early_Dismissal FROM attendance_record WHERE (Name = '" + str(lookup_record) + "' or Day = '" + str(lookup_record) + "' or Subject = '" + str(lookup_record) + "' or Room = '" + str(lookup_record) + "' or Section = '" + str(lookup_record) + "' or Time_in = '" + str(lookup_record) + "' or Time_out = '" + str(lookup_record) + "' or _Date = '" + str(lookup_record) + "' or Status = '" + str(lookup_record) + "' or Late = '" + str(lookup_record) + "' or Early_Dismissal = '" + str(lookup_record) + "') AND Department='Mathematics'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_math_rec.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]), tag="evenrow")
            else:
                data_table_math_rec.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]), tag="oddrow")
            count += 1
            data_table_math_rec.tag_configure('evenrow', background='#EEEEEE')
            data_table_math_rec.tag_configure('oddrow', background='#EEEEEE')
            search_math_rec.delete(0, END)

        conn.commit()
        conn.close()

            # Get And Disply the data in the table
    def math_read():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
                        attendance_record(
                            "ID" INTEGER,
                            "Employee_No" TEXT,
                            "Name"  TEXT,
                            "Department" TEXT,
                            "Day" TEXT,
                            "Subject" TEXT,
                            "Room" TEXT,
                            "Section" TEXT,
                            "Time_in" TEXT,
                            "Time_out" TEXT,
                            "_Date" TEXT,
                            "Status" TEXT,
                            "Late" TEXT,
                            "Early_Dismissal" TEXT,
                            PRIMARY KEY("ID" AUTOINCREMENT))""")

        # cursor.execute("""INSERT INTO attendance_record (ID,Employee_No,Name,Department,Day,Subject,Room,Section,Time_in,Time_out,_Date,Status)
        #                 VAlUES
        #                 (1,234,'neil','ite','Monday','Math','401','4A','8:23:45 AM','5:23:45 PM','24/11/2022','Present'),
        #                 (2,345,'josel','ite','Friday','Science','410','4C','9:12:45 AM','6:23:45 PM','24/11/2022','Late') """)

        cursor.execute("SELECT Name,Department,Day,Subject,Room,Section,Time_in,Time_out,_Date,Status,Late,Early_Dismissal FROM attendance_record WHERE Department='Mathematics'")
        results_math = cursor.fetchall()
        conn.commit()
        return results_math

    # def delete_math(data):
    #     conn = sqlite3.connect("data/data.db")
    #     cursor = conn.cursor()

    #     cursor.execute("""CREATE TABLE IF NOT EXISTS 
    #         attendance_record(ID INTEGER PRIMARY KEY,Employee_No INTEGER,Name TEXT,
    #         Department TEXT,Time_in TEXT,Time_out TEXT,_Date TEXT,Status TEXT)""")

    #     cursor.execute("DELETE FROM attendance_record WHERE Employee_No ='" + srt(data) + "'")
    #     conn.commit()

            # Refresh the tabble on Treeview
    def refreshTable_math():
        for data_math in data_table_math_rec.get_children():
            data_table_math_rec.delete(data_math)

        for results_math_rec in reverse(math_read()):
            data_table_math_rec.insert(parent='', index='end', iid=results_math_rec, text="", values=(results_math_rec), tag="orow")
        data_table_math_rec.tag_configure('orow', background='#EEEEEE')

            # GET the Count of Total Faculty, Total Present, Total Late and Total Absent
    def count_data():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        date_mathematics = date_lb_math_rec.cget("text")

        cursor.execute("SELECT COUNT(*) FROM faculty_data WHERE Position='Employee'")
        total_math = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE  Department='Mathematics' AND Status='Present' AND _Date='"+ str(date_mathematics) +"'")
        present_math = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Mathematics' AND Status='Absent' AND _Date='"+ str(date_mathematics) +"'")
        absent_math = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Mathematics' AND Status='Late' AND _Date='"+ str(date_mathematics) +"'")
        late_math = cursor.fetchall()

        total_faculty_lb_math_rec.configure(text=total_math)
        total_present_lb_math_rec.configure(text=present_math)
        total_absent_lb_math_rec.configure(text=absent_math)
        total_late_lb_math_rec.configure(text=late_math)

        conn.commit()
        conn.close()

    def print_math():
            file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

            cols = ['Name','Department','Day','Subject','Room','Section','Time in','Time out','Date','Remarks','Late','Early Dismissal']
            path = 'excelfile/read_data_employee_mathematics.csv'
            excel_name = 'excelfile/new_datasave.xlsx'
            lst = []
            with open(path,"w",newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=',')
                for row_id in data_table_math_rec.get_children():
                    row = data_table_math_rec.item(row_id,'values')
                    lst.append(row)
                lst = list(map(list,lst))
                lst.insert(0,cols)
                for row in lst:
                    csvwriter.writerow(row)

            writer = pd.ExcelWriter(excel_name)
            df = pd.read_csv(path)
            df.to_excel(writer,'sheet1', startrow = 3, index = False)
            
            workbook = writer.book
            worksheet = writer.sheets['sheet1']
            worksheet.write(0,0,'Departmet:_Mathematics_ ', workbook.add_format({'bold': True}))
            worksheet.write(1,0,'Name:________________ ', workbook.add_format({'bold': True}))
            worksheet.write(1,3,'Employee No:________________ ', workbook.add_format({'bold': True}))

            writer.save()
            source = "excelfile/new_datasave.xlsx"
            if file:
                shutil.copy(source,file)
                conn = sqlite3.connect("data/data.db")
                cursor = conn.cursor()

                currentDateTime = datetime.datetime.now()

                cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    activity_log(
                                "ID"    INTEGER,
                                "Name"  TEXT,
                                "Activity"  TEXT,
                                "Department"    TEXT,
                                "Date_Time" TIMESTAMP,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                                )""")

                eName = pg4_lb_name.cget("text")
                eDepartment = pg4_lb_dept.cget("text")

                insetdata = str(eName),'Print',str(eDepartment),currentDateTime
                cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                    VAlUES(?,?,?,?)""", insetdata)
                conn.commit()
                conn.close()
                refreshTable_log()
                
            else:
                messagebox.showinfo("Message", "You did not save the file!!")

         # Data Table "TreeView"
    scrollbarx_math_rec = Scrollbar(mathematics_att_record, orient=HORIZONTAL)
    scrollbarx_math_rec.place(x=710, y=584, width=347)
    scrollbary_math_rec = Scrollbar(mathematics_att_record, orient=VERTICAL)
    scrollbary_math_rec.place(x=1040, y=366, height=219)

    # style = ttk.Style()
    # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table_math_rec = ttk.Treeview(mathematics_att_record)
    data_table_math_rec.place(x=710, y=366, width=330, height=219)
    data_table_math_rec.configure(yscrollcommand=scrollbary_math_rec.set, xscrollcommand=scrollbarx_math_rec.set)

    scrollbarx_math_rec.configure(command=data_table_math_rec.xview)
    scrollbary_math_rec.configure(command=data_table_math_rec.yview)

    data_table_math_rec['columns'] = ("Name","Department","Day","Subject","Room","Section","Time in","Time out","Date","Remarks","Late","Early Dismissal")
    # Format Columns
    data_table_math_rec.column("#0", width=0, stretch=NO)
    data_table_math_rec.column("Name", anchor=W, width=100)
    data_table_math_rec.column("Department", anchor=W, width=200)
    data_table_math_rec.column("Day", anchor=W, width=100)
    data_table_math_rec.column("Subject", anchor=W, width=100)
    data_table_math_rec.column("Room", anchor=W, width=100)
    data_table_math_rec.column("Section", anchor=W, width=100)
    data_table_math_rec.column("Time in", anchor=W, width=100)
    data_table_math_rec.column("Time out", anchor=W, width=100)
    data_table_math_rec.column("Date", anchor=W, width=100)
    data_table_math_rec.column("Remarks", anchor=W, width=100)
    data_table_math_rec.column("Late", anchor=W, width=100)
    data_table_math_rec.column("Early Dismissal", anchor=W, width=100)

    # Create Headings
    data_table_math_rec.heading("Name", text="Name", anchor=CENTER)
    data_table_math_rec.heading("Department", text="Department", anchor=CENTER)
    data_table_math_rec.heading("Day", text="Day", anchor=CENTER)
    data_table_math_rec.heading("Subject", text="Subject", anchor=CENTER)
    data_table_math_rec.heading("Room", text="Room", anchor=CENTER)
    data_table_math_rec.heading("Section", text="Section", anchor=CENTER)
    data_table_math_rec.heading("Time in", text="Time in", anchor=CENTER)
    data_table_math_rec.heading("Time out", text="Time out", anchor=CENTER)
    data_table_math_rec.heading("Date", text="Date", anchor=CENTER)
    data_table_math_rec.heading("Remarks", text="Remarks", anchor=CENTER)
    data_table_math_rec.heading("Late", text="Late", anchor=CENTER)
    data_table_math_rec.heading("Early Dismissal", text="Early Dismissal", anchor=CENTER)

    # data_table_math_rec.bind("<ButtonRelease-1>", select_row_math)

    refreshTable_math()

    def select_row_math(e):
        selected = data_table_math_rec_IR.focus()
        values = data_table_math_rec_IR.item(selected, 'values')

        if values :
            employee_num_math_rec.configure(state='normal')
            employee_name_math_rec.configure(state='normal')
            
            employee_num_math_rec.delete(0, END)
            employee_name_math_rec.delete(0, END)

            employee_num_math_rec.insert(0, values[0])
            employee_name_math_rec.insert(0, values[1])
            
            employee_num_math_rec.configure(state='disabled',text='')
            employee_name_math_rec.configure(state='disabled')
        else:
            messagebox.showinfo("Error", "There is no selected data on the table !!")

    def math_read_IR():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            attendance_record(ID INTEGER PRIMARY KEY,Employee_No INTEGER,Name TEXT,
            Department TEXT,Time_in TEXT,Time_out TEXT,_Date TEXT,Status TEXT)""")

        cursor.execute("SELECT Employee_No,Name FROM attendance_record WHERE Department='Mathematics'")
        results_math_IR = cursor.fetchall()
        conn.commit()
        return results_math_IR

    def refreshTable_math_IR():
        for data_math_IR in data_table_math_rec_IR.get_children():
            data_table_math_rec_IR.delete(data_math_IR)

        for results_math_rec_IR in reverse(math_read_IR()):
            data_table_math_rec_IR.insert(parent='', index='end', iid=results_math_rec_IR, text="", values=(results_math_rec_IR), tag="orow")
        data_table_math_rec_IR.tag_configure('orow', background='#EEEEEE')

    def search_data_math_IR():
        lookup_record = search_math_rec_IR.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for record in data_table_math_rec_IR.get_children():
            data_table_math_rec_IR.delete(record)
        
        cursor.execute("SELECT Employee_No,Name FROM attendance_record WHERE Employee_No = '" + str(lookup_record) + "' AND Department='Mathematics'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_math_rec_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="evenrow")
            else:
                data_table_math_rec_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="oddrow")
            count += 1
            data_table_math_rec_IR.tag_configure('evenrow', background='#EEEEEE')
            data_table_math_rec_IR.tag_configure('oddrow', background='#EEEEEE')
            search_math_rec_IR.delete(0, END)

        conn.commit()
        conn.close()

         # Data Table "TreeView" Individual Report
    scrollbary_math_rec = Scrollbar(mathematics_att_record, orient=VERTICAL)
    scrollbary_math_rec.place(x=645, y=366, height=219)

    # style = ttk.Style()
    # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table_math_rec_IR = ttk.Treeview(mathematics_att_record)
    data_table_math_rec_IR.place(x=315, y=366, width=330, height=219)
    data_table_math_rec_IR.configure(yscrollcommand=scrollbary_math_rec.set)

    scrollbary_math_rec.configure(command=data_table_math_rec_IR.yview)

    data_table_math_rec_IR['columns'] = ("Employee No.","Name")
    # Format Columns Individual Report
    data_table_math_rec_IR.column("#0", width=0, stretch=NO)
    data_table_math_rec_IR.column("Employee No.", anchor=W, width=50)
    data_table_math_rec_IR.column("Name", anchor=W, width=100)

    # Create Headings Individual Report
    data_table_math_rec_IR.heading("Employee No.", text="Employee No.", anchor=CENTER)
    data_table_math_rec_IR.heading("Name", text="Name", anchor=CENTER)

    data_table_math_rec_IR.bind("<ButtonRelease-1>", select_row_math)

    refreshTable_math_IR()

        # Time Text
    time_lb = Label(mathematics_att_record, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    time_lb.place(x=540, y=10)

        # date Text
    date_lb = Label(mathematics_att_record, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    date_lb.place(x=710, y=10)

        # Time Label
    time_lb_math_rec = Label(mathematics_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    time_lb_math_rec.place(x=590, y=10)

        # date Label
    date_lb_math_rec = Label(mathematics_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    date_lb_math_rec.place(x=760, y=10)
    

        # Total Faculty Label
    total_faculty_lb_math_rec = Label(mathematics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_faculty_lb_math_rec.place(x=294, y=190)

        # Total Present Label
    total_present_lb_math_rec = Label(mathematics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_present_lb_math_rec.place(x=512, y=190)

        # Total Absent Label
    total_absent_lb_math_rec = Label(mathematics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_absent_lb_math_rec.place(x=717, y=190)

        # Total Late Label
    total_late_lb_math_rec = Label(mathematics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_late_lb_math_rec.place(x=948, y=190)

    def error():
        emp_num = employee_num_math_rec.get()
        emp_name = employee_name_math_rec.get()

        if emp_num == "" or emp_name == "":
            messagebox.showinfo("Error", "Please Seleted a row on the table to open Summary Report !!")
        else:
            summary()

        # Entry Employee Number
    employee_num_math_rec = Entry(mathematics_att_record)
    employee_num_math_rec.place(x=315, y=586, width=100)

        # Entry Employee Name
    employee_name_math_rec = Entry(mathematics_att_record)
    employee_name_math_rec.place(x=425, y=586, width=100)

        # Summary Report Button 
    math_rec_button_report = customtkinter.CTkButton(master=mathematics_att_record, text="Summary Report" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#C0C0C0",hover_color="#006699", command=error)
    math_rec_button_report.place(x=550, y=586, height=21,width=110)

         # Search Entry Individual Report
    search_ent_math_rec_IR = StringVar()
    search_math_rec_IR = Entry(mathematics_att_record, textvariable = search_ent_math_rec_IR)
    search_math_rec_IR.place(x=385, y=305, width=190)

        # Search Button Individual Report
    search_btn_math_rec_IR = PhotoImage(file = "pic/btn_search_small.png")
    math_rec_button_search_IR = customtkinter.CTkButton(master=mathematics_att_record,image=search_btn_math_rec_IR, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_math_IR)
    math_rec_button_search_IR.place(x=590, y=307, height=17,width=70)

        # Show All Button Individual Report
    showall_btn_math_rec_IR = PhotoImage(file = "pic/btn_showall_small.png")
    math_rec_button_showall_IR = customtkinter.CTkButton(master=mathematics_att_record,image=showall_btn_math_rec_IR, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_math_IR)
    math_rec_button_showall_IR.place(x=445, y=608, height=21,width=90)

        # Search Entry
    search_ent = StringVar()
    search_math_rec = Entry(mathematics_att_record, textvariable = search_ent)
    search_math_rec.place(x=780, y=307, width=190)

        # Search Button
    search_btn_math_rec = PhotoImage(file = "pic/btn_search_small.png")
    math_rec_button_search = customtkinter.CTkButton(master=mathematics_att_record,image=search_btn_math_rec, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_math)
    math_rec_button_search.place(x=975, y=307, height=17,width=70)

        # Show All Button
    showall_btn_math_rec = PhotoImage(file = "pic/btn_showall_small.png")
    math_rec_button_showall = customtkinter.CTkButton(master=mathematics_att_record,image=showall_btn_math_rec, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_math)
    math_rec_button_showall.place(x=885, y=608, height=21,width=90)

        # Print Button
    print_btn_math_rec = PhotoImage(file = "pic/btn_print.png")
    math_rec_button_print = customtkinter.CTkButton(master=mathematics_att_record,image=print_btn_math_rec, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_math)
    math_rec_button_print.place(x=785, y=608, height=20,width=80)

        # Back Button
    math_rec_back = PhotoImage(file = "pic/btn_back_page.png")
    math_rec_button_back = customtkinter.CTkButton(master=mathematics_att_record,image=math_rec_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(attendance_record))
    math_rec_button_back.place(x=45, y=595, height=50,width=140)

    time()
    count_data()

    # ============= Summary Report  ========================================================================================================================

    def summary_psyc():
        popupwindow_psyc = Toplevel(main_window)
        popupwindow_psyc.title("Individual Summary Report")
        popupwindow_psyc.geometry('1020x650')
        popupwindow_psyc.grab_set()
        popupwindow_psyc.resizable(False,False)

            # open background image
        popupwindow_psyc.summary_image = Image.open('pic/16.png')
        popupwindow_psyc.summary_resize_image = popupwindow_psyc.summary_image.resize((1020,650))
        popupwindow_psyc.photo = ImageTk.PhotoImage(popupwindow_psyc.summary_resize_image)
        popupwindow_psyc.summary_bg_img_lb = Label(popupwindow_psyc, image = popupwindow_psyc.photo)
        popupwindow_psyc.summary_bg_img_lb.pack()

        emp_num = employee_num_psyc.get()
        emp_name = employee_name_psyc.get()

             # Get Current Time and Date
        def time_report():
            string_time = strftime('%I:%M:%S %p')
            time_lb_summary_psyc.configure(text = string_time)
            time_lb_summary_psyc.after(1000, time_report)

            string_date = strftime('%d-%m-20%y')
            date_lb_summary_psyc.configure(text = string_date)

        def display_info():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT Department FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            dept = cursor.fetchone()

            cursor.execute("SELECT Status FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            st = cursor.fetchone()

            cursor.execute("SELECT Time_in FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            Tmin = cursor.fetchone()

            cursor.execute("SELECT Time_out FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            Tmout = cursor.fetchone()

            cursor.execute("SELECT _Date FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            dt = cursor.fetchone()

            summary_department_combobox_psyc.configure(state='normal')
            employee_num_summary_psyc.configure(state='normal')
            employee_name_summary_psyc.configure(state='normal')
            att_status_summary_psyc.configure(state='normal')
            time_in_summary_psyc.configure(state='normal')
            time_out_summary_psyc.configure(state='normal')
            date_summary_psyc_psyc.configure(state='normal')

            summary_department_combobox_psyc.insert(0,dept)
            employee_num_summary_psyc.insert(0,emp_num)
            employee_name_summary_psyc.insert(0,emp_name)
            att_status_summary_psyc.insert(0,st)
            time_in_summary_psyc.insert(0,Tmin)
            time_out_summary_psyc.insert(0,Tmout)
            date_summary_psyc_psyc.insert(0,dt)

            summary_department_combobox_psyc.configure(state='disabled')
            employee_num_summary_psyc.configure(state='disabled')
            employee_name_summary_psyc.configure(state='disabled')
            att_status_summary_psyc.configure(state='disabled')
            time_in_summary_psyc.configure(state='disabled')
            time_out_summary_psyc.configure(state='disabled')
            date_summary_psyc_psyc.configure(state='disabled')

            conn.commit()
            conn.close()

        def count_data_report():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            date_psychology = date_lb_summary_psyc.cget("text")

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE  Department='Psychology' AND Status='Present' AND _Date='"+ str(date_psychology) +"'")
            present_psyc = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE  Department='Psychology' AND Status='Late' AND _Date='"+ str(date_psychology) +"'")
            late_psyc = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Psychology' AND Status='Absent' AND _Date='"+ str(date_psychology) +"'")
            absent_psyc = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Psychology' AND Status='Early Dismissal' AND _Date='"+ str(date_psychology) +"'")
            earldis_psyc = cursor.fetchall()

            total_present_lb_summary_psyc.configure(text=present_psyc)
            total_late_lb_summary_psyc.configure(text=late_psyc)
            total_absent_lb_summary_psyc.configure(text=absent_psyc)
            total_earldis_lb_summary_psyc.configure(text=earldis_psyc)

            conn.commit()
            conn.close()

        def psyc_read_report():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            results_report = cursor.fetchall()
            conn.commit()
            return results_report

        def refreshTable_psyc_report():
            for data_report in data_table_summary_psyc.get_children():
                data_table_summary_psyc.delete(data_report)

            for results_report in reverse(psyc_read_report()):
                data_table_summary_psyc.insert(parent='', index='end', iid=results_report, text="", values=(results_report), tag="orow")
            data_table_summary_psyc.tag_configure('orow', background='#EEEEEE')

        def search_present():
            date_psychology = date_lb_summary_psyc.cget("text")
            employee_num_summary_psyc.configure(state='normal')
            emplno = employee_num_summary_psyc.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_psyc.get_children():
                data_table_summary_psyc.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Psychology' AND Status='Present' AND _Date='"+ str(date_psychology) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_psyc.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_psyc.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary_psyc.configure(state='disabled')
                summary_button_print1_psyc.configure(state='disabled')
            employee_num_summary_psyc.configure(state='disabled')
            summary_button_print1_psyc.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_late():
            date_psychology = date_lb_summary_psyc.cget("text")
            employee_num_summary_psyc.configure(state='normal')
            emplno = employee_num_summary_psyc.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_psyc.get_children():
                data_table_summary_psyc.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Psychology' AND Status='Late' AND _Date='"+ str(date_psychology) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_psyc.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_psyc.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary_psyc.configure(state='disabled')
                summary_button_print1_psyc.configure(state='disabled')
            employee_num_summary_psyc.configure(state='disabled')
            summary_button_print1_psyc.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_absent():
            date_psychology = date_lb_summary_psyc.cget("text")
            employee_num_summary_psyc.configure(state='normal')
            emplno = employee_num_summary_psyc.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_psyc.get_children():
                data_table_summary_psyc.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Psychology' AND Status='Absent' AND _Date='"+ str(date_psychology) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_psyc.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_psyc.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary_psyc.configure(state='disabled')
                summary_button_print1_psyc.configure(state='disabled')
            employee_num_summary_psyc.configure(state='disabled')
            summary_button_print1_psyc.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_earlydismissal():
            date_psychology = date_lb_summary_psyc.cget("text")
            employee_num_summary_psyc.configure(state='normal')
            emplno = employee_num_summary_psyc.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_psyc.get_children():
                data_table_summary_psyc.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Psychology' AND Status='Early Dismissal' AND _Date='"+ str(date_psychology) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_psyc.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_psyc.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary_psyc.configure(state='disabled')
                summary_button_print1_psyc.configure(state='disabled')
            employee_num_summary_psyc.configure(state='disabled')
            summary_button_print1_psyc.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_date_psyc():
            date_psychology = dtr_summary_psyc.get()
            employee_num_summary_psyc.configure(state='normal')
            emplno = employee_num_summary_psyc.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_psyc.get_children():
                data_table_summary_psyc.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Psychology' AND _Date='"+ str(date_psychology) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_psyc.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_psyc.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary_psyc.configure(state='disabled')
                summary_button_print1_psyc.configure(state='normal')
                dtr_summary_psyc.delete(0,END)
            employee_num_summary_psyc.configure(state='disabled')

            conn.commit()
            conn.close()

        def print_data_psyc():
            summary_department_combobox_psyc.configure(state='normal')
            employee_name_summary_psyc.configure(state='normal')
            employee_num_summary_psyc.configure(state='normal')

            dep = summary_department_combobox_psyc.get()
            name = employee_name_summary_psyc.get()
            num = employee_num_summary_psyc.get()

            file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

            cols = ['Date','Time in','Time out','Late','Early Dismissal']
            path = 'excelfile/read_data_employee_psychology.csv'
            excel_name = 'excelfile/new_datasave_psychology.xlsx'
            lst = []
            with open(path,"w",newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=',')
                for row_id in data_table_summary_psyc.get_children():
                    row = data_table_summary_psyc.item(row_id,'values')
                    lst.append(row)
                lst = list(map(list,lst))
                lst.insert(0,cols)
                for row in lst:
                    csvwriter.writerow(row)

            writer = pd.ExcelWriter(excel_name)
            df = pd.read_csv(path)
            df.to_excel(writer,'sheet1', startrow = 3, index = False)
            
            workbook = writer.book
            worksheet = writer.sheets['sheet1']
            worksheet.write(0,0,'Departmet:  ' + dep, workbook.add_format({'bold': True}))
            worksheet.write(1,0,'Name:  ' + name, workbook.add_format({'bold': True}))
            worksheet.write(1,3,'Employee No:  ' + num, workbook.add_format({'bold': True}))

            writer.save()
            source = "excelfile/new_datasave_psychology.xlsx"
            if file:
                shutil.copy(source,file)
                conn = sqlite3.connect("data/data.db")
                cursor = conn.cursor()

                currentDateTime = datetime.datetime.now()

                cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    activity_log(
                                "ID"    INTEGER,
                                "Name"  TEXT,
                                "Activity"  TEXT,
                                "Department"    TEXT,
                                "Date_Time" TIMESTAMP,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                                )""")

                eName = pg4_lb_name.cget("text")
                eDepartment = pg4_lb_dept.cget("text")

                insetdata = str(eName),'Print',str(eDepartment),currentDateTime
                cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                    VAlUES(?,?,?,?)""", insetdata)
                conn.commit()
                conn.close()
                refreshTable_log()
                summary_button_print1_psyc.configure(state='disabled')
            else:
                messagebox.showinfo("Message", "You did not save the file!!")

            summary_department_combobox_psyc.configure(state='disabled')
            employee_name_summary_psyc.configure(state='disabled')
            employee_num_summary_psyc.configure(state='disabled')

                 # Data Table "TreeView"
        scrollbarx_summary_psyc = Scrollbar(popupwindow_psyc, orient=HORIZONTAL)
        scrollbarx_summary_psyc.place(x=500, y=584, width=367)
        scrollbary_summary_psyc = Scrollbar(popupwindow_psyc, orient=VERTICAL)
        scrollbary_summary_psyc.place(x=869, y=225, height=358)

        # style = ttk.Style()
        # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

        data_table_summary_psyc = ttk.Treeview(popupwindow_psyc)
        data_table_summary_psyc.place(x=500, y=225, width=368, height=358)
        data_table_summary_psyc.configure(yscrollcommand=scrollbary_summary_psyc.set, xscrollcommand=scrollbarx_summary_psyc.set)

        scrollbarx_summary_psyc.configure(command=data_table_summary_psyc.xview)
        scrollbary_summary_psyc.configure(command=data_table_summary_psyc.yview)

        data_table_summary_psyc['columns'] = ("Date","Time in","Time out","Late","Early Dismissal")
        # Format Columns
        data_table_summary_psyc.column("#0", width=0, stretch=NO)
        data_table_summary_psyc.column("Date", anchor=W, width=100)
        data_table_summary_psyc.column("Time in", anchor=W, width=100)
        data_table_summary_psyc.column("Time out", anchor=W, width=100)
        data_table_summary_psyc.column("Late", anchor=W, width=100)
        data_table_summary_psyc.column("Early Dismissal", anchor=W, width=100)

        # Create Headings
        data_table_summary_psyc.heading("Date", text="Date", anchor=CENTER)
        data_table_summary_psyc.heading("Time in", text="Time in", anchor=CENTER)
        data_table_summary_psyc.heading("Time out", text="Time out", anchor=CENTER)
        data_table_summary_psyc.heading("Late", text="Late", anchor=CENTER)
        data_table_summary_psyc.heading("Early Dismissal", text="Early Dismissal", anchor=CENTER)

        refreshTable_psyc_report()

                # Time Text
        time_lb = Label(popupwindow_psyc, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        time_lb.place(x=360, y=10)

            # date Text
        date_lb = Label(popupwindow_psyc, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        date_lb.place(x=530, y=10)

            # Time Label
        time_lb_summary_psyc = Label(popupwindow_psyc, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        time_lb_summary_psyc.place(x=410, y=10)

            # date Label
        date_lb_summary_psyc = Label(popupwindow_psyc, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        date_lb_summary_psyc.place(x=580, y=10)

            # ComboBox College Department
        summary_department_combobox_psyc = ttk.Combobox(popupwindow_psyc, state='disabled', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
        summary_department_combobox_psyc.place(x=253, y=245, width=175)

            # Entry Employee Number
        employee_num_summary_psyc = Entry(popupwindow_psyc, state='disabled')
        employee_num_summary_psyc.place(x=240, y=308, width=80)

            # Entry Employee Name
        employee_name_summary_psyc = Entry(popupwindow_psyc, state='disabled')
        employee_name_summary_psyc.place(x=240, y=330, width=80)

            # Entry Attendance Satatus
        att_status_summary_psyc = Entry(popupwindow_psyc, state='disabled')
        att_status_summary_psyc.place(x=240, y=352, width=80)

            # Entry Time In
        time_in_summary_psyc = Entry(popupwindow_psyc, state='disabled')
        time_in_summary_psyc.place(x=370, y=308, width=80)

            # Entry Time Out
        time_out_summary_psyc = Entry(popupwindow_psyc, state='disabled')
        time_out_summary_psyc.place(x=370, y=330, width=80)

            # Entry Date
        date_summary_psyc_psyc = Entry(popupwindow_psyc, state='disabled')
        date_summary_psyc_psyc.place(x=370, y=352, width=80)

           # Entry dtr
        dtr_summary_psyc = Entry(popupwindow_psyc,)
        dtr_summary_psyc.place(x=152, y=470, width=80)

            # Button Present
        present_btn_summary_psyc = PhotoImage(file = "pic/btn_present.png")
        summary_button_present_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=present_btn_summary_psyc, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_present)
        summary_button_present_psyc.place(x=175, y=103, height=78,width=150)

            # Button Late
        late_btn_summary_psyc = PhotoImage(file = "pic/btn_late.png")
        summary_button_late_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=late_btn_summary_psyc, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_late)
        summary_button_late_psyc.place(x=355, y=103, height=78,width=150)

            # Button Absent
        absent_btn_summary_psyc = PhotoImage(file = "pic/btn_absent.png")
        summary_button_absent_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=absent_btn_summary_psyc, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_absent)
        summary_button_absent_psyc.place(x=525, y=103, height=78,width=150)

            # Button Early Dismisal
        ed_btn_summary_psyc = PhotoImage(file = "pic/btn_early_dis.png")
        summary_button_ed_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=ed_btn_summary_psyc, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_earlydismissal)
        summary_button_ed_psyc.place(x=705, y=103, height=78,width=150)

            # Total Present Label
        total_present_lb_summary_psyc = Label(popupwindow_psyc, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_present_lb_summary_psyc.place(x=225, y=136)

            # Total Late Label
        total_late_lb_summary_psyc = Label(popupwindow_psyc, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_late_lb_summary_psyc.place(x=405, y=136)

            # Total Absent Label
        total_absent_lb_summary_psyc = Label(popupwindow_psyc, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_absent_lb_summary_psyc.place(x=575, y=136)

            # Total Early Dismisal Label
        total_earldis_lb_summary_psyc = Label(popupwindow_psyc, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_earldis_lb_summary_psyc.place(x=755, y=136)

            # Print Button
        print_btn_summary_psyc = PhotoImage(file = "pic/btn_print.png")
        summary_button_print_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=print_btn_summary_psyc, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_data_psyc)
        summary_button_print_psyc.place(x=258, y=375, height=20,width=80)

            # Generate Button
        generate_btn_summary_psyc = PhotoImage(file = "pic/btn_generate.png")
        summary_button_generate_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=generate_btn_summary_psyc, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=search_date_psyc)
        summary_button_generate_psyc.place(x=258, y=468, height=20,width=80)

            # Print Button
        summary_button_print1_psyc = customtkinter.CTkButton(master=popupwindow_psyc,state='disabled',image=print_btn_summary_psyc, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_data_psyc)
        summary_button_print1_psyc.place(x=358, y=468, height=20,width=80)

            # Show All Button
        showall_btn_summary_psyc = PhotoImage(file = "pic/btn_showall_small.png")
        summary_button_showall_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=showall_btn_summary_psyc, text="" ,
                                                    corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_psyc_report)
        summary_button_showall_psyc.place(x=650, y=598, height=20,width=90)

        display_info()
        time_report()
        count_data_report()

    # ============= Psychology Attendance Record Frame =============================================================================

        # open background image
    psychology_att_record.psyc_image = Image.open('pic/17.png')
    psychology_att_record.psyc_resize_image = psychology_att_record.psyc_image.resize((1362, 692))
    psychology_att_record.photo = ImageTk.PhotoImage(psychology_att_record.psyc_resize_image)
    psychology_att_record.psyc_bg_img_lb = Label(psychology_att_record, image = psychology_att_record.photo)
    psychology_att_record.psyc_bg_img_lb.pack()

         # Get Current Time and Date
    def time_psyc():
        string_time_psyc = strftime('%I:%M:%S %p')
        time_lb_psyc.configure(text = string_time_psyc)
        time_lb_psyc.after(1000, time_psyc)

        string_date_psyc = strftime('%d-%m-20%y')
        date_lb_psyc.configure(text = string_date_psyc)

            # Get And Disply the data in the table
    def psyc_read():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            attendance_record(
                            "ID" INTEGER,
                            "Employee_No" TEXT,
                            "Name"  TEXT,
                            "Department" TEXT,
                            "Day" TEXT,
                            "Subject" TEXT,
                            "Room" TEXT,
                            "Section" TEXT,
                            "Time_in" TEXT,
                            "Time_out" TEXT,
                            "_Date" TEXT,
                            "Status" TEXT,
                            "Late" TEXT,
                            "Early_Dismissal" TEXT,
                            PRIMARY KEY("ID" AUTOINCREMENT))""")

        cursor.execute("SELECT Name,Department,Day,Subject,Room,Section,Time_in,Time_out,_Date,Status,Late,Early_Dismissal FROM attendance_record WHERE Department='Psychology'")
        results_psyc = cursor.fetchall()
        conn.commit()
        return results_psyc

        # Refresh the tabble on Treeview
    def refreshTable_psyc():
        for data_psyc in data_table_psyc.get_children():
            data_table_psyc.delete(data_psyc)

        for results_psyc_rec in reverse(psyc_read()):
            data_table_psyc.insert(parent='', index='end', iid=results_psyc_rec, text="", values=(results_psyc_rec), tag="orow")
        data_table_psyc.tag_configure('orow', background='#EEEEEE')

            # GET the Count of Total Faculty, Total Present, Total Late and Total Absent
    def count_data_psyc():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        date_psychology = date_lb_psyc.cget("text")

        cursor.execute("SELECT COUNT(*) FROM faculty_data WHERE Position='Employee'")
        total_psyc = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE  Department='Psychology' AND Status='Present' AND _Date='"+ str(date_psychology) +"'")
        present_psyc = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Psychology' AND Status='Absent' AND _Date='"+ str(date_psychology) +"'")
        absent_psyc = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Psychology' AND Status='Late' AND _Date='"+ str(date_psychology) +"'")
        late_psyc = cursor.fetchall()

        total_faculty_lb_psyc.configure(text=total_psyc)
        total_present_lb_psyc.configure(text=present_psyc)
        total_absent_lb_psyc.configure(text=absent_psyc)
        total_late_lb_psyc.configure(text=late_psyc)

        conn.commit()
        conn.close()

    def search_data_psyc():
        lookup_record = search_psyc.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for record in data_table_psyc.get_children():
            data_table_psyc.delete(record)
        
        cursor.execute("SELECT Name,Department,Day,Subject,Room,Section,Time_in,Time_out,_Date,Status,Late,Early_Dismissal FROM attendance_record WHERE (Name = '" + str(lookup_record) + "' or Day = '" + str(lookup_record) + "' or Subject = '" + str(lookup_record) + "' or Room = '" + str(lookup_record) + "' or Section = '" + str(lookup_record) + "' or Time_in = '" + str(lookup_record) + "' or Time_out = '" + str(lookup_record) + "' or _Date = '" + str(lookup_record) + "' or Status = '" + str(lookup_record) + "' or Late = '" + str(lookup_record) + "' or Early_Dismissal = '" + str(lookup_record) + "') AND Department='Psychology'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]), tag="evenrow")
            else:
                data_table_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]), tag="oddrow")
            count += 1
            data_table_psyc.tag_configure('evenrow', background='#EEEEEE')
            data_table_psyc.tag_configure('oddrow', background='#EEEEEE')
            search_psyc.delete(0, END)

        conn.commit()
        conn.close()
    def print_psyc():
            file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

            cols = ['Name','Department','Day','Subject','Room','Section','Time in','Time out','Date','Remarks','Late','Early Dismissal']
            path = 'excelfile/read_data_employee_psychology.csv'
            excel_name = 'excelfile/new_datasave_psychology.xlsx'
            lst = []
            with open(path,"w",newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=',')
                for row_id in data_table_psyc.get_children():
                    row = data_table_psyc.item(row_id,'values')
                    lst.append(row)
                lst = list(map(list,lst))
                lst.insert(0,cols)
                for row in lst:
                    csvwriter.writerow(row)

            writer = pd.ExcelWriter(excel_name)
            df = pd.read_csv(path)
            df.to_excel(writer,'sheet1', startrow = 3, index = False)
            
            workbook = writer.book
            worksheet = writer.sheets['sheet1']
            worksheet.write(0,0,'Departmet:_Psychology_ ', workbook.add_format({'bold': True}))
            worksheet.write(1,0,'Name:________________ ', workbook.add_format({'bold': True}))
            worksheet.write(1,3,'Employee No:________________ ', workbook.add_format({'bold': True}))

            writer.save()
            source = "excelfile/new_datasave_psychology.xlsx"
            if file:
                shutil.copy(source,file)
                conn = sqlite3.connect("data/data.db")
                cursor = conn.cursor()

                currentDateTime = datetime.datetime.now()

                cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    activity_log(
                                "ID"    INTEGER,
                                "Name"  TEXT,
                                "Activity"  TEXT,
                                "Department"    TEXT,
                                "Date_Time" TIMESTAMP,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                                )""")

                eName = pg4_lb_name.cget("text")
                eDepartment = pg4_lb_dept.cget("text")

                insetdata = str(eName),'Print',str(eDepartment),currentDateTime
                cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                    VAlUES(?,?,?,?)""", insetdata)
                conn.commit()
                conn.close()
                refreshTable_log()
                
            else:
                messagebox.showinfo("Message", "You did not save the file!!")

         # Data Table "TreeView"
    scrollbarx_psyc = Scrollbar(psychology_att_record, orient=HORIZONTAL)
    scrollbarx_psyc.place(x=710, y=584, width=347)
    scrollbary_psyc = Scrollbar(psychology_att_record, orient=VERTICAL)
    scrollbary_psyc.place(x=1040, y=366, height=219)

    # style = ttk.Style()
    # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table_psyc = ttk.Treeview(psychology_att_record)
    data_table_psyc.place(x=710, y=366, width=330, height=219)
    data_table_psyc.configure(yscrollcommand=scrollbary_psyc.set, xscrollcommand=scrollbarx_psyc.set)

    scrollbarx_psyc.configure(command=data_table_psyc.xview)
    scrollbary_psyc.configure(command=data_table_psyc.yview)

    data_table_psyc['columns'] = ("Name","Department","Day","Subject","Room","Section","Time in","Time out","Date","Remarks","Late","Early Dismissal")
    # Format Columns
    data_table_psyc.column("#0", width=0, stretch=NO)
    data_table_psyc.column("Name", anchor=W, width=100)
    data_table_psyc.column("Department", anchor=W, width=200)
    data_table_psyc.column("Day", anchor=W, width=100)
    data_table_psyc.column("Subject", anchor=W, width=100)
    data_table_psyc.column("Room", anchor=W, width=100)
    data_table_psyc.column("Section", anchor=W, width=100)
    data_table_psyc.column("Time in", anchor=W, width=100)
    data_table_psyc.column("Time out", anchor=W, width=100)
    data_table_psyc.column("Date", anchor=W, width=100)
    data_table_psyc.column("Remarks", anchor=W, width=100)
    data_table_psyc.column("Late", anchor=W, width=100)
    data_table_psyc.column("Early Dismissal", anchor=W, width=100)

    # Create Headings
    data_table_psyc.heading("Name", text="Name", anchor=CENTER)
    data_table_psyc.heading("Department", text="Department", anchor=CENTER)
    data_table_psyc.heading("Day", text="Day", anchor=CENTER)
    data_table_psyc.heading("Subject", text="Subject", anchor=CENTER)
    data_table_psyc.heading("Room", text="Room", anchor=CENTER)
    data_table_psyc.heading("Section", text="Section", anchor=CENTER)
    data_table_psyc.heading("Time in", text="Time in", anchor=CENTER)
    data_table_psyc.heading("Time out", text="Time out", anchor=CENTER)
    data_table_psyc.heading("Date", text="Date", anchor=CENTER)
    data_table_psyc.heading("Remarks", text="Remarks", anchor=CENTER)
    data_table_psyc.heading("Late", text="Late", anchor=CENTER)
    data_table_psyc.heading("Early Dismissal", text="Early Dismissal", anchor=CENTER)

    # data_table_psyc.bind("<ButtonRelease-1>", select_row_psyc)

    refreshTable_psyc()

    def select_row_psyc(e):
        selected = data_table_psyc_IR.focus()
        values = data_table_psyc_IR.item(selected, 'values')

        if values:
            employee_num_psyc.configure(state='normal')
            employee_name_psyc.configure(state='normal')

            employee_num_psyc.delete(0, END)
            employee_name_psyc.delete(0, END)

            employee_num_psyc.insert(0, values[0])
            employee_name_psyc.insert(0, values[1])
            
            employee_num_psyc.configure(state='disabled')
            employee_name_psyc.configure(state='disabled')
        else:
            messagebox.showinfo("Error", "There is no  selected data on the table !!")
        

    def psyc_read_IR():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            attendance_record(ID INTEGER PRIMARY KEY,Employee_No INTEGER,Name TEXT,
            Department TEXT,Time_in TEXT,Time_out TEXT,_Date TEXT,Status TEXT)""")

        cursor.execute("SELECT Employee_No,Name FROM attendance_record WHERE Department='Psychology'")
        results_psyc_IR = cursor.fetchall()
        conn.commit()
        return results_psyc_IR

        # Refresh the tabble on Treeview
    def refreshTable_psyc_IR():
        for data_psyc in data_table_psyc_IR.get_children():
            data_table_psyc_IR.delete(data_psyc)

        for results_psyc_rec_IR in reverse(psyc_read_IR()):
            data_table_psyc_IR.insert(parent='', index='end', iid=results_psyc_rec_IR, text="", values=(results_psyc_rec_IR), tag="orow")
        data_table_psyc_IR.tag_configure('orow', background='#EEEEEE')

    def search_data_psyc_IR():
        lookup_record = search_psyc_IR.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for record in data_table_psyc_IR.get_children():
            data_table_psyc_IR.delete(record)
        
        cursor.execute("SELECT Employee_No,Name FROM attendance_record WHERE Employee_No = '" + str(lookup_record) + "' AND Department='Psychology'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_psyc_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="evenrow")
            else:
                data_table_psyc_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="oddrow")
            count += 1
            data_table_psyc_IR.tag_configure('evenrow', background='#EEEEEE')
            data_table_psyc_IR.tag_configure('oddrow', background='#EEEEEE')
            search_psyc_IR.delete(0, END)

        conn.commit()
        conn.close()

         # Data Table "TreeView"
    scrollbary_psyc_IR = Scrollbar(psychology_att_record, orient=VERTICAL)
    scrollbary_psyc_IR.place(x=645, y=366, height=219)

    # style = ttk.Style()
    # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table_psyc_IR = ttk.Treeview(psychology_att_record)
    data_table_psyc_IR.place(x=315, y=366, width=330, height=219)
    data_table_psyc_IR.configure(yscrollcommand=scrollbary_psyc_IR.set)

    scrollbary_psyc_IR.configure(command=data_table_psyc_IR.yview)

    data_table_psyc_IR['columns'] = ("Employee No.","Name")
    # Format Columns
    data_table_psyc_IR.column("#0", width=0, stretch=NO)
    data_table_psyc_IR.column("Employee No.", anchor=W, width=50)
    data_table_psyc_IR.column("Name", anchor=W, width=100)

    # Create Headings
    data_table_psyc_IR.heading("Employee No.", text="Employee No.", anchor=CENTER)
    data_table_psyc_IR.heading("Name", text="Name", anchor=CENTER)

    data_table_psyc_IR.bind("<ButtonRelease-1>", select_row_psyc)

    refreshTable_psyc_IR()

        # Time Text
    time_lb = Label(psychology_att_record, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    time_lb.place(x=540, y=10)

        # date Text
    date_lb = Label(psychology_att_record, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    date_lb.place(x=710, y=10)

        # Time Label
    time_lb_psyc = Label(psychology_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    time_lb_psyc.place(x=590, y=10)

        # date Label
    date_lb_psyc = Label(psychology_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    date_lb_psyc.place(x=760, y=10)

        # Total Faculty Label
    total_faculty_lb_psyc = Label(psychology_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_faculty_lb_psyc.place(x=347, y=190)

        # Total Present Label
    total_present_lb_psyc = Label(psychology_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_present_lb_psyc.place(x=565, y=190)

        # Total Absent Label
    total_absent_lb_psyc = Label(psychology_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_absent_lb_psyc.place(x=772, y=190)

        # Total Late Label
    total_late_lb_psyc = Label(psychology_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_late_lb_psyc.place(x=990, y=190)

    def error_psyc():
        emp_num = employee_num_psyc.get()
        emp_name = employee_name_psyc.get()

        if emp_num == "" or emp_name == "":
            messagebox.showinfo("Error", "Please Seleted a row on the table to open Summary Report !!")
        else:
            summary_psyc()

        # Entry Employee Number
    employee_num_psyc = Entry(psychology_att_record)
    employee_num_psyc.place(x=315, y=586, width=100)

        # Entry Employee Name
    employee_name_psyc = Entry(psychology_att_record)
    employee_name_psyc.place(x=425, y=586, width=100)
    
        # Summary Report Button 
    psyc_button_report = customtkinter.CTkButton(master=psychology_att_record, text="Summary Report",
                                                corner_radius=3,bg='#ffffff', fg_color="#C0C0C0",hover_color="#006699", command=error_psyc)
    psyc_button_report.place(x=550, y=586, height=21,width=110)

         # Search Entry Individual Report
    search_ent_psyc_IR = StringVar()
    search_psyc_IR = Entry(psychology_att_record, textvariable = search_ent_psyc_IR)
    search_psyc_IR.place(x=385, y=305, width=190)

        # Search Button Individual Report
    search_btn_psyc_IR = PhotoImage(file = "pic/btn_search_small.png")
    psyc_button_search_IR = customtkinter.CTkButton(master=psychology_att_record,image=search_btn_psyc_IR, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_psyc_IR)
    psyc_button_search_IR.place(x=590, y=307, height=17,width=70)

        # Show All Button Individual Report
    showall_btn_psyc_IR = PhotoImage(file = "pic/btn_showall_small.png")
    psyc_button_showall_IR = customtkinter.CTkButton(master=psychology_att_record,image=showall_btn_psyc_IR, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_psyc_IR)
    psyc_button_showall_IR.place(x=445, y=608, height=21,width=90)

        # Search Entry
    search_ent_psyc = StringVar()
    search_psyc = Entry(psychology_att_record, textvariable = search_ent_psyc)
    search_psyc.place(x=780, y=307, width=190)

        # Search Button
    search_btn_psyc = PhotoImage(file = "pic/btn_search_small.png")
    psyc_button_search = customtkinter.CTkButton(master=psychology_att_record,image=search_btn_psyc, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command= search_data_psyc)
    psyc_button_search.place(x=975, y=307, height=17,width=70)

        # Show All Button
    showall_btn_psyc = PhotoImage(file = "pic/btn_showall_small.png")
    psyc_button_showall = customtkinter.CTkButton(master=psychology_att_record,image=showall_btn_psyc, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command= refreshTable_psyc)
    psyc_button_showall.place(x=885, y=608, height=21,width=90)

        # Print Button
    print_btn_psyc = PhotoImage(file = "pic/btn_print.png")
    psyc_button_print = customtkinter.CTkButton(master=psychology_att_record,image=print_btn_psyc, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_psyc)
    psyc_button_print.place(x=785, y=608, height=20,width=80)

        # Back Button
    psyc_back = PhotoImage(file = "pic/btn_back_page.png")
    psyc_button_back = customtkinter.CTkButton(master=psychology_att_record,image=psyc_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(attendance_record))
    psyc_button_back.place(x=45, y=595, height=50,width=140)

    time_psyc()
    count_data_psyc()
    # ============= Summary Report ========================================================================================================================

    def summary_applied():
        popupwindow_applied = Toplevel(main_window)
        popupwindow_applied.title("Individual Summary Report")
        popupwindow_applied.geometry('1020x650')
        popupwindow_applied.grab_set()
        popupwindow_applied.resizable(False,False)

            # open background image
        popupwindow_applied.summary_image = Image.open('pic/16.png')
        popupwindow_applied.summary_resize_image = popupwindow_applied.summary_image.resize((1020,650))
        popupwindow_applied.photo = ImageTk.PhotoImage(popupwindow_applied.summary_resize_image)
        popupwindow_applied.summary_bg_img_lb = Label(popupwindow_applied, image = popupwindow_applied.photo)
        popupwindow_applied.summary_bg_img_lb.pack()

        emp_num = employee_num_applied.get()
        emp_name = employee_name_applied.get()

             # Get Current Time and Date
        def time_report():
            string_time = strftime('%I:%M:%S %p')
            time_lb_summary_applied.configure(text = string_time)
            time_lb_summary_applied.after(1000, time_report)

            string_date = strftime('%d-%m-20%y')
            date_lb_summary_applied.configure(text = string_date)

        def display_info():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT Department FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            dept = cursor.fetchone()

            cursor.execute("SELECT Status FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            st = cursor.fetchone()

            cursor.execute("SELECT Time_in FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            Tmin = cursor.fetchone()

            cursor.execute("SELECT Time_out FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            Tmout = cursor.fetchone()

            cursor.execute("SELECT _Date FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            dt = cursor.fetchone()

            summary_department_combobox_applied.configure(state='normal')
            employee_num_summary_applied.configure(state='normal')
            employee_name_summary_applied.configure(state='normal')
            att_status_summary_applied.configure(state='normal')
            time_in_summary_applied.configure(state='normal')
            time_out_summary_applied.configure(state='normal')
            date_summary_applied.configure(state='normal')

            summary_department_combobox_applied.insert(0,dept)
            employee_num_summary_applied.insert(0,emp_num)
            employee_name_summary_applied.insert(0,emp_name)
            att_status_summary_applied.insert(0,st)
            time_in_summary_applied.insert(0,Tmin)
            time_out_summary_applied.insert(0,Tmout)
            date_summary_applied.insert(0,dt)

            summary_department_combobox_applied.configure(state='disabled')
            employee_num_summary_applied.configure(state='disabled')
            employee_name_summary_applied.configure(state='disabled')
            att_status_summary_applied.configure(state='disabled')
            time_in_summary_applied.configure(state='disabled')
            time_out_summary_applied.configure(state='disabled')
            date_summary_applied.configure(state='disabled')

            conn.commit()
            conn.close()

        def count_data_report():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            date_physics = date_lb_summary_applied.cget("text")

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE  Department='Applied Physics' AND Status='Present' AND _Date='"+ str(date_physics) +"'")
            present_math = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE  Department='Applied Physics' AND Status='Late' AND _Date='"+ str(date_physics) +"'")
            late_math = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Applied Physics' AND Status='Absent' AND _Date='"+ str(date_physics) +"'")
            absent_math = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Applied Physics' AND Status='Early Dismissal' AND _Date='"+ str(date_physics) +"'")
            earldis_math = cursor.fetchall()

            total_present_lb_summary_applied.configure(text=present_math)
            total_late_lb_summary_applied.configure(text=late_math)
            total_absent_lb_summary_applied.configure(text=absent_math)
            total_earldis_lb_summary_applied.configure(text=earldis_math)

            conn.commit()
            conn.close()

        def applied_read_report():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            results_report = cursor.fetchall()
            conn.commit()
            return results_report

        def refreshTable_applied_report():
            for data_report in data_table_summary_applied.get_children():
                data_table_summary_applied.delete(data_report)

            for results_report in reverse(applied_read_report()):
                data_table_summary_applied.insert(parent='', index='end', iid=results_report, text="", values=(results_report), tag="orow")
            data_table_summary_applied.tag_configure('orow', background='#EEEEEE')

        def search_present():
            date_physics = date_lb_summary_applied.cget("text")
            employee_num_summary_applied.configure(state='normal')
            emplno = employee_num_summary_applied.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_applied.get_children():
                data_table_summary_applied.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Applied Physics' AND Status='Present' AND _Date='"+ str(date_physics) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_applied.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_applied.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary_applied.configure(state='disabled')
                summary_button_print1_applied.configure(state='disabled')
            summary_button_print1_applied.configure(state='disabled')
            employee_num_summary_applied.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_late():
            date_physics = date_lb_summary_applied.cget("text")
            employee_num_summary_applied.configure(state='normal')
            emplno = employee_num_summary_applied.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_applied.get_children():
                data_table_summary_applied.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Applied Physics' AND Status='Late' AND _Date='"+ str(date_physics) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_applied.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_applied.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary_applied.configure(state='disabled')
                summary_button_print1_applied.configure(state='disabled')
            summary_button_print1_applied.configure(state='disabled')
            employee_num_summary_applied.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_absent():
            date_physics = date_lb_summary_applied.cget("text")
            employee_num_summary_applied.configure(state='normal')
            emplno = employee_num_summary_applied.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_applied.get_children():
                data_table_summary_applied.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Applied Physics' AND Status='Absent' AND _Date='"+ str(date_physics) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_applied.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_applied.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary_applied.configure(state='disabled')
                summary_button_print1_applied.configure(state='disabled')
            summary_button_print1_applied.configure(state='disabled')
            employee_num_summary_applied.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_earlydismissal():
            date_physics= date_lb_summary_applied.cget("text")
            employee_num_summary_applied.configure(state='normal')
            emplno = employee_num_summary_applied.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_applied.get_children():
                data_table_summary_applied.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Applied Physics' AND Status='Early Dismissal' AND _Date='"+ str(date_physics) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_applied.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_applied.tag_configure('oddrow', background='#EEEEEE')
                employee_num_summary_applied.configure(state='disabled')
                summary_button_print1_applied.configure(state='disabled')
            summary_button_print1_applied.configure(state='disabled')
            employee_num_summary_applied.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_date_applied():
            date_physics= dtr_summary_applied.get()
            employee_num_summary_applied.configure(state='normal')
            emplno = employee_num_summary_applied.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_applied.get_children():
                data_table_summary_applied.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emplno) +"' AND Department='Applied Physics' AND _Date='"+ str(date_physics) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_applied.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_applied.tag_configure('oddrow', background='#EEEEEE')
                dtr_summary_applied.delete(0,END)
                employee_num_summary_applied.configure(state='disabled')
                summary_button_print1_applied.configure(state='normal')
            employee_num_summary_applied.configure(state='disabled')

            conn.commit()
            conn.close()

        def print_data_applied():
            summary_department_combobox_applied.configure(state='normal')
            employee_name_summary_applied.configure(state='normal')
            employee_num_summary_applied.configure(state='normal')

            dep = summary_department_combobox_applied.get()
            name = employee_name_summary_applied.get()
            num = employee_num_summary_applied.get()

            file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

            cols = ['Date','Time in','Time out','Late','Early Dismissal']
            path = 'excelfile/read_data_employee_appliedphysics.csv'
            excel_name = 'excelfile/new_datasave_appliedphysics.xlsx'
            lst = []
            with open(path,"w",newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=',')
                for row_id in data_table_summary_applied.get_children():
                    row = data_table_summary_applied.item(row_id,'values')
                    lst.append(row)
                lst = list(map(list,lst))
                lst.insert(0,cols)
                for row in lst:
                    csvwriter.writerow(row)

            writer = pd.ExcelWriter(excel_name)
            df = pd.read_csv(path)
            df.to_excel(writer,'sheet1', startrow = 3, index = False)
            
            workbook = writer.book
            worksheet = writer.sheets['sheet1']
            worksheet.write(0,0,'Departmet:  ' + dep, workbook.add_format({'bold': True}))
            worksheet.write(1,0,'Name:  ' + name, workbook.add_format({'bold': True}))
            worksheet.write(1,3,'Employee No:  ' + num, workbook.add_format({'bold': True}))

            writer.save()
            source = "excelfile/new_datasave_appliedphysics.xlsx"
            if file:
                shutil.copy(source,file)
                conn = sqlite3.connect("data/data.db")
                cursor = conn.cursor()

                currentDateTime = datetime.datetime.now()

                cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    activity_log(
                                "ID"    INTEGER,
                                "Name"  TEXT,
                                "Activity"  TEXT,
                                "Department"    TEXT,
                                "Date_Time" TIMESTAMP,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                                )""")

                eName = pg4_lb_name.cget("text")
                eDepartment = pg4_lb_dept.cget("text")

                insetdata = str(eName),'Print',str(eDepartment),currentDateTime
                cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                    VAlUES(?,?,?,?)""", insetdata)
                conn.commit()
                conn.close()
                refreshTable_log()
                summary_button_print1_applied.configure(state='disabled')
            else:
                messagebox.showinfo("Message", "You did not save the file!!")

            summary_department_combobox_applied.configure(state='disabled')
            employee_name_summary_applied.configure(state='disabled')
            employee_num_summary_applied.configure(state='disabled')

                 # Data Table "TreeView"
        scrollbarx_summary_applied = Scrollbar(popupwindow_applied, orient=HORIZONTAL)
        scrollbarx_summary_applied.place(x=500, y=584, width=367)
        scrollbary_summary_applied = Scrollbar(popupwindow_applied, orient=VERTICAL)
        scrollbary_summary_applied.place(x=869, y=225, height=358)

        # style = ttk.Style()
        # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

        data_table_summary_applied = ttk.Treeview(popupwindow_applied)
        data_table_summary_applied.place(x=500, y=225, width=368, height=358)
        data_table_summary_applied.configure(yscrollcommand=scrollbary_summary_applied.set, xscrollcommand=scrollbarx_summary_applied.set)

        scrollbarx_summary_applied.configure(command=data_table_summary_applied.xview)
        scrollbary_summary_applied.configure(command=data_table_summary_applied.yview)

        data_table_summary_applied['columns'] = ("Date","Time in","Time out","Late","Early Dismissal")
        # Format Columns
        data_table_summary_applied.column("#0", width=0, stretch=NO)
        data_table_summary_applied.column("Date", anchor=W, width=100)
        data_table_summary_applied.column("Time in", anchor=W, width=100)
        data_table_summary_applied.column("Time out", anchor=W, width=100)
        data_table_summary_applied.column("Late", anchor=W, width=100)
        data_table_summary_applied.column("Early Dismissal", anchor=W, width=100)

        # Create Headings
        data_table_summary_applied.heading("Date", text="Date", anchor=CENTER)
        data_table_summary_applied.heading("Time in", text="Time in", anchor=CENTER)
        data_table_summary_applied.heading("Time out", text="Time out", anchor=CENTER)
        data_table_summary_applied.heading("Late", text="Late", anchor=CENTER)
        data_table_summary_applied.heading("Early Dismissal", text="Early Dismissal", anchor=CENTER)

        refreshTable_applied_report()

                # Time Text
        time_lb = Label(popupwindow_applied, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        time_lb.place(x=360, y=10)

            # date Text
        date_lb = Label(popupwindow_applied, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        date_lb.place(x=530, y=10)

            # Time Label
        time_lb_summary_applied = Label(popupwindow_applied, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        time_lb_summary_applied.place(x=410, y=10)

            # date Label
        date_lb_summary_applied = Label(popupwindow_applied, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        date_lb_summary_applied.place(x=580, y=10)

            # ComboBox College Department
        summary_department_combobox_applied = ttk.Combobox(popupwindow_applied, state='disabled', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
        summary_department_combobox_applied.place(x=253, y=245, width=175)

            # Entry Employee Number
        employee_num_summary_applied = Entry(popupwindow_applied, state='disabled')
        employee_num_summary_applied.place(x=240, y=308, width=80)

            # Entry Employee Name
        employee_name_summary_applied = Entry(popupwindow_applied, state='disabled')
        employee_name_summary_applied.place(x=240, y=330, width=80)

            # Entry Attendance Satatus
        att_status_summary_applied = Entry(popupwindow_applied, state='disabled')
        att_status_summary_applied.place(x=240, y=352, width=80)

            # Entry Time In
        time_in_summary_applied = Entry(popupwindow_applied, state='disabled')
        time_in_summary_applied.place(x=370, y=308, width=80)

            # Entry Time Out
        time_out_summary_applied = Entry(popupwindow_applied, state='disabled')
        time_out_summary_applied.place(x=370, y=330, width=80)

            # Entry Date
        date_summary_applied = Entry(popupwindow_applied, state='disabled')
        date_summary_applied.place(x=370, y=352, width=80)

           # Entry dtr
        dtr_summary_applied = Entry(popupwindow_applied)
        dtr_summary_applied.place(x=152, y=470, width=80)

            # Button Present
        present_btn_summary_applied = PhotoImage(file = "pic/btn_present.png")
        summary_button_present_applied = customtkinter.CTkButton(master=popupwindow_applied,image=present_btn_summary_applied, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_present)
        summary_button_present_applied.place(x=175, y=103, height=78,width=150)

            # Button Late
        late_btn_summary_applied = PhotoImage(file = "pic/btn_late.png")
        summary_button_late_applied = customtkinter.CTkButton(master=popupwindow_applied,image=late_btn_summary_applied, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_late)
        summary_button_late_applied.place(x=355, y=103, height=78,width=150)

            # Button Absent
        absent_btn_summary_applied = PhotoImage(file = "pic/btn_absent.png")
        summary_button_absent_applied = customtkinter.CTkButton(master=popupwindow_applied,image=absent_btn_summary_applied, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_absent)
        summary_button_absent_applied.place(x=525, y=103, height=78,width=150)

            # Button Early Dismisal
        ed_btn_summary_applied = PhotoImage(file = "pic/btn_early_dis.png")
        summary_button_ed_applied = customtkinter.CTkButton(master=popupwindow_applied,image=ed_btn_summary_applied, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_earlydismissal)
        summary_button_ed_applied.place(x=705, y=103, height=78,width=150)

            # Total Present Label
        total_present_lb_summary_applied = Label(popupwindow_applied, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_present_lb_summary_applied.place(x=225, y=136)

            # Total Late Label
        total_late_lb_summary_applied = Label(popupwindow_applied, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_late_lb_summary_applied.place(x=405, y=136)

            # Total Absent Label
        total_absent_lb_summary_applied = Label(popupwindow_applied, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_absent_lb_summary_applied.place(x=575, y=136)

            # Total Early Dismisal Label
        total_earldis_lb_summary_applied = Label(popupwindow_applied, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_earldis_lb_summary_applied.place(x=755, y=136)

            # Print Button
        print_btn_summary_applied = PhotoImage(file = "pic/btn_print.png")
        summary_button_print_applied = customtkinter.CTkButton(master=popupwindow_applied,image=print_btn_summary_applied, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_data_applied)
        summary_button_print_applied.place(x=258, y=375, height=20,width=80)

            # Generate Button
        generate_btn_summary_applied = PhotoImage(file = "pic/btn_generate.png")
        summary_button_generate_applied = customtkinter.CTkButton(master=popupwindow_applied,image=generate_btn_summary_applied, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=search_date_applied)
        summary_button_generate_applied.place(x=258, y=468, height=20,width=80)

            # Print Button
        summary_button_print1_applied = customtkinter.CTkButton(master=popupwindow_applied,state='disabled',image=print_btn_summary_applied, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_data_applied)
        summary_button_print1_applied.place(x=358, y=468, height=20,width=80)

            # Show All Button
        showall_btn_summary_applied = PhotoImage(file = "pic/btn_showall_small.png")
        summary_button_showall_applied = customtkinter.CTkButton(master=popupwindow_applied,image=showall_btn_summary_applied, text="" ,
                                                    corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_applied_report)
        summary_button_showall_applied.place(x=650, y=598, height=20,width=90)

        display_info()
        time_report()
        count_data_report()

    # ============= Applied Physics Attendance Record Frame =============================================================================

        # open background image
    applied_physics_att_record.applied_image = Image.open('pic/18.png')
    applied_physics_att_record.applied_resize_image = applied_physics_att_record.applied_image.resize((1362, 692))
    applied_physics_att_record.photo = ImageTk.PhotoImage(applied_physics_att_record.applied_resize_image)
    applied_physics_att_record.applied_bg_img_lb = Label(applied_physics_att_record, image = applied_physics_att_record.photo)
    applied_physics_att_record.applied_bg_img_lb.pack()

        #  Get Current Time and Date
    def time_applied():
        string_time_applied = strftime('%I:%M:%S %p')
        time_lb_applied.configure(text = string_time_applied)
        time_lb_applied.after(1000, time_applied)

        string_date_applied = strftime('%d-%m-20%y')
        date_lb_applied.configure(text = string_date_applied)

            # Get And Disply the data in the table
    def applied_read():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            attendance_record(
                            "ID" INTEGER,
                            "Employee_No" TEXT,
                            "Name"  TEXT,
                            "Department" TEXT,
                            "Day" TEXT,
                            "Subject" TEXT,
                            "Room" TEXT,
                            "Section" TEXT,
                            "Time_in" TEXT,
                            "Time_out" TEXT,
                            "_Date" TEXT,
                            "Status" TEXT,
                            "Late" TEXT,
                            "Early_Dismissal" TEXT,
                            PRIMARY KEY("ID" AUTOINCREMENT))""")

        cursor.execute("SELECT Name,Department,Day,Subject,Room,Section,Time_in,Time_out,_Date,Status,Late,Early_Dismissal FROM attendance_record WHERE Department='Applied Physics'")
        results_applied = cursor.fetchall()
        conn.commit()
        return results_applied

        # Refresh the tabble on Treeview
    def refreshTable_applied():
        for data_applied in data_table_applied.get_children():
            data_table_applied.delete(data_applied)

        for results_applied_rec in reverse(applied_read()):
            data_table_applied.insert(parent='', index='end', iid=results_applied_rec, text="", values=(results_applied_rec), tag="orow")
        data_table_applied.tag_configure('orow', background='#EEEEEE')

            # GET the Count of Total Faculty, Total Present, Total Late and Total Absent
    def count_data_applied():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        date_physics = date_lb_applied.cget("text")

        cursor.execute("SELECT COUNT(*) FROM faculty_data WHERE Position='Employee'")
        total_physics = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE  Department='Applied Physics' AND Status='Present' AND _Date='"+ str(date_physics) +"'")
        present_physics = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Applied Physics' AND Status='Absent' AND _Date='"+ str(date_physics) +"'")
        absent_physics = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='Applied Physics' AND Status='Late' AND _Date='"+ str(date_physics) +"'")
        late_physics = cursor.fetchall()

        total_faculty_lb_applied.configure(text=total_physics)
        total_present_lb_applied.configure(text=present_physics)
        total_absent_lb_applied.configure(text=absent_physics)
        total_late_lb_applied.configure(text=late_physics)

        conn.commit()
        conn.close()

    def search_data_applied():
        lookup_record = search_applied.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for record in data_table_applied.get_children():
            data_table_applied.delete(record)
        
        cursor.execute("SELECT Name,Department,Day,Subject,Room,Section,Time_in,Time_out,_Date,Status,Late,Early_Dismissal FROM attendance_record WHERE (Name = '" + str(lookup_record) + "' or Day = '" + str(lookup_record) + "' or Subject = '" + str(lookup_record) + "' or Room = '" + str(lookup_record) + "' or Section = '" + str(lookup_record) + "' or Time_in = '" + str(lookup_record) + "' or Time_out = '" + str(lookup_record) + "' or _Date = '" + str(lookup_record) + "' or Status = '" + str(lookup_record) + "' or Late = '" + str(lookup_record) + "' or Early_Dismissal = '" + str(lookup_record) + "') AND Department='Applied Physics'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]), tag="evenrow")
            else:
                data_table_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]), tag="oddrow")
            count += 1
            data_table_applied.tag_configure('evenrow', background='#EEEEEE')
            data_table_applied.tag_configure('oddrow', background='#EEEEEE')
            search_applied.delete(0, END)

        conn.commit()
        conn.close()

    def print_applied():
            file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

            cols =  ['Name','Department','Day','Subject','Room','Section','Time in','Time out','Date','Remarks','Late','Early Dismissal']
            path = 'excelfile/read_data_employee_appliedphysics.csv'
            excel_name = 'excelfile/new_datasave_appliedphysics.xlsx'
            lst = []
            with open(path,"w",newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=',')
                for row_id in data_table_applied.get_children():
                    row = data_table_applied.item(row_id,'values')
                    lst.append(row)
                lst = list(map(list,lst))
                lst.insert(0,cols)
                for row in lst:
                    csvwriter.writerow(row)

            writer = pd.ExcelWriter(excel_name)
            df = pd.read_csv(path)
            df.to_excel(writer,'sheet1', startrow = 3, index = False)
            
            workbook = writer.book
            worksheet = writer.sheets['sheet1']
            worksheet.write(0,0,'Departmet:_Applied Physics_ ', workbook.add_format({'bold': True}))
            worksheet.write(1,0,'Name:________________ ', workbook.add_format({'bold': True}))
            worksheet.write(1,3,'Employee No:________________ ', workbook.add_format({'bold': True}))

            writer.save()
            source = "excelfile/new_datasave_appliedphysics.xlsx"
            if file:
                shutil.copy(source,file)
                conn = sqlite3.connect("data/data.db")
                cursor = conn.cursor()

                currentDateTime = datetime.datetime.now()

                cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    activity_log(
                                "ID"    INTEGER,
                                "Name"  TEXT,
                                "Activity"  TEXT,
                                "Department"    TEXT,
                                "Date_Time" TIMESTAMP,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                                )""")

                eName = pg4_lb_name.cget("text")
                eDepartment = pg4_lb_dept.cget("text")

                insetdata = str(eName),'Print',str(eDepartment),currentDateTime
                cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                    VAlUES(?,?,?,?)""", insetdata)
                conn.commit()
                conn.close()
                refreshTable_log()
                
            else:
                messagebox.showinfo("Message", "You did not save the file!!")

         # Data Table "TreeView"
    scrollbarx_applied = Scrollbar(applied_physics_att_record, orient=HORIZONTAL)
    scrollbarx_applied.place(x=710, y=584, width=347)
    scrollbary_applied = Scrollbar(applied_physics_att_record, orient=VERTICAL)
    scrollbary_applied.place(x=1040, y=366, height=219)

    # style = ttk.Style()
    # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table_applied = ttk.Treeview(applied_physics_att_record)
    data_table_applied.place(x=710, y=366, width=330, height=219)
    data_table_applied.configure(yscrollcommand=scrollbary_applied.set, xscrollcommand=scrollbarx_applied.set)

    scrollbarx_applied.configure(command=data_table_applied.xview)
    scrollbary_applied.configure(command=data_table_applied.yview)

    data_table_applied['columns'] = ("Name","Department","Day","Subject","Room","Section","Time in","Time out","Date","Remarks","Late","Early Dismissal")
    # Format Columns
    data_table_applied.column("#0", width=0, stretch=NO)
    data_table_applied.column("Name", anchor=W, width=100)
    data_table_applied.column("Department", anchor=W, width=200)
    data_table_applied.column("Day", anchor=W, width=100)
    data_table_applied.column("Subject", anchor=W, width=100)
    data_table_applied.column("Room", anchor=W, width=100)
    data_table_applied.column("Section", anchor=W, width=100)
    data_table_applied.column("Time in", anchor=W, width=100)
    data_table_applied.column("Time out", anchor=W, width=100)
    data_table_applied .column("Date", anchor=W, width=100)
    data_table_applied.column("Remarks", anchor=W, width=100)
    data_table_applied.column("Late", anchor=W, width=100)
    data_table_applied.column("Early Dismissal", anchor=W, width=100)

    # Create Headings
    data_table_applied.heading("Name", text="Name", anchor=CENTER)
    data_table_applied.heading("Department", text="Department", anchor=CENTER)
    data_table_applied.heading("Day", text="Day", anchor=CENTER)
    data_table_applied.heading("Subject", text="Subject", anchor=CENTER)
    data_table_applied.heading("Room", text="Room", anchor=CENTER)
    data_table_applied.heading("Section", text="Section", anchor=CENTER)
    data_table_applied.heading("Time in", text="Time in", anchor=CENTER)
    data_table_applied.heading("Time out", text="Time out", anchor=CENTER)
    data_table_applied.heading("Date", text="Date", anchor=CENTER)
    data_table_applied.heading("Remarks", text="Remarks", anchor=CENTER)
    data_table_applied.heading("Late", text="Late", anchor=CENTER)
    data_table_applied.heading("Early Dismissal", text="Early Dismissal", anchor=CENTER)

    # data_table_applied.bind("<ButtonRelease-1>", select_row_applied)

    refreshTable_applied()

    def select_row_applied_IR(e):
        selected = data_table_applied_IR.focus()
        values = data_table_applied_IR.item(selected, 'values')

        if values:
            employee_num_applied.configure(state='normal')
            employee_name_applied.configure(state='normal')
            
            employee_num_applied.delete(0, END)
            employee_name_applied.delete(0, END)

            employee_num_applied.insert(0, values[0])
            employee_name_applied.insert(0, values[1])

            employee_num_applied.configure(state='disabled')
            employee_name_applied.configure(state='disabled')
        else:
            messagebox.showinfo("Error", "There is no selected data on the table !!")
        

    def applied_read_IR():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            attendance_record(ID INTEGER PRIMARY KEY,Employee_No INTEGER,Name TEXT,
            Department TEXT,Time_in TEXT,Time_out TEXT,_Date TEXT,Status TEXT)""")

        cursor.execute("SELECT Employee_No,Name FROM attendance_record WHERE Department='Applied Physics'")
        results_applied_IR = cursor.fetchall()
        conn.commit()
        return results_applied_IR

        # Refresh the tabble on Treeview
    def refreshTable_applied_IR():
        for data_applied_IR in data_table_applied_IR.get_children():
            data_table_applied_IR.delete(data_applied_IR)

        for results_applied_rec_IR in reverse(applied_read_IR()):
            data_table_applied_IR.insert(parent='', index='end', iid=results_applied_rec_IR, text="", values=(results_applied_rec_IR), tag="orow")
        data_table_applied_IR.tag_configure('orow', background='#EEEEEE')

    def search_data_applied_IR():
        lookup_record = search_applied_IR.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for record in data_table_applied_IR.get_children():
            data_table_applied_IR.delete(record)
        
        cursor.execute("SELECT Employee_No,Name FROM attendance_record WHERE Employee_No = '" + str(lookup_record) + "' AND Department='Applied Physics'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_applied_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="evenrow")
            else:
                data_table_applied_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="oddrow")
            count += 1
            data_table_applied_IR.tag_configure('evenrow', background='#EEEEEE')
            data_table_applied_IR.tag_configure('oddrow', background='#EEEEEE')
            search_applied_IR.delete(0, END)

        conn.commit()
        conn.close()
 
         # Data Table "TreeView" Individual Report
    scrollbary_applied_IR = Scrollbar(applied_physics_att_record, orient=VERTICAL)
    scrollbary_applied_IR.place(x=645, y=366, height=219)

    # style = ttk.Style()
    # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table_applied_IR = ttk.Treeview(applied_physics_att_record)
    data_table_applied_IR.place(x=315, y=366, width=330, height=219)
    data_table_applied_IR.configure(yscrollcommand=scrollbary_applied_IR.set)

    scrollbary_applied_IR.configure(command=data_table_applied_IR.yview)

    data_table_applied_IR['columns'] = ("Employee No.","Name")
    # Format Columns Individual Report
    data_table_applied_IR.column("#0", width=0, stretch=NO)
    data_table_applied_IR.column("Employee No.", anchor=W, width=50)
    data_table_applied_IR.column("Name", anchor=W, width=100)

    # Create Headings Individual Report
    data_table_applied_IR.heading("Employee No.", text="Employee No.", anchor=CENTER)
    data_table_applied_IR.heading("Name", text="Name", anchor=CENTER)

    data_table_applied_IR.bind("<ButtonRelease-1>", select_row_applied_IR)

    refreshTable_applied_IR()

        # Time Text
    time_lb = Label(applied_physics_att_record, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    time_lb.place(x=540, y=1)

        # date Text
    date_lb = Label(applied_physics_att_record, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    date_lb.place(x=710, y=1)

        # Time Label
    time_lb_applied = Label(applied_physics_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    time_lb_applied.place(x=590, y=1)

        # date Label
    date_lb_applied = Label(applied_physics_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    date_lb_applied.place(x=760, y=1)

        # Total Faculty Label
    total_faculty_lb_applied = Label(applied_physics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_faculty_lb_applied.place(x=347, y=190)

        # Total Present Label
    total_present_lb_applied = Label(applied_physics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_present_lb_applied.place(x=565, y=190)

        # Total Absent Label
    total_absent_lb_applied = Label(applied_physics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_absent_lb_applied.place(x=772, y=190)

        # Total Late Label
    total_late_lb_applied = Label(applied_physics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_late_lb_applied.place(x=990, y=190)

    def error_applied():
        emp_num = employee_num_applied.get()
        emp_name = employee_name_applied.get()

        if emp_num == "" or emp_name == "":
            messagebox.showinfo("Error", "Please Seleted a row on the table to open Summary Report !!")
        else:
            summary_applied()

        # Entry Employee Number
    employee_num_applied = Entry(applied_physics_att_record)
    employee_num_applied.place(x=315, y=586, width=100)

        # Entry Employee Name
    employee_name_applied = Entry(applied_physics_att_record)
    employee_name_applied.place(x=425, y=586, width=100)

        # Summary Report Button 
    applied_button_report = customtkinter.CTkButton(master=applied_physics_att_record, text="Summary Report" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#C0C0C0",hover_color="#006699", command=error_applied)
    applied_button_report.place(x=550, y=586, height=21,width=110)

         # Search Entry Individual Report
    search_ent_applied_IR = StringVar()
    search_applied_IR = Entry(applied_physics_att_record, textvariable = search_ent_applied_IR)
    search_applied_IR.place(x=385, y=305, width=190)

        # Search Button Individual Report
    search_btn_applied_IR = PhotoImage(file = "pic/btn_search_small.png")
    applied_button_search_IR = customtkinter.CTkButton(master=applied_physics_att_record,image=search_btn_applied_IR, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_applied_IR)
    applied_button_search_IR.place(x=590, y=307, height=17,width=70)

        # Show All Button Individual Report
    showall_btn_applied_IR = PhotoImage(file = "pic/btn_showall_small.png")
    applied_button_showall_IR = customtkinter.CTkButton(master=applied_physics_att_record,image=showall_btn_applied_IR, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_applied_IR)
    applied_button_showall_IR.place(x=445, y=608, height=21,width=90)

        # Search Entry
    search_ent_applied = StringVar()
    search_applied = Entry(applied_physics_att_record, textvariable = search_ent_applied)
    search_applied.place(x=780, y=307, width=190)

        # Search Button
    search_btn_applied = PhotoImage(file = "pic/btn_search_small.png")
    applied_button_search = customtkinter.CTkButton(master=applied_physics_att_record,image=search_btn_applied, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_applied)
    applied_button_search.place(x=975, y=307, height=17,width=70)

        # Show All Button
    showall_btn_applied = PhotoImage(file = "pic/btn_showall_small.png")
    applied_button_showall = customtkinter.CTkButton(master=applied_physics_att_record,image=showall_btn_applied, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_applied)
    applied_button_showall.place(x=885, y=608, height=21,width=90)

        # Print Button
    print_btn_applied = PhotoImage(file = "pic/btn_print.png")
    applied_button_print = customtkinter.CTkButton(master=applied_physics_att_record,image=print_btn_applied, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_applied)
    applied_button_print.place(x=785, y=608, height=20,width=80)

        # Back Button
    applied_back = PhotoImage(file = "pic/btn_back_page.png")
    applied_button_back = customtkinter.CTkButton(master=applied_physics_att_record,image=applied_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(attendance_record))
    applied_button_back.place(x=45, y=595, height=50,width=140)

    time_applied()
    count_data_applied()

    # ============= Summary Report In Frame ========================================================================================================================

    def summary_ite():
        popupwindow_ite = Toplevel(main_window)
        popupwindow_ite.title("Individual Summary Report")
        popupwindow_ite.geometry('1020x650')
        popupwindow_ite.grab_set()
        popupwindow_ite.resizable(False,False)

            # open background image
        popupwindow_ite.summary_image = Image.open('pic/16.png')
        popupwindow_ite.summary_resize_image = popupwindow_ite.summary_image.resize((1020,650))
        popupwindow_ite.photo = ImageTk.PhotoImage(popupwindow_ite.summary_resize_image)
        popupwindow_ite.summary_bg_img_lb = Label(popupwindow_ite, image = popupwindow_ite.photo)
        popupwindow_ite.summary_bg_img_lb.pack()

        emp_num = employee_num_ite.get()
        emp_name = employee_name_ite.get()

             # Get Current Time and Date
        def time_report():
            string_time = strftime('%I:%M:%S %p')
            time_lb_summary_ite.configure(text = string_time)
            time_lb_summary_ite.after(1000, time_report)

            string_date = strftime('%d-%m-20%y')
            date_lb_summary_ite.configure(text = string_date)

        def display_info():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT Department FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            dept = cursor.fetchone()

            cursor.execute("SELECT Status FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            st = cursor.fetchone()

            cursor.execute("SELECT Time_in FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            Tmin = cursor.fetchone()

            cursor.execute("SELECT Time_out FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            Tmout = cursor.fetchone()

            cursor.execute("SELECT _Date FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            dt = cursor.fetchone()


            summary_department_combobox_ite.configure(state='normal')
            employee_num_summary_ite.configure(state='normal')
            employee_name_summary_ite.configure(state='normal')
            att_status_summary_ite.configure(state='normal')
            time_in_summary_ite.configure(state='normal')
            time_out_summary_ite.configure(state='normal')
            date_summary_ite.configure(state='normal')

            summary_department_combobox_ite.insert(0,dept)
            employee_num_summary_ite.insert(0,emp_num)
            employee_name_summary_ite.insert(0,emp_name)
            att_status_summary_ite.insert(0,st)
            time_in_summary_ite.insert(0,Tmin)
            time_out_summary_ite.insert(0,Tmout)
            date_summary_ite.insert(0,dt)

            summary_department_combobox_ite.configure(state='disabled')
            employee_num_summary_ite.configure(state='disabled')
            employee_name_summary_ite.configure(state='disabled')
            att_status_summary_ite.configure(state='disabled')
            time_in_summary_ite.configure(state='disabled')
            time_out_summary_ite.configure(state='disabled')
            date_summary_ite.configure(state='disabled')

            conn.commit()
            conn.close()

        def count_data_report():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            date_IT = date_lb_summary_ite.cget("text")

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE  Department='ITE' AND Status='Present' AND _Date='"+ str(date_IT) +"'")
            present_math = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE  Department='ITE' AND Status='Late' AND _Date='"+ str(date_IT) +"'")
            late_math = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='ITE' AND Status='Absent' AND _Date='"+ str(date_IT) +"'")
            absent_math = cursor.fetchall()

            cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='ITE' AND Status='Early Dismissal' AND _Date='"+ str(date_IT) +"'")
            earldis_math = cursor.fetchall()

            total_present_lb_summary_ite.configure(text=present_math)
            total_late_lb_summary_ite.configure(text=late_math)
            total_absent_lb_summary_ite.configure(text=absent_math)
            total_earldis_lb_summary_ite.configure(text=earldis_math)

            conn.commit()
            conn.close()

        def ite_read_report():
            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Employee_No='"+ str(emp_num) +"' AND Name='"+ str(emp_name) +"'")
            results_math_report = cursor.fetchall()
            conn.commit()
            return results_math_report

        def refreshTable_ite_report():
            for data_report in data_table_summary_ite.get_children():
                data_table_summary_ite.delete(data_report)

            for results_report in reverse(ite_read_report()):
                data_table_summary_ite.insert(parent='', index='end', iid=results_report, text="", values=(results_report), tag="orow")
            data_table_summary_ite.tag_configure('orow', background='#EEEEEE')

        def search_present():
            date_IT = date_lb_summary_ite.cget("text")
            employee_name_summary_ite.configure(state='normal')
            sname = employee_name_summary_ite.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_ite.get_children():
                data_table_summary_ite.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Name ='"+ str(sname) +"' AND Department='ITE' AND Status='Present' AND _Date='"+ str(date_IT) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_ite.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_ite.tag_configure('oddrow', background='#EEEEEE')
                employee_name_summary_ite.configure(state='disabled')
                summary_button_print1_ite.configure(state='disabled')
            summary_button_print1_ite.configure(state='disabled')
            employee_name_summary_ite.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_late():
            date_IT = date_lb_summary_ite.cget("text")
            employee_name_summary_ite.configure(state='normal')
            sname = employee_name_summary_ite.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_ite.get_children():
                data_table_summary_ite.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Name ='"+ str(sname) +"' AND Department='ITE' AND Status='Late' AND _Date='"+ str(date_IT) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_ite.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_ite.tag_configure('oddrow', background='#EEEEEE')
                employee_name_summary_ite.configure(state='disabled')
                summary_button_print1_ite.configure(state='disabled')
            summary_button_print1_ite.configure(state='disabled')
            employee_name_summary_ite.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_absent():
            date_IT = date_lb_summary_ite.cget("text")
            employee_name_summary_ite.configure(state='normal')
            sname = employee_name_summary_ite.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_ite.get_children():
                data_table_summary_ite.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Name ='"+ str(sname) +"' AND Department='ITE' AND Status='Absent' AND _Date='"+ str(date_IT) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_ite.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_ite.tag_configure('oddrow', background='#EEEEEE')
                employee_name_summary_ite.configure(state='disabled')
                summary_button_print1_ite.configure(state='disabled')
            summary_button_print1_ite.configure(state='disabled')
            employee_name_summary_ite.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_earlydismissal():
            date_IT = date_lb_summary_ite.cget("text")
            employee_name_summary_ite.configure(state='normal')
            sname = employee_name_summary_ite.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_ite.get_children():
                data_table_summary_ite.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Name ='"+ str(sname) +"' AND Department='ITE' AND Status='Early Dismissal' AND _Date='"+ str(date_IT) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_ite.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_ite.tag_configure('oddrow', background='#EEEEEE')
                employee_name_summary_ite.configure(state='disabled')
                summary_button_print1_ite.configure(state='disabled')
            summary_button_print1_ite.configure(state='disabled')
            employee_name_summary_ite.configure(state='disabled')

            conn.commit()
            conn.close()

        def search_date():
            date_IT = dtr_summary_ite.get()
            employee_name_summary_ite.configure(state='normal')
            sname = employee_name_summary_ite.get()

            conn = sqlite3.connect("data/data.db")
            cursor = conn.cursor()

            # Clear the Treeview
            for record in data_table_summary_ite.get_children():
                data_table_summary_ite.delete(record)
            
            cursor.execute("SELECT _Date,Time_in,Time_out,Late,Early_Dismissal FROM attendance_record WHERE Name ='"+ str(sname) +"' AND Department='ITE' AND _Date='"+ str(date_IT) +"'")
            records = cursor.fetchall()

            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    data_table_summary_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
                else:
                    data_table_summary_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
                count += 1
                data_table_summary_ite.tag_configure('evenrow', background='#EEEEEE')
                data_table_summary_ite.tag_configure('oddrow', background='#EEEEEE')
                dtr_summary_ite.delete(0,END)
                employee_name_summary_ite.configure(state='disabled')
                summary_button_print1_ite.configure(state='normal')
            employee_name_summary_ite.configure(state='disabled')

            conn.commit()
            conn.close()

        def print_data_ite():
            summary_department_combobox_ite.configure(state='normal')
            employee_name_summary_ite.configure(state='normal')
            employee_num_summary_ite.configure(state='normal')

            dep = summary_department_combobox_ite.get()
            name = employee_name_summary_ite.get()
            num =employee_num_summary_ite.get()

            file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

            cols = ['Date','Time in','Time out','Late','Early Dismissal']
            path = 'excelfile/read_data_employee_ite.csv'
            excel_name = 'excelfile/new_datasave_ite.xlsx'
            lst = []
            with open(path,"w",newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=',')
                for row_id in data_table_summary_ite.get_children():
                    row = data_table_summary_ite.item(row_id,'values')
                    lst.append(row)
                lst = list(map(list,lst))
                lst.insert(0,cols)
                for row in lst:
                    csvwriter.writerow(row)

            writer = pd.ExcelWriter(excel_name)
            df = pd.read_csv(path)
            df.to_excel(writer,'sheet1', startrow = 3, index = False)
            
            workbook = writer.book
            worksheet = writer.sheets['sheet1']
            worksheet.write(0,0,'Departmet:  ' + dep, workbook.add_format({'bold': True}))
            worksheet.write(1,0,'Name:  ' + name, workbook.add_format({'bold': True}))
            worksheet.write(1,3,'Employee No:  ' + num, workbook.add_format({'bold': True}))

            writer.save()
            source = "excelfile/new_datasave_ite.xlsx"
            if file:
                shutil.copy(source,file)
                conn = sqlite3.connect("data/data.db")
                cursor = conn.cursor()

                currentDateTime = datetime.datetime.now()

                cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    activity_log(
                                "ID"    INTEGER,
                                "Name"  TEXT,
                                "Activity"  TEXT,
                                "Department"    TEXT,
                                "Date_Time" TIMESTAMP,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                                )""")

                eName = pg4_lb_name.cget("text")
                eDepartment = pg4_lb_dept.cget("text")

                insetdata = str(eName),'Print',str(eDepartment),currentDateTime
                cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                    VAlUES(?,?,?,?)""", insetdata)
                conn.commit()
                conn.close()
                refreshTable_log()
                summary_button_print1_ite.configure(state='disabled')
            else:
                messagebox.showinfo("Message", "You did not save the file!!")

            summary_department_combobox_ite.configure(state='disabled')
            employee_name_summary_ite.configure(state='disabled')
            employee_num_summary_ite.configure(state='disabled')

                 # Data Table "TreeView"
        scrollbarx_summary_ite = Scrollbar(popupwindow_ite, orient=HORIZONTAL)
        scrollbarx_summary_ite.place(x=500, y=584, width=367)
        scrollbary_summary_ite = Scrollbar(popupwindow_ite, orient=VERTICAL)
        scrollbary_summary_ite.place(x=869, y=225, height=358)

        # style = ttk.Style()
        # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

        data_table_summary_ite = ttk.Treeview(popupwindow_ite)
        data_table_summary_ite.place(x=500, y=225, width=368, height=358)
        data_table_summary_ite.configure(yscrollcommand=scrollbary_summary_ite.set, xscrollcommand=scrollbarx_summary_ite.set)

        scrollbarx_summary_ite.configure(command=data_table_summary_ite.xview)
        scrollbary_summary_ite.configure(command=data_table_summary_ite.yview)

        data_table_summary_ite['columns'] = ("Date","Time in","Time out","Late","Early Dismissal")
        # Format Columns
        data_table_summary_ite.column("#0", width=0, stretch=NO)
        data_table_summary_ite.column("Date", anchor=W, width=100)
        data_table_summary_ite.column("Time in", anchor=W, width=100)
        data_table_summary_ite.column("Time out", anchor=W, width=100)
        data_table_summary_ite.column("Late", anchor=W, width=100)
        data_table_summary_ite.column("Early Dismissal", anchor=W, width=100)

        # Create Headings
        data_table_summary_ite.heading("Date", text="Date", anchor=CENTER)
        data_table_summary_ite.heading("Time in", text="Time in", anchor=CENTER)
        data_table_summary_ite.heading("Time out", text="Time out", anchor=CENTER)
        data_table_summary_ite.heading("Late", text="Late", anchor=CENTER)
        data_table_summary_ite.heading("Early Dismissal", text="Early Dismissal", anchor=CENTER)

        refreshTable_ite_report()

                # Time Text
        time_lb = Label(popupwindow_ite, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        time_lb.place(x=360, y=10)

            # date Text
        date_lb = Label(popupwindow_ite, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        date_lb.place(x=530, y=10)

            # Time Label
        time_lb_summary_ite = Label(popupwindow_ite, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        time_lb_summary_ite.place(x=410, y=10)

            # date Label
        date_lb_summary_ite = Label(popupwindow_ite, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
        date_lb_summary_ite.place(x=580, y=10)

            # ComboBox College Department
        summary_department_combobox_ite = ttk.Combobox(popupwindow_ite, state='disabled', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
        summary_department_combobox_ite.place(x=253, y=245, width=175)

            # Entry Employee Number
        employee_num_summary_ite = Entry(popupwindow_ite, state='disabled')
        employee_num_summary_ite.place(x=240, y=308, width=80)

            # Entry Employee Name
        employee_name_summary_ite = Entry(popupwindow_ite, state='disabled')
        employee_name_summary_ite.place(x=240, y=330, width=80)

            # Entry Attendance Satatus
        att_status_summary_ite = Entry(popupwindow_ite, state='disabled')
        att_status_summary_ite.place(x=240, y=352, width=80)

            # Entry Time In
        time_in_summary_ite = Entry(popupwindow_ite, state='disabled')
        time_in_summary_ite.place(x=370, y=308, width=80)

            # Entry Time Out
        time_out_summary_ite = Entry(popupwindow_ite, state='disabled')
        time_out_summary_ite.place(x=370, y=330, width=80)

            # Entry Date
        date_summary_ite = Entry(popupwindow_ite, state='disabled')
        date_summary_ite.place(x=370, y=352, width=80)

           # Entry dtr
        dtr_summary_ite = Entry(popupwindow_ite)
        dtr_summary_ite.place(x=152, y=470, width=80)

            # Button Present
        present_btn_summary_ite = PhotoImage(file = "pic/btn_present.png")
        summary_button_present_ite = customtkinter.CTkButton(master=popupwindow_ite,image=present_btn_summary_ite, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_present)
        summary_button_present_ite.place(x=175, y=103, height=78,width=150)

            # Button Late
        late_btn_summary_ite = PhotoImage(file = "pic/btn_late.png")
        summary_button_late_ite = customtkinter.CTkButton(master=popupwindow_ite,image=late_btn_summary_ite, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_late)
        summary_button_late_ite.place(x=355, y=103, height=78,width=150)

            # Button Absent
        absent_btn_summary_ite = PhotoImage(file = "pic/btn_absent.png")
        summary_button_absent_ite = customtkinter.CTkButton(master=popupwindow_ite,image=absent_btn_summary_ite, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_absent)
        summary_button_absent_ite.place(x=525, y=103, height=78,width=150)

            # Button Early Dismisal
        ed_btn_summary_ite = PhotoImage(file = "pic/btn_early_dis.png")
        summary_button_ed_ite = customtkinter.CTkButton(master=popupwindow_ite,image=ed_btn_summary_ite, text="" ,
                                                    corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_earlydismissal)
        summary_button_ed_ite.place(x=705, y=103, height=78,width=150)

            # Total Present Label
        total_present_lb_summary_ite = Label(popupwindow_ite, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_present_lb_summary_ite.place(x=225, y=136)

            # Total Late Label
        total_late_lb_summary_ite = Label(popupwindow_ite, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_late_lb_summary_ite.place(x=405, y=136)

            # Total Absent Label
        total_absent_lb_summary_ite = Label(popupwindow_ite, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_absent_lb_summary_ite.place(x=575, y=136)

            # Total Early Dismisal Label
        total_earldis_lb_summary_ite = Label(popupwindow_ite, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
        total_earldis_lb_summary_ite.place(x=755, y=136)

            # Print Button
        print_btn_summary_ite = PhotoImage(file = "pic/btn_print.png")
        summary_button_print_ite = customtkinter.CTkButton(master=popupwindow_ite,image=print_btn_summary_ite, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_data_ite)
        summary_button_print_ite.place(x=258, y=375, height=20,width=80)

            # Generate Button
        generate_btn_summary_ite = PhotoImage(file = "pic/btn_generate.png")
        summary_button_generate_ite = customtkinter.CTkButton(master=popupwindow_ite,image=generate_btn_summary_ite, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=search_date)
        summary_button_generate_ite.place(x=258, y=468, height=20,width=80)

            # Print Button
        summary_button_print1_ite = customtkinter.CTkButton(master=popupwindow_ite,state='disabled',image=print_btn_summary_ite, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_data_ite)
        summary_button_print1_ite.place(x=358, y=468, height=20,width=80)

            # Show All Button
        showall_btn_summary_ite = PhotoImage(file = "pic/btn_showall_small.png")
        summary_button_showall_ite = customtkinter.CTkButton(master=popupwindow_ite,image=showall_btn_summary_ite, text="" ,
                                                    corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_ite_report)
        summary_button_showall_ite.place(x=650, y=598, height=20,width=90)

        display_info()
        time_report()
        count_data_report()


    # ============= ITE Attendance Record Frame =============================================================================

        # open background image
    ite_att_record.ite_image = Image.open('pic/20.png')
    ite_att_record.ite_resize_image = ite_att_record.ite_image.resize((1362, 692))
    ite_att_record.photo = ImageTk.PhotoImage(ite_att_record.ite_resize_image)
    ite_att_record.ite_bg_img_lb = Label(ite_att_record, image = ite_att_record.photo)
    ite_att_record.ite_bg_img_lb.pack()

        #  Get Current Time and Date
    def time_ite():
        string_time_ite = strftime('%I:%M:%S %p')
        time_lb_ite.configure(text = string_time_ite)
        time_lb_ite.after(1000, time_ite)

        string_date_ite = strftime('%d-%m-20%y')
        date_lb_ite.configure(text = string_date_ite)

            # Get And Disply the data in the table
    def ite_read():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            attendance_record(
                            "ID" INTEGER,
                            "Employee_No" TEXT,
                            "Name"  TEXT,
                            "Department" TEXT,
                            "Day" TEXT,
                            "Subject" TEXT,
                            "Room" TEXT,
                            "Section" TEXT,
                            "Time_in" TEXT,
                            "Time_out" TEXT,
                            "_Date" TEXT,
                            "Status" TEXT,
                            "Late" TEXT,
                            "Early_Dismissal" TEXT,
                            PRIMARY KEY("ID" AUTOINCREMENT))""")

        cursor.execute("SELECT Name,Department,Day,Subject,Room,Section,Time_in,Time_out,_Date,Status,Late,Early_Dismissal FROM attendance_record WHERE Department='ITE'")
        results_ite = cursor.fetchall()
        conn.commit()
        return results_ite

        # Refresh the tabble on Treeview
    def refreshTable_ite():

        for data_ite in data_table_ite.get_children():
            data_table_ite.delete(data_ite)

        for results_ite_rec in reverse(ite_read()):
            data_table_ite.insert(parent='', index='end', iid=results_ite_rec, text="", values=(results_ite_rec), tag="orow")
        data_table_ite.tag_configure('orow', background='#EEEEEE')

            # GET the Count of Total Faculty, Total Present, Total Late and Total Absent
    def count_data_ite():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        date_IT = date_lb_ite.cget("text")

        cursor.execute("SELECT COUNT(*) FROM faculty_data WHERE Position='Employee'")
        total_IT = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='ITE' AND Status='Present' AND _Date='"+ str(date_IT) +"'")
        present_IT = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='ITE' AND Status='Absent' AND _Date='"+ str(date_IT) +"'")
        absent_IT = cursor.fetchall()

        cursor.execute("SELECT COUNT(Status) FROM attendance_record WHERE Department='ITE' AND Status='Late' AND _Date='"+ str(date_IT) +"'")
        late_IT = cursor.fetchall()

        total_faculty_lb_ite.configure(text=total_IT)
        total_present_lb_ite.configure(text=present_IT)
        total_absent_lb_ite.configure(text=absent_IT)
        total_late_lb_ite.configure(text=late_IT)

        conn.commit()
        conn.close()

    def search_data_ite():
        lookup_record = search_ite.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for record in data_table_ite.get_children():
            data_table_ite.delete(record)
        
        cursor.execute("SELECT Name,Department,Day,Subject,Room,Section,Time_in,Time_out,_Date,Status,Late,Early_Dismissal FROM attendance_record WHERE (Name = '" + str(lookup_record) + "' or Day = '" + str(lookup_record) + "' or Subject = '" + str(lookup_record) + "' or Room = '" + str(lookup_record) + "' or Section = '" + str(lookup_record) + "' or Time_in = '" + str(lookup_record) + "' or Time_out = '" + str(lookup_record) + "' or _Date = '" + str(lookup_record) + "' or Status = '" + str(lookup_record) + "' or Late = '" + str(lookup_record) + "' or Early_Dismissal = '" + str(lookup_record) + "') AND Department='ITE'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]), tag="evenrow")
            else:
                data_table_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]), tag="oddrow")
            count += 1
            data_table_ite.tag_configure('evenrow', background='#EEEEEE')
            data_table_ite.tag_configure('oddrow', background='#EEEEEE')
            search_ite.delete(0, END)

        conn.commit()
        conn.close()

    def print_ite():
            file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

            cols = ['Name','Department','Day','Subject','Room','Section','Time in','Time out','Date','Remarks','Late','Early Dismissal']
            path = 'excelfile/read_data_employee_ite.csv'
            excel_name = 'excelfile/new_datasave_ite.xlsx'
            lst = []
            with open(path,"w",newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=',')
                for row_id in data_table_ite.get_children():
                    row = data_table_ite.item(row_id,'values')
                    lst.append(row)
                lst = list(map(list,lst))
                lst.insert(0,cols)
                for row in lst:
                    csvwriter.writerow(row)

            writer = pd.ExcelWriter(excel_name)
            df = pd.read_csv(path)
            df.to_excel(writer,'sheet1', startrow = 3, index = False)
            
            workbook = writer.book
            worksheet = writer.sheets['sheet1']
            worksheet.write(0,0,'Departmet:_ITE_ ', workbook.add_format({'bold': True}))
            worksheet.write(1,0,'Name:________________ ', workbook.add_format({'bold': True}))
            worksheet.write(1,3,'Employee No:________________ ', workbook.add_format({'bold': True}))

            writer.save()
            source = "excelfile/new_datasave_ite.xlsx"
            if file:
                shutil.copy(source,file)
                conn = sqlite3.connect("data/data.db")
                cursor = conn.cursor()

                currentDateTime = datetime.datetime.now()

                cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    activity_log(
                                "ID"    INTEGER,
                                "Name"  TEXT,
                                "Activity"  TEXT,
                                "Department"    TEXT,
                                "Date_Time" TIMESTAMP,
                                PRIMARY KEY("ID" AUTOINCREMENT)
                                )""")

                eName = pg4_lb_name.cget("text")
                eDepartment = pg4_lb_dept.cget("text")

                insetdata = str(eName),'Print',str(eDepartment),currentDateTime
                cursor.execute("""INSERT INTO activity_log (Name,Activity,Department,Date_Time) 
                                    VAlUES(?,?,?,?)""", insetdata)
                conn.commit()
                conn.close()
                refreshTable_log()
                
            else:
                messagebox.showinfo("Message", "You did not save the file!!")

         # Data Table "TreeView"
    scrollbarx_ite = Scrollbar(ite_att_record, orient=HORIZONTAL)
    scrollbarx_ite.place(x=710, y=584, width=347)
    scrollbary_ite = Scrollbar(ite_att_record, orient=VERTICAL)
    scrollbary_ite.place(x=1040, y=366, height=219)

    # style = ttk.Style()
    # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table_ite = ttk.Treeview(ite_att_record)
    data_table_ite.place(x=710, y=366, width=330, height=219)
    data_table_ite.configure(yscrollcommand=scrollbary_ite.set, xscrollcommand=scrollbarx_ite.set)

    scrollbarx_ite.configure(command=data_table_ite.xview)
    scrollbary_ite.configure(command=data_table_ite.yview)

    data_table_ite['columns'] = ("Name","Department","Day","Subject","Room","Section","Time in","Time out","Date","Remarks","Late","Early Dismissal")
    # Format Columns
    data_table_ite.column("#0", width=0, stretch=NO)
    data_table_ite.column("Name", anchor=W, width=100)
    data_table_ite.column("Department", anchor=W, width=200)
    data_table_ite.column("Day", anchor=W, width=100)
    data_table_ite.column("Subject", anchor=W, width=100)
    data_table_ite.column("Room", anchor=W, width=100)
    data_table_ite.column("Section", anchor=W, width=100)
    data_table_ite.column("Time in", anchor=W, width=100)
    data_table_ite.column("Time out", anchor=W, width=100)
    data_table_ite.column("Date", anchor=W, width=100)
    data_table_ite.column("Remarks", anchor=W, width=100)
    data_table_ite.column("Late", anchor=W, width=100)
    data_table_ite.column("Early Dismissal", anchor=W, width=100)

    # Create Headings
    data_table_ite.heading("Name", text="Name", anchor=CENTER)
    data_table_ite.heading("Department", text="Department", anchor=CENTER)
    data_table_ite.heading("Day", text="Day", anchor=CENTER)
    data_table_ite.heading("Subject", text="Subject", anchor=CENTER)
    data_table_ite.heading("Room", text="Room", anchor=CENTER)
    data_table_ite.heading("Section", text="Section", anchor=CENTER)
    data_table_ite.heading("Time in", text="Time in", anchor=CENTER)
    data_table_ite.heading("Time out", text="Time out", anchor=CENTER)
    data_table_ite.heading("Date", text="Date", anchor=CENTER)
    data_table_ite.heading("Remarks", text="Remarks", anchor=CENTER)
    data_table_ite.heading("Late", text="Late", anchor=CENTER)
    data_table_ite.heading("Early Dismissal", text="Early Dismissal", anchor=CENTER)

    # data_table_ite.bind("<ButtonRelease-1>", select_row_ite)

    refreshTable_ite()

    def select_row_ite_IR(e):
        selected = data_table_ite_IR.focus()
        values = data_table_ite_IR.item(selected, 'values')

        if values:
            employee_num_ite.configure(state='normal')
            employee_name_ite.configure(state='normal')

            employee_num_ite.delete(0, END)
            employee_name_ite.delete(0, END)

            employee_num_ite.insert(0, values[0])
            employee_name_ite.insert(0, values[1])

            employee_num_ite.configure(state='disabled',text='')
            employee_name_ite.configure(state='disabled')

        else:
            messagebox.showinfo("Error", "There is no selected data on the table !!")
        

    def ite_read_IR():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            attendance_record(ID INTEGER PRIMARY KEY,Employee_No INTEGER,Name TEXT,
            Department TEXT,Time_in TEXT,Time_out TEXT,_Date TEXT,Status TEXT)""")

        cursor.execute("SELECT Employee_No,Name FROM attendance_record WHERE Department='ITE'")
        results_ite_IR = cursor.fetchall()
        conn.commit()
        return results_ite_IR

        # Refresh the tabble on Treeview
    def refreshTable_ite_IR():

        for data_ite_IR in data_table_ite_IR.get_children():
            data_table_ite_IR.delete(data_ite_IR)

        for results_ite_rec_IR in reverse(ite_read_IR()):
            data_table_ite_IR.insert(parent='', index='end', iid=results_ite_rec_IR, text="", values=(results_ite_rec_IR), tag="orow")
        data_table_ite_IR.tag_configure('orow', background='#EEEEEE')

    def search_data_ite_IR():
        lookup_record = search_ite_IR.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for record in data_table_ite_IR.get_children():
            data_table_ite_IR.delete(record)
        
        cursor.execute("SELECT Employee_No,Name FROM attendance_record WHERE Employee_No = '" + str(lookup_record) + "' AND Department='ITE'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_ite_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],), tag="evenrow")
            else:
                data_table_ite_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],), tag="oddrow")
            count += 1
            data_table_ite_IR.tag_configure('evenrow', background='#EEEEEE')
            data_table_ite_IR.tag_configure('oddrow', background='#EEEEEE')
            search_ite_IR.delete(0, END)

        conn.commit()
        conn.close()

         # Data Table "TreeView" Individual Report
    # scrollbarx_ite_IR = Scrollbar(ite_att_record, orient=HORIZONTAL)
    # scrollbarx_ite_IR.place(x=710, y=584, width=347)
    scrollbary_ite_IR = Scrollbar(ite_att_record, orient=VERTICAL)
    scrollbary_ite_IR.place(x=645, y=366, height=219)

    # style = ttk.Style()
    # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table_ite_IR = ttk.Treeview(ite_att_record)
    data_table_ite_IR.place(x=315, y=366, width=330, height=219)
    data_table_ite_IR.configure(yscrollcommand=scrollbary_ite_IR.set)

    # scrollbarx_ite_IR.configure(command=data_table_ite.xview)
    scrollbary_ite_IR.configure(command=data_table_ite.yview)

    data_table_ite_IR['columns'] = ("Employee No.","Name",)
    # Format Columns Individual Report
    data_table_ite_IR.column("#0", width=0, stretch=NO)
    data_table_ite_IR.column("Employee No.", anchor=W, width=50)
    data_table_ite_IR.column("Name", anchor=W, width=100)
    

    # Create Headings Individual Report
    data_table_ite_IR.heading("Employee No.", text="Employee No.", anchor=CENTER)
    data_table_ite_IR.heading("Name", text="Name", anchor=CENTER)

    data_table_ite_IR.bind("<ButtonRelease-1>", select_row_ite_IR)

    refreshTable_ite_IR()

        # Time Text
    time_lb = Label(ite_att_record, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    time_lb.place(x=540, y=10)

        # date Text
    date_lb = Label(ite_att_record, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    date_lb.place(x=710, y=10)

        # Time Label
    time_lb_ite = Label(ite_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    time_lb_ite.place(x=590, y=10)

        # date Label
    date_lb_ite = Label(ite_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
    date_lb_ite.place(x=760, y=10)

        # Total Faculty Label
    total_faculty_lb_ite = Label(ite_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_faculty_lb_ite.place(x=347, y=190)

        # Total Present Label
    total_present_lb_ite = Label(ite_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_present_lb_ite.place(x=565, y=190)

        # Total Absent Label
    total_absent_lb_ite = Label(ite_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_absent_lb_ite.place(x=772, y=190)

        # Total Late Label
    total_late_lb_ite = Label(ite_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
    total_late_lb_ite.place(x=990, y=190)

    def error_ite():
        emp_num = employee_num_ite.get()
        emp_name = employee_name_ite.get()

        if emp_num == "" or emp_name == "":
            messagebox.showinfo("Error", "Please Seleted a row on the table to open Summary Report !!")
        else:
            summary_ite()

        # Entry Employee Number
    employee_num_ite = Entry(ite_att_record)
    employee_num_ite.place(x=315, y=586, width=100)

        # Entry Employee Name
    employee_name_ite = Entry(ite_att_record)
    employee_name_ite.place(x=425, y=586, width=100)

         # Summary Report Button 
    ite_button_report = customtkinter.CTkButton(master=ite_att_record, text="Summary Report" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#C0C0C0",hover_color="#006699", command=error_ite)
    ite_button_report.place(x=550, y=586, height=21,width=110)

         # Search Entry Individual Report
    search_ent_ite_IR = StringVar()
    search_ite_IR = Entry(ite_att_record, textvariable = search_ent_ite_IR)
    search_ite_IR.place(x=385, y=305, width=190)

        # Search Button Individual Report
    search_btn_ite_IR = PhotoImage(file = "pic/btn_search_small.png")
    ite_button_search_IR = customtkinter.CTkButton(master=ite_att_record,image=search_btn_ite_IR, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_ite_IR)
    ite_button_search_IR.place(x=590, y=307, height=17,width=70)

        # Show All Button Individual Report
    showall_btn_ite_IR = PhotoImage(file = "pic/btn_showall_small.png")
    ite_button_showall_IR = customtkinter.CTkButton(master=ite_att_record,image=showall_btn_ite_IR, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_ite_IR)
    ite_button_showall_IR.place(x=445, y=608, height=21,width=90)

        # Search Entry
    search_ent_ite = StringVar()
    search_ite = Entry(ite_att_record, textvariable = search_ent_ite)
    search_ite.place(x=780, y=307, width=190)

        # Search Button
    search_btn_ite = PhotoImage(file = "pic/btn_search_small.png")
    ite_button_search = customtkinter.CTkButton(master=ite_att_record,image=search_btn_ite, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_ite)
    ite_button_search.place(x=975, y=307, height=17,width=70)

        # Show All Button
    showall_btn_ite = PhotoImage(file = "pic/btn_showall_small.png")
    ite_button_showall = customtkinter.CTkButton(master=ite_att_record,image=showall_btn_ite, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_ite)
    ite_button_showall.place(x=885, y=608, height=21,width=90)

         # Print Button
    print_btn_ite = PhotoImage(file = "pic/btn_print.png")
    ite_button_print = customtkinter.CTkButton(master=ite_att_record,image=print_btn_ite, text="",
                                                    corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_ite)
    ite_button_print.place(x=785, y=608, height=20,width=80)

        # Back Button
    ite_back = PhotoImage(file = "pic/btn_back_page.png")
    ite_button_back = customtkinter.CTkButton(master=ite_att_record,image=ite_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(attendance_record))
    ite_button_back.place(x=45, y=595, height=50,width=140)

    time_ite()
    count_data_ite()

    # ============= Acitivity Log In Frame ========================================================================================================================

        # open background image
    activity_log.act_image = Image.open('pic/7a.png')
    activity_log.act_resize_image = activity_log.act_image.resize((1362, 692))
    activity_log.photo = ImageTk.PhotoImage(activity_log.act_resize_image)
    activity_log.act_bg_img_lb = Label(activity_log, image = activity_log.photo)
    activity_log.act_bg_img_lb.pack()

        # Get And Disply the data in the table
    def log_read():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM activity_log")
        results_log = cursor.fetchall()
        conn.commit()
        return results_log

        # Refresh the tabble on Treeview
    def refreshTable_log():

        for data_log in data_table_act.get_children():
            data_table_act.delete(data_log)

        for results_log in reverse(log_read()):
            data_table_act.insert(parent='', index='end', iid=results_log, text="", values=(results_log), tag="orow")
        data_table_act.tag_configure('orow', background='#EEEEEE')

    def search_data_log():
        lookup_record = search_act.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for record in data_table_act.get_children():
            data_table_act.delete(record)
        
        cursor.execute("SELECT * FROM activity_log WHERE Name = '" + str(lookup_record) + "' or  Activity = '" + str(lookup_record) + "'or Department = '" + str(lookup_record) + "' or Date_Time = '" + str(lookup_record) + "'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_act.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="evenrow")
            else:
                data_table_act.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]), tag="oddrow")
            count += 1
            data_table_act.tag_configure('evenrow', background='#EEEEEE')
            data_table_act.tag_configure('oddrow', background='#EEEEEE')
            search_act.delete(0, END)

        conn.commit()
        conn.close()

     # Data Table "TreeView"
    scrollbary_act = Scrollbar(activity_log, orient=VERTICAL)
    scrollbary_act.place(x=1030, y=230, height=350)

    # style = ttk.Style()
    # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table_act = ttk.Treeview(activity_log)
    data_table_act.place(x=290, y=230, width=740, height=350)
    data_table_act.configure(yscrollcommand=scrollbary_act.set)

    scrollbary_act.configure(command=data_table_act.yview)

    data_table_act['columns'] = ("ID","Employee Number","Activity","Department","Date & Time")
    # Format Columns
    data_table_act.column("#0", width=0, stretch=NO)
    data_table_act.column("ID", anchor=CENTER,width=0)
    data_table_act.column("Employee Number", anchor=CENTER, width=50)
    data_table_act.column("Activity", anchor=CENTER, width=50)
    data_table_act.column("Department", anchor=CENTER, width=50)
    data_table_act.column("Date & Time", anchor=CENTER, width=50)

    # Create Headings
    data_table_act.heading("ID", text="ID", anchor=CENTER)
    data_table_act.heading("Employee Number", text="Employee Number", anchor=CENTER)
    data_table_act.heading("Activity", text="Activity", anchor=CENTER)
    data_table_act.heading("Department", text="Department", anchor=CENTER)
    data_table_act.heading("Date & Time", text="Date & Time", anchor=CENTER)

    refreshTable_log()

    # Search Entry
    search_entry_act = StringVar()
    search_act = Entry(activity_log, textvariable = search_entry_act)
    search_act.place(x=550, y=171, width=190)

        # Search Button
    search_btn_act = PhotoImage(file = "pic/btn_search.png")
    act_button_search = customtkinter.CTkButton(master=activity_log,image=search_btn_act, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_log)
    act_button_search.place(x=760, y=170, height=20,width=90)

        # Show All Button
    showall_btn_act = PhotoImage(file = "pic/btn_showall.png")
    act_button_showall = customtkinter.CTkButton(master=activity_log,image=showall_btn_act, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_log)
    act_button_showall.place(x=625, y=594, height=27,width=110)

        # Back Button
    act_back = PhotoImage(file = "pic/btn_back_page.png")
    act_button_back = customtkinter.CTkButton(master=activity_log,image=act_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
    act_button_back.place(x=85, y=495, height=50,width=140)

    

    main_window.mainloop()

w.destroy()
new_win()
w.mainloop()
