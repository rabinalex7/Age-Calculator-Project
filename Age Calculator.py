from tkinter import *
import math
from tkinter import messagebox
from calendar import Calendar
from PIL import Image,ImageTk
from tkcalendar import *
from datetime import datetime,date
from dateutil.relativedelta import relativedelta

window = Tk()

global dob, dob_year, dob_month, dob_day, current_date, current_year, current_month, current_day, d1, d2, age_days, cal, date_window, age, dob_entry

def date_of_birth():
    global dob, dob_year, dob_month, dob_day, dob_entry
    dob = dob_entry.get()  ##strptime(): stands for "string parse time" and is used to convert a string representing a date or time into a datetime object.You need to specify the format that the string is in.
    dob_year = datetime.strptime(dob, "%d-%m-%Y").year
    dob_month = datetime.strptime(dob, "%d-%m-%Y").month
    dob_day = datetime.strptime(dob, "%d-%m-%Y").day

def current_dates():
    global current_date, current_year, current_month, current_day
    current_date = date.today()
    current_date_formatted = current_date.strftime("%d-%m-%Y")  ##strftime():stands for "string format time" and is used to convert a datetime object into a string.
    current_year = datetime.strptime(current_date_formatted, "%d-%m-%Y").year
    current_month = datetime.strptime(current_date_formatted, "%d-%m-%Y").month
    current_day = datetime.strptime(current_date_formatted, "%d-%m-%Y").day

def date_difference():
    global dob, dob_year, dob_month, dob_day, current_date, current_year, current_month, current_day, d1, d2, age_days, cal, date_window, age
    d1 = datetime(dob_year, dob_month, dob_day)
    d2 = datetime(current_year, current_month, current_day)

def reset():
    global dob_entry
    dob_entry.delete(0,END)
    dob_entry.insert(0,"DD-MM-YYYY")

def pick_date(event):
    global cal, date_window
    dob_entry.delete(0,END)
    date_window = Toplevel()
    date_window.grab_set()
    date_window.resizable(0,0)
    date_window.title("select Date Of Birth")
    date_window.geometry("250x220+640+545")
    cal = Calendar(date_window,Selectmode="day",date_pattern="DD-MM-YYYY")
    cal.place(x=0,y=0)

    btn_sub = Button(date_window,text="SUBMIT",font=("times new roman",10),command=grab_date,bg="green",activeforeground="white",activebackground="green",fg="white")
    btn_sub.place(x=150,y=190)
    btn_close = Button(date_window, text=" CLOSE ", font=("times new roman", 10), command=close, bg="red",activeforeground="white", activebackground="red", fg="white")
    btn_close.place(x=50, y=190)

def grab_date():
    dob_entry.delete(0,END)
    dob_entry.insert(0,cal.get_date())
    date_window.destroy()

def exit():
    window.destroy()
def close():
    date_window.destroy()
def key_enter(event):
    age_calculation()

def age_calculation():
    def try_again():
        submit_window.destroy()
    def quit():
        window.destroy()

    global dob, dob_year, dob_month, dob_day, current_date, current_year, current_month, current_day, d1, d2, age_days, age
    try:
        date_window.destroy()
        date_of_birth()
        current_dates()
        date_difference()
        age = relativedelta(d2,d1)
        submit_window = Toplevel()
        submit_window.geometry("600x700+400+10")
        submit_window.config(bg="light blue")
        submit_window.resizable(0,0)
        submit_window.title("RESULT")
        submit_window.attributes("-topmost", True)

        wel_label = Label(submit_window,text="WELCOME !!",font=("times new roman",50,"bold"),bg= "light blue",fg="red")
        wel_label.place(x=80,y=20)
        yr_label = Label(submit_window,text=f"You're {age.years} Years ",font=("times new roman",40,"italic"),bg= "light blue",fg="blue")
        yr_label.place(x=100,y=150)
        mn_label = Label(submit_window,text=f"{age.months} Months & {age.days} Days",font=("times new roman",40,"italic"),bg= "light blue",fg="blue")
        mn_label.place(x=70,y=250)
        old_label = Label(submit_window,text=f" OLD ",font=("times new roman",40,"italic"),bg= "light blue",fg="blue")
        old_label.place(x=200,y=350)
        thk_label = Label(submit_window,text=f" THANK YOU !!",font=("times new roman",40,"bold"),bg= "light blue",fg="green")
        thk_label.place(x=100,y=450)
        submit_window.grab_set()
        submit_window.attributes("-topmost", True)

        btn_tryagain =  Button(submit_window,text="TRY AGAIN",command = try_again,bg="orange",activeforeground="white",activebackground="orange",fg="white",font=("times new roman",15),height=1,width=15)
        btn_tryagain.place(x=80,y=550)

        btn_quit = Button(submit_window,text="QUIT",command = quit,bg="red",activeforeground="white",activebackground="red",fg="white",font=("times new roman",15),height=1,width=15)
        btn_quit.place(x=350,y=550)

    except:
        messagebox.showerror("ERROR","Please! Enter a Valid Input Format(DD-MM-YYYY) with Hyphen(-) Symbol")

