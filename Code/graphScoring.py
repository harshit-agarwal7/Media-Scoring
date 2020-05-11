import pandas as pd
import math

def calculateScore(accounts, mediaLoc):
	""" Calculates the average distance of a media organization from the propaganda accounts of a political party"""
	score = 0
	for acc in accounts:
		accLoc = df[(df['Id'] == acc)].index.values.astype(int)[0]

		dist = 0
		for i in range(1, 5):
			dist = dist + math.pow(df.loc[mediaLoc, 'Dimension_{0}'.format(i)] - df.loc[accLoc, 'Dimension_{0}'.format(i)], 2)
		dist = math.sqrt(dist)

		score = score + dist

	return score/len(accounts)


df = pd.read_csv('Degree50Dim4.csv')

listOfMedia = ['aajtak', 'AmarUjalaNews', 'BloombergQuint', 'bsindia', 'BTVI', 'businessline', 'CNBCTV18Live', 'CNBC_Awaaz', 'CNNnews18', 'DainikBhaskar', 'DDNewsLive', 'DeccanChronicle', 'DeccanHerald', 'dna', 'EconomicTimes', 'ETNOWlive', 'FinancialXpress', 'firstpost', 'FortuneIndia', 'fpjindia', 'HindustanTimes', 'htTweets', 'HuffPostIndia', 'IndianExpress', 'IndiaToday', 'indiatvnews', 'JagranNews', 'livemint', 'LogicalIndians', 'mid_day', 'MirrorNow', 'MumbaiMirror', 'NavbharatTimes', 'ndtv', 'ndtvindia', 'NDTVProfit', 'NewIndianXpress', 'News18India', 'News24', 'NEWS9', 'newslaundry', 'NewsX', 'OfficialRDIndia', 'Oneindia', 'otvnews', 'Outlookindia', 'postcard_news', 'qzindia', 'RealRediffCom', 'republic', 'ReutersIndia', 'rightlog_in', 'RisingKashmir', 'rpbreakingnews', 'RVCJ_FB', 'ScoopWhoop', 'scroll_in', 'SundayGuardian', 'SwarajyaMag', 'TheAsianAgeNews', 'thebetterindia', 'TheDailyPioneer', 'thenewsminute', 'TheQuint', 'TheStatesmanLtd', 'thetribunechd', 'TheWeek', 'thewire_in', 'the_hindu', 'TimesNow', 'otimesofindia', 'WIONews', 'YahooNews', 'YouthKiAwaaz', 'ZeeBusiness', 'ZeeNews']

I = pd.Index(listOfMedia, name="rows")
C = pd.Index(['Closeness to BJP', 'Closeness to Congress'], name="columns")
dfResult = pd.DataFrame(index=I, columns=C)

dfBJP = pd.read_csv('BJPPropaganda.csv') #BJPPropaganda.csv contains accounts that were spreading propaganda for BJP 
dfCongress = pd.read_csv('CongressPropaganda.csv')
BJPAccounts = dfBJP["Id"].tolist()
CongressAccounts = dfCongress["Id"].tolist()


for mediaHouse in listOfMedia:
	if df['Label'].str.contains(mediaHouse).any():
		mediaLoc = df[(df['Label'] == mediaHouse)].index.values.astype(int)[0]

		BJPScore = 0
		CongressScore = 0

		BJPScore = calculateScore(BJPAccounts, mediaLoc)
		CongressScore = calculateScore(CongressAccounts, mediaLoc)

		dfResult.at[mediaHouse, 'Closeness to BJP'] = BJPScore
		dfResult.at[mediaHouse, 'Closeness to Congress'] = CongressScore 
		print("Closeness to BJP:", BJPScore, "Closeness to Congress:",  CongressScore)

dfResult.to_csv('PropagandaClosenessDim4Degree50.csv')			
	# The smaller the distance, the closer the node will be to the propaganda nodes. 
