# خلق قاموس لتخزين معلومات الموظفين والمبيعات
employees = {}

# الدالة لحساب الراتب الشهري للموظف
def calculate_salary(sales):
    fixed_salary = 700000  # الراتب الثابت
    commission = sales * 0.09  # العمولة
    total_salary = fixed_salary + commission
    return total_salary

# الدالة لحساب المبيعات الشهرية لكل موظف
def calculate_total_sales(sales_info):
    total_sales = 0
    for product in sales_info:
        quantity, price = sales_info[product]
        total_sales += quantity * price
    return total_sales

# الدالة للعثور على أعلى 3 موظفين بناءً على المبيعات
def find_top_3_employees(employees_dict):
    sorted_employees = sorted(employees_dict.items(), key=lambda x: calculate_total_sales(x[1]['sales']), reverse=True)
    top_3_employees = sorted_employees[:3]
    return top_3_employees

def find_top_1_employee(employees_dict):
    sorted_employees = sorted(employees_dict.items(), key=lambda x: calculate_total_sales(x[1]['sales']), reverse=True)
    top_1_employees = sorted_employees[:1]
    return top_1_employees

# الدالة للعثور على المنتج الأعلى مبيعًا
def find_top_selling_product(employees_dict):
    product_sales = {}
    for employee, sales_info in employees_dict.items():
        for product in sales_info['sales']:
            if product in product_sales:
                product_sales[product] += product[1][0]
            else:
                product_sales[product] = product[1][0]
    top_product = max(product_sales, key=product_sales.get)
    return top_product

# الدالة لإدخال معلومات الموظف
def input_employee_data():
    name = input("Name: ")
    social_security_number = input("Social assurance number: ")
    email = input("E-mail: ")
    mobile_number = input("Phone: ")

    sales_info = {}
    while True:
        product = input("Product name (type finish if no more):")
        if product == "finish":
            break
        quantity = int(input("Amount: "))
        price = float(input("Price: "))
        sales_info[product] = (quantity, price)

    employees[social_security_number] = {"name": name, "email": email, "phone": mobile_number, "sales": sales_info}

# الدالة لعرض معلومات الموظفين مرتبة بشكل تنازلي بناءً على الراتب
def display_employees_sorted_by_salary(employees_dict):
    sorted_employees = sorted(employees_dict.items(), key=lambda x: calculate_salary(calculate_total_sales(x[1]['sales'])), reverse=True)
    for employee, employee_data in sorted_employees:
        print(f"Name: {employee_data['name']}")
        print(f"Social assurance number: {employee}")
        print(f"Salary: {calculate_salary(calculate_total_sales(employee_data['sales']))} SYR")
        print("------------")

# الدالة لعرض المعلومات المتعلقة بأعلى 3 موظفين بناءً على المبيعات
def display_top_3_employees(top_3_employees_list):
    for i, (employee, total_sales) in enumerate(top_3_employees_list, start=1):
        employee_data = employees[employee]
        print(f"Order: {i}")
        print(f"Name: {employee_data['name']}")
        print(f"Social assurance number: {employee}")
        print(f"Salary: {calculate_salary(calculate_total_sales(employee_data['sales']))} SYR")
        print(f"Sales: {total_sales} sales")
        print("------------")

# الدالة لعرض المنتج الأعلى مبيعًا
def display_top_selling_product(top_product):
    print(f"Most sold products: {top_product}")
    
def calculate_employee_salary(employees_dict, employee_number):
    if employee_number in employees_dict:
        employee_info = employees_dict[employee_number]
        sales_info = employee_info["sales"]
        total_sales = calculate_total_sales(sales_info)
        salary = calculate_salary(total_sales)
        return salary
    else:
        return None  # إذا لم يتم العثور على الموظف

# دالة لكتابة معلومات الموظفين إلى ملف نصي
def write_employees_to_file(employees_dict, filename):
    with open(filename, 'w') as file:
        for employee_number, employee_data in employees_dict.items():
            file.write(f"d: {employee_number}\n")
            file.write(f"d: {employee_data['name']}\n")
            file.write(f"d: {employee_data['email']}\n")
            file.write(f"d: {employee_data['phone']}\n")
            for product, (quantity, price) in employee_data['sales'].items():
                file.write(f"{product}: {quantity}, {price}\n")
            file.write("------\n")

# دالة لاسترجاع معلومات الموظفين من ملف نصي إلى قاموس
def read_employees_from_file(filename):
    employees = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            employee_number = lines[i].strip().split(": ")[1]
            i += 1
            name = lines[i].strip().split(": ")[1]
            i += 1
            email = lines[i].strip().split(": ")[1]
            i += 1
            mobile = lines[i].strip().split(": ")[1]
            i += 1
            sales = {}
            while i < len(lines) and lines[i] != "------\n":
                product_info = lines[i].strip().split(": ")
                product = product_info[0]
                [quantity, price] = product_info[1].split(", ")
                sales[product] = (float(quantity), float(price))
                i += 1
            employees[employee_number] = {
                "name": name,
                "email": email,
                "phone": mobile,
                "sales": sales
            }
            i += 1
    return employees


# البرنامج الرئيسي
while True:
    choice = input("Select:\n1. Input new employee\n2. Top 3 employees with most Sells\n3. Employees information sorted\n4. Most sold product\n5. Employee Salarys\n6. Top 1 employee with most sales\n7. Write employees to a file\n8. Read the data in text file\n9. Exit\n Your choice: ")

    if choice == "1":
        input_employee_data()
    elif choice == "2":
        top_3_employees = find_top_3_employees(employees)
        display_top_3_employees(top_3_employees)
    elif choice == "3":
        display_employees_sorted_by_salary(employees)
    elif choice == "4":
        top_product = find_top_selling_product(employees)
        display_top_selling_product(top_product)
    elif choice == "5":
        number = input("Employee number: ")
        salary = calculate_employee_salary(employees, number)
        print(f"Salary: {salary}")
    elif choice == "6":
        top_1_employees = find_top_1_employee(employees)
        display_top_3_employees(top_1_employees)
    elif choice == "7":
        write_employees_to_file(employees,'content.txt')
    elif choice == "8":
        employees = read_employees_from_file('content.txt')
    elif choice == "9":
        break
    else:
        print("Invalid selection.")
