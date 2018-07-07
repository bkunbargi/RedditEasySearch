import praw
import config
import sys
import time

file = open('/Users/Kunbargi/Desktop/reddit bot/allsubreddits.txt','r')

def login():
    #Returns a reddit thing
    print("Logging in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "learning to use bots")
    print("You are in!")
    return r

r = login()

def run_bot(r,subred,spec_com):
    print("Retrieving Results")
    for submission in r.subreddit(subred).search(spec_com,time_filter = 'day'):
            print(submission.title)
            print(submission.permalink)
            submission.comments.replace_more(limit = None)
            for top_level_comment in submission.comments.list():
                if spec_com in top_level_comment.body.split():
                     print("Thread: " + submission.title)
                     print(top_level_comment.body)


subred = input("Enter a valid Subreddit: ")
spec_com = input("What Keywords are you looking for: ")

'''to preform a deeper search '''
#sub_list = []
#for element in file:
#    for subr in element.split('/'):
#        if subred in subr:
#            sub_list.append(subr)
#print(sub_list)


#other_subs = r.subreddits.search(subred)
#for name in other_subs:
#    print(name)

#print()
#print()
#sub_names = r.subreddits.search_by_name(subred)
#for name in sub_names:
#    print(name)



'''run the bot'''
print('Running the bot')
run_bot(r,subred,spec_com)
