def make_tweet_list(tweet):
    if len(tweet) <= 140:
            return [tweet]
    else:
        tweet_list = []
        while tweet:
            tweet_list.append(tweet[:137] + ('...' if tweet[137:] else ''))
            tweet = tweet[137:]
        return tweet_list


def pop_a_tweet(tweet_stack='tweet_stack.txt'):
    import os
    DATA_DIR = os.path.dirname(os.path.abspath(__file__))
    STACK_FILE = os.path.join(DATA_DIR, tweet_stack)
    tweets = open(STACK_FILE, 'r').readlines()
    if tweets:
        popped_tweet = tweets.pop().strip()
        f = open(STACK_FILE, 'w')
        f.writelines(tweets)
        f.close()
        return make_tweet_list(popped_tweet)


import sys
tweet_list = []
for tweet in sys.argv[1:]:
    tweet_list += make_tweet_list(tweet)
if not tweet_list:
    tweet_list = pop_a_tweet()
if tweet_list:
    from twitter import Api as TwitterApi
    print 'Attempting Twitter Api Login...'
    Twitter = TwitterApi(
        consumer_key="Your Twitter CONSUMER_KEY",
        consumer_secret="Your Twitter CONSUMER_SECRET",
        access_token_key="Your Twitter ACCESS_TOKEN_KEY",
        access_token_secret="Your Twitter ACCESS_TOKEN_SECRET"
    )
    for tweet in tweet_list:
        Twitter.PostUpdate(tweet)
        print 'Tweeting:', tweet
    print "Tweeted successfully!"
else:
    print "Oops!. No tweets found in the tweet_stack!"
