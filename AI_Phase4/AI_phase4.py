import plotly.express as px
import pandas as pd

# Load the CSV file
df = pd.read_csv('Tweets.csv')

# Create a new column called `count` and populate it with the number of tweets for each sentiment label
df['count'] = df['airline_sentiment'].value_counts()

# Create a bar chart of the overall sentiment distribution
fig = px.bar(df, x='airline_sentiment', y='name', color='airline_sentiment', color_continuous_scale='Viridis')
fig.update_layout(title='Overall Sentiment Distribution', xaxis_title='Sentiment Label', yaxis_title='Number of Tweets')
fig.show()

# Create a pie chart of the overall sentiment distribution
fig = px.pie(df, values='count', names='airline_sentiment', hole=0.5)
fig.update_layout(title='Overall Sentiment Distribution')
fig.show()

# Create a word cloud of the most common words used in the tweets
words = df['text'].str.split().sum()
fig = px.wordcloud(words, max_font_size=50, max_words=200)
fig.update_layout(title='Word Cloud of Most Common Words')
fig.show()

# Create a map of the locations from which the tweets were sent
fig = px.scatter_mapbox(df, lat='tweet_latitude', lon='tweet_longitude', color='airline_sentiment', size_max=15, zoom=3)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(title='Map of Tweet Locations')
fig.show()

# Create a scatter plot of the sentiment score vs. retweet count
fig = px.scatter(df, x='retweet_count', y='airline_sentiment', color='airline_sentiment')
fig.update_layout(title='Scatter Plot of Sentiment Score vs. Retweet Count', xaxis_title='Retweet Count', yaxis_title='Sentiment Score')
fig.show()

# Create a box plot of the sentiment score for each airline
fig = px.box(df, x='airline_name', y='airline_sentiment', color='airline_name')
fig.update_layout(title='Box Plot of Sentiment Score for Each Airline', yaxis_title='Sentiment Score')
fig.show()

# Create a line chart of the average sentiment score over time
df_sentiment_over_time = df.groupby('tweet_created')['airline_sentiment'].mean()
fig = px.line(df_sentiment_over_time, x=df_sentiment_over_time.index, y=df_sentiment_over_time.values)
fig.update_layout(title='Line Chart of Average Sentiment Score Over Time', xaxis_title='Date', yaxis_title='Sentiment Score')
fig.show()
