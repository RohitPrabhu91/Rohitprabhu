import pandas as pd
import matplotlib.pyplot as plt

# Create a list of marketing persons
marketing_persons = ["Alice", "Bob", "Carol", "Dave", "Eve","Sanjiv","Vignesh","sandy","Rohith prabu","Santhosh"]

# Create a list of their sales
sales = [10000, 40000, 25000, 30000, 20000,19000,60000,49000,35000,33000]

# Create a DataFrame
df = pd.DataFrame({"Marketing Person": marketing_persons, "Sales": sales})

# Sort the DataFrame by sales
df = df.sort_values(by=["Sales"], ascending=False)

# Choose the type of chart
chart_type = "bar"

# Create the chart
if chart_type == "bar":
    plt.bar(df["Marketing Person"], df["Sales"])
elif chart_type == "pie":
    plt.pie(df["Sales"], labels=df["Marketing Person"], autopct="%1.1f%%")

# Set the chart title and labels
plt.title("Sales by Marketing Person")
plt.xlabel("Marketing Person")
plt.ylabel("Sales")

# Show the chart
plt.show()
