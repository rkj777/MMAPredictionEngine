import requests
import bs4
import json
from collections import OrderedDict

def main():
    scrapeFighterInfoPage()
    # print(elems[0].text)

    # saveWebPage("http://www.fightmetric.com/fighter-details/d0f3959b4a9747e6", "test2.txt")
    
def saveWebPage(url, fileName):
    res = requests.get(url)
    res.raise_for_status()
    file = open(fileName, 'wb')
    for chunk in res.iter_content(100000):
        file.write(chunk)

    file.close()

def scrapeFighterInfoPage():
   response = open("test2.txt")
   soupRes = bs4.BeautifulSoup(response)
   elems = soupRes.select('.b-list__info-box li')
   for elements in elems:
       print(elements.findAll(text=True))
       #print(elements.findAll(text=True)[2].strip())

   #print(elems)





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






