from flask import Flask, request, render_template
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Define the path to the Excel file
excel_file = r'C:\Users\p.gopalan\OneDrive - Q.VITEC GmbH\Documents\prana_bu.xlsx'

# Function to update the Excel sheet with new expenses
def update_excel(expenses, excel_path):
    try:
        # Load existing Excel file
        df = pd.read_excel(excel_path)
        print("Excel file loaded successfully.")
    except FileNotFoundError:
        # Create a new DataFrame if the file doesn't exist
        df = pd.DataFrame(columns=[
            "Date", "Salary", "Rent", "Internet", "Loan Repayment", 
            "Utilities", "Food & Groceries", "Transportation", 
            "Laundry/Washing", "Entertainment", "Miscellaneous", 
            "Remaining Balance"
        ])
        print("Excel file not found. Created a new DataFrame.")

    # Convert the list of expenses to a DataFrame
    new_expenses_df = pd.DataFrame(expenses, columns=[
        "Date", "Salary", "Rent", "Internet", "Loan Repayment", 
        "Utilities", "Food & Groceries", "Transportation", 
        "Laundry/Washing", "Entertainment", "Miscellaneous", 
        "Remaining Balance"
    ])
    print("New expenses DataFrame created:", new_expenses_df)

    # Append the new expenses to the existing DataFrame
    updated_df = pd.concat([df, new_expenses_df], ignore_index=True)
    print("Updated DataFrame:", updated_df)

    # Save the updated DataFrame back to the Excel file
    updated_df.to_excel(excel_path, index=False)
    print("Data saved to Excel file successfully.")

@app.route('/')
def index():
    return render_template('index.html', balance=None)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    # Retrieve form data
    salary = float(request.form['salary'])
    rent = float(request.form['rent'])
    internet = float(request.form['internet'])
    loan = float(request.form['loan'])
    utilities = float(request.form['utilities'])
    food_groceries = float(request.form['food_groceries'])
    transportation = float(request.form['transportation'])
    laundry = float(request.form['laundry'])
    entertainment = float(request.form['entertainment'])
    miscellaneous = float(request.form['miscellaneous'])
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Calculate remaining balance
    total_expenses = rent + internet + loan + utilities + food_groceries + transportation + laundry + entertainment + miscellaneous
    remaining_balance = salary - total_expenses

    # Create a new expense entry
    expense = [[date, salary, rent, internet, loan, utilities, food_groceries, transportation, laundry, entertainment, miscellaneous, remaining_balance]]
    print("Expense entry created:", expense)
    update_excel(expense, excel_file)

    return render_template('index.html', balance=remaining_balance)

if __name__ == '__main__':
    app.run(debug=True)