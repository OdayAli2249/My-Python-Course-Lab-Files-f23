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

# البرنامج الرئيسي
while True:
    choice = input("Select:\n1. Input new employee\n2. Top 3 employees with most Sells\n3. Employees information sorted\n4. Most sold product\n5. Exit\n Your choice: ")

    if choice == "1":
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
    elif choice == "2":
        sorted_employees = sorted(employees.items(), key=lambda x: calculate_total_sales(x[1]['sales']), reverse=True)
        top_3_employees = sorted_employees[:3]
        for i, (employee, total_sales) in enumerate(top_3_employees, start=1):
            employee_data = employees[employee]
            print(f"Order: {i}")
            print(f"Name: {employee_data['name']}")
            print(f"Social assurance number: {employee}")
            print(f"Salary: {calculate_salary(calculate_total_sales(employee_data['sales']))} SYR")
            print(f"Sales: {total_sales} sales")
            print("------------")
    elif choice == "3":
        sorted_employees = sorted(employees.items(), key=lambda x: calculate_salary(calculate_total_sales(x[1]['sales'])), reverse=True)
        for employee, employee_data in sorted_employees:
            print(f"Name: {employee_data['name']}")
            print(f"Social assurance number: {employee}")
            print(f"Salary: {calculate_salary(calculate_total_sales(employee_data['sales']))} SYR")
            print("------------")
    elif choice == "4":
        product_sales = {}
        for employee, sales_info in employees.items():
            for product in sales_info['sales']:
                if product in product_sales:
                   product_sales[product] += product[1][0]
                else:
                   product_sales[product] = product[1][0]
        top_product = max(product_sales, key=product_sales.get)
        print(f"Most sold products: {top_product}")
    elif choice == "5":
        break
    else:
        print("Invalid selection.")
