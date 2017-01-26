import requests
import bs4
import json
from collections import OrderedDict

def main():
    scrapeFighterInfoPage({})
    # print(elems[0].text)

    # saveWebPage("http://www.fightmetric.com/fighter-details/d0f3959b4a9747e6", "test2.txt")
    
def saveWebPage(url, fileName):
    res = requests.get(url)
    res.raise_for_status()
    file = open(fileName, 'wb')
    for chunk in res.iter_content(100000):
        file.write(chunk)

    file.close()

def scrapeFighterInfoPage(individualFighterInformationDict):
    response = open("test2.txt")
    soupRes = bs4.BeautifulSoup(response, 'lxml')
    figherStatsHTML = soupRes.select('.b-list__info-box li')

    fighterCareerStats = []

    for elements in figherStatsHTML:
        statArray = elements.findAll(text=True)
        fighterCareerStats.append(statArray[2].strip())


    individualFighterInformationDict['Height'] = fighterCareerStats[0]
    individualFighterInformationDict['Weight'] = fighterCareerStats[1]
    individualFighterInformationDict['Reach'] = fighterCareerStats[2]
    individualFighterInformationDict['Stance'] = fighterCareerStats[3]
    individualFighterInformationDict['Birthday'] = fighterCareerStats[4]
    individualFighterInformationDict['SignificantStrikesLandedPerMinute'] = fighterCareerStats[5]
    individualFighterInformationDict['SignificantStrikingAccuracy'] = fighterCareerStats[6]
    individualFighterInformationDict['SignificantStrikesAbsorbedPerMinute'] = fighterCareerStats[7]
    individualFighterInformationDict['SignificantStrikeDefence'] = fighterCareerStats[8]
    individualFighterInformationDict['AverageTakedownsLandedPer15Minutes'] = fighterCareerStats[10]
    individualFighterInformationDict['TakedownAccuracy'] = fighterCareerStats[11]
    individualFighterInformationDict['TakedownDefense'] = fighterCareerStats[12]
    individualFighterInformationDict['AverageSubmissionsAttemptedPer15Minutes'] = fighterCareerStats[13]

    




def getAllFighters():
    response = open("test.txt")
    soupRes = bs4.BeautifulSoup(response)
    elems = soupRes.select('tr')
    elems = elems[2:]

    FightInformation = []

    for figherInfo in elems:
        figherInfoElements = figherInfo.select('td')
        individualFighterInformation = []
        individualFighterInformationDict = OrderedDict()
        for infoField in figherInfoElements:
            individualFighterInformation.append(infoField.text.strip())


        individualFighterInformationDict['name'] = individualFighterInformation[0] + ' ' + individualFighterInformation[1]
        individualFighterInformationDict['nickName'] = individualFighterInformation[2]
        individualFighterInformationDict['height'] = individualFighterInformation[3]
        individualFighterInformationDict['weight'] = individualFighterInformation[4]
        individualFighterInformationDict['reach'] = individualFighterInformation[5]
        individualFighterInformationDict['stance'] = individualFighterInformation[6]
        individualFighterInformationDict['wins'] = individualFighterInformation[7]
        individualFighterInformationDict['loses'] = individualFighterInformation[8]
        individualFighterInformationDict['draws'] = individualFighterInformation[9]
        FightInformation.append(individualFighterInformationDict)

    jsonFight = json.dumps(FightInformation)
    print(jsonFight)


if __name__ == '__main__':
    main()





