################################################################################
##                   Copyright(c) Arsalan Khairani, 2014                      ##
##                                                                            ##
##               Introduction to Data Science by Bill Howe, UW                ##
##                           Hosted on Coursera                               ##
##                               Python 2.7                                   ##
##                                                                            ##
## This code tends to analyze tweets and based on the words (positive or      ##
## Negative) words used assign a score to each tweet. Only works for english  ##
## words. AFINN-111.txt contains all the most commonly used english words     ##
## with their score labeled by Finn Arup Nielsen in 2009-2011. It then finds  ##
## out using the score assigned, the happiest state of all in United States.  ##
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

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    tweets = {}
    tweetScore = {}
    stateScore = {}
    i = 0

    # Process each line and convert it into json
    for line in tweet_file:
        tweetJS = json.loads(line)

        # if tweet donot contains text place empty and score 0
        if "text" not in tweetJS.keys():
            tweets[i] = ""
            tweetScore[i] = 0
            continue

        tweets[i] = tweetJS["text"].encode('utf-8')
              
        score = 0

        # Break the lines into words and process each word
        for word in tweets[i].split(' '):
            if word in scores.keys():
                score += scores[word]

        tweetScore[i] = score

        # Get location of each tweet user (location: LosAngeles, CA)
        loc = tweetJS["user"]["location"].encode('utf-8').split(', ')
        if (len(loc) >= 2):
            
            # Get the state initials
            if (loc[1] in states.keys()):
                if loc[1] in stateScore.keys():
                    stateScore[loc[1]] += tweetScore[i]
                else:
                    stateScore[loc[1]] = tweetScore[i]

        # Increment dictionary index
        i+=1

    # Print in the requried format
    print (max(stateScore, key = stateScore.get))

# All states names with abbreviations
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

if __name__ == '__main__':
    main()
