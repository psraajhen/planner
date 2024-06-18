from flask import Flask, request, render_template
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Define the path to the Excel file
excel_file = r'C:\Users\p.gopalan\OneDrive - Q.VITEC GmbH\Desktop\prana\bu_pran\budget\prana_bu.xlsx'

# Function to update the Excel sheet with new expenses
def update_excel(expenses, excel_path):
    try:
        # Load existing Excel file
        df = pd.read_excel(excel_path)
    except FileNotFoundError:
        # Create a new DataFrame if the file doesn't exist
        df = pd.DataFrame(columns=["Date", "Description", "Category", "Amount", "Payment Method", "Notes"])

    # Convert the list of expenses to a DataFrame
    new_expenses_df = pd.DataFrame(expenses, columns=["Date", "Description", "Category", "Amount", "Payment Method", "Notes"])

    # Append the new expenses to the existing DataFrame
    updated_df = pd.concat([df, new_expenses_df], ignore_index=True)

    # Save the updated DataFrame back to the Excel file
    updated_df.to_excel(excel_path, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    description = request.form['description']
    category = request.form['category']
    amount = float(request.form['amount'])
    payment_method = request.form['payment_method']
    notes = request.form['notes']
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = [[date, description, category, amount, payment_method, notes]]
    update_excel(expense, excel_file)

    return "Expense added successfully!"

if __name__ == '__main__':
    app.run(debug=True)
