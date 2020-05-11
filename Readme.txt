In this project, I have collected all tweets from all popular hashtags relating to the Pulwama attack from 14th Feb (day of attack) to 21st Feb. I have used this data to find out which news outlets are used by political parties to spread their propaganda. I have done this by identifying accounts which spread propaganda on behalf of BJP and Congress and then finding out which news organizations are 'closer' to them on the graph. To measure this closeness, I have used Multidimensional Scaling Analysis(MDS) using the MDS plugin on Gephi. The plugin uses path distances between nodes as input it assigns geometric coordinates to the nodes in such a way that nodes with shorter path distances are close together and nodes with longer path distances are far apart. All graph analysis was done using the help of Gephi.

Code:

extractingFollowerIds.py - mines follower ids of a given twitter handle

extractingWeights.py - extracts count of how many times one twitter account retweets another. This information is used as the weight between the nodes in the graph.

graphScoring.py - Finds how 'close' a media organization is to a given political party. (See description above on how closeness is measured)

idsToNames.py - Mines twitter handles of users using their twitter Ids.

intersectionScoring.py - calculates the intersection scores described in the Results section.


Datasets:

masterFileWithWeights.csv contains information about how many times a Twitter user retweeted any other user in the database. I ran ForceAtlas2 using Gephi on this dataset to have a graphical representation in which users that retweet each other more are placed closer.

BJPPropaganda.csv and CongressPropaganda.csv contains the list of accounts that were spreading their propaganda on behalf of BJP and Congress respectively. I found this by locating networks in which users that had an unusually large number of tweets and who retweet each other very often. These lists have all accounts that retweet other accounts in the local networks more than 30 times.

(I have not uploaded many of the datasets to keep the repository small in size.)
 
Results and Misc:

BJPGraph.xlsx and CongressGraph.xlsx contains graphs that show which media organizations are preferred by propaganda accounts of either party.(These graphs are incomplete as I couldn't find the time to run analysis for all organizations.)

intersectionValues.csv contains ratios of common number of followers and total number of followers for every pair of media organizations.

IntersectionValues_j.csv contains jaccard scores for every pair of media organizations

twitterNetwork.gephi is the graph file that can be run using Gephi to play around with the graph.

ForceAtlasonNodes.png is a screenshot of the graph after running ForceAtlas2 on it.


Contact me if you need any help understanding the project or want access to all the datasets that I had mined.