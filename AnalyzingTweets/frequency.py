################################################################################
##                   Copyright(c) Arsalan Khairani, 2014                      ##
##                                                                            ##
##               Introduction to Data Science by Bill Howe, UW                ##
##                           Hosted on Coursera                               ##
##                               Python 2.7                                   ##
##                                                                            ##
## This code tends to calculate the frequency at which the word appears in    ##
## tweets. Thus can be used to find out what's trending.                      ##
################################################################################

import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    tweets = {}
    wordFrequency = {}    
    i = 0

    # Process each line and convert it into json
    for line in tweet_file:
        tweetJS = json.loads(line)

        # if tweet donot contains text place empty
        if "text" not in tweetJS.keys():
            tweets[i] = ""

        else:
            tweetText = tweetJS["text"].encode('utf-8')

            # Remove new line character so as to have correct format in output
            fixedTweetText = tweetText.replace('\n', '')
            tweets[i] = fixedTweetText
            
        unappearedTerms = []

        # Break the lines into words and process each word to count frequency
        for word in tweets[i].split(' '):
            if word in wordFrequency.keys():
                wordFrequency[word] += 1
            else:
                wordFrequency[word] = 1

        # Increment dictionary index
        i+=1

    # Compute total frequency
    totalFrequency = sum(wordFrequency.values())

    # Print in required format
    for word in wordFrequency:
        frequency = float(wordFrequency[word])/float(totalFrequency)
        print('%s %.4f' % (word, frequency))

if __name__ == '__main__':
    main()
