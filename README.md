# Expense Tracker Application

This is a simple Expense Tracker application built using Flask and Pandas. It allows users to input various expenses via a web interface and automatically updates an Excel sheet with the new data, including the current date and time and calculating the remaining balance.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the Repository** (if applicable)
    ```sh
    git clone https://github.com/yourusername/expense-tracker.git](https://github.com/psraajhen/budget.git
    cd expense-tracker
    ```

2. **Create a Virtual Environment** (optional but recommended)
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Required Python Packages**
    ```sh
    pip install flask pandas openpyxl
    ```

## Files and Directories

- `app.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
  - `index.html`: The HTML template for the expense input form and balance display.
- `expenses.xlsx`: The Excel file where the expenses are recorded (created automatically on first run).

## Usage

1. **Run the Flask Application**
    ```sh
    python app.py
    ```

2. **Open the Application in a Web Browser**
    Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Add Expenses**
    Fill in the form with your expenses and submit. The remaining balance will be displayed on the page, and the data will be saved to `expenses.xlsx`.

After submitting the form, the application will calculate the remaining balance and save the data to `expenses.xlsx`.



If the data is not being saved to the Excel file, check the console output for debugging print statements. Ensure that the Python process has write permissions to the directory and that no other application is locking the Excel file.




