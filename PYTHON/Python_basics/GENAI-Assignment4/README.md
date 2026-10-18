# Python File Handling - Sales and Product Data



## Overview



This project demonstrates basic Python file handling without advanced libraries. It covers writing, reading, appending, summarizing sales data, creating product files from user input, checking whether a requested file exists, and exporting discounted product prices.



## Task 1 - Write Sales Records



Create a list of sales amounts and write each value on a new line in `sales_data.txt` using write mode (`w`). Reopen the file in read mode (`r`) and display all saved sales records.



Example sales:



```text
1200
450
980
1500
3000
```



## Task 2 - Read File in Different Ways



Read `sales_data.txt` using basic Python file-reading methods:



- `.read()` - reads the complete file.
- `.readline()` - reads one line.
- `.readlines()` - reads all lines into a list.
- `.strip()` - removes newline characters.
- `int()` - converts sales values from strings to integers.



## Task 3 - Append New Sales



Add new sales values to the existing `sales_data.txt` file using append mode (`a`).



New sales:



```text
5000
2500
1700
```



After appending, reopen the file, display all updated records, and count the total number of sales records.



## Task 4 - Generate Sales Summary Report



Read all values from `sales_data.txt`, convert them to integers, and calculate:



- Total Sales
- Highest Sale
- Lowest Sale
- Average Sale



Example logic:



```python
sales = []



with open("sales_data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            sales.append(int(line))



if len(sales) > 0:
    total_sales = sum(sales)
    highest_sale = max(sales)
    lowest_sale = min(sales)
    average_sale = total_sales / len(sales)



    print("Total Sales:", total_sales)
    print("Highest Sale:", highest_sale)
    print("Lowest Sale:", lowest_sale)
    print("Average Sale:", round(average_sale, 2))
```



## Task 5 - Create Product Info File



Ask the user for three product names and their prices. Save them in a new file named `products.txt` using this format:



```text
ProductName | Price
```



Example:



```text
Laptop | 55000.00
Mouse | 750.00
Keyboard | 1500.00
```



After writing the products, reopen `products.txt` in read mode and print each saved line with proper formatting.



## Task 6 - Open a User-Selected File



Ask the user to enter a filename. Use the allowed `os.path.exists()` check before opening the file.



```python
import os



filename = input("Enter filename to open: ")



if os.path.exists(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    print(content)
else:
    print("File not found. Please check the filename.")
```



This task uses a simple condition rather than exception handling.



## Task 7 - Export Discounted Prices



Create the following product-price dictionary:



```python
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}
```



Ask the user for a discount percentage. Calculate the discounted price for every product and create `discount_report.txt` using this format:



```text
Product | Original Price | Discounted Price
```



After writing the report, reopen the file and print its contents. The optional summary contains:



- Total Items
- Average Discounted Price



## Files Created



After completing the assignment, the project can contain:



```text
python-file-handling/
|-- README.md
|-- task1.py
|-- task2.py
|-- task3.py
|-- task4.py
|-- task5.py
|-- task6.py
|-- task7.py
|-- sales_data.txt
|-- products.txt
`-- discount_report.txt
```



The individual Python filenames above are a suggested organization. Use your actual `.py` filenames if they are different.



## Requirements



- Python 3
- No third-party packages required
- `os.path.exists()` is used only for Task 6 as allowed by the assignment



## How to Run and Check



### 1. Open the project folder



Open Terminal, Command Prompt, PowerShell, or the terminal in your code editor and move to the folder containing the Python files.



### 2. Check Python



Run:



```bash
python --version
```



If your system uses the `python3` command, use `python3` instead of `python` in the examples below.



### 3. Run Tasks 1 to 3 in order



```bash
python task1.py
python task2.py
python task3.py
```



Check that `sales_data.txt` is created by Task 1, can be read in Task 2, and contains the appended sales values after Task 3.



### 4. Run Task 4



```bash
python task4.py
```



Check that the terminal displays Total Sales, Highest Sale, Lowest Sale, and Average Sale from `sales_data.txt`.



### 5. Run Task 5



```bash
python task5.py
```



Enter three product names and prices when prompted. Check that `products.txt` is created and that the program reads and displays its contents.



### 6. Run Task 6



```bash
python task6.py
```



Test first with an existing filename such as:



```text
sales_data.txt
```



Then test with a filename that does not exist. The program should display:



```text
File not found. Please check the filename.
```



### 7. Run Task 7



```bash
python task7.py
```



Enter a discount percentage when prompted. Check that `discount_report.txt` contains each product, original price, discounted price, and the optional summary when implemented.



## Final Verification Checklist



- `sales_data.txt` contains the original and appended sales records.
- Task 4 reads existing sales data and prints the required summary.
- `products.txt` contains three user-entered products and prices.
- Task 6 reads an existing file and displays the required message for a missing file.
- `discount_report.txt` contains the exported discounted product prices.
- All programs run using basic Python file operations without third-party libraries.



## Concepts Covered



- File write mode (`w`)
- File read mode (`r`)
- File append mode (`a`)
- `.read()`, `.readline()`, and `.readlines()`
- `.write()`
- `.strip()`
- `with open()` and basic `open()` / `close()`
- Lists and dictionaries
- Loops and conditions
- String-to-integer conversion
- `sum()`, `max()`, `min()`, and `len()`
- User input
- `os.path.exists()`
 