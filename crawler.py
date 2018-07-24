from praw.models import comment_forest
import praw
import config
import sys
import time

#file = open('/Users/Kunbargi/Desktop/reddit bot/allsubreddits.txt','r')

def login():
    '''Returns logged in reddit instance'''
    print("Logging in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "learning to use bots")
    print("You are in!")
    return r



def get_subs(query):
    set_list = set()
    for sub in r.subreddits.search_by_name(query):
        if str(query) not in sub.title.lower():
            continue
        set_list.add(sub)
    for sub in r.subreddits.search(query):
        if str(query) not in sub.title.lower():
            continue
        set_list.add(sub)
    return set_list


def scrape_threads(sub_list,keyword):
    organized_sub = []
    for subs in sub_list:
        print(subs)
        sublist_posts = r.subreddit('{}'.format(subs)).hot(limit = 25)
        sub_dict = dict()
        for submission in sublist_posts:
            if keyword in submission.title:
                print(submission.title)
                time.sleep(1)
                sub_dict[submission.title] = submission.id
            else:
                continue
        organized_sub.append(sub_dict)
        #organized_sub.append({submission.title:submission for submission in sublist_posts})
        time.sleep(1)
    print(organized_sub)
    print()
    return organized_sub


def DFT(parent_comment):
    comment_list = []
    children = [i for i in parent_comment]
    visited_dic = {i:False for i in children}
    if False not in visited_dic.values():
        return comment_list
    else:
        for k,v in visited_dic.items():
            if v == False:
                curr_child = k
                visited_dic[k] = True
                comment_list.append(curr_child.body)
            if curr_child.replies:
                comment_list.append(DFT(curr_child.replies))

    return comment_list


def submission_scrape(sub_id):
    submission = r.submission(id = sub_id)
    forest = comment_forest.CommentForest(submission,submission.comments)
    comment_list = DFT(forest)
    print(comment_list)
    return comment_list



if __name__ == '''__main__''':
    r = login()
    sub_topic = input('What kind of subreddits are you looking for (one word): ')
    subs = get_subs(sub_topic)
    keyword = input('Keyword for threads: ')
    submission_dict_list = scrape_threads(subs,keyword)

    for dict in submission_dict_list:
        for k,v in dict.items():
            if keyword in k:
                print(k)
                submission_scrape(dict[k])
                print()
