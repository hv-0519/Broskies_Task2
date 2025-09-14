import pandas as pd
import matplotlib.pyplot as plt
import io

# Data from the avg_transactions.csv file snippet
csv_data = """sale_date,avg_transaction
2025-09-01,69.6875
2025-09-02,81.81818181818181
2025-09-03,42.5
2025-09-04,72.14285714285714
2025-09-05,48.888888888888886
2025-09-06,47.10526315789474
2025-09-07,80.5
2025-09-08,41.0
2025-09-09,60.88235294117647
2025-09-10,57.857142857142854
"""

# Read the data into a pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(df['sale_date'], df['avg_transaction'], color='lightgreen')

# Add labels and title
plt.xlabel('Sale Date')
plt.ylabel('Average Transaction')
plt.title('Average Transaction per Day')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the chart as a PNG image
plt.savefig('avg_transactions_bar_chart.png')
