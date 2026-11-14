import csv
FILENAME = "employees.csv"
def process_payroll(filename):
    gross_total = deductions_total = net_total = 0
    count = 0
    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            required = {"EmployeeID", "Name", "BasicSalary"}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                print("Error: Invalid CSV headers."); return
            print("ID | Name | Basic | Gross | PF | Net")
            for row in reader:
                try:
                    emp_id, name = row["EmployeeID"].strip(), row["Name"].strip()
                    basic = float(row["BasicSalary"])
                    if not emp_id or not name or basic < 0: print("Skipping invalid record."); continue
                    hra, da, pf = basic * .20, basic * .10, basic * .12
                    gross, net = basic + hra + da, basic + hra + da - pf
                    print(f"{emp_id} | {name} | {basic:.2f} | {gross:.2f} | {pf:.2f} | {net:.2f}")
                    gross_total += gross; deductions_total += pf; net_total += net; count += 1
                except (ValueError, AttributeError, TypeError): print("Skipping invalid record.")
        if not count: print("No valid employee records found."); return
        print("Employees:", count)
        print(f"Total Gross Salary: {gross_total:.2f}")
        print(f"Total PF Deductions: {deductions_total:.2f}")
        print(f"Total Net Salary: {net_total:.2f}")
    except FileNotFoundError: print("Error: Employee CSV file not found.")
    except PermissionError: print("Error: Permission denied.")
    except OSError as error: print("Error reading CSV file:", error)
if __name__ == "__main__": process_payroll(FILENAME)
