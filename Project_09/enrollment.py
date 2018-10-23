import sys
import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv('data/CRDC2013_14.csv', encoding='Latin-1')
    data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']
    all_enrollment = data['total_enrollment'].sum()
    
    races = ['HI', 'AM', 'AS', 'HP', 'BL', 'WH', 'TR']
    genders = ['M', 'F']
    
    totals = {}
    for race in races:
        race_m = 'SCH_ENR_' + race + '_' + genders[0]
        race_f = 'SCH_ENR_' + race + '_' + genders[1]
        totals[race_m] = data[race_m].sum() / all_enrollment
        totals[race_f] = data[race_f].sum() / all_enrollment
    
    for key, value in totals.items():
        print(key, value)