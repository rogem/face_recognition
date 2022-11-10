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

    show_frame(page1)

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

    global emp_uname 
    global emp_pass
    
    emp_uname=''
    emp_pass=''
    
    def get_value_uname():
        emp_uname = empl_log_txtbox_username.get()
        return emp_uname
    def get_value_pass():
        emp_pass = empl_log_txtbox_pass.get()
        return emp_pass

        # Account verification
    def verify():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # cursor.execute("""CREATE TABLE IF NOT EXISTS 
        #     user_login(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Username TEXT, Password TEXT, Position TEXt)""")

        # cursor.execute("INSERT INTO user_login (Username,Password) VALUES ('admin', '123' , 'admin')")

        uname = empl_log_txtbox_username.get()
        pwd = empl_log_txtbox_pass.get()
        emply = "Employee"

        if uname=='' or pwd=='':
            messagebox.showinfo("Error", "Please Fill The Empty Field!!")
        else:
            cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(uname) + "' AND  Password = '" + str(pwd) + "' AND  Position = '" + str(emply) + "'")
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

                show_frame(attendance_monitoring)
                messagebox.showinfo("Messgae", "WELCOME USER" )

                empl_log_txtbox_username.delete(0, END)
                empl_log_txtbox_pass.delete(0, END)
                check_button_empl_log.deselect()

                # currentDateTime = datetime.datetime.now()

                # cursor.execute("""CREATE TABLE IF NOT EXISTS 
                #     activity_log(ID INTEGER PRIMARY KEY,Name TEXT,Activity TEXT,
                #     Department TEXT,Date_Time TIMESTAMP)""")

                # insertdata = """INSERT INTO activity_log (Name,Activity,Department,Date_Time)
                #         VAlUES(?,?,?,?,?);"""
                # cursor.execute(insertdata, (get_Name,'login',get_Department,currentDateTime))
            else:
                messagebox.showinfo("Error", "Please provide correct username and password!!")

                

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

    # ============= Employee Attendance Record In Frame ========================================================================================================================

        # open background image
    attendance_monitoring.att_mon_image = Image.open('pic/6.png')
    attendance_monitoring.att_mon_resize_image = attendance_monitoring.att_mon_image.resize((1362, 692))
    attendance_monitoring.photo = ImageTk.PhotoImage(attendance_monitoring.att_mon_resize_image)
    attendance_monitoring.att_mon_bg_img_lb = Label(attendance_monitoring, image = attendance_monitoring.photo)
    attendance_monitoring.att_mon_bg_img_lb.pack()

    def user_read():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # uname = get_value_uname()
        # pwd = get_value_pass()

        # cursor.execute("SELECT Employee_Name FROM faculty_data WHERE Username like '"+ str(uname)+"' AND Password like '"+ str(pwd)+"'")
        # get_Name = cursor.fetchone()
        # cursor.execute("SELECT College_Department FROM faculty_data WHERE Username like '"+ str(uname)+"' AND Password like '"+ str(pwd)+"'")
        # get_Department = cursor.fetchone()


        set_name='pano'
        # set_department=get_Department

        # Name =att_mon_lb_name.cget("text")
        print(set_name)

        cursor.execute("SELECT Time_in,Time_out,_Date,Status FROM attendance_record WHERE Name='"+ str(set_name) +"' AND Department='Psychology'")
        results_user = cursor.fetchall()
        conn.commit()
        
        global num
        num = 0

        for record in results_user:
            if num % 2 == 0:
                data_table_emp_att_rec.insert(parent='', index='end', iid=num, text="", values=(record[0],record[1],record[2],record[3]), tag="evenrow")
            else:
                data_table_emp_att_rec.insert(parent='', index='end', iid=num, text="", values=(record[0],record[1],record[2],record[3]), tag="oddrow")
            num += 1
            data_table_emp_att_rec.tag_configure('evenrow', background='#EEEEEE')
            data_table_emp_att_rec.tag_configure('oddrow', background='#EEEEEE')

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
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command="")
    att_mon_button_showall.place(x=680, y=655, height=27,width=110)

        # Logout Button
    att_mon_logout = PhotoImage(file = "pic/btn_logout.png")
    att_mon_button_logout = customtkinter.CTkButton(master=attendance_monitoring,image=att_mon_logout, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#ffffff",hover_color="#6699cc", command=lambda: show_frame(employee_login))
    att_mon_button_logout.place(x=30, y=565, height=100,width=100)

    user_read()

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

        # Account verification
    def verify():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # cursor.execute("""CREATE TABLE IF NOT EXISTS 
        #     user_login(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Username TEXT, Password TEXT, Position TEXt)""")

        # cursor.execute("INSERT INTO user_login (Username,Password) VALUES ('admin', '123' , 'admin')")

        uname = pg3_txtbox_username.get()
        pwd = pg3_txtbox_pass.get()
        adm = "Admin"
        state = "On"

        count = 3
        
        if uname=='' or pwd=='':
            messagebox.showinfo("Error", "Please Fill The Empty Field!!")
        else:
            cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(uname) + "' AND  Password = '" + str(pwd) + "' AND  Position = '" + str(adm) + "' AND Status ='" + str(state) + "'")
            if cursor.fetchone():
                show_frame(page4)
                messagebox.showinfo("Messgae", "WELCOME USER")

                pg3_txtbox_username.delete(0, END)
                pg3_txtbox_pass.delete(0, END)
                check_button.deselect()
            else:
                while count !=0:
                    messagebox.showinfo("Error", "Reamaining Attempt: "+ str(count))
                    count-=1

                else:
                    messagebox.showinfo("Error", "Access denied, Out of try !!")


        # if uname=='' or pwd=='':
        #     messagebox.showinfo("Error", "Please Fill The Empty Field!!")
        # else:
        #     cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(uname) + "' AND  Password = '" + str(pwd) + "' AND  Position = '" + str(adm) + "' AND Status ='" + str(state) + "'")
        #     if cursor.fetchone():
        #         show_frame(page4)
        #         messagebox.showinfo("Messgae", "WELCOME USER")

        #         pg3_txtbox_username.delete(0, END)
        #         pg3_txtbox_pass.delete(0, END)
        #         check_button.deselect()
        #     else:
        #         messagebox.showinfo("Error", "Please provide correct username and password!!")

        conn.commit()

        # Login Button
    login_img_btn = PhotoImage(file = "pic/login.png")
    pg3_button = Button(page3, image=login_img_btn, borderwidth=0, bg='#1f2a76', command=verify)
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

        # Logout Button
    logout_btn = PhotoImage(file = "pic/logout.png")
    pg4_button_logout = customtkinter.CTkButton(master=page4,image=logout_btn, text="" ,
                                                corner_radius=30,bg_color='#ffffff', fg_color="#ffffff",hover_color="#6699cc", command=lambda: show_frame(page3))
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

    # ============= Faculty Information Frame ===================================================================================================================================================

        # open background image
    faculty_information.fac_inf_image = Image.open('pic/10.png')
    faculty_information.fac_inf_resize_image = faculty_information.fac_inf_image.resize((1362, 692))
    faculty_information.photo = ImageTk.PhotoImage(faculty_information.fac_inf_resize_image)
    faculty_information.fac_inf_bg_img_lb = Label(faculty_information, image = faculty_information.photo)
    faculty_information.fac_inf_bg_img_lb.pack()

        # Clear Text Field
    def clear():
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
    def update(Employee_No,Email,Employee_Name,Gender,Age,Contact_Number,Address,College_Department,Username,Password,Position,Status,idEmployee_No):
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            faculty_data(Employee_No TEXT, Email TEXT, Employee_Name TEXT,
            Gender TEXT,Age TEXT,Contact_Number TEXT,Address TEXT,College_Department TEXT,
            Username TEXT, Password TEXT, Position TEXT, Status TEXT)""")

        cursor.execute("UPDATE faculty_data SET Employee_No = '" + str(Employee_No) + "', Email = '" + str(Email) + "', Employee_Name = '" + str(Employee_Name) + "', Gender = '" + str(Gender) + "', Age = '" + str(Age) + "', Contact_Number = '" + str(Contact_Number) + "', Address = '" + str(Address) + "', College_Department = '" + str(College_Department) + "', Username = '" + str(Username) + "', Password = '" + str(Password) + "', Position = '" + str(Position) + "', Status = '" + str(Status) + "' WHERE Employee_No = '"+ str(idEmployee_No)+"'")
        conn.commit()

    def check_duplicate():
        Employee_No = employee_num_fac_inf.get()
        Email = email_fac_inf.get()
        Contact_Number = con_num_fac_inf.get()
        Username = username_fac_inf.get()
        Password = password_fac_inf.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM faculty_data WHERE Employee_No = '" + str(Employee_No) + "' or  Email = '" + str(Email) + "'  or Contact_Number = '" + str(Contact_Number) + "' or Username = '" + str(Username) + "' or Password = '" + str(Password) + "'")
        records = cursor.fetchone()

        if records is not None:
            return True
        else:
            return False

        conn.commit()

        # Add Faculty 
    def Save_Data():
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

        if save_status == "" or save_employee_number == "" or save_email == "" or save_employee_name == "" or save_gender == "" or save_age == "" or save_contact_number == "" or save_address == "" or save_college_department == "" or save_username == "" or save_password == "" or save_position == "":
            messagebox.showinfo("Error", "Please fill up the blank entry!!")
            return
        else:
            if check_duplicate() == False:
                messagebox.showinfo("Messgae", "Data Added!!")
                insert(str(save_employee_number),str(save_email),str(save_employee_name),str(save_gender),str(save_age),str(save_contact_number),str(save_address),str(save_college_department),str(save_username),str(save_password),str(save_position),str(save_status)) 
                clear()
            else:
                messagebox.showinfo("Error", "Employee Number, Email or Contact Number Already Exist")
                return
            
        refreshTable()

    def select_row(e):
        clear()

        selected = data_table.focus()
        values = data_table.item(selected, 'values')

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

        # Updating Selected Data
    def Update_Data():

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
        else:
            messagebox.showinfo("Messgae", "Data Updated!!")
            update(save_employee_number,save_email,save_employee_name,save_gender,save_age,save_contact_number,save_address,save_college_department,save_username,save_password,save_position,save_status,update_name)
            clear()     
        refreshTable()

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

    data_table['columns'] = ("Status","Employee No.","Email","Employee Name","Gender","Age","Contact Number","Address","College Department","Username","Password","Position")
    # Format Columns
    data_table.column("#0", width=0, stretch=NO)
    data_table.column("Employee No.", anchor=W, width=150)
    data_table.column("Email", anchor=W, width=100)
    data_table.column("Employee Name", anchor=W, width=200)
    data_table.column("Gender", anchor=W, width=100)
    data_table.column("Age", anchor=W, width=100)
    data_table.column("Contact Number", anchor=W, width=200)
    data_table.column("Address", anchor=W, width=300)
    data_table.column("College Department", anchor=W, width=150)
    data_table.column("Username", anchor=W, width=100)
    data_table.column("Password", anchor=W, width=100)
    data_table.column("Position", anchor=W, width=100)
    data_table.column("Status", anchor=W, width=50)

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
    department_combobox = ttk.Combobox(faculty_information, values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
    department_combobox.place(x=382, y=202, width=200)
    # state="readonly"
    
        # Entry Employee Number
    employee_num_fac_inf = Entry(faculty_information)
    employee_num_fac_inf.place(x=200, y=288, width=125)

        # Entry Employee Name
    employee_name_fac_inf = Entry(faculty_information)
    employee_name_fac_inf.place(x=385, y=288, width=125)

        # ComboBox Gender
    gender_combobox_fac_inf = ttk.Combobox(faculty_information, values=["Male", "Female"])
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
    status_combobox_fac_inf = ttk.Combobox(faculty_information, values=["On", "Off"])
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
    position_fac_inf = ttk.Combobox(faculty_information, values=["Admin", "Employee"])
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

        # Add Faculty Button
    add_fac_btn = PhotoImage(file = "pic/btn_add_faculty.png")
    add_button_fac_inf = customtkinter.CTkButton(master=faculty_information,image=add_fac_btn, text="" ,
                                                corner_radius=6, fg_color="#00436e",hover_color="#006699", command= Save_Data)
    add_button_fac_inf.place(x=380, y=506, height=32,width=131)

        # Update Button
    def Update():
        print("update")
    update_btn = PhotoImage(file = "pic/btn_update.png")
    button_update = customtkinter.CTkButton(master=faculty_information,image=update_btn, text="" ,
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


    # ============= Mathematics Attendance Record Frame =============================================================================

        # open background image
    mathematics_att_record.math_rec_image = Image.open('pic/9.png')
    mathematics_att_record.math_rec_resize_image = mathematics_att_record.math_rec_image.resize((1362, 692))
    mathematics_att_record.photo = ImageTk.PhotoImage(mathematics_att_record.math_rec_resize_image)
    mathematics_att_record.math_rec_bg_img_lb = Label(mathematics_att_record, image = mathematics_att_record.photo)
    mathematics_att_record.math_rec_bg_img_lb.pack()

    def normal():
        employee_num_math_rec.configure(state='normal')
        employee_name_math_rec.configure(state='normal')
        math_rec_department_combobox.configure(state='normal')
        time_in_math_rec.configure(state='normal')
        time_out_math_rec.configure(state='normal')
        date_math_rec.configure(state='normal')
        att_status_math_rec.configure(state='normal')

    def disable_text():
        employee_num_math_rec.configure(state='disabled',text='')
        employee_name_math_rec.configure(state='disabled')
        math_rec_department_combobox.configure(state='disabled')
        time_in_math_rec.configure(state='disabled')
        time_out_math_rec.configure(state='disabled')
        date_math_rec.configure(state='disabled')
        att_status_math_rec.configure(state='disabled')

    def reset():
        normal()
        employee_num_math_rec.delete(0, END)
        employee_name_math_rec.delete(0, END)
        math_rec_department_combobox.delete(0, END)
        time_in_math_rec.delete(0, END)
        time_out_math_rec.delete(0, END)
        date_math_rec.delete(0, END)
        att_status_math_rec.delete(0, END)
        disable_text()

         # Get Current Time and Date
    def time():
        string_time = strftime('%I:%M:%S %p')
        time_lb_math_rec.configure(text = string_time)
        time_lb_math_rec.after(1000, time)

        string_date = strftime('%d/%m/20%y')
        date_lb_math_rec.configure(text = string_date)

            # search Data
    def search_data_math():
        lookup_record = search_math_rec.get()

        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for record in data_table_math_rec.get_children():
            data_table_math_rec.delete(record)
        
        cursor.execute("SELECT Employee_No,Name,Department,Time_in,Time_out,_Date,Status FROM attendance_record WHERE (Employee_No = '" + str(lookup_record) + "' or  Name = '" + str(lookup_record) + "' or Time_in = '" + str(lookup_record) + "' or Time_out = '" + str(lookup_record) + "' or _Date = '" + str(lookup_record) + "' or Status = '" + str(lookup_record) + "') AND Department='Mathematics'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_math_rec.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tag="evenrow")
            else:
                data_table_math_rec.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tag="oddrow")
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
            attendance_record(ID INTEGER PRIMARY KEY,Employee_No INTEGER,Name TEXT,
            Department TEXT,Time_in TEXT,Time_out TEXT,_Date TEXT,Status TEXT)""")

        # cursor.execute("""INSERT INTO attendance_record (ID,Employee_No,Name,Department,Time_in,Time_out,_Date,Status)
        #                 VAlUES
        #                 (1,234,'neil','ite','8:23:45 AM','5:23:45 PM','26/10/2022','Present'),
        #                 (2,345,'josel','ite','9:12:45 AM','6:23:45 PM','26/10/2022','Late') """)

        cursor.execute("SELECT Employee_No,Name,Department,Time_in,Time_out,_Date,Status FROM attendance_record WHERE Department='Mathematics'")
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

    def select_row_math(e):
        selected = data_table_math_rec.focus()
        values = data_table_math_rec.item(selected, 'values')

        normal()

        employee_num_math_rec.delete(0, END)
        employee_name_math_rec.delete(0, END)
        math_rec_department_combobox.delete(0, END)
        time_in_math_rec.delete(0, END)
        time_out_math_rec.delete(0, END)
        date_math_rec.delete(0, END)
        att_status_math_rec.delete(0, END)

        employee_num_math_rec.insert(0, values[0])
        employee_name_math_rec.insert(0, values[1])
        math_rec_department_combobox.insert(0, values[2])
        time_in_math_rec.insert(0, values[3])
        time_out_math_rec.insert(0, values[4])
        date_math_rec.insert(0, values[5])
        att_status_math_rec.insert(0, values[6])

        disable_text()

    def print_data_math():
        file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

        cols = ['Employee No.','Name','Department','Time in','Time out','Date','Status']
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
        df.to_excel(writer,'sheet1')
        writer.save()
        source = "excelfile/new_datasave.xlsx"
        if file:
            shutil.copy(source,file)
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

    data_table_math_rec['columns'] = ("Employee No.","Name","Department","Time in","Time out","Date","Status")
    # Format Columns
    data_table_math_rec.column("#0", width=0, stretch=NO)
    data_table_math_rec.column("Employee No.", anchor=W, width=150)
    data_table_math_rec.column("Name", anchor=W, width=100)
    data_table_math_rec.column("Department", anchor=W, width=200)
    data_table_math_rec.column("Time in", anchor=W, width=100)
    data_table_math_rec.column("Time out", anchor=W, width=100)
    data_table_math_rec.column("Date", anchor=W, width=100)
    data_table_math_rec.column("Status", anchor=W, width=100)

    # Create Headings
    data_table_math_rec.heading("Employee No.", text="Employee No.", anchor=CENTER)
    data_table_math_rec.heading("Name", text="Name", anchor=CENTER)
    data_table_math_rec.heading("Department", text="Department", anchor=CENTER)
    data_table_math_rec.heading("Time in", text="Time in", anchor=CENTER)
    data_table_math_rec.heading("Time out", text="Time out", anchor=CENTER)
    data_table_math_rec.heading("Date", text="Date", anchor=CENTER)
    data_table_math_rec.heading("Status", text="Status", anchor=CENTER)

    data_table_math_rec.bind("<ButtonRelease-1>", select_row_math)

    refreshTable_math()

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

        # ComboBox College Department
    math_rec_department_combobox = ttk.Combobox(mathematics_att_record, values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
    math_rec_department_combobox.place(x=445, y=305, width=200)

        # Entry Employee Number
    employee_num_math_rec = Entry(mathematics_att_record)
    employee_num_math_rec.place(x=404, y=366, width=110)

        # Entry Employee Name
    employee_name_math_rec = Entry(mathematics_att_record)
    employee_name_math_rec.place(x=404, y=397, width=110)

        # Entry Attendance Satatus
    att_status_math_rec = Entry(mathematics_att_record)
    att_status_math_rec.place(x=404, y=428, width=110)

        # Entry Time In
    time_in_math_rec = Entry(mathematics_att_record)
    time_in_math_rec.place(x=565, y=366, width=110)

        # Entry Time Out
    time_out_math_rec = Entry(mathematics_att_record)
    time_out_math_rec.place(x=565, y=397, width=110)

        # Entry Date
    date_math_rec = Entry(mathematics_att_record)
    date_math_rec.place(x=565, y=428, width=110)

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
    math_rec_button_showall.place(x=843, y=608, height=21,width=90)

        # Reset Button
    reset_btn_math_rec = PhotoImage(file = "pic/btn_reset_small.png")
    math_rec_button_reset = customtkinter.CTkButton(master=mathematics_att_record,image=reset_btn_math_rec, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=reset)
    math_rec_button_reset.place(x=510, y=519, height=25,width=100)

        # Print Button
    print_btn_math_rec = PhotoImage(file = "pic/btn_print.png")
    math_rec_button_print = customtkinter.CTkButton(master=mathematics_att_record,image=print_btn_math_rec, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=print_data_math)
    math_rec_button_print.place(x=372, y=519, height=25,width=100)

        # Back Button
    math_rec_back = PhotoImage(file = "pic/btn_back_page.png")
    math_rec_button_back = customtkinter.CTkButton(master=mathematics_att_record,image=math_rec_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(attendance_record))
    math_rec_button_back.place(x=45, y=595, height=50,width=140)

    time()
    count_data()

    # ============= Psychology Attendance Record Frame =============================================================================

        # open background image
    psychology_att_record.psyc_image = Image.open('pic/10a.png')
    psychology_att_record.psyc_resize_image = psychology_att_record.psyc_image.resize((1362, 692))
    psychology_att_record.photo = ImageTk.PhotoImage(psychology_att_record.psyc_resize_image)
    psychology_att_record.psyc_bg_img_lb = Label(psychology_att_record, image = psychology_att_record.photo)
    psychology_att_record.psyc_bg_img_lb.pack()

         # Get Current Time and Date
    def time_psyc():
        string_time_psyc = strftime('%I:%M:%S %p')
        time_lb_psyc.configure(text = string_time_psyc)
        time_lb_psyc.after(1000, time_psyc)

        string_date_psyc = strftime('%d/%m/20%y')
        date_lb_psyc.configure(text = string_date_psyc)

    def normal_psyc():
        employee_num_psyc.configure(state='normal')
        employee_name_psyc.configure(state='normal')
        psyc_department_combobox.configure(state='normal')
        time_in_psyc.configure(state='normal')
        time_out_psyc.configure(state='normal')
        date_psyc.configure(state='normal')
        att_status_psyc.configure(state='normal')
        
    def disable_text_psyc():
        employee_num_psyc.configure(state='disabled',text='')
        employee_name_psyc.configure(state='disabled')
        psyc_department_combobox.configure(state='disabled')
        time_in_psyc.configure(state='disabled')
        time_out_psyc.configure(state='disabled')
        date_psyc.configure(state='disabled')
        att_status_psyc.configure(state='disabled')

    def reset_psyc():
        normal_psyc()
        employee_num_psyc.delete(0, END)
        employee_name_psyc.delete(0, END)
        psyc_department_combobox.delete(0, END)
        time_in_psyc.delete(0, END)
        time_out_psyc.delete(0, END)
        date_psyc.delete(0, END)
        att_status_psyc.delete(0, END)
        disable_text_psyc()

    def select_row_psyc(e):
        selected = data_table_psyc.focus()
        values = data_table_psyc.item(selected, 'values')

        normal_psyc()

        employee_num_psyc.delete(0, END)
        employee_name_psyc.delete(0, END)
        psyc_department_combobox.delete(0, END)
        time_in_psyc.delete(0, END)
        time_out_psyc.delete(0, END)
        date_psyc.delete(0, END)
        att_status_psyc.delete(0, END)

        employee_num_psyc.insert(0, values[0])
        employee_name_psyc.insert(0, values[1])
        psyc_department_combobox.insert(0, values[2])
        time_in_psyc.insert(0, values[3])
        time_out_psyc.insert(0, values[4])
        date_psyc.insert(0, values[5])
        att_status_psyc.insert(0, values[6])

        disable_text_psyc()

            # Get And Disply the data in the table
    def psyc_read():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            attendance_record(ID INTEGER PRIMARY KEY,Employee_No INTEGER,Name TEXT,
            Department TEXT,Time_in TEXT,Time_out TEXT,_Date TEXT,Status TEXT)""")

        cursor.execute("SELECT Employee_No,Name,Department,Time_in,Time_out,_Date,Status FROM attendance_record WHERE Department='Psychology'")
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
        
        cursor.execute("SELECT Employee_No,Name,Department,Time_in,Time_out,_Date,Status FROM attendance_record WHERE (Employee_No = '" + str(lookup_record) + "' or  Name = '" + str(lookup_record) + "' or  Department = '" + str(lookup_record) + "' or Time_in = '" + str(lookup_record) + "' or Time_out = '" + str(lookup_record) + "' or _Date = '" + str(lookup_record) + "' or Status = '" + str(lookup_record) + "') AND Department='Psychology'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[6]), tag="evenrow")
            else:
                data_table_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[6]), tag="oddrow")
            count += 1
            data_table_psyc.tag_configure('evenrow', background='#EEEEEE')
            data_table_psyc.tag_configure('oddrow', background='#EEEEEE')
            search_psyc.delete(0, END)

        conn.commit()
        conn.close()

    def print_data_psyc():
        file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

        cols = ['Employee No.','Name','Department','Time in','Time out','Date','Status']
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
        df.to_excel(writer,'sheet1')
        writer.save()
        source = "excelfile/new_datasave_psychology.xlsx"
        if file:
            shutil.copy(source,file)
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

    data_table_psyc['columns'] = ("Employee No.","Name","Department","Time in","Time out","Date","Status")
    # Format Columns
    data_table_psyc.column("#0", width=0, stretch=NO)
    data_table_psyc.column("Employee No.", anchor=W, width=150)
    data_table_psyc.column("Name", anchor=W, width=100)
    data_table_psyc.column("Department", anchor=W, width=200)
    data_table_psyc.column("Time in", anchor=W, width=100)
    data_table_psyc.column("Time out", anchor=W, width=100)
    data_table_psyc.column("Date", anchor=W, width=100)
    data_table_psyc.column("Status", anchor=W, width=100)

    # Create Headings
    data_table_psyc.heading("Employee No.", text="Employee No.", anchor=CENTER)
    data_table_psyc.heading("Name", text="Name", anchor=CENTER)
    data_table_psyc.heading("Department", text="Department", anchor=CENTER)
    data_table_psyc.heading("Time in", text="Time in", anchor=CENTER)
    data_table_psyc.heading("Time out", text="Time out", anchor=CENTER)
    data_table_psyc.heading("Date", text="Date", anchor=CENTER)
    data_table_psyc.heading("Status", text="Status", anchor=CENTER)

    data_table_psyc.bind("<ButtonRelease-1>", select_row_psyc)

    refreshTable_psyc()

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

        # ComboBox College Department
    psyc_department_combobox = ttk.Combobox(psychology_att_record, values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
    psyc_department_combobox.place(x=445, y=305, width=200)

        # Entry Employee Number
    employee_num_psyc = Entry(psychology_att_record)
    employee_num_psyc.place(x=404, y=366, width=110)

        # Entry Employee Name
    employee_name_psyc = Entry(psychology_att_record)
    employee_name_psyc.place(x=404, y=397, width=110)

        # Entry Attendance Satatus
    att_status_psyc = Entry(psychology_att_record)
    att_status_psyc.place(x=404, y=428, width=110)

        # Entry Time In
    time_in_psyc = Entry(psychology_att_record)
    time_in_psyc.place(x=565, y=366, width=110)

        # Entry Time Out
    time_out_psyc = Entry(psychology_att_record)
    time_out_psyc.place(x=565, y=397, width=110)

        # Entry Date
    date_psyc = Entry(psychology_att_record)
    date_psyc.place(x=565, y=428, width=110)

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
    psyc_button_showall.place(x=843, y=608, height=21,width=90)

        # Reset Button
    reset_btn_psyc = PhotoImage(file = "pic/btn_reset_small.png")
    psyc_button_reset = customtkinter.CTkButton(master=psychology_att_record,image=reset_btn_psyc, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command= reset_psyc)
    psyc_button_reset.place(x=510, y=519, height=25,width=100)

        # Print Button
    print_btn_psyc = PhotoImage(file = "pic/btn_print.png")
    psyc_button_print = customtkinter.CTkButton(master=psychology_att_record,image=print_btn_psyc, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=print_data_psyc)
    psyc_button_print.place(x=372, y=519, height=25,width=100)

        # Back Button
    psyc_back = PhotoImage(file = "pic/btn_back_page.png")
    psyc_button_back = customtkinter.CTkButton(master=psychology_att_record,image=psyc_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(attendance_record))
    psyc_button_back.place(x=45, y=595, height=50,width=140)

    time_psyc()
    count_data_psyc()

    # ============= Applied Physics Attendance Record Frame =============================================================================

        # open background image
    applied_physics_att_record.applied_image = Image.open('pic/10b.png')
    applied_physics_att_record.applied_resize_image = applied_physics_att_record.applied_image.resize((1362, 692))
    applied_physics_att_record.photo = ImageTk.PhotoImage(applied_physics_att_record.applied_resize_image)
    applied_physics_att_record.applied_bg_img_lb = Label(applied_physics_att_record, image = applied_physics_att_record.photo)
    applied_physics_att_record.applied_bg_img_lb.pack()

        #  Get Current Time and Date
    def time_applied():
        string_time_applied = strftime('%I:%M:%S %p')
        time_lb_applied.configure(text = string_time_applied)
        time_lb_applied.after(1000, time_applied)

        string_date_applied = strftime('%d/%m/20%y')
        date_lb_applied.configure(text = string_date_applied)

    def normal_applied():
        employee_num_applied.configure(state='normal')
        employee_name_applied.configure(state='normal')
        applied_department_combobox.configure(state='normal')
        time_in_applied.configure(state='normal')
        time_out_applied.configure(state='normal')
        date_applied.configure(state='normal')
        att_status_applied.configure(state='normal')

    def disable_text_applied():
        employee_num_applied.configure(state='disabled',text='')
        employee_name_applied.configure(state='disabled')
        applied_department_combobox.configure(state='disabled')
        time_in_applied.configure(state='disabled')
        time_out_applied.configure(state='disabled')
        date_applied.configure(state='disabled')
        att_status_applied.configure(state='disabled')

    def reset_applied():
        normal_applied()
        employee_num_applied.delete(0, END)
        employee_name_applied.delete(0, END)
        applied_department_combobox.delete(0, END)
        time_in_applied.delete(0, END)
        time_out_applied.delete(0, END)
        date_applied.delete(0, END)
        att_status_applied.delete(0, END)
        disable_text_applied()

    def select_row_applied(e):
        selected = data_table_applied.focus()
        values = data_table_applied.item(selected, 'values')

        normal_applied()

        employee_num_applied.delete(0, END)
        employee_name_applied.delete(0, END)
        applied_department_combobox.delete(0, END)
        time_in_applied.delete(0, END)
        time_out_applied.delete(0, END)
        date_applied.delete(0, END)
        att_status_applied.delete(0, END)

        employee_num_applied.insert(0, values[0])
        employee_name_applied.insert(0, values[1])
        applied_department_combobox.insert(0, values[2])
        time_in_applied.insert(0, values[3])
        time_out_applied.insert(0, values[4])
        date_applied.insert(0, values[5])
        att_status_applied.insert(0, values[6])

        disable_text_applied()

            # Get And Disply the data in the table
    def applied_read():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            attendance_record(ID INTEGER PRIMARY KEY,Employee_No INTEGER,Name TEXT,
            Department TEXT,Time_in TEXT,Time_out TEXT,_Date TEXT,Status TEXT)""")

        cursor.execute("SELECT Employee_No,Name,Department,Time_in,Time_out,_Date,Status FROM attendance_record WHERE Department='Applied Physics'")
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
        
        cursor.execute("SELECT Employee_No,Name,Department,Time_in,Time_out,_Date,Status FROM attendance_record WHERE (Employee_No = '" + str(lookup_record) + "' or  Name = '" + str(lookup_record) + "' or  Department = '" + str(lookup_record) + "' or Time_in = '" + str(lookup_record) + "' or Time_out = '" + str(lookup_record) + "' or _Date = '" + str(lookup_record) + "' or Status = '" + str(lookup_record) + "') AND Department='Applied Physics'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[6],record[6]), tag="evenrow")
            else:
                data_table_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[6],record[6]), tag="oddrow")
            count += 1
            data_table_applied.tag_configure('evenrow', background='#EEEEEE')
            data_table_applied.tag_configure('oddrow', background='#EEEEEE')
            search_applied.delete(0, END)

        conn.commit()
        conn.close()

    def print_data_applied():
        file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

        cols = ['Employee No.','Name','Department','Time in','Time out','Date','Status']
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
        df.to_excel(writer,'sheet1')
        writer.save()
        source = "excelfile/new_datasave_appliedphysics.xlsx"
        if file:
            shutil.copy(source,file)
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

    data_table_applied['columns'] = ("Employee No.","Name","Department","Time in","Time out","Date","Status")
    # Format Columns
    data_table_applied.column("#0", width=0, stretch=NO)
    data_table_applied.column("Employee No.", anchor=W, width=150)
    data_table_applied.column("Name", anchor=W, width=100)
    data_table_applied.column("Department", anchor=W, width=200)
    data_table_applied.column("Time in", anchor=W, width=100)
    data_table_applied.column("Time out", anchor=W, width=100)
    data_table_applied .column("Date", anchor=W, width=100)
    data_table_applied .column("Status", anchor=W, width=100)

    # Create Headings
    data_table_applied.heading("Employee No.", text="Employee No.", anchor=CENTER)
    data_table_applied.heading("Name", text="Name", anchor=CENTER)
    data_table_applied.heading("Department", text="Department", anchor=CENTER)
    data_table_applied.heading("Time in", text="Time in", anchor=CENTER)
    data_table_applied.heading("Time out", text="Time out", anchor=CENTER)
    data_table_applied.heading("Date", text="Date", anchor=CENTER)
    data_table_applied.heading("Status", text="Status", anchor=CENTER)

    data_table_applied.bind("<ButtonRelease-1>", select_row_applied)

    refreshTable_applied()

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

        # ComboBox College Department
    applied_department_combobox = ttk.Combobox(applied_physics_att_record, values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
    applied_department_combobox.place(x=445, y=305, width=200)

        # Entry Employee Number
    employee_num_applied = Entry(applied_physics_att_record)
    employee_num_applied.place(x=404, y=366, width=110)

        # Entry Employee Name
    employee_name_applied = Entry(applied_physics_att_record)
    employee_name_applied.place(x=404, y=397, width=110)

        # Entry Attendance Satatus
    att_status_applied = Entry(applied_physics_att_record)
    att_status_applied.place(x=404, y=428, width=110)

        # Entry Time In
    time_in_applied = Entry(applied_physics_att_record)
    time_in_applied.place(x=565, y=366, width=110)

        # Entry Time Out
    time_out_applied = Entry(applied_physics_att_record)
    time_out_applied.place(x=565, y=397, width=110)

        # Entry Date
    date_applied = Entry(applied_physics_att_record)
    date_applied.place(x=565, y=428, width=110)

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
    applied_button_showall.place(x=843, y=608, height=21,width=90)

        # Reset Button
    reset_btn_applied = PhotoImage(file = "pic/btn_reset_small.png")
    applied_button_reset = customtkinter.CTkButton(master=applied_physics_att_record,image=reset_btn_applied, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=reset_applied)
    applied_button_reset.place(x=510, y=519, height=25,width=100)

        # Print Button
    print_btn_applied = PhotoImage(file = "pic/btn_print.png")
    applied_button_print = customtkinter.CTkButton(master=applied_physics_att_record,image=print_btn_applied, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=print_data_applied)
    applied_button_print.place(x=372, y=519, height=25,width=100)

        # Back Button
    applied_back = PhotoImage(file = "pic/btn_back_page.png")
    applied_button_back = customtkinter.CTkButton(master=applied_physics_att_record,image=applied_back, text="" ,
                                                corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(attendance_record))
    applied_button_back.place(x=45, y=595, height=50,width=140)

    time_applied()
    count_data_applied()

    # ============= Applied Physics Attendance Record Frame =============================================================================

        # open background image
    ite_att_record.ite_image = Image.open('pic/10c.png')
    ite_att_record.ite_resize_image = ite_att_record.ite_image.resize((1362, 692))
    ite_att_record.photo = ImageTk.PhotoImage(ite_att_record.ite_resize_image)
    ite_att_record.ite_bg_img_lb = Label(ite_att_record, image = ite_att_record.photo)
    ite_att_record.ite_bg_img_lb.pack()

        #  Get Current Time and Date
    def time_ite():
        string_time_ite = strftime('%I:%M:%S %p')
        time_lb_ite.configure(text = string_time_ite)
        time_lb_ite.after(1000, time_ite)

        string_date_ite = strftime('%d/%m/20%y')
        date_lb_ite.configure(text = string_date_ite)

    def normal_ite():
        employee_num_ite.configure(state='normal')
        employee_name_ite.configure(state='normal')
        ite_department_combobox.configure(state='normal')
        time_in_ite.configure(state='normal')
        time_out_ite.configure(state='normal')
        date_ite.configure(state='normal')
        att_status_ite.configure(state='normal')

    def disable_text_ite():
        employee_num_ite.configure(state='disabled',text='')
        employee_name_ite.configure(state='disabled')
        ite_department_combobox.configure(state='disabled')
        time_in_ite.configure(state='disabled')
        time_out_ite.configure(state='disabled')
        date_ite.configure(state='disabled')
        att_status_ite.configure(state='disabled')

    def reset_ite():
        normal_ite()
        employee_num_ite.delete(0, END)
        employee_name_ite.delete(0, END)
        ite_department_combobox.delete(0, END)
        time_in_ite.delete(0, END)
        time_out_ite.delete(0, END)
        date_ite.delete(0, END)
        att_status_ite.delete(0, END)
        disable_text_ite()

    def select_row_ite(e):
        selected = data_table_ite.focus()
        values = data_table_ite.item(selected, 'values')

        normal_ite()

        employee_num_ite.delete(0, END)
        employee_name_ite.delete(0, END)
        ite_department_combobox.delete(0, END)
        time_in_ite.delete(0, END)
        time_out_ite.delete(0, END)
        date_ite.delete(0, END)
        att_status_ite.delete(0, END)

        employee_num_ite.insert(0, values[0])
        employee_name_ite.insert(0, values[1])
        ite_department_combobox.insert(0, values[2])
        time_in_ite.insert(0, values[3])
        time_out_ite.insert(0, values[4])
        date_ite.insert(0, values[5])
        att_status_ite.insert(0, values[6])

        disable_text_ite()

            # Get And Disply the data in the table
    def ite_read():
        conn = sqlite3.connect("data/data.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS 
            attendance_record(ID INTEGER PRIMARY KEY,Employee_No INTEGER,Name TEXT,
            Department TEXT,Time_in TEXT,Time_out TEXT,_Date TEXT,Status TEXT)""")

        cursor.execute("SELECT Employee_No,Name,Department,Time_in,Time_out,_Date,Status FROM attendance_record WHERE Department='ITE'")
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
        
        cursor.execute("SELECT Employee_No,Name,Department,Time_in,Time_out,_Date,Status FROM attendance_record WHERE (Employee_No = '" + str(lookup_record) + "' or  Name = '" + str(lookup_record) + "'or Time_in = '" + str(lookup_record) + "' or Time_out = '" + str(lookup_record) + "' or _Date = '" + str(lookup_record) + "' or Status = '" + str(lookup_record) + "') AND Department='ITE'")
        records = cursor.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                data_table_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tag="evenrow")
            else:
                data_table_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tag="oddrow")
            count += 1
            data_table_ite.tag_configure('evenrow', background='#EEEEEE')
            data_table_ite.tag_configure('oddrow', background='#EEEEEE')
            search_ite.delete(0, END)

        conn.commit()
        conn.close()

    def print_data_ite():
        file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

        cols = ['Employee No.','Name','Department','Time in','Time out','Date','Status']
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
        df.to_excel(writer,'sheet1')
        writer.save()
        source = "excelfile/new_datasave_ite.xlsx"
        if file:
            shutil.copy(source,file)
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

    data_table_ite['columns'] = ("Employee No.","Name","Department","Time in","Time out","Date","Status")
    # Format Columns
    data_table_ite.column("#0", width=0, stretch=NO)
    data_table_ite.column("Employee No.", anchor=W, width=150)
    data_table_ite.column("Name", anchor=W, width=100)
    data_table_ite.column("Department", anchor=W, width=200)
    data_table_ite.column("Time in", anchor=W, width=100)
    data_table_ite.column("Time out", anchor=W, width=100)
    data_table_ite.column("Date", anchor=W, width=100)
    data_table_ite.column("Status", anchor=W, width=100)

    # Create Headings
    data_table_ite.heading("Employee No.", text="Employee No.", anchor=CENTER)
    data_table_ite.heading("Name", text="Name", anchor=CENTER)
    data_table_ite.heading("Department", text="Department", anchor=CENTER)
    data_table_ite.heading("Time in", text="Time in", anchor=CENTER)
    data_table_ite.heading("Time out", text="Time out", anchor=CENTER)
    data_table_ite.heading("Date", text="Date", anchor=CENTER)
    data_table_ite.heading("Status", text="Status", anchor=CENTER)

    data_table_ite.bind("<ButtonRelease-1>", select_row_ite)

    refreshTable_ite()

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

        # ComboBox College Department
    ite_department_combobox = ttk.Combobox(ite_att_record, values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
    ite_department_combobox.place(x=445, y=305, width=200)

        # Entry Employee Number
    employee_num_ite = Entry(ite_att_record)
    employee_num_ite.place(x=404, y=366, width=110)

        # Entry Employee Name
    employee_name_ite = Entry(ite_att_record)
    employee_name_ite.place(x=404, y=397, width=110)

        # Entry Attendance Satatus
    att_status_ite = Entry(ite_att_record)
    att_status_ite.place(x=404, y=428, width=110)

        # Entry Time In
    time_in_ite = Entry(ite_att_record)
    time_in_ite.place(x=565, y=366, width=110)

        # Entry Time Out
    time_out_ite = Entry(ite_att_record)
    time_out_ite.place(x=565, y=397, width=110)

        # Entry Date
    date_ite = Entry(ite_att_record)
    date_ite.place(x=565, y=428, width=110)

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
    ite_button_showall.place(x=843, y=608, height=21,width=90)

        # Reset Button
    reset_btn_ite = PhotoImage(file = "pic/btn_reset_small.png")
    ite_button_reset = customtkinter.CTkButton(master=ite_att_record,image=reset_btn_ite, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=reset_ite)
    ite_button_reset.place(x=510, y=519, height=25,width=100)

        # Print Button
    print_btn_ite = PhotoImage(file = "pic/btn_print.png")
    ite_button_print = customtkinter.CTkButton(master=ite_att_record,image=print_btn_ite, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=print_data_ite)
    ite_button_print.place(x=372, y=519, height=25,width=100)

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

     # Data Table "TreeView"
    scrollbary_act = Scrollbar(activity_log, orient=VERTICAL)
    scrollbary_act.place(x=1030, y=230, height=350)

    # style = ttk.Style()
    # style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

    data_table_act = ttk.Treeview(activity_log)
    data_table_act.place(x=290, y=230, width=740, height=350)
    data_table_act.configure(yscrollcommand=scrollbary_act.set)

    scrollbary_act.configure(command=data_table_act.yview)

    data_table_act['columns'] = ("Name","Activity","Department","Time","Date")
    # Format Columns
    data_table_act.column("#0", width=0, stretch=NO)
    data_table_act.column("Name", anchor=CENTER, width=50)
    data_table_act.column("Activity", anchor=CENTER, width=50)
    data_table_act.column("Department", anchor=CENTER, width=50)
    data_table_act.column("Time", anchor=CENTER, width=50)
    data_table_act.column("Date", anchor=CENTER, width=50)

    # Create Headings
    data_table_act.heading("Name", text="Name", anchor=CENTER)
    data_table_act.heading("Activity", text="Activity", anchor=CENTER)
    data_table_act.heading("Department", text="Department", anchor=CENTER)
    data_table_act.heading("Time", text="Time", anchor=CENTER)
    data_table_act.heading("Date", text="Date", anchor=CENTER)

    # Search Entry
    search_entry_att_mon = StringVar()
    search_att_mon = Entry(activity_log, textvariable = search_entry_att_mon)
    search_att_mon.place(x=550, y=171, width=190)

        # Search Button
    search_btn_act = PhotoImage(file = "pic/btn_search.png")
    act_button_search = customtkinter.CTkButton(master=activity_log,image=search_btn_act, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command= "")
    act_button_search.place(x=760, y=170, height=20,width=90)

        # Show All Button
    showall_btn_act = PhotoImage(file = "pic/btn_showall.png")
    act_button_showall = customtkinter.CTkButton(master=activity_log,image=showall_btn_act, text="" ,
                                                corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command="")
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
