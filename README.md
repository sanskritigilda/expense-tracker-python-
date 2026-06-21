# Expense Tracker Python

A simple command-line Expense Tracker built using Python. This application helps users manage daily expenses by adding, viewing, deleting, and calculating total spending. Expense data is stored in a JSON file for persistence.

## Features

* Add new expenses
* View all saved expenses
* Delete expenses by ID
* Calculate total spending
* View available expense categories
* Save data in a JSON file
* Automatic data loading on startup
* Category selection using if-else statements
* Menu navigation using Python match-case (switch-case)

## Categories

1. Food
2. Travel
3. Shopping
4. Bills
5. Entertainment
6. Health
7. Other

## Technologies Used

* Python 3
* JSON
* File Handling

## Project Structure

```text
expense-tracker-python/
│
├── expense_tracker.py
├── expenses.json
└── README.md
```

## How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/expense-tracker-python.git
```

### Navigate to the Project Folder

```bash
cd expense-tracker-python
```

### Run the Program

```bash
python expense_tracker.py
```

## Menu Options

```text
===== Expense Tracker =====
1. Add Expense
2. View All Expenses
3. Delete Expense
4. Calculate Total Spending
5. View Categories
6. Save Data
7. Exit
```

## Example Output

```text
===== Categories =====
1. Food
2. Travel
3. Shopping
4. Bills
5. Entertainment
6. Health
7. Other

Select category number: 3
Selected Category: Shopping

Expense Added Successfully!
Description : Shoes
Amount      : ₹2500.00
Category    : Shopping
Date        : 21-06-2026
```

## Data Storage

Expenses are stored in the `expenses.json` file:

```json
[
    {
        "id": 1,
        "description": "Shoes",
        "amount": 2500,
        "category": "Shopping",
        "date": "21-06-2026"
    }
]
```

## Future Enhancements

* Update expenses
* Search expenses
* Category-wise reports
* Monthly spending summary
* Graphical User Interface (GUI)
* Expense analytics and charts

## Author

**Sanskriti Gilda**

This project was developed using Python to practice:

* File Handling
* JSON Data Storage
* Functions
* Conditional Statements (if-elif-else)
* Switch Case using match-case
* Menu-Driven Programming

## License

This project is open-source and available for learning and educational purposes.
