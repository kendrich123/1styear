#  Calingin, Ken Drich L.

from tkinter import *               # For tkinter
from tkinter import messagebox      # For the messagebox
import os                           # To find the txt file
import json                         # To get the data from the txt file
from tkinter.ttk import Combobox    # For the combobox

final = Tk()  # Create window
final.geometry('1200x700')  # Window size
final.resizable(False, False)  # Make the window not resizable
final.title('Student Information Trial')  # Window title


def main():

    def records():  # Display all the data inputted
        record_display.configure(state="normal")
        record_display.delete(1.0, END)

        if not student_list:
            record_display.insert(END, "No record yet")

        else:
            # Sort the student list by last name
            sorted_student_list = sorted(student_list.items(), key=lambda x: x[1][0]['lastname'])

            # Loop through the sorted student list and display the information
            for i, (key, value) in enumerate(sorted_student_list, start=1):
                pair = str(i) + ". " + key + "    " + value[0]['lastname'] + ", " + value[0]['firstname'] + "\n \n"
                record_display.insert(END, pair)

        record_display.configure(state="disabled")

    def search():  # Search Student ID to see data
        display_info = box_all.get()
        if display_info in student_list:
            for i in student_list[display_info]:
                messagebox.showinfo('STUDENT INFORMATION    ', "----------------------------------------"
                                                               "\n  Student ID: " + display_info +
                                    "\n  Last Name: " + i['lastname'] +
                                    "\n  First Name: " + i['firstname'] +
                                    "\n  Middle Name: " + i['middlename'] +
                                    "\n  Gender: " + i['gender'] +
                                    "\n  Email: " + i['email'] +
                                    "\n  Contact#: " + i['contact'] +
                                    "\n  Address: " + i['address'] +
                                    "\n  Emergency Contact"
                                    "\n  Name: " + i['emergencyname'] +
                                    "\n  Contact#: " + i['emergencycontact'] +
                                    "\n  Program: " + i['program'] +
                                    "\n  Course: " + i['course'] +
                                    "\n  Year: " + i['year'] +
                                    "\n  Midterm: " + i['midterm'] +
                                    "\n  Final: " + i['final'] +
                                    "\n----------------------------------------")

        else:
            messagebox.showerror('STUDENT INFORMATION    ', "No ID Found")

    def add():  # Add the data (list) to its corresponding Student ID in the dictionary
        result = messagebox.askyesno('STUDENT INFORMATION', "Do you want to add ?")
        if result:
            get_id = box_id.get()
            student_list[get_id] = added()
            clear()
            messagebox.showinfo('STUDENT INFORMATION    ', "Data Added")

        else:
            final.update()

    def added():
        info = []  # A list for the dictionary (student id)
        last = box_lastname.get()
        first = box_firstname.get()
        middle = box_middle_name.get()
        gender = select_gender.get()
        email0 = box_email.get()
        contact = box_contact_num.get()
        address = box_address.get()
        emergency_name = box_emergency_name.get()
        emergency_contact = box_emergency_contact.get()
        program = select_program.get()
        course = select_course.get()
        year = select_year.get()
        midterm = box_midterm.get()
        final0 = box_final.get()

        info.append({'lastname': last, 'firstname': first, 'middlename': middle, 'gender': gender, 'email': email0,
                     'contact': contact, 'address': address, 'emergencyname': emergency_name,
                     'emergencycontact': emergency_contact, 'program': program, 'course': course, 'year': year,
                     'midterm': midterm, 'final': final0})

        return info

    def delete():  # Delete a data via Student ID
        get_id = box_all.get()
        result = messagebox.askyesno('STUDENT INFORMATION', "Do you want to delete ?")
        if result:
            if get_id in student_list:
                del student_list[get_id]
                messagebox.showinfo('STUDENT INFORMATION', "Deleted")
                return student_list

            else:
                messagebox.showerror('STUDENT INFORMATION', "No ID Found")

        else:
            final.update()

    def edit():  # Edit a data using Student ID
        get_id = box_all.get()
        check = box_id.get()
        if get_id in student_list:
            if not check == box_all.get():
                for i in student_list[get_id]:
                    box_id.insert(END, get_id)
                    box_lastname.insert(END, i['lastname'])
                    box_firstname.insert(END, i['firstname'])
                    box_middle_name.insert(END, i['middlename'])
                    select_gender.set(i['gender'])
                    box_email.insert(END, i['email'])
                    box_contact_num.insert(END, i['contact'])
                    box_address.insert(END, i['address'])
                    box_emergency_name.insert(END, i['emergencyname'])
                    box_emergency_contact.insert(END, i['emergencycontact'])
                    select_program.set(i['program'])
                    select_course.set(i['course'])
                    select_year.set(i['year'])
                    box_midterm.insert(END, i['midterm'])
                    box_final.insert(END, i['final'])

        else:
            messagebox.showerror('STUDENT INFORMATION', "No ID Found")

    def clear():  # Clear inputs on screen
        box_id.delete(0, END)
        box_lastname.delete(0, END)
        box_firstname.delete(0, END)
        box_middle_name.delete(0, END)
        select_gender.set("")
        box_email.delete(0, END)
        box_contact_num.delete(0, END)
        box_address.delete(0, END)
        box_emergency_name.delete(0, END)
        box_emergency_contact.delete(0, END)
        select_program.set("")
        select_course.set("")
        select_year.set("")
        box_midterm.delete(0, END)
        box_final.delete(0, END)
        box_all.delete(0, END)
        box_file.delete(0, END)

    def create_file():  # Create a txt file
        get_file = box_file.get()
        if not os.path.isfile(get_file):
            txt_file = open(get_file, 'x')  # Create txt file

            txt_file.close()
            messagebox.showinfo('STUDENT INFORMATION    ', "File created")
        else:
            messagebox.showerror('STUDENT INFORMATION    ', "File already exist")

    def open_file():  # Opens a txt file and gets the data
        get_file = box_file.get()
        if os.path.isfile(get_file):
            if os.path.getsize(get_file) > 0:
                with open(get_file, 'r') as txt_file:
                    saved_file = json.load(txt_file)
                    student_list.update(saved_file)
                messagebox.showinfo('STUDENT INFORMATION    ', "File opened")
            else:
                messagebox.showerror('STUDENT INFORMATION    ', "File empty")

        else:
            messagebox.showerror('STUDENT INFORMATION    ', "File doesn't exist")

    def save_file():  # Saves the data in the inputted txt file
        get_file = box_file.get()
        if os.path.isfile(get_file):
            if os.path.getsize(get_file) > 0:
                with open(get_file, 'r+') as txt_file:
                    saved_file = json.load(txt_file)
                    student_list.update(saved_file)
                    json.dump(student_list, txt_file, indent=2)  # Save the data (dictionary) in the txt file
                messagebox.showinfo('STUDENT INFORMATION    ', "Data saved")

            else:
                with open(get_file, 'w') as txt_file:
                    json.dump(student_list, txt_file, indent=2)  # Save the data (dictionary) in the txt file
                messagebox.showinfo('STUDENT INFORMATION    ', "Data saved")

        else:
            messagebox.showerror('STUDENT INFORMATION    ', "File doesn't exist")

    def main_select(i):
        selected_item = select_program.get()
        update_select(selected_item)

    def update_select(selected_item):
        select_course['values'] = choices[selected_item]
        select_course.current(0)

    student_list = {}  # Create a dictionary to save data (list) in its corresponding student ID

    select_gender = StringVar()  # Gets the value selected in the option menu (gender)
    select_year = StringVar()  # Gets the value selected in the option menu (year)
    selection_gender = ["Male", "Female"]
    selection_year = ["1st Year", "2nd Year", "3rd Year", "4th Year", "5th Year", "6th Year", "7th Year", "8th Year"]

    choices = {
        'College of Engineering and Architecture': ('Bachelor of Science in Architecture',
                                                    'Bachelor of Science in Civil Engineering',
                                                    'Bachelor of Science in Mechanical Engineering',
                                                    'Bachelor of Science in Computer Engineering',
                                                    'Bachelor of Science in Geodetic Engineering',
                                                    'Bachelor of Science in Electrical Engineering',
                                                    'Bachelor of Science in Electronics Engineering'),
        'College of Information Technology and Computing': ('Bachelor of Science in Information Technology',
                                                            'Bachelor of Science in Technology Communication Management',
                                                            'Bachelor of Science in Data Science',
                                                            'Bachelor of Science in Computer Science'),
        'College of Science and Mathematics': ('Bachelor of Science in Applied Mathematics',
                                               'Bachelor of Science in Applied Physics',
                                               'Bachelor of Science in Chemistry',
                                               'Bachelor of Science in Environmental Science',
                                               'Bachelor of Science in Food Technology'),
        'College of Science and Technology Education': ('Bachelor in Secondary Education Major in Science',
                                                        'Bachelor of Secondary Education Major in Mathematics',
                                                        'Bachelor in Technology and Livelihood Education',
                                                        'Bachelor in Technical-Vocational Teacher Education'),
        'College of Technology': ('Bachelor of Science in Electronics Technology', 'Bachelor of Science in Autotronics',
                                  'Bachelor of Science in Energy Systems and Management',
                                  'Bachelor of Science in Electro-Mechanical Technology',
                                  'Bachelor of Science in Manufacturing Engineering Technology')
    }

    # Create the first Combobox
    select_program = Combobox(final, width=40, font=("Georgia", 10))
    select_program['values'] = tuple(choices.keys())
    select_program.bind("<<ComboboxSelected>>", main_select)

    # Create the second Combobox
    select_course = Combobox(final, width=40, font=("Georgia", 10))

    # Add a text widget to display record
    record_display = Text(final, font=("Georgia", 15))
    record_display.place(x=815, y=250, relwidth=0.3, relheight=0.63)

    # Add a scrollbar to the text widget (vertical)
    scroll = Scrollbar(final, orient='vertical', command=record_display.yview)
    scroll.place(x=1180, y=250, relwidth=0.017, relheight=0.63)

    # Configure the text widget to use the scrollbar
    record_display.configure(yscrollcommand=scroll.set)

    # Label for instructions
    instruct = ("\nThis program runs on Student ID\n"  # Variable that holds the instructions (str)
                "\nAdd/Update - Saves what you input\n"
                "Clear - Easily clear what you input\n"
                "Records - To see all you've saved data in the board\n"
                "Search - Particularly find and see full info of a student\n"
                "Edit - Appears what you have already inputted data for\nthat particular student so you can easily"
                " edit it\n(Click Add/Update to save the edited data)\n"
                "Delete - Deletes a particular student(Data)\n"
                "Create - Creates a file if you don't have one\n"
                "Open - Opens a file if you have already have one\n"
                "Save - Saves your data inputted in the file")
    instruct_display = Label(final, text=instruct, font=('Georgia', 10), justify=LEFT)
    instruct_display.place(x=440, y=400, relwidth=0.3, relheight=0.35)

    # Create labels
    display_id = Label(final, text="Student ID: ", font=('Georgia', 10))
    display_lastname = Label(final, text="Last Name: ", font=('Georgia', 10))
    display_firstname = Label(final, text="First Name: ", font=('Georgia', 10))
    display_middle_name = Label(final, text="Middle Name: ", font=('Georgia', 10))
    display_gender = Label(final, text="Gender: ", font=('Georgia', 10))
    display_email = Label(final, text="Email: ", font=('Georgia', 10))
    display_contact_num = Label(final, text="Contact#: ", font=('Georgia', 10))
    display_address = Label(final, text="Address: ", font=('Georgia', 10))
    display_emergency = Label(final, text="Emergency Contact", font=('Georgia', 10))
    display_emergency_name = Label(final, text="Name: ", font=('Georgia', 10))
    display_emergency_contact = Label(final, text="Contact#: ", font=('Georgia', 10))
    display_program = Label(final, text="Program: ", font=('Georgia', 10))
    display_course = Label(final, text="Course: ", font=('Georgia', 10))
    display_year = Label(final, text="Year: ", font=('Georgia', 10))
    display_grade = Label(final, text="Grade", font=('Georgia', 10))
    display_midterm = Label(final, text="Midterm: ", font=('Georgia', 10))
    display_final = Label(final, text="Final: ", font=('Georgia', 10))

    # Create entries and option menu
    box_id = Entry(final)
    box_lastname = Entry(final)
    box_firstname = Entry(final)
    box_middle_name = Entry(final)
    box_gender = OptionMenu(final, select_gender, *selection_gender)
    box_email = Entry(final)
    box_contact_num = Entry(final)
    box_address = Entry(final)
    box_emergency_name = Entry(final)
    box_emergency_contact = Entry(final)
    box_year = OptionMenu(final, select_year, *selection_year)
    box_midterm = Entry(final)
    box_final = Entry(final)
    box_all = Entry(final)
    box_file = Entry(final)

    # Create buttons
    button_records = Button(final, text="Records", command=records)
    button_search = Button(final, text="Search", command=search)
    button_add = Button(final, text="Add/Update", command=add)
    button_edit = Button(final, text="Edit", command=edit)
    button_delete = Button(final, text="Delete", command=delete)
    button_clear = Button(final, text="Clear", command=clear)
    button_create = Button(final, text="Create", command=create_file)
    button_open = Button(final, text="Open", command=open_file)
    button_save = Button(final, text="Save", command=save_file)

    # Display labels
    display_id.place(x=90, y=50)
    display_lastname.place(x=340, y=50)
    display_firstname.place(x=590, y=50)
    display_middle_name.place(x=840, y=50)
    display_gender.place(x=90, y=100)
    display_email.place(x=340, y=100)
    display_contact_num.place(x=590, y=100)
    display_address.place(x=840, y=100)
    display_emergency.place(x=240, y=150)
    display_emergency_name.place(x=90, y=200)
    display_emergency_contact.place(x=340, y=200)
    display_program.place(x=90, y=250)
    display_course.place(x=90, y=300)
    display_year.place(x=590, y=250)
    display_grade.place(x=740, y=150)
    display_midterm.place(x=590, y=200)
    display_final.place(x=840, y=200)

    # Display entries, option menu and buttons
    box_id.place(x=190, y=50)
    box_lastname.place(x=440, y=50)
    box_firstname.place(x=690, y=50)
    box_middle_name.place(x=940, y=50)
    box_gender.place(x=190, y=95)
    box_email.place(x=440, y=100)
    box_contact_num.place(x=690, y=100)
    box_address.place(x=940, y=100)
    box_emergency_name.place(x=190, y=200)
    box_emergency_contact.place(x=440, y=200)
    select_program.place(x=190, y=250)
    select_course.place(x=190, y=300)
    box_year.place(x=690, y=245)
    box_midterm.place(x=690, y=200)
    box_final.place(x=940, y=200)
    box_all.place(x=100, y=400)
    box_file.place(x=100, y=450)
    button_search.place(x=250, y=397)
    button_add.place(x=690, y=295)
    button_edit.place(x=320, y=397)
    button_delete.place(x=380, y=397)
    button_clear.place(x=690, y=345)
    button_records.place(x=690, y=395)
    button_create.place(x=250, y=447)
    button_open.place(x=320, y=447)
    button_save.place(x=380, y=447)


