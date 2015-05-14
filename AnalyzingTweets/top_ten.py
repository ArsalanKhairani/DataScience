################################################################################
##                   Copyright(c) Arsalan Khairani, 2014                      ##
##                                                                            ##
##               Introduction to Data Science by Bill Howe, UW                ##
##                           Hosted on Coursera                               ##
##                               Python 2.7                                   ##
##                                                                            ##
## This code analyze the tweets and extract out the hashtags from it. By      ##
## analyzing many tweets it then gives out top ten hashtags that are trending ##
################################################################################

import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    
    hashtags = {}

    # Process each line and convert it into json
    for line in tweet_file:
        tweetJS = json.loads(line)

        allHashtags = []

        # If it have entities key
        if "entities" in tweetJS:
            entities = tweetJS["entities"]

            # and have hashtags
            if "hashtags" in entities:
                allHashtags = entities["hashtags"]

        # For all hashtags in a tweet increment its score in dictionary
        for hashtag in allHashtags:
            ht = hashtag["text"].encode('utf-8')
            if ht in hashtags.keys():
                hashtags[ht] += 1
            else:
                hashtags[ht] = 1

    # Get the top ten
    toptenHashtags = sorted(hashtags.keys(), key = lambda k:hashtags[k], reverse=True)[:10]

    # Print in required format
    for hs in toptenHashtags:
        print ('%s %d'%(hs, hashtags[hs]))
    
if __name__ == '__main__':
    main()
