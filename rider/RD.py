from import_this import(
    generate_race_data,
    RaceInfo,
)
from seconds import seconds_conversion

def win_racer(race_data):
    winner: str =""
    for i in race_data.values():
        if i.get('FinishedPlace') == 1:
            winner = i.get('RacerName')
            print("Выиграл -",winner,"!!! Поздравляем!!")
            print("_"*(28 + len(winner)))
    return 
def first_three_racers(race_data):
    print("\nПервые три места:\n")
    for i in race_data.values():
        if i.get('FinishedPlace') == 1:
            print('\tГонщик на 1 месте:')
            print('\t\tИмя:',i.get('RacerName'))
            print('\t\tКоманда:',i.get('RacerTeam'))
            print('\t\tВремя:',seconds_conversion(i.get('FinishedTimeSeconds')))
    for i in race_data.values():
        if i.get('FinishedPlace') == 2:
            print('\n\tГонщик на 2 месте:')
            print('\t\tИмя:',i.get('RacerName'))
            print('\t\tКоманда:',i.get('RacerTeam'))
            print('\t\tВремя:',seconds_conversion(i.get('FinishedTimeSeconds')))
    for i in race_data.values():
        if i.get('FinishedPlace') == 3:
            print('\n\tГонщик на 3 месте:')
            print('\t\tИмя:',i.get('RacerName'))
            print('\t\tКоманда:',i.get('RacerTeam'))
            print('\t\tВремя:',seconds_conversion(i.get('FinishedTimeSeconds')))
    return

if __name__ == '__main__': 
    race_data: RaceInfo = generate_race_data(10)
    win_racer(race_data)
    first_three_racers(race_data)