account = []


def signin():

    def verify():
        user = box_user.get()
        password = box_pass.get()

        with open('account.txt', 'r') as txt_file:
            saved_file = json.load(txt_file)
            for entry in saved_file:
                if entry not in account:
                    account.append(entry)

        for acc in account:
            if acc['username'] == user and acc['password'] == password:
                messagebox.showinfo('STUDENT INFORMATION', "Hello, " + acc['name'].capitalize())

                display_signin.pack_forget()
                box_user.pack_forget()
                box_pass.pack_forget()
                button_signin.pack_forget()
                display_signup.pack_forget()
                button_signup.pack_forget()
                main()

                break

            elif acc['username'] == user and acc['password'] != password:
                messagebox.showerror('STUDENT INFORMATION', "Wrong Password")
                break

            elif acc['username'] != user:
                messagebox.showerror('STUDENT INFORMATION', "Wrong Username")
                break

    def signup_proceed():
        display_signin.pack_forget()
        box_user.pack_forget()
        box_pass.pack_forget()
        button_signin.pack_forget()
        display_signup.pack_forget()
        button_signup.pack_forget()
        signup()

    def user_enter(i):
        box_user.delete(0, END)

    def user_leave(i):
        user = box_user.get()
        if user == '':
            box_user.insert(0, 'Username')

    def pass_enter(i):
        box_pass.delete(0, END)

    def pass_leave(i):
        password = box_pass.get()
        if password == '':
            box_pass.insert(0, 'Password')

    display_signin = Label(final, text="Sign In")
    display_signup = Label(final, text="Don't have an account?")

    box_user = Entry(final, width=20, font=('Georgia', 12), justify=CENTER)
    box_user.insert(0, 'Username')
    box_user.bind('<FocusIn>', user_enter)
    box_user.bind('<FocusOut>', user_leave)

    box_pass = Entry(final, width=20, font=('Georgia', 12), justify=CENTER)
    box_pass.insert(0, 'Password')
    box_pass.bind('<FocusIn>', pass_enter)
    box_pass.bind('<FocusOut>', pass_leave)

    button_signin = Button(final, text='Sign In', border=1, width=10, font=('Georgia', 12), command=verify)
    button_signup = Button(final, text='Sign Up', border=0, font=('Georgia', 12), fg='skyblue', command=signup_proceed)

    display_signin.pack(pady=(250, 0))
    box_user.pack(pady=10)
    box_pass.pack(pady=10)
    button_signin.pack(pady=10)
    display_signup.pack(pady=(10, 0))
    button_signup.pack()

    # display_signup.place(x=510, y=95)
    # button_signup.place(x=640, y=95)


