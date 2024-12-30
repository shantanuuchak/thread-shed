# Reading from a txt file
daily_sales = open('daily-sales.txt', 'r').read()



# === Task 1-4: Replace and Split Transactions
# Replace the artifact ';,;' with a unique character '🌉' to avoid splitting transaction data
daily_sales_replaced = daily_sales.replace(';,;', '🌉')
# Split the string into individual transactions using ',' as the delimiter
daily_transactions = daily_sales_replaced.split(',')

# === Task 5-7: Split Each Transaction into Data Points
# Split each transaction into a list of its data points using '🌉' as the delimiter
daily_transactions_split = [i.split('🌉') for i in daily_transactions]

# === Task 8-9: Clean Up Whitespace
# Initialize an empty list to store cleaned transactions
transactions_clean = []
# Iterate through each transaction and strip whitespace from each data point
for daily_transaction in daily_transactions_split:
    new_transaction = []
    for transaction in daily_transaction:
        new_transaction.append(transaction.strip())
    transactions_clean.append(new_transaction)

# === Task 10-12: Separate Data into Lists
# Initialize empty lists for customers, sales, and thread_sold
customers = []
sales = []
thread_sold = []
# Append each data point to the respective list
for transaction in transactions_clean:
    customers.append(transaction[0])
    sales.append(transaction[1])
    thread_sold.append(transaction[2])

# === Task 13-15: Calculate Total Sales
# Initialize total_sales to 0
total_sales = 0
# Convert each sale amount from string to float and add to total_sales
for sale in sales:
    total_sales += float(sale[1:])  # Remove the '$' before conversion
# Print the total sales amount
print(total_sales)

# === Task 16-18: Split Thread Colors
# Initialize an empty list to store individual thread colors
thread_sold_split = []
# Split multiple colors in a single transaction and append each color to the list
for thread in thread_sold:
    if "&" not in thread:
        thread_sold_split.append(thread)
        continue
    for i in thread.split("&"):
        thread_sold_split.append(i)

# === Task 19-21: Count Thread Colors
# Define a function to count occurrences of a specific color in thread_sold_split
def color_count(color):
    count = 0
    for thread in thread_sold_split:
        if color == thread:
            count += 1
    return count

# Test the color_count function for 'white'
print(color_count('white'))

# Create a list of unique colors from thread_sold_split
colors = list(set(thread_sold_split))

# === Task 22: Print Thread Sales Summary
# Iterate through each color and print the number of threads sold for that color
for color in colors:
    print("Thread Shed sold {count} threads of {color} thread today.".format(count=color_count(color),color=color))

print(total_sales)