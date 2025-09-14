import pandas as pd
import matplotlib.pyplot as plt
import io

# Data from the daily_totals.csv file snippet
csv_data = """sale_date,daily_total
2025-09-01,1115
2025-09-02,900
2025-09-03,425
2025-09-04,1010
2025-09-05,880
2025-09-06,895
2025-09-07,805
2025-09-08,410
2025-09-09,1035
2025-09-10,810
"""

# Read the data into a pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(df['sale_date'], df['daily_total'], color='coral')

# Add labels and title
plt.xlabel('Sale Date')
plt.ylabel('Daily Total')
plt.title('Daily Total Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the chart as a PNG image
plt.savefig('daily_totals_bar_chart.png')
