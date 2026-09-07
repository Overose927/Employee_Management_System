#James Smidt
#CIS261
#Employee Management System
#Phase 4

from datetime import datetime

#Employee class with an init constructor that: accepts parameters self, first_name, last_name, employee_id, hours, rate, and record_date_str=None; Handles
#record_date if none and if it is provided converts string to datetime, initialize atrributes: gross_pay, deductions, and net_pay to 0.0, and automatically
#calls the calculation methods calculate_gross_pay, calculate_deductions, and calculate_net_pay.
class Employee:
    def __init__(self, first_name, last_name, employee_id, hours, rate, record_date_str=None):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.hours = hours
        self.rate = rate
        if record_date_str is None:
            self.record_date = datetime.now()
        else:
            self.record_date = datetime.strptime(record_date_str, "%Y-%m-%d")
        self.gross_pay = 0.0
        self.deductions = 0.0
        self.net_pay = 0.0
        self.calculate_gross_pay()
        self.calculate_deductions()
        self.calculate_net_pay()
    
#Method calculate_gross_pay that calculates gross pay with overtime and stores in self.gross_pay.
    def calculate_gross_pay(self):
        if self.hours > 40:                               #greater 40 hours
            base_pay = 40 * self.rate
            overtime_pay = (self.hours - 40) * (self.rate * 1.5)
            self.gross_pay = base_pay + overtime_pay
        else:
            self.gross_pay = self.hours * self.rate            #up to 40 hours

#Method calculate_deeductions that calculates 25% of gross_pay and stores as self.deductions
    def calculate_deductions(self):
        self.deductions = self.gross_pay * 0.25

#Method calculate_net_pay that calculates gross_pay - deductions and stores in self.net_pay
    def calculate_net_pay(self):
        self.net_pay = self.gross_pay - self.deductions

#Method worked_overtime that returns true if an employee worked more than 40 hours, false is less than 40 hours
    def worked_overtime(self):
        return self.hours > 40

#Method is_high_earner(minimum = 1000) that returns true if gross pay is greater than the minimum, false if less than minimum
    def is_high_earner(self):
        minimum = 1000
        return self.gross_pay > minimum

#Method to_file_string that returns pipe_delimited string for file storage and has 9 fields
    def to_file_string(self):
        record_date_str = self.record_date.strftime("%Y-%m-%d")
        return f"{self.first_name}|{self.last_name}|{self.employee_id}|{self.hours}|{self.rate}|{self.gross_pay}|{self.deductions}|{self.net_pay}|{record_date_str}"

#Method __str__ that returns formatted string for display
    def __str__(self):
        record_str = self.record_date.strftime("%Y-%m-%d")
        return (f"Date:          {record_str}\n"
                f"Name:          {self.first_name} {self.last_name}\n"
                f"Employee ID:   {self.employee_id}\n"
                f"Hours Worked:  {self.hours:,.1f}\n"
                f"Hourly Rate:   {self.rate:,.2f}\n"
                f"Gross Pay:     {self.gross_pay:,.2f}\n"
                f"Deductions:    {self.deductions:,.2f}\n"
                f"Net Pay:       {self.net_pay:,.2f}\n"
                )

#Class HRUser with an init constructor that accepts the parameters username, password, role, and full_name, uses self to store all parameters as attributes,
#and the only accepted roles to be either HR Manager and HR Staff
class HRUser:
    def __init__(self, username, password, role, full_name):
        self.username = username
        self.password = password
        if role == "HR Manager" or role =="HR Staff":
            self.role = role
        self.full_name = full_name
        
#Security function called create_default_users that creates and returns a list with 2 default HRUser objects, HRManager and HRStaff
def create_default_users():
    users = []
    hr_manager = HRUser("hrmanager", "hr2024", "HR Manager", "Admin User")
    users.append(hr_manager)
    hr_staff = HRUser("hrstaff", "staff123", "HR Staff", "Staff User")
    users.append(hr_staff)
    return users

#Function called display_login_screen that display login prompt with system title
def display_login_screen():
    print("=" * 50)
    print("EMPLOYEE MANAGEMENT SYSTEM - SECURE LOGIN PORTAL")
    print("=" * 50)
    print("Please login using your username and password to continue.")
    print("=" * 50 +"\n")

#Function called authenicate_user with users, username, and password as the parameters that loops through the users list, compares entered username and password
#with each user, and returns the HRUser object if match found and None if not found
def authenicate_user(users, username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None

#Function called display_access_granted with username and role as the parameters that displays a success message with username and role and shows the 
#permissions based on the role.
def display_access_granted(username, role):
    print(f"Welcome, {username} has successfully signed in.")
    print(f"You are signed in as {role}")
    if role == "HR Manager":
        print("Full-access:  Process Employee Records, Generate Reports, and Manage User Accounts")
    else:
        print(f"\nRead-Only Access:  Generate Reports Only.")
    print("=" * 50)
    input("\nPress Enter to Continue...")

#Function called display_access_denied that displays an access denied message
def display_access_denied():
    print("\n" + "=" * 50)
    print("ACCESS DENIED")
    print("=" * 50)
    print("Invalid Username or password.")
    print("=" * 50 + "\n")

#User management called add_new_user with users as the parameter.  It Prompts for: username, password, roll, and full_name, creates a new HRUser object,
#appends to users list, and displays confirmationm message.
def add_new_user(users):
    print("\n" + "=" * 50)
    print("When prompted input the username, password, role, and full name of the employee you want to add to the record.")
    print("=" * 50)
    while True:
        username = input("Enter the username of the employee being added:  ")
        password = input("Enter the password of the employee added:  ")
        password_test = input("Reenter the password to validate:  ")
        while password != password_test:
            print("Passwords do not match please try again.")
            password = input("Enter the password of the employee added:  ")
            password_test = input("Reenter the password to validate:  ")
        role = input("Please specify the security role for the employee (1 - HR Manager / 2 - HR Staff):  ")
        while role not in ["1", "2"]:
            role = input("Invalid response please press 1 for HR Manager or 2 for HR Staff")
        if role == "1":
            role = "HR Manager"
        else:
            role = "HR Staff"
        full_name = input("Please enter the employees first and last name:  ")
        user = HRUser(username, password, role, full_name)
        users.append(user)
        print("=" * 50)
        print(f"User record has successfully updated with the new user {username}")
        decision = input("Do you want to input an additional user? (1 - Yes, 2 - No):  ")
        while decision not in ["1", "2"]:
            decision = input("Invalid entry, please type 1 to continue or 2 to exit:  ")
        if decision == "2":
            return users
        print("=" * 50 + "\n")

#Function called display_all_users that accepts users as a parameter that displays all users without showing password.
def display_all_users(users):
    print("\n" + "=" * 50)
    print("List of all users in record: ")
    for user in users:
        print(f"Username:   {user.username}")
        print(f"Role:       {user.role}")
        print(f"Name:       {user.full_name}")
        print("=" * 50)
    input("Press Enter to return to User Management Menu.")

#Function called save_users_to_file with users and filename as the parameter that writes users to file in pipe-delimiting format, and uses try except for error handling
def save_users_to_file(users, filename):
    try:
        with open(filename, 'w') as file:
            for user in users:
                line = f"{user.username}|{user.password}|{user.role}|{user.full_name}"
                file.write(line + "\n")
        print("\n" + "=" * 50)
        print("FILE SAVE SUCCESSFUL")
        print("=" * 50)
        print(f"Saved {len(users)} record(s) to: {filename}")
        print("=" * 50)
    except Exception as error:
        print(f"\nError saving file: {error}")

#Function called load_users_from_file with filename as the parameter that reads users from file, Creates HRUser objects from parsed data, returns list of 
#HRUser objects, and handles FileNotFound error by creating default users if file doesn't exist.
def load_users_from_file(filename):
    users = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    part = line.split('|')
                    user = HRUser(
                        username = part[0],
                        password = part[1],
                        role = part[2],
                        full_name = part[3]
                    )
                    users.append(user)
    except FileNotFoundError:
        print(f"No data found in {filename}.")
        users = create_default_users()
    except Exception as error:
        print(f"Error reading file: {error}")
    return users

#Function called display_user_management_menu that displays a sub menu to add a new user, view all users, and return to main menu
def display_user_management_menu():
    print("\n" + "=" * 50)
    print("USER MANAGEMENT MENU")
    print("=" * 50)
    print("1. Add New User")
    print("2. View All Users")
    print("3. Return To Main Menu")
    print("=" * 50)

def manage_user_accounts(users, users_filename):
    while True:
        display_user_management_menu()
        choice = get_menu_choice()
        if choice == "1":
            add_new_user(users)
        elif choice == "2":
            display_all_users(users)
        elif choice == "3":
            print("\nReturning to Main Menu")
            break
        else:
            print("\nInvalid entry.  Please try again.")
    
#Function called display menu with role as the parameter that shows different menau options based on roles
def display_menu(role):
    print("\n" + "=" * 50)
    print("MAIN MENU")
    print(f"You are signed in with {role} permissions.")
    print("=" * 50)
    if role == "HR Manager":
        print("1. Process Employee Records")
        print("2. View Reports")
        print("3. Manage User Accounts")
        print("4. Exit")
    else:
        print("1. View Reports")
        print("2. Exit")

def get_menu_choice():
    choice = input("Enter the menu option:  ")
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Invalid entry, please try again:  ")
    return choice

#Function called get_employee_info that returns first name and last name.
def get_employee_name():
    first_name = str(input("Please input the employee's first name or type ESC to end your session:  "))
    while len(first_name) == 0:
        first_name = str(input("Field cannot be empty, please input a valid first name:  "))
    if first_name.upper() == "ESC":
        return "ESC", ""
    last_name = str(input("Please input the employee's last name:  "))
    while len(last_name) == 0:
        last_name = str(input("Field cannot be empty, please input a valid last name:  "))
    return first_name, last_name

#Function called get_employee_id that returns the employee ID as a string
def get_employee_id():
    employee_id = str(input("Please input the employee's ID:  "))
    while len(employee_id) == 0:
        employee_id = str(input("Field cannot be empty, please input a valid employee id:  "))
    return employee_id

#Function called get_hours_worked that returns hours worked as a float
def get_hours_worked():
    while True:
        try:
            hours = float(input("Please input the amount of hours the employee worked as a decimal:  "))
            while hours < 0:
                hours = float(input("Field cannot be a negative number, please input the amount of hours the employee worked."))
            return hours
        except ValueError:
            print("Input not recognized.  Please enter a numeric value.")

#Function called get_hourly_rate that returns the employees hourly rate as a float
def get_hourly_rate():
    while True:
        try:
            rate = float(input("Please input the employee's hourly rate as a decimal:  "))
            while rate < 0 or rate == 0:
                rate = float(input("Field cannot be a negative number or zero, please input a positive non-zero number:  "))
            return rate
        except ValueError:
            print("Input not recognized.  Please enter a numeric value.")

#Function called process_employee_records with filename as the parameter that:  Prompts for employee information, Creates Employee objects, appends to list
#saves to file using object's to_file_string method, and only accessible to HR Managers
def process_employee_records(filename):
    today = datetime.now()
    date_string = today.strftime("%Y-%m-%d")
    print("=" * 50)
    print("Employee Record Processing")
    print(f"Date: {date_string}")
    print("Instructions:")
    print("Enter the employees payroll information when prompted.")
    print("Type ESC to end the employee data entry when finished.")
    print("Overtime is calculated as 1.5X the employees hourly rate after the first 40 hours worked.")
    print("Deductions are 25% of the employees gross pay.  15% from federal income tax, 10% from state income tax, and 5% from benfits.")
    input("Press enter to start.")
    print("=" * 50)
    print("Starting new employee management session.")
    print("All data will be saved after you exit the program.")
    employee_records = []
    while True:
        print("\n---Enter Employee information---")
        first_name, last_name = get_employee_name()
        if first_name.upper() == "ESC":
            break
        employee_id = get_employee_id()
        hours = get_hours_worked()
        rate = get_hourly_rate()
        employee = Employee(first_name, last_name, employee_id, hours, rate)
        employee_records.append(employee)
        print(employee)
        print("=" * 50)
        print("Employee's payroll information has been processed successfully!")
        print("=" * 50)
    if len(employee_records) > 0:
        save_records_to_file(employee_records, filename)
    else:
        print("No records were processed today.")
        print("=" * 50)

#Function called view_reports with filename as the parameter that loads employees from file using Employee object creation, calls generate_report to display
#the report, and ensure that it is available to HR Managers and HR Staff
def view_reports(filename):
    employee_records = load_records_from_file(filename)
    while True:
        print("\n" + "=" * 50)
        print("Reports Menu")
        print("=" * 50)
        print("1. Generate Reports")
        print("2. Search Records")
        print("3. Exit")
        choice = get_menu_choice()
        if choice == "1":
            generate_reports(employee_records)
            input("Press Enter to Continue.")
        elif choice == "2":
            search_records_menu(employee_records)
        elif choice == "3":
            print("\nReturning to main menu...")
            break
        else:
            print("Invalid entry.  Please try again.")

#Function called generate_reports with employee_record and filename as the parameter that displays all employee records using object attributes, Calculates and 
#displays statistics, shows count of overtime employees using .worked_overtime method, and shows cont of high earners using the .is_high_earner method.
def generate_reports(employee_records):
    today = datetime.now().strftime("%Y-%m-%d")
    total_employees = 0                           #Initialized 4 variables(total employees, total gross, total deductions, and total net)
    total_gross = 0.0
    total_deductions = 0.0
    total_net = 0.0
    print("\n" + "=" * 50)
    print("EMPLOYEE RECORDS - COMPLETE REPORT")
    print(f"Report Date: {today}")
    print("=" * 50)
    if len(employee_records) == 0:
        print("No records found.")
        print("=" * 50)
        return
    print(f"\nTotal Employee records found {len(employee_records)}")
    print("---ALL EMPLOYEE RECORDS---\n")
    for i, record in enumerate(employee_records, 1):
        date = record.record_date.strftime("%Y-%m-%d")
        print("=" * 50)
        print(f"{i}. Date Processed: {date}.  Name: {record.first_name} {record.last_name}.")
        print(f"Employee ID: {record.employee_id}.  Hours worked: {record.hours:,.1f}.  Hourly Rate: ${record.rate:,.2f}.")
        print(f"Gross pay: ${record.gross_pay:,.2f}.  Deductions paid: ${record.deductions:,.2f}.  Net pay: ${record.net_pay:,.2f}\n")      
    total_gross, average_gross, highest_gross, lowest_gross = calculate_payroll_statistics(employee_records)
    total_employees = len(employee_records)
    total_deductions = sum(record.deductions for record in employee_records)
    total_net = sum(record.net_pay for record in employee_records)
    overtime_employees = sum(1 for record in employee_records if record.worked_overtime())
    high_earners = sum(1 for record in employee_records if record.is_high_earner())
    display_statistics(total_employees, total_gross, total_deductions, total_net, average_gross, highest_gross, lowest_gross, overtime_employees, high_earners)


#Fuction that displays a welcome message with instructions for how to use the program.  It will also inform the user how overtime will be calculated and
#how deductions are calculated.
def welcome_message(current_user):
    today = datetime.now()
    date_string = today.strftime("%Y-%m-%d")
    print("=" * 50)
    print("Employee Management System")
    print(f"Date: {date_string}")
    print("Instructions:")
    print("Welcome to the Employee Management System")
    print("Once signed in, use the number keys to navigate the menus")
    if current_user == "HR Manager":
        print("The Process Employees menu will allow you to add employees to the employee record")
    print("The View Reports menu will allow you to search for employees and generate reports")
    if current_user == "HR Manager":
        print("The Manage User Accounts menu will allow you to add users to the employee management system.")
    input("\nPress Enter to Continue...")

#Function called display_summary with the parameters total_employees, total_gross, total_deductions, and total_net.  This function displays summary
#totals for all employees processed.
def display_statistics(total_employees, total_gross, total_deductions, total_net, average_gross, highest_gross, lowest_gross, overtime_employees, high_earners):
    print("=" * 50)
    print("EMPLOYEE RECORD STATISTICS")
    print("=" * 50)
    print(f"Total employees processed:                                                    {total_employees}")
    print(f"Total gross paid out to employees:                                            ${total_gross:,.2f}")
    print(f"Total deductions processed:                                                   ${total_deductions:,.2f}")
    print(f"Total net pay paid out to employees:                                          ${total_net:,.2f}")
    print(f"Average gross pay:                                                            ${average_gross:,.2f}")
    print(f"Highest gross pay:                                                            ${highest_gross:,.2f}")
    print(f"Lowest gross pay:                                                             ${lowest_gross:,.2f}")
    print(f"Amount of employees who worked overtime:                                      {overtime_employees}")
    print(f"Amount of employees who were high earners (earned more than $1,000 gross):    {high_earners}")
    print("=" * 50 + "\n")

#Function called calculate_payroll_statistics() that accepts employee_records as a parameter.  It will use python's built in math functions to 
#calculate four values:  Total gross pay using sum(gross_pays), Average gross pay using sum(gross_pays)/len(gross_pays), highest gross pay using
#max(gross_pays), and the lowest gross pay using min(gross_pays).  It will then return total_gross, average_gross, highest_gross, and lowest gross
#using a single return statement.
def calculate_payroll_statistics(employee_records):                        #updated to take the list of dictionaries as a parameter
    if len(employee_records) == 0:
        return 0.0, 0.0, 0.0, 0.0
    gross_pays = [record.gross_pay for record in employee_records]     #Uses list comprehesion to extract data
    total_gross = sum(gross_pays)
    average_gross = total_gross/len(gross_pays)
    highest_gross = max(gross_pays)
    lowest_gross = min(gross_pays)
    return total_gross, average_gross, highest_gross, lowest_gross

#Function called search_records_menu that accepts employee_records as the parameter that displays a menu to search for employees by employee id, first name, 
#and last name.
def search_records_menu(employee_records):
    while True:
        print("\n" + "=" * 50)
        print("Search Employee Menu")
        print("=" * 50)
        print("1. Find employee by Employee ID")
        print("2. Find employee by First Name")
        print("3. Find employee by Last Name")
        print("4. Exit")
        choice = get_menu_choice()
        if choice == "1":
            print("\n" + "=" * 50)
            searched_employee_id = input("Enter the Employee ID to search for:  ")
            employee_id_search_results = find_employee_by_id(employee_records, searched_employee_id)
            display_filtered_records(employee_id_search_results, f"Searching for Employee ID {searched_employee_id}.")
            input("Press Enter to Return to the search menu.")
        elif choice == "2":
            print("\n" + "=" * 50)
            searched_first_name = input("Enter the First Name of the Employee(s) you are searching for:  ")
            employee_first_name_search_results = find_employee_by_first_name(employee_records, searched_first_name)
            display_filtered_records(employee_first_name_search_results, f"Searching for Employee(s) with the First Name {searched_first_name}")
            input("Press Enter to Return to the search menu.")
        elif choice == "3":
            print("\n" + "=" * 50)
            searched_last_name = input("Enter the Last Name of the Employee(s) you are searching for:  ")
            employee_last_name_search_results = find_employee_by_last_name(employee_records, searched_last_name)
            display_filtered_records(employee_last_name_search_results, f"Searching for Employee(s) with the Last Name {searched_last_name}")
            input("Press Enter to Return to the search menu.")
        elif choice == "4":
            print("\nReturning to the Reports Menu...")
            break
        else:
            print("Invalid entry.  Please try again.")

#Function called find_employee_by_id with employee_records and employee_id as parameters that searches for employees by ID and returns a list of matching records
def find_employee_by_id(employee_records, employee_id):
    find_employee_id = []
    for employee_record in employee_records:
        if employee_record.employee_id == employee_id:
            find_employee_id.append(employee_record)
    return find_employee_id

#Function called find_employee_by_first_name with employee_records and first_name as parameters that searches for all employees with matching first name
#being case insensitive and returns a list of matching records
def find_employee_by_first_name(employee_records, first_name):
    find_employee_first_name = []
    for employee_record in employee_records:
        if employee_record.first_name.lower() == first_name.lower():
            find_employee_first_name.append(employee_record)
    return find_employee_first_name

#Function called find_employee_by_last_name with employee_records and last_name as parameters that searches for all employees with matching last name
#being case insensitive and returns a list of matching records
def find_employee_by_last_name(employee_records, last_name):
    find_employee_last_name = []
    for employee_record in employee_records:
        if employee_record.last_name.lower() == last_name.lower():
            find_employee_last_name.append(employee_record)
    return find_employee_last_name

#Function called display_filtered_records that accepts two parameters employee_records (filtered list) and filter_description(string) that 
#displays a filtered description.
def display_filtered_records(employee_records, filter_description):
    print("\n"+ "=" * 50)
    print(f"{filter_description.upper()}")      #Displays the filtered description
    print("=" * 50)
    if len(employee_records) == 0:               #Handles an empty list with a no matching records found message
        print("No matching records found.\n")
        print("=" * 50)
    else:
        print(f"Found {len(employee_records)} matching record(s):\n")      #Shows the count of matching records
        for employee_record in employee_records:               #Displays each record as a filtered list
            print(employee_record)

#Function called save_records_to_file with employee_records and filename as the parameters that opens file in write mode, writes each record as on line with
#Pipe-delimited format, uses try/except to handle errors,
def save_records_to_file(employee_records, filename):
    try:
        with open(filename, 'a') as file:
            for record in employee_records:
                line = record.to_file_string()
                file.write(line + "\n")
        print("\n" + "=" * 50)
        print("FILE SAVED SUCCESSFULLY")                             #Displays a success message after saving
        print("=" * 50)
        print(f"Saved {len(employee_records)} record(s) to {filename}.")
        print("=" * 50)
    except Exception as error:
        print(f"\nError saving file: {error}")

#Function called load_records_from_file with filename as the parameter that opens the file in readmode, and uses try/except for error handling, 
def load_records_from_file(filename):
    employee_records = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()                             #Reads each line
                if line:
                    parts = line.split('|')                #Splits the line by the pipe character
                    date_object = datetime.strptime(parts[8], "%Y-%m-%d")             #Converts the datetime string into a datetime object
                    record = Employee(
                        first_name = parts[0],
                        last_name = parts[1],
                        employee_id = parts[2],
                        hours = float(parts[3]),
                        rate = float(parts[4]),
                        record_date_str = parts[8]
                    )
                    employee_records.append(record)                  #Appends the object to list
        print(f"Loaded {len(employee_records)} record(s) from {filename}")  
    except FileNotFoundError:                               #Handles errors if the file does not exist
        print(f"No records existing in {filename}.")
        print("Starting program with an empty record.")
    except Exception as error:
        print(f"Error reading file: {error}")
    return employee_records                                          #Returns a list of employee record dictionaries

#Function that validates a valid search request of yes or no
def search_validation(search_key):                          
    while search_key.lower() not in ["yes", "no"]:
        search_key = input("Please enter either yes or no:  ")
    return search_key

#Main function
def main():
    filename = "employee_records.txt"                     #set the filename variable
    users_filename = "hr_users.txt"
    users = load_users_from_file(users_filename)          #loads users
    display_login_screen()                                #displays the login screen
    username = input("Username:  ")                       #Prompts for username
    password = input("Password:  ")                       #Prompts for password
    current_user = authenicate_user(users, username, password)      #authenicates that the user is valid
    if current_user is None:                              #displays access denied if user is not valid
        display_access_denied()
        return
    display_access_granted(current_user.username, current_user.role)                                #displays access granted if user is valid
    welcome_message(current_user.role)
    while True:
        display_menu(current_user.role)
        choice = get_menu_choice()                     #Menu helper function to get the menu choice
        if choice == "1":                                #Menu Display  
            if current_user.role =="HR Manager":
                process_employee_records(filename)
            else:
                view_reports(filename)
        elif choice == "2":
            if current_user.role == "HR Manager":
                view_reports(filename)
            else:
                print(f"Thank you {current_user.username}.")
                print("Logging out...")
                break
        elif choice == "3" and current_user.role == "HR Manager":
            manage_user_accounts(users, users_filename)
        elif choice == "4" and current_user.role == "HR Manager":
            save_users_to_file(users, users_filename)
            print(f"Thank you {current_user.username}.")
            print("Logging out...")
            break
        else:
            print("\nInvalid choice.  Please try again.")
main()