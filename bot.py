#!/usr/bin/env python

import praw, config, time, os

def login():
    print("Logging in...")
    r = praw.Reddit(username = config.username,
                   password = config.password,
                   client_id = config.client_id,
                   client_secret = config.client_secret,
                   user_agent = config.user_agent)
    
    print("logged in!")
    
    return r

def run(r,comments_store):
    
    for comment in r.subreddit('test').comments(limit=50):
        
        if 'itshappening.gif' in comment.body.lower() and comment.id not in comments_store and comment.author != r.user.me():
            print("String match found!")
            comment.reply("[Here is the link to gif](https://i.makeagif.com/media/5-07-2015/6JX4yh.gif)")
            print("reply successful")
            comments_store.append(comment.id)
            
            with open("list_of_ids.txt","a") as f:
                f.write(comment.id + "\n")
    
    print("sleeping for 10 seconds")
    
    time.sleep(10)
            

def get_comments():
    if not os.path.isfile("list_of_ids.txt"):
        comments_store = []
    else:
        with open("list_of_ids.txt","r") as f:
            comments_store = f.read()
            comments_store = comments_store.split("\n")
            comments_store = filter(None,comments_store)
    
    return comments_store

    
reddit = login()
comments_store = get_comments()

while True:
    run(reddit,comments_store)

    