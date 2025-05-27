import pandas as pd
import numpy as np

class Employee:
    def __init__(self, Owner, Company, no_of_employee):
        self.Owner = Owner
        self.Company = Company
        self.no_of_employee = no_of_employee

    @staticmethod
    def report():
        print("Welcome to make the employee report: ")
        names = []
        salaries = []
        departments = []
        roles = []
        performance_scores = []

        N = int(input("Enter number of Employees again: "))
        for _ in range(N):
            name = input("Enter the Name: ")
            salary = float(input("Enter the Salary: "))
            department = input("Enter the Department: ")
            role = input("Enter the Role: ")
            performance_score = input("Enter the Performance Score: ")

            names.append(name)
            salaries.append(salary)
            departments.append(department)
            roles.append(role)
            performance_scores.append(performance_score)

       
        data = pd.DataFrame({
            "Name": names,
            "Salary": salaries,
            "Department": departments,
            "Role": roles,
            "Performance_Score": performance_scores
        })

        print("\nThe employees data:")
        print(data)

        print("\nThe employees who have salary less than 50000:")
        print(data[data["Salary"] < 50000])

        
        min_salary_index = data["Salary"].idxmin()
        max_salary_index = data["Salary"].idxmax()
        min_person = data.loc[min_salary_index, "Name"]
        max_person = data.loc[max_salary_index, "Name"]
        min_salary = data.loc[min_salary_index, "Salary"]
        max_salary = data.loc[max_salary_index, "Salary"]

        print(f"\n🪙 {min_person} has the **lowest** salary: {min_salary}")
        print(f"💰 {max_person} has the **highest** salary: {max_salary}")
    
        print("If you Want this again then type : 1.Add New Employee(1)\n2.View Stats(2)\n3.Exprot file into csv(3)\n4.Exit(Any_key)")
        choice=int(input("Enter your choice: "))
        if choice==1:
            emp.report()
        elif choice==2:
            print(data)
        elif choice==3:
            data.to_csv("The Info.csv",index=False)
        else:
            print("Thank you")
        
N = int(input("Enter number of Employees: "))
emp = Employee("Anurag", "My_code_world", N)
print(f"\nOwner: {emp.Owner}, Company: {emp.Company}, Total Employees Expected: {emp.no_of_employee}")
emp.report()
    
