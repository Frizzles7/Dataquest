import read

def remove_subdomain(url):
    url = str(url)
    if url.count('.') > 1:
        ind = url.find('.')
        return url[ind+1:]
    else:
        return url

df = read.load_data()
domain_counts = df['url'].dropna().apply(remove_subdomain).value_counts()

if __name__ == "__main__":
    for name, row in domain_counts[0:99].items():
        print("{0}: {1}".format(name, row))
