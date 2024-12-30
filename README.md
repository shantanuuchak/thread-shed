# Thread Shed Sales Analysis

## Project Overview

This project involves parsing and analyzing sales data from a sewing supply store called "Thread Shed." The data is stored in a single, complex string that includes customer names, sales amounts, thread colors, and sale dates. The goal is to clean and organize this data into separate lists for customers, sales, and thread colors, calculate the total sales for the day, and determine the number of threads sold for each color.

## Key Tasks

1. **Data Parsing**: Replace artifacts in the string and split it into individual transactions.
2. **Data Cleaning**: Remove unnecessary whitespace from each data point.
3. **Data Organization**: Separate the cleaned data into lists for customers, sales, and thread colors.
4. **Sales Calculation**: Calculate the total sales amount for the day.
5. **Thread Color Analysis**: Count the number of threads sold for each color.

## Usage

1. **Prepare the data:**

- Create a text file named `daily-sales.txt` containing your sales data in the following format:

```
customer_name;color_1;color_2;color_3;...;sales_amount
...
```

- Replace `;` with `;,;` for multiple colors in a single transaction.
- Example:

```
John Doe;red;blue;,;;$15.00
Jane Smith;green;,;;$10.00
David Lee;white;black;,;;$20.00
```

2. **Run the script:**

- Execute the Python script from your terminal:

```bash
python thread_sales_analysis.py
```

3. **View the results:**

- The script will print the total sales amount to the console.
- A bar chart will be generated and saved as `thread_sales.png` in the same directory as the script.

## Visualization

The generated `thread_sales.png` will display:

- **X-axis:** Thread colors
- **Y-axis:** Number of threads sold for each color
- **Bar chart:** Visual representation of thread sales by color

**Note:** This assumes you have matplotlib installed. If not, install it using:

```bash
pip install matplotlib

## Learning Outcomes

- Practice string manipulation and list operations in Python.
- Gain experience in basic data analysis and organization.
- Develop skills in cleaning and processing raw data for analysis.

This project is a practical exercise in handling and analyzing real-world data using Python, focusing on string operations and list management.
```
