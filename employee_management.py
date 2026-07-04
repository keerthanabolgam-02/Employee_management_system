import pandas as pd

# Load the CSV file
df = pd.read_csv("employees.csv")

# Display employee data
print("========== EMPLOYEE DATA ==========")
print(df)

# Average salary
average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)

# Department count
print("\n========== DEPARTMENT COUNT ==========")
department_count = df["Department"].value_counts()
print(department_count)

# Salary threshold
threshold = int(input("\nEnter salary threshold: "))

# Filter employees
filtered_data = df[df["Salary"] > threshold]

print("\n========== EMPLOYEES WITH SALARY ABOVE", threshold, "==========")
print(filtered_data)

# Export filtered data
filtered_data.to_csv("filtered_employees.csv", index=False)

print("\nFiltered employee data has been saved to 'filtered_employees.csv'")
