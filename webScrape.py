import requests
import bs4
import json
from collections import OrderedDict

def main():
    scrapeFightPage("", {},True)
    # print(elems[0].text)

    #saveWebPage("http://www.fightmetric.com/fight-details/84c5035830ebb421", "test4.txt")
    
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

    # Scraping Past Fight Information
    fightHistroyTable = soupRes.select('tr')
    scrapedPastFightData = []
    
    for pastFight in fightHistroyTable[2:3]:
        pastFightInfo = pastFight.select('td')

        fightInfoLink = pastFight.select('a')[0].get('href')

        #print(pastFightInfo)
        pastFightInfoArray = []
        pastFightInfoDictionary = {}
        for inforField in pastFightInfo:
            pastFightInfoArray.append(inforField.findAll(text=True))

        pastFightInfoDictionary['Result'] = pastFightInfoArray[0][2].strip()
        pastFightInfoDictionary['Opponent'] = pastFightInfoArray[1][6].strip()
        pastFightInfoDictionary['Result'] = pastFightInfoArray[7][1].strip()
        pastFightInfoDictionary["EndRound"] = pastFightInfoArray[8][1].strip()
        pastFightInfoDictionary["EndTime"] = pastFightInfoArray[9][1].strip()
        pastFightInfoDictionary["ResultMethod"] = pastFightInfoArray[7][3].strip()

        # Fields that may not be important features

        # Fighter name redundant. Uncomment to add fighter name to each fight history
        # pastFightInfoDictionary['FighterName'] = pastFightInfoArray[1][2].strip()

        # Fight card name
        # pastFightInfoDictionary['FightCardName'] = pastFightInfoArray[6][2].strip()

        # Fight date
        # pastFightInfoDictionary['FightDate'] = pastFightInfoArray[6][6].strip()

        scrapedPastFightData.append(pastFightInfoDictionary)

        # Moving into individual fight web pages

    print(scrapedPastFightData)

