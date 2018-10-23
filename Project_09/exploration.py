import sys
import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv('data/CRDC2013_14.csv', encoding='Latin-1')
    jj_counts = data['JJ'].value_counts()
    magnet_counts = data['SCH_STATUS_MAGNET'].value_counts()
    print('JJ counts: ', jj_counts)
    print('Magent counts: ', magnet_counts)
    
    print(pd.pivot_table(data, values=['TOT_ENR_M', 'TOT_ENR_F'], index='JJ', aggfunc='sum'))
    print(pd.pivot_table(data, values=['TOT_ENR_M', 'TOT_ENR_F'], index='SCH_STATUS_MAGNET', aggfunc='sum'))