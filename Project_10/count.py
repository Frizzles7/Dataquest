import read
from collections import Counter
import re

df = read.load_data()

# concatenate all headlines with spaces
all_headlines = df['headline'].str.cat(sep=' ').lower()
# remove all special characters
all_headlines = re.sub('[^A-Za-z0-9 ]+', '', all_headlines)
# create counts for each word in headl
counts = Counter(all_headlines.split())

if __name__ == "__main__":
    print(counts.most_common(100))
