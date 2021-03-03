import ESPNtop100

# empty lists to be looped through and populated with draft data
pickList = []
teamList = []
playerList = []
schoolList = []

# These will become the lists with the extracted data
lists = [pickList,
         teamList,
         playerList,
         schoolList]

lists = ESPNtop100.scrapeESPN('https://www.espn.com/nba/draft/bestavailable', lists)
lists = ESPNtop100.scrapeESPN('https://www.espn.com/nba/draft/bestavailable/_/position/ovr/page/2', lists)
lists = ESPNtop100.scrapeESPN('https://www.espn.com/nba/draft/bestavailable/_/position/ovr/page/3', lists)
lists = ESPNtop100.scrapeESPN('https://www.espn.com/nba/draft/bestavailable/_/position/ovr/page/4', lists)
print(lists)
print(zip(*lists))
for column in zip(*lists):
    for n, elem in enumerate(column):
        if n != 1:
            print(elem,end=' ')
    print()
