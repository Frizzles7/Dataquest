import pandas as pd

def load_data():
    dataset = pd.read_csv('hn_stories.csv', 
                    names = ['submission_time', 'upvotes', 'url', 'headline'])
    return dataset

if __name__ == "__main__":
    dataset = load_data()
 