def in_days():
    global dob, dob_year, dob_month, dob_day, current_date, current_year, current_month, current_day, d1, d2, age_days, age

    def try_again():
        days_window.destroy()
    def quit():
        window.destroy()
    try:
        date_of_birth()
        current_dates()
        date_difference()
        age_days = d2 - d1

        days_window = Toplevel()
        days_window.geometry("600x700+400+10")
        days_window.config(bg="light blue")
        days_window.resizable(0,0)
        days_window.title("RESULT")
        days_window.attributes("-topmost", True)

        wel_label = Label(days_window,text="WELCOME !!",font=("times new roman",50,"bold"),bg= "light blue",fg="red")
        wel_label.place(x=80,y=20)
        yr_label = Label(days_window,text=f"You're {age_days.days} Days ",font=("times new roman",40,"italic"),bg= "light blue",fg="blue")
        yr_label.place(x=100,y=150)
        old_label = Label(days_window,text=f" OLD ",font=("times new roman",40,"italic"),bg= "light blue",fg="blue")
        old_label.place(x=200,y=250)
        thk_label = Label(days_window,text=f" THANK YOU !!",font=("times new roman",40,"bold"),bg= "light blue",fg="green")
        thk_label.place(x=100,y=350)
        days_window.grab_set()
        days_window.attributes("-topmost", True)

        btn_tryagain =  Button(days_window,text="TRY AGAIN",command = try_again,bg="orange",activeforeground="white",activebackground="orange",fg="white",font=("times new roman",15),height=1,width=15)
        btn_tryagain.place(x=80,y=550)

        btn_exit = Button(days_window,text="QUIT",command = quit,bg="red",activeforeground="white",activebackground="red",fg="white",font=("times new roman",15),height=1,width=15)
        btn_exit.place(x=350,y=550)
    except:
        messagebox.showerror("ERROR","Please! Enter a Valid Input Format(DD-MM-YYYY) with Hyphen(-) Symbol")

