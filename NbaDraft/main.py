import ESPNtop100

# empty lists to be looped through and populated with draft data
pickList = []
teamList = []
playerList = []
schoolList = []
positionList = []

# These will become the lists with the extracted data
lists = [pickList,
         teamList,
         playerList,
         schoolList,
         positionList]

lists = ESPNtop100.scrapeESPN('https://www.espn.com/nba/draft/bestavailable', lists)
lists = ESPNtop100.scrapeESPN('https://www.espn.com/nba/draft/bestavailable/_/position/ovr/page/2', lists)
lists = ESPNtop100.scrapeESPN('https://www.espn.com/nba/draft/bestavailable/_/position/ovr/page/3', lists)
lists = ESPNtop100.scrapeESPN('https://www.espn.com/nba/draft/bestavailable/_/position/ovr/page/4', lists)

formattedLists = lists[0:1]
formattedLists.extend(lists[2:])

for column in zip(*formattedLists):
    for n, elem in enumerate(column):
        print(elem,end=' ')
    print()