def scrapeFightPage(url, pastFightInfoDictionary, victory):
    response = requests.get('http://www.fightmetric.com/fight-details/1d7015553debd1c8')

    if victory:
        fighterIndex = 3
        opponentIndex = 1
    else:
        fighterIndex = 1
        opponentIndex = 3

    soupRes = bs4.BeautifulSoup(response.text,'lxml')

    elems = soupRes.select(".b-fight-details__table-body")
    totalFightStats = elems[0].select("td")

    pastFightInfoDictionary['fighterKnockDowns'] = totalFightStats[1].findAll(text=True)[fighterIndex].strip()
    pastFightInfoDictionary['OpponentKnockDowns'] = totalFightStats[1].findAll(text=True)[opponentIndex].strip()
    pastFightInfoDictionary['FighterSignificantStrikes'] = totalFightStats[2].findAll(text=True)[fighterIndex].strip()
    pastFightInfoDictionary['OpponentSignificantStrikes'] = totalFightStats[2].findAll(text=True)[opponentIndex].strip()
    pastFightInfoDictionary['FighterSignificantStrikesPercent'] = totalFightStats[3].findAll(text=True)[fighterIndex].strip()
    pastFightInfoDictionary['OpponentSignificantStrikesPercent'] = totalFightStats[3].findAll(text=True)[opponentIndex].strip()
    pastFightInfoDictionary['FighterTotalStrikes'] = totalFightStats[4].findAll(text=True)[fighterIndex].strip()
    pastFightInfoDictionary['OpponentTotalStrikes'] = totalFightStats[4].findAll(text=True)[opponentIndex].strip()
    pastFightInfoDictionary['FighterTakedowns'] = totalFightStats[5].findAll(text=True)[fighterIndex].strip()
    pastFightInfoDictionary['OpponentTakedowns'] = totalFightStats[5].findAll(text=True)[opponentIndex].strip()
    pastFightInfoDictionary['FighterTakedownPercentage'] = totalFightStats[6].findAll(text=True)[fighterIndex].strip()
    pastFightInfoDictionary['OpponentTakedownPercentage'] = totalFightStats[6].findAll(text=True)[opponentIndex].strip()
    pastFightInfoDictionary['FighterSubmissionAttempts'] = totalFightStats[7].findAll(text=True)[fighterIndex].strip()
    pastFightInfoDictionary['OpponentSubmissionAttempts'] = totalFightStats[7].findAll(text=True)[opponentIndex].strip()
    pastFightInfoDictionary['FighterPass'] = totalFightStats[8].findAll(text=True)[fighterIndex].strip()
    pastFightInfoDictionary['OpponentPass'] = totalFightStats[8].findAll(text=True)[opponentIndex].strip()
    pastFightInfoDictionary['FighterReversals'] = totalFightStats[9].findAll(text=True)[fighterIndex].strip()
    pastFightInfoDictionary['OpponentReversals'] = totalFightStats[9].findAll(text=True)[opponentIndex].strip()
    #print(pastFightInfoDictionary)



    elems = soupRes.select("table")

    totalFightStats = elems[1].select("tr")

    #overallStats = totalFightStats[1].select("td")



    totalRoundArray = []
    for row in totalFightStats[1:]:
        row = row.select("td")
        totalRoundStats = {}
        overallStatsText = [statElement.findAll(text=True) for statElement in row]
        totalRoundStats['fighterKnockDowns'] = overallStatsText[1][fighterIndex].strip()
        totalRoundStats['OpponentKnockDowns'] = overallStatsText[1][opponentIndex].strip()
        totalRoundStats['FighterSignificantStrikes'] = overallStatsText[2][fighterIndex].strip()
        totalRoundStats['OpponentSignificantStrikes'] = overallStatsText[2][opponentIndex].strip()
        totalRoundStats['FighterSignificantStrikesPercent'] = overallStatsText[3][fighterIndex].strip()
        totalRoundStats['OpponentSignificantStrikesPercent'] = overallStatsText[3][opponentIndex].strip()
        totalRoundStats['FighterTotalStrikes'] = overallStatsText[4][fighterIndex].strip()
        totalRoundStats['OpponentTotalStrikes'] = overallStatsText[4][opponentIndex].strip()
        totalRoundStats['FighterTakedowns'] = overallStatsText[5][fighterIndex].strip()
        totalRoundStats['OpponentTakedowns'] = overallStatsText[5][opponentIndex].strip()
        totalRoundStats['FighterTakedownPercentage'] = overallStatsText[6][fighterIndex].strip()
        totalRoundStats['OpponentTakedownPercentage'] = overallStatsText[6][opponentIndex].strip()
        totalRoundStats['FighterSubmissionAttempts'] = overallStatsText[7][fighterIndex].strip()
        totalRoundStats['OpponentSubmissionAttempts'] = overallStatsText[7][opponentIndex].strip()
        totalRoundStats['FighterPass'] = overallStatsText[8][fighterIndex].strip()
        totalRoundStats['OpponentPass'] = overallStatsText[8][opponentIndex].strip()
        totalRoundStats['FighterReversals'] = overallStatsText[9][fighterIndex].strip()
        totalRoundStats['OpponentReversals'] = overallStatsText[9][opponentIndex].strip()
        totalRoundArray.append(totalRoundStats)

    pastFightInfoDictionary['RoundByRoundTotals'] = totalRoundArray
    #print(pastFightInfoDictionary)
    #print(overallStatsText)


    sigFightStats = elems[2].select("tr")
    sigFightStats = sigFightStats[1].select("td")
    sigStatsText = [statElement.findAll(text=True) for statElement in sigFightStats]
    #print(sigStatsText)

    pastFightInfoDictionary['fighterHeadSigStrikes'] = sigStatsText[3][fighterIndex].strip()
    pastFightInfoDictionary['OpponentHeadSigStrikes'] = sigStatsText[3][opponentIndex].strip()
    pastFightInfoDictionary['FighterBodySigStrikes'] = sigStatsText[4][fighterIndex].strip()
    pastFightInfoDictionary['OpponentBodySigStrikes'] = sigStatsText[4][opponentIndex].strip()
    pastFightInfoDictionary['FighterLegSigStrikes'] = sigStatsText[5][fighterIndex].strip()
    pastFightInfoDictionary['OpponentLegSigStrikes'] = sigStatsText[5][opponentIndex].strip()
    pastFightInfoDictionary['FighterDistanceSigStrikes'] = sigStatsText[6][fighterIndex].strip()
    pastFightInfoDictionary['OpponentDistanceSigStrikes'] = sigStatsText[6][opponentIndex].strip()
    pastFightInfoDictionary['FighterClinchSigStrikes'] = sigStatsText[7][fighterIndex].strip()
    pastFightInfoDictionary['OpponentClinchSigStrikes'] = sigStatsText[7][opponentIndex].strip()
    pastFightInfoDictionary['FighterGroundSigStrikes'] = sigStatsText[8][fighterIndex].strip()
    pastFightInfoDictionary['OpponentGroundSigStrikes'] = sigStatsText[8][opponentIndex].strip()

    #print(pastFightInfoDictionary)


    roundByRoundSigStats = elems[3].select("tr")
    sigRoundArray = []
    for row in roundByRoundSigStats[1:]:
        row = row.select("td")
        sigRoundStats = {}
        overallStatsText = [statElement.findAll(text=True) for statElement in row]
        sigRoundStats['fighterSigStrikes'] = overallStatsText[1][fighterIndex].strip()
        sigRoundStats['OpponentSigStrikes'] = overallStatsText[1][opponentIndex].strip()
        sigRoundStats['fighterSigStrikesPercent'] = overallStatsText[2][fighterIndex].strip()
        sigRoundStats['OpponentSigStrikesPercent'] = overallStatsText[2][opponentIndex].strip()
        sigRoundStats['fighterHeadSigStrikes'] = overallStatsText[3][fighterIndex].strip()
        sigRoundStats['OpponentHeadSigStrikes'] = overallStatsText[3][opponentIndex].strip()
        sigRoundStats['FighterBodySigStrikes'] = overallStatsText[4][fighterIndex].strip()
        sigRoundStats['OpponentBodySigStrikes'] = overallStatsText[4][opponentIndex].strip()
        sigRoundStats['FighterLegSigStrikes'] = overallStatsText[5][fighterIndex].strip()
        sigRoundStats['OpponentLegSigStrikes'] = overallStatsText[5][opponentIndex].strip()
        sigRoundStats['FighterDistanceSigStrikes'] = overallStatsText[6][fighterIndex].strip()
        sigRoundStats['OpponentDistanceSigStrikes'] = overallStatsText[6][opponentIndex].strip()
        sigRoundStats['FighterClinchSigStrikes'] = overallStatsText[7][fighterIndex].strip()
        sigRoundStats['OpponentClinchSigStrikes'] = overallStatsText[7][opponentIndex].strip()
        sigRoundStats['FighterGroundSigStrikes'] = overallStatsText[8][fighterIndex].strip()
        sigRoundStats['OpponentGroundSigStrikes'] = overallStatsText[8][opponentIndex].strip()
        sigRoundArray.append(sigRoundStats)

    pastFightInfoDictionary['SigRoundByRoundTotals'] = sigRoundArray
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






