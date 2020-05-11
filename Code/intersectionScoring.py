import numpy as np
import pandas as pd

#listOfMedia = ['aajtak.csv', 'AmarUjalaNews.csv', 'BloombergQuint.csv', 'bsindia.csv', 'BTVI.csv', 'businessline.csv', 'CNBCTV18Live.csv', 'CNBC_Awaaz.csv', 'CNNnews18.csv', 'DainikBhaskar.csv', 'DDNewsLive.csv', 'DeccanChronicle.csv', 'DeccanHerald.csv', 'dna.csv', 'EconomicTimes.csv', 'ETNOWlive.csv', 'FinancialXpress.csv', 'firstpost.csv', 'FortuneIndia.csv', 'fpjindia.csv', 'HindustanTimes.csv', 'htTweets.csv', 'HuffPostIndia.csv', 'IndianExpress.csv', 'IndiaToday.csv', 'indiatvnews.csv', 'JagranNews.csv', 'livemint.csv', 'LogicalIndians.csv', 'mid_day.csv', 'MirrorNow.csv', 'MumbaiMirror.csv', 'NavbharatTimes.csv', 'ndtv.csv', 'ndtvindia.csv', 'NDTVProfit.csv', 'NewIndianXpress.csv', 'News18India.csv', 'News24.csv', 'NEWS9.csv', 'newslaundry.csv', 'NewsX.csv', 'OfficialRDIndia.csv', 'Oneindia.csv', 'otvnews.csv', 'Outlookindia.csv', 'postcard_news.csv', 'qzindia.csv', 'RealRediffCom.csv', 'republic.csv', 'ReutersIndia.csv', 'rightlog_in.csv', 'RisingKashmir.csv', 'rpbreakingnews.csv', 'RVCJ_FB.csv', 'ScoopWhoop.csv', 'scroll_in.csv', 'SundayGuardian.csv', 'SwarajyaMag.csv', 'TheAsianAgeNews.csv', 'thebetterindia.csv', 'TheDailyPioneer.csv', 'thenewsminute.csv', 'TheQuint.csv', 'TheStatesmanLtd.csv', 'thetribunechd.csv', 'TheWeek.csv', 'thewire_in.csv', 'the_hindu.csv', 'TimesNow.csv', 'otimesofindia.csv', 'WIONews.csv', 'YahooNews.csv', 'YouthKiAwaaz.csv', 'ZeeBusiness.csv', 'ZeeNews.csv']
listOfMedia = ['ndtv.csv', 'otimesofindia.csv']


I = pd.Index(listOfMedia, name="rows")
C = pd.Index(listOfMedia, name="columns")
df = pd.DataFrame(index=I, columns=C) #df stores intersection_of_sets/size_of_set
df_j = pd.DataFrame(index=I, columns=C) #df_j stores jaccard values

for i in range(len(listOfMedia)-1):
	data1 = np.loadtxt(listOfMedia[i], skiprows=1, dtype=object)
	len1 = len(data1)
	for j in range(i+1,len(listOfMedia)):
		data2 = np.loadtxt(listOfMedia[j], skiprows=1, dtype=object)
		len2 = len(data2)

		commonIds = np.intersect1d(data1, data2)

		df.at[listOfMedia[i],listOfMedia[j]] = len(commonIds)/len1
		df.at[listOfMedia[j],listOfMedia[i]] = len(commonIds)/len2

		jscore = len(commonIds) / (len1 + len2 - len(commonIds)) #Jaccard Score
		df_j.at[listOfMedia[i],listOfMedia[j]] = jscore


df.to_csv('intersectionValues.csv')
df_j.to_csv('intersectionValues_j.csv')

