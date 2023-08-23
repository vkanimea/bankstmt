import pandas as pd
import matplotlib.pyplot as plt

def generate_report(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Separate expenses and income
    expenses = df[df['debit'].notna()]
    income = df[df['credit'].notna()]

    # Generate summary tables
    expenses_summary = expenses.groupby('description').sum()
    income_summary = income.groupby('description').sum()

    # Generate pie charts
    expenses_summary['debit'].plot(kind='pie', autopct='%1.1f%%')
    plt.title('Expenses')
    plt.show()

    income_summary['credit'].plot(kind='pie', autopct='%1.1f%%')
    plt.title('Income')
    plt.show()

# Call the function with your CSV file
generate_report('your_file.csv')
