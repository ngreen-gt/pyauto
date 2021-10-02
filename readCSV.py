import pandas as pd

autos = pd.read_csv("autos.csv", header=0)

#autos = autos.
teams = autos.drop_duplicates('team').sort_values('team')
teams = teams['team'].tolist()

for team in teams:
    print(autos[autos.team == team])


print(teams)
# print(autos[autos.team == 1108])