def in_weeks():
    global dob, dob_year, dob_month, dob_day, current_date, current_year, current_month, current_day, d1, d2, age_days, age

    def try_again():
        week_window.destroy()
    def quit():
        window.destroy()

    try:
        date_of_birth()
        current_dates()
        date_difference()
        age_days = d2 - d1
        age_in_weeks = (round(age_days.days//7)) + (round((age_days.days%7)/7,1))
        age_week_weeks = round(age_days.days//7)
        age_week_days  = round(age_days.days%7)

        week_window = Toplevel()
        week_window.geometry("600x700+400+10")
        week_window.config(bg="light blue")
        week_window.resizable(0, 0)
        week_window.title("RESULT")
        week_window.attributes("-topmost", True)

        wel_label = Label(week_window, text="WELCOME !!", font=("times new roman", 50, "bold"), bg="light blue",fg="red")
        wel_label.place(x=80, y=20)
        yr_label = Label(week_window, text=f"You're {age_in_weeks} Weeks OLD", font=("times new roman", 40, "italic"),bg="light blue", fg="blue")
        yr_label.place(x=20, y=150)
        mn_label = Label(week_window, text=f"{age_week_weeks} Weeks & {age_week_days} Days OLD",font=("times new roman", 40, "italic"), bg="light blue", fg="blue")
        mn_label.place(x=5, y=350)
        old_label = Label(week_window, text=f" (OR) ", font=("times new roman", 40, "italic"), bg="light blue",fg="brown")
        old_label.place(x=200, y=250)
        thk_label = Label(week_window, text=f" THANK YOU !!", font=("times new roman", 40, "bold"), bg="light blue",fg="green")
        thk_label.place(x=100, y=450)
        week_window.grab_set()
        week_window.attributes("-topmost", True)

        btn_tryagain = Button(week_window, text="TRY AGAIN", command=try_again, bg="orange", activeforeground="white",activebackground="orange", fg="white", font=("times new roman", 15), height=1, width=15)
        btn_tryagain.place(x=80, y=550)

        btn_exit = Button(week_window, text="QUIT", command=quit, bg="red", activeforeground="white",activebackground="red", fg="white", font=("times new roman", 15), height=1, width=15)
        btn_exit.place(x=350, y=550)
    except:
        messagebox.showerror("ERROR","Please! Enter a Valid Input Format(DD-MM-YYYY) with Hyphen(-) Symbol")

def in_months():
    global dob, dob_year, dob_month, dob_day, current_date, current_year, current_month, current_day, d1, d2, age_days, age

    def try_again():
        month_window.destroy()
    def quit():
        window.destroy()

    try:
        date_of_birth()
        current_dates()
        date_difference()
        age_days = d2 - d1
        age = relativedelta(d2,d1)

        total = 0
        if (dob_month > 2) and (current_month < 2):
            for i in range(dob_year+1,current_year):
                if (i%4==0 and i%100!=0) or (i%400==0 and i%100==0):
                    total +=1
        elif (dob_month <= 2) and (current_month < 2):
            for i in range(dob_year,current_year):
                if (i%4==0 and i%100!=0) or (i%400==0 and i%100==0):
                    total +=1
        elif (dob_month > 2) and (current_month >= 2):
            for i in range(dob_year+1, current_year+1):
                if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0 and i % 100 == 0):
                    total +=1
        elif (dob_month <= 2) and (current_month > 2):
            for i in range(dob_year,current_year+1):
                if (i%4==0 and i%100!=0) or (i%400==0 and i%100==0):
                    total +=1
        else:
            for i in range(dob_year,current_year):
                if (i%4==0 and i%100!=0) or (i%400==0 and i%100==0):
                    total += 1

        leap_years_count = total

        years = (age_days.days - leap_years_count)/365
        age_in_months = round(years*12,2)
        tup = math.modf(age_in_months)
        t1 = round(tup[0],3)
        t2 = round(tup[1])

        month_window = Toplevel()
        month_window.geometry("600x700+400+10")
        month_window.config(bg="light blue")
        month_window.resizable(0,0)
        month_window.title("RESULT")
        month_window.attributes("-topmost", True)

        wel_label = Label(month_window,text="WELCOME !!",font=("times new roman",50,"bold"),bg= "light blue",fg="red")
        wel_label.place(x=80,y=20)
        yr_label = Label(month_window, text=f"You're {age_in_months} months OLD", font=("times new roman", 40, "italic"),bg="light blue", fg="blue")
        yr_label.place(x=5, y=150)
        mn_label = Label(month_window, text=f"{t2} Months & {age.days} Days OLD",font=("times new roman", 40, "italic"), bg="light blue", fg="blue")
        mn_label.place(x=5, y=350)
        old_label = Label(month_window, text=f" (OR) ", font=("times new roman", 40, "italic"), bg="light blue",fg="brown")
        old_label.place(x=200, y=250)
        thk_label = Label(month_window,text=f" THANK YOU !!",font=("times new roman",40,"bold"),bg= "light blue",fg="green")
        thk_label.place(x=100,y=450)
        month_window.grab_set()
        month_window.attributes("-topmost", True)

        btn_tryagain =  Button(month_window,text="TRY AGAIN",command = try_again,bg="orange",activeforeground="white",activebackground="orange",fg="white",font=("times new roman",15),height=1,width=15)
        btn_tryagain.place(x=80,y=550)

        btn_exit = Button(month_window,text="QUIT",command = quit,bg="red",activeforeground="white",activebackground="red",fg="white",font=("times new roman",15),height=1,width=15)
        btn_exit.place(x=350,y=550)
    except:
        messagebox.showerror("ERROR","Please! Enter a Valid Input Format(DD-MM-YYYY) with Hyphen(-) Symbol")

window.resizable(0,0)
window.title("AGE CALCULATOR")
icon = PhotoImage(file="img.png")
window.iconphoto(True,icon)
window.geometry("600x700+400+10")
window.config(bg="#FFFFFF")
img = Image.open("img_1.png")
age_img = ImageTk.PhotoImage(img)

label = Label(window,image=age_img,compound=TOP)
label.pack()
label = Label(window,text="AGE CALCULATOR",bg="white",fg="red",font=("times new roman",30,"underline"))
label.pack()
dob_label = Label(window,text="Date Of Birth :",bg="white",fg="green",font=("times new roman",15))
dob_label.place(x=110,y=475)
dob_entry = Entry(window,bg="light blue",fg="red",font=("times new roman",15),highlightthickness=0,relief=FLAT)
dob_entry.place(x=240,y=475,width=250)
dob_entry.insert(0,"DD-MM-YYYY")
dob_entry.bind("<1>",pick_date)
dob_entry.bind("<Return>",key_enter)

btn_submit = Button(window,text="SUBMIT",command=age_calculation,bg="green",activeforeground="white",activebackground="green",fg="white",font=("times new roman",15),height=1,width=15)
btn_submit.place(x=125,y=550)
btn_reset = Button(window,text="RESET",command=reset,bg="red",activeforeground="white",activebackground="red",fg="white",font=("times new roman",15),height=1,width=15)
btn_reset.place(x=300,y=550)
btn_days = Button(window,text="IN DAYS",command=in_days,bg="light green",activeforeground="black",activebackground="light blue",fg="black",font=("times new roman",15),height=1,width=15)
btn_days.place(x=380,y=600)
btn_months = Button(window,text="IN MONTHS",command=in_months,bg="light green",activeforeground="black",activebackground="light blue",fg="black",font=("times new roman",15),height=1,width=15)
btn_months.place(x=35,y=600)
btn_weeks = Button(window,text="IN WEEKS",command=in_weeks,bg="light green",activeforeground="black",activebackground="light blue",fg="black",font=("times new roman",15),height=1,width=15)
btn_weeks.place(x=210,y=600)
btn_exit = Button(window,text="EXIT",command=exit,bg="orange",activeforeground="white",activebackground="orange",fg="white",font=("times new roman",15),height=1,width=15)
btn_exit.place(x=210,y=650)

window.mainloop()