def signup():
    if not os.path.isfile('account.txt'):
        txt_file_acc = open('account.txt', 'x')

        txt_file_acc.close()

    def create():

        created()
        if os.path.getsize('account.txt') > 0:
            with open('account.txt', 'r+') as txt_file:
                saved_file = json.load(txt_file)
                for entry in saved_file:
                    if entry not in account:
                        account.append(entry)
                txt_file.seek(0)
                json.dump(account, txt_file, indent=2)
                txt_file.truncate()

        else:
            with open('account.txt', 'w') as txt_file:
                json.dump(account, txt_file, indent=2)

    def created():
        name = box_name.get()
        user = box_user.get()
        password = box_pass.get()
        confirm = box_confirm_pass.get()

        if name == '' or name == 'Name' or user == '' or user == 'Username' or password == '' or password == 'Password':
            messagebox.showerror('STUDENT INFORMATION', "Invalid blank input")
        elif password == confirm:
            # Extract every username and names value
            usernames = [value['username'] for value in account]
            names = [i['name'] for i in account]

            if user in usernames:
                messagebox.showerror('STUDENT INFORMATION', "Username already exist")
            elif name in names:
                messagebox.showerror('STUDENT INFORMATION', "Name already exist")
            else:
                account.append({'username': user, 'password': password, 'name': name})
                messagebox.showinfo('STUDENT INFORMATION', "Account Created")
        else:
            messagebox.showerror('STUDENT INFORMATION', "Passwords don't match")

    def signin_proceed():
        display_signup.pack_forget()
        display_signin.pack_forget()
        box_name.pack_forget()
        box_user.pack_forget()
        box_pass.pack_forget()
        box_confirm_pass.pack_forget()
        button_create.pack_forget()
        button_signin.pack_forget()
        signin()

    def name_enter(i):
        box_name.delete(0, END)

    def name_leave(i):
        name = box_name.get()
        if name == '':
            box_name.insert(0, 'Name')

    def user_enter(i):
        box_user.delete(0, END)

    def user_leave(i):
        user = box_user.get()
        if user == '':
            box_user.insert(0, 'Username')

    def pass_enter(i):
        box_pass.delete(0, END)

    def pass_leave(i):
        password = box_pass.get()
        if password == '':
            box_pass.insert(0, 'Password')

    def confirm_pass_enter(i):
        box_confirm_pass.delete(0, END)

    def confirm_pass_leave(i):
        password = box_confirm_pass.get()
        if password == '':
            box_confirm_pass.insert(0, 'Confirm Password')

    display_signup = Label(final, text="Sign Up")
    display_signin = Label(final, text="I have an account")

    box_name = Entry(final, width=20, font=('Georgia', 12), justify=CENTER)
    box_name.insert(0, 'Name')
    box_name.bind('<FocusIn>', name_enter)
    box_name.bind('<FocusOut>', name_leave)

    box_user = Entry(final, width=20, font=('Georgia', 12), justify=CENTER)
    box_user.insert(0, 'Username')
    box_user.bind('<FocusIn>', user_enter)
    box_user.bind('<FocusOut>', user_leave)

    box_pass = Entry(final, width=20, font=('Georgia', 12), justify=CENTER)
    box_pass.insert(0, 'Password')
    box_pass.bind('<FocusIn>', pass_enter)
    box_pass.bind('<FocusOut>', pass_leave)

    box_confirm_pass = Entry(final, width=20, font=('Georgia', 12), justify=CENTER)
    box_confirm_pass.insert(0, 'Confirm Password')
    box_confirm_pass.bind('<FocusIn>', confirm_pass_enter)
    box_confirm_pass.bind('<FocusOut>', confirm_pass_leave)

    button_create = Button(final, text='Create', border=1, width=10, font=('Georgia', 12), command=create)
    button_signin = Button(final, text='Sign In', border=0, font=('Georgia', 12), fg='skyblue', command=signin_proceed)

    display_signup.pack(pady=(250, 0))
    box_name.pack(pady=10)
    box_user.pack(pady=10)
    box_pass.pack(pady=10)
    box_confirm_pass.pack(pady=10)
    button_create.pack(pady=10)
    display_signin.pack(pady=(10, 0))
    button_signin.pack()


signin()

final.mainloop()  # makes it loop infinitely

#  Calingin, Ken Drich L.
