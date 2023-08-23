import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def generate_report(csv_file, period=None):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Convert 'Debit' and 'Credit' columns to numeric values, removing any commas
    df['Debit'] = pd.to_numeric(df['Debit'].str.replace(',', ''), errors='coerce')
    df['Credit'] = pd.to_numeric(df['Credit'].str.replace(',', ''), errors='coerce')
    
    # Convert the date column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

    # Filter the data based on the specified period
    if period == 'w':
        df = df[df['date'] >= datetime.now() - pd.DateOffset(weeks=1)]
    elif period == 'm':
        df = df[df['date'] >= datetime.now() - pd.DateOffset(months=1)]
    elif period == 'q':
        df = df[df['date'] >= datetime.now() - pd.DateOffset(months=3)]

    # Separate expenses and income
    expenses = df[df['Debit'].notna()]
    income = df[df['Credit'].notna()]

    # Generate summary tables
    expenses_summary = expenses.groupby('Description').sum()
    income_summary = income.groupby('Description').sum()

    # Generate pie charts
    expenses_summary['Debit'].plot(kind='pie', autopct='%1.1f%%')
    plt.title('Expenses')
    plt.savefig(f'expenses_pie_{datetime.now().strftime("%Y%m%d%H%M%S")}.png')
    plt.show()
    plt.clf()

    income_summary['Credit'].plot(kind='pie', autopct='%1.1f%%')
    plt.title('Income')
    plt.savefig(f'income_pie_{datetime.now().strftime("%Y%m%d%H%M%S")}.png')
    plt.show()
    plt.clf()

    # Generate bar graphs
    expenses_summary['Debit'].plot(kind='bar')
    plt.title('Expenses')
    plt.savefig(f'expenses_bar_{datetime.now().strftime("%Y%m%d%H%M%S")}.png')
    plt.show()
    plt.clf()

    income_summary['Credit'].plot(kind='bar')
    plt.title('Income')
    plt.savefig(f'income_bar_{datetime.now().strftime("%Y%m%d%H%M%S")}.png')
    plt.show()
    plt.clf()

import argparse

# Create a parser
parser = argparse.ArgumentParser(description='Generate a financial report from a CSV file.')

# Add arguments
parser.add_argument('csv_file', type=str, help='The path to the CSV file.')
parser.add_argument('--period', type=str, choices=['w', 'm', 'q'], help='The period to generate the report for. Can be "w" for week, "m" for month, or "q" for quarter.')

# Parse arguments
args = parser.parse_args()

# Call the function with the parsed arguments
generate_report(args.csv_file, args.period)
