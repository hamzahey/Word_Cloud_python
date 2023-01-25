import pandas as pd
from wordcloud import WordCloud, STOPWORDS

# Read the CSV file
df = pd.read_csv("gdelt_conflict.csv")

# Concatenate all the text columns into one string
text = ' '.join(df[['CountryName','EventRootDescr','EventDescr']].apply(lambda x: ' '.join(x.astype(str)), axis=1).tolist())


# Create a word cloud object
wordcloud = WordCloud(stopwords=STOPWORDS,collocations=False,max_words=176000, background_color='white',height=600,width=1200).generate(text)


# Save the word cloud as a PNG image
wordcloud.to_file("wordcloud.png")
