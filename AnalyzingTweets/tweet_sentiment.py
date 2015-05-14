################################################################################
##                   Copyright(c) Arsalan Khairani, 2014                      ##
##                                                                            ##
##               Introduction to Data Science by Bill Howe, UW                ##
##                           Hosted on Coursera                               ##
##                               Python 2.7                                   ##
##                                                                            ##
## Skeleton code was provided as startup. This code tends to analyze tweets   ##
## and based on the words (positive or Negative) used assign a score to       ##
## each tweet. Only works for english words. AFINN-111.txt contains all the   ##
## most commonly used english words with their score labeled by               ##
## Finn Arup Nielsen in 2009-2011.                                            ##
##                                                                            ##
## This database of words is copyright protected and distributed under        ##
## "Open Database License (ODbL) v1.0"                                        ##
## http://www.opendatacommons.org/licenses/odbl/1.0/ or a similar             ##
## copyleft license.                                                          ##
################################################################################

import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}

    # The sent_file contains tab delimaters words and their scores
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)

    tweets = {}
    tweetScore = {}
    i = 0

    # Process each line and convert it into json
    for line in tweet_file:
        tweetJS = json.loads(line)

        # if tweet donot contains text place empty and score 0
        if "text" not in tweetJS.keys():
            tweets[i] = ""
            tweetScore[i] = 0
            continue # Goto next line
        
        tweets[i] = tweetJS["text"].encode('utf-8')

        score = 0

        # Break the lines into words and process each word
        for word in tweets[i].split(' '):
            if word in scores.keys():
                score += scores[word]

        tweetScore[i] = score

        # Increment dictionary index    
        i+=1

    for key in tweetScore:
        print (tweetScore[key])

if __name__ == '__main__':
    main()
