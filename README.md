# Financial Report

This repository contains a script named `financial_report.py` that processes a bank statement file. 

## Functionality
The script reads the input bank statement file and generates a financial report. The report includes income and expenses presented in both a table, a pie chart, and a bar graph.

## Input Statement File
The input statement file should have the following headers: date, description, debit, credit, balance.

## Usage
To use the script, provide the bank statement file as an input. You can also specify the period for which the report should be generated. The period can be a week (w), a month (m), or a quarter (q). If the period is not specified, the report will be generated for the full period.

```bash
python financial_report.py <bank_statement_file> <period>
```
## Installing Required Python Modules

Before running the script, you need to install the required Python modules. You can do this by using the `requirements.txt` file that is included in this repository. Here is the command to install the required Python modules:

```bash
pip install -r requirements.txt
```

## Running the Script

After installing the required Python modules, you can run the script. Here is the basic command:

```bash
python financial_report.py <bank_statement_file> <period>
```

## Running the Script without Python

This script can also be run as a standalone executable without needing Python installed on the system. Here are the steps to create the executable:

1. Install PyInstaller. PyInstaller is not a part of the standard Python library, so it needs to be installed separately. You can install it using pip:

```bash
pip install pyinstaller
```

2. Once PyInstaller is installed, you can use it to convert the Python script into an executable. Here is the basic command:

```bash
pyinstaller --onefile financial_report.py
```

The `--onefile` option tells PyInstaller to create a single executable file. If you don't use this option, PyInstaller will create a directory that contains an executable along with some other files that the executable needs to run.

The executable will be created in the `dist` directory that PyInstaller creates in the same directory where your Python script is located.

Please note that the executable will be platform-specific. That means if you create the executable on a Windows system, it will only run on Windows. If you want to create an executable for a different platform, you need to run PyInstaller on that platform.
