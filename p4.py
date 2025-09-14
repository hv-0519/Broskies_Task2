import pandas as pd
import matplotlib.pyplot as plt
import io

# Data from the sales_data.csv file snippet
csv_data = """sale_date,product_id,quantity,price
2025-09-01,4,5,20
2025-09-01,5,5,15
2025-09-01,3,3,20
2025-09-01,5,4,20
2025-09-01,5,2,25
2025-09-01,2,4,30
2025-09-01,1,4,15
2025-09-01,5,4,10
2025-09-01,1,3,20
2025-09-01,2,4,25
2025-09-01,3,4,25
2025-09-01,1,3,30
2025-09-01,3,5,10
2025-09-01,2,4,10
2025-09-01,4,2,15
2025-09-01,1,2,30
2025-09-02,4,4,25
2025-09-02,4,5,20
2025-09-02,1,4,15
2025-09-02,4,2,15
2025-09-02,2,2,25
2025-09-05,4,2,20
2025-09-05,1,5,10
2025-09-05,1,3,10
2025-09-05,2,2,25
2025-09-05,5,1,10
2025-09-05,3,2,30
2025-09-05,4,2,25
2025-09-05,3,3,10
2025-09-05,5,4,15
2025-09-05,3,1,10
2025-09-05,4,3,30
2025-09-05,3,4,25
2025-09-05,3,4,20
2025-09-06,3,3,25
2025-09-06,4,1,10
2025-09-06,2,1,20
2025-09-06,4,1,10
2025-09-06,2,2,20
2025-09-06,4,2,10
2025-09-06,4,4,10
2025-09-06,2,1,20
"""

# Read the data into a pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# Calculate total revenue per transaction
df['total_revenue'] = df['quantity'] * df['price']

# Group by product_id and sum the total_revenue
product_revenue = df.groupby('product_id')['total_revenue'].sum().reset_index()

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(product_revenue['product_id'], product_revenue['total_revenue'], color='purple')

# Add labels and title
plt.xlabel('Product ID')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Product from Sales Data')
plt.xticks(product_revenue['product_id'])
plt.tight_layout()

# Save the chart as a PNG image
plt.savefig('sales_data_product_revenue_bar_chart.png')
