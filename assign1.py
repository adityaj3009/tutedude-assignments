# A dict has been created named emp_id which contains unique employee id in 
# key, val pair for name, age(int), department, salary(int)

emp_data = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Aditya', 'age': 20, 'department': 'Data analyst', 'salary': 45000},
    103: {'name': 'Shravani', 'age': 24, 'department': 'Data Scientist', 'salary': 75000},
    104: {'name': 'Aditya', 'age': 25, 'department': 'Cloud Engineer', 'salary': 55000}
}

# a function main_menu() is created 
# a while true loop is there to keep showing menu until exit and it consist of 4 option, from which they can choose any one using "choice input"
# then if elif else choices are created 

def main_menu():
    while True:
        print("\n----Employee Management System----")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_emp()
        elif choice == '2':
            view_emp()
        elif choice == '3':
            search_emp()
        elif choice == '4':
            print("Thank you!!!")
            break
        else:
            print("Invalid choice. Please enter a number only between 1 and 4.")


# function add_emp() is use to add new employee into dict
#it first take employee id and if its present then its show error and then exit function
# if id is new it collects remaining data
# .strip() - removes excess space like "  abcd" - output- abcd
# age, salary converted to int
# then it store data in dict emp_data

def add_emp():
    emp_id = int(input("Enter your Employee ID: "))
    if emp_id in emp_data:
        print("Employee id already exist. Please try a new employee ID")
        return
    
    name = input("Enter Employee Name: ").strip()
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ").strip()
    salary = int(input("Enter Employee Salary: "))

    emp_data[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print("Employee was added successfully!\n")

# this function helps to view saved data
# if no data available it will say that 
# else it will show all details
def view_emp():
    print("\nEmployee list...")
    print("-"*30)

    if not emp_data:
        print("No data available.")
    else:
        print("Employee details: \n")
        for emp_id, emp in emp_data.items():
            print("ID: ", emp_id)
            print("Name: ", emp['name'])
            print("Age:", emp['age'])
            print("Department:", emp['department'])
            print("Salary:", emp['salary'])
            print("-" * 30)



# this function used to search employee
# first it will ask for emp id, if provided wrong it will through error
# else will ask for details and show employee information
def search_emp():
    print("\nSearch Employee...")
    try:
        emp_id = int(input("Enter Employee ID to search: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    if emp_id in emp_data:
        emp = emp_data[emp_id]
        print("\nEmployee Found:")
        print("-" * 30)
        print("ID:", emp_id)
        print("Name:", emp['name'])
        print("Age:", emp['age'])
        print("Department:", emp['department'])
        print("Salary:", emp['salary'])
        print("-" * 30)
    else:
        print("Employee not found.")

main_menu()
