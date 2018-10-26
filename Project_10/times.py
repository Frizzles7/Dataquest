import read
from dateutil.parser import parse

# determine hour of submission
def extract_hour(timestamp):
    exact_time = parse(timestamp)
    hour = exact_time.hour
    return hour

df = read.load_data()
times = df['submission_time'].dropna().apply(extract_hour).value_counts()

if __name__ == "__main__":
    # print results to show most common submission hours
    for name, row in times.items():
        print("{0}: {1}".format(name, row))
