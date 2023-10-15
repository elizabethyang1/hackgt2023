import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Load your data from a CSV file
data = pd.read_csv('nonnecessities.csv')

# Convert the "Date" column to a datetime object
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')

# Extract date-related features
data['Month'] = data['Date'].dt.month
data['DayOfWeek'] = data['Date'].dt.dayofweek  # Monday: 0, Sunday: 6
data['IsWeekend'] = data['DayOfWeek'].isin([5, 6]).astype(int)  # Binary indicator for weekends

# Define your feature set (X) and target variable (y)
X = data[['Month', 'DayOfWeek', 'IsWeekend']]
y = data['Price']

# Create a linear regression model and fit it to the data
model = LinearRegression()
model.fit(X, y)

# Determine the last date in the dataset
last_date = data['Date'].max()

# Create future dates starting right after the last date and continuing for 2 months
future_dates = [last_date + timedelta(days=i) for i in range(1, 61)]  # 2 months ahead (30 days/month)

# Prepare future data with date-related features for each future date
future_data = pd.DataFrame({
    'Month': [date.month for date in future_dates],
    'DayOfWeek': [date.dayofweek for date in future_dates],
    'IsWeekend': [int(date.dayofweek in [5, 6]) for date in future_dates]
})

# Predict future spending for each future date
predicted_spending = model.predict(future_data)

# Create a graph to visualize the data
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Price'], label='Current Spending', marker='o')
plt.plot(future_dates, predicted_spending, label='Future Predictions', marker='x')

# Customize the plot
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Current Spending vs. Future Predictions (2 Months Ahead from Last Date)')
plt.legend()

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()
plt.savefig('wantsProj.png')
print("done")