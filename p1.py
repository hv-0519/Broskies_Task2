import pandas as pd
import matplotlib.pyplot as plt
import io

# Data from the top_products.csv file snippet
csv_data = """product_name,total_revenue
Product A,2275
Product E,1855
Product D,1490
Product B,1375
Product C,1290
"""

# Read the data into a pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# Sort the DataFrame by total_revenue for better visualization
df = df.sort_values(by='total_revenue', ascending=False)

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['product_name'], df['total_revenue'], color='skyblue')

# Add labels and title
plt.xlabel('Product Name')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Product')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the chart as a PNG image
plt.savefig('top_products_bar_chart.png')
