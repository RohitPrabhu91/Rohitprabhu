import csv
import matplotlib.pyplot as plt

# Open the CSV file
with open('Tweets.csv', 'r', encoding='utf-8') as f:
  reader = csv.reader(f)

  # Skip the header row
  next(reader)

  # Create a dictionary to store the number of tweets for each airline sentiment
  airline_sentiment_counts = {}

  # Iterate over the rows in the CSV file and count the number of tweets for each airline sentiment
  for row in reader:
    airline_sentiment = row[1]

    if airline_sentiment in airline_sentiment_counts:
      airline_sentiment_counts[airline_sentiment] += 1
    else:
      airline_sentiment_counts[airline_sentiment] = 1

# Create a bar chart to show the number of tweets for each airline sentiment
plt.bar(airline_sentiment_counts.keys(), airline_sentiment_counts.values(), color=['green', 'yellow', 'red'])

# Set the title and labels for the bar chart
plt.title('Twitter US Airline Sentiment')
plt.xlabel('Airline Sentiment')
plt.ylabel('Number of Tweets')

# Add a grid to the bar chart
plt.grid(True)

# Rotate the x-axis labels to prevent overlapping
plt.xticks(rotation=45)

# Show the bar chart
plt.show()
