import csv
import matplotlib.pyplot as plt

# Read the CSV file
with open('Tweets.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

# Extract the data columns
tweet_ids = [row[0] for row in data]
airline_sentiments = [row[1] for row in data]
airline_sentiment_confidences = [row[2] for row in data]
negative_reasons = [row[3] for row in data]
negative_reason_confidences = [row[4] for row in data]
airlines = [row[5] for row in data]
airline_sentiment_golds = [row[6] for row in data]
airline_names = [row[7] for row in data]
negative_reason_golds = [row[8] for row in data]
# Try to convert the retweet_count to an integer. If the conversion fails, set the retweet_count to 0.
retweet_counts = []
for row in data:
    try:
        retweet_counts.append(int(row[9]))
    except ValueError:
        retweet_counts.append(0)
texts = [row[10] for row in data]
tweet_coords = [row[11] for row in data]
tweet_createds = [row[12] for row in data]
tweet_locations = [row[13] for row in data]
user_timezones = [row[14] for row in data]

# Create a dictionary to store the data by airline
airline_data = {}
for i in range(len(airline_names)):
    airline = airline_names[i]
    if airline not in airline_data:
        airline_data[airline] = []
    airline_data[airline].append({
        'tweet_id': tweet_ids[i],
        'airline_sentiment': airline_sentiments[i],
        'airline_sentiment_confidence': airline_sentiment_confidences[i],
        'negative_reason': negative_reasons[i],
        'negative_reason_confidence': negative_reason_confidences[i],
        'airline_sentiment_gold': airline_sentiment_golds[i],
        'negative_reason_gold': negative_reason_golds[i],
        'retweet_count': retweet_counts[i],
        'text': texts[i],
        'tweet_coord': tweet_coords[i],
        'tweet_created': tweet_createds[i],
        'tweet_location': tweet_locations[i],
        'user_timezone': user_timezones[i]
    })

# Create a bar chart showing the number of tweets for each airline
plt.figure(figsize=(10, 6))
plt.bar(airline_names, [len(airline_data[airline]) for airline in airline_names])
plt.xlabel('Airline')
plt.ylabel('Number of tweets')
plt.title('Number of tweets for each airline in the Tweets')
plt.show()

# Create a pie chart showing the percentage of tweets with each airline sentiment
airline_sentiment_counts = {}
for airline in airline_data:
    for tweet in airline_data[airline]:
        airline_sentiment = tweet['airline_sentiment']
        if airline_sentiment not in airline_sentiment_counts:
            airline_sentiment_counts[airline_sentiment] = 0
        airline_sentiment_counts[airline_sentiment] += 1

plt.figure(figsize=(10, 6))
plt.pie(list(airline_sentiment_counts.values()), labels=list(airline_sentiment_counts.keys()), autopct='%1.1f%%')
plt.title('Percentage of tweets with each airline sentiment')
plt.show()

# Create a scatter plot showing the relationship between
