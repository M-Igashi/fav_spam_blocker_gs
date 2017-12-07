#coding: utf-8

import tweepy
import json
import argparse


options = argparse.ArgumentParser()
options.add_argument('--consumer-key', required=True)
options.add_argument('--consumer-secret', required=True)
options.add_argument('--token', required=True)
options.add_argument('--token-secret', required=True)
options.add_argument('--user-name', required=True)
options.add_argument('--num-digits', default=3)
options.add_argument('--unlock', action='store_true')


def spam_block(consumer_key, consumer_secret, token, token_secret, user_name, num_digits=3):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)
                         
    api = tweepy.API(auth)
    
    for i in range(10**(num_digits - 1)):
    
        target_screen_name = user_name + str(i).zfill(num_digits)
    
        try:
            user = api.get_user(screen_name=target_screen_name)
            api.create_block(target_screen_name)
        
        except:
            print(u"%sは存在しないか何らかの理由でブロックできませんでした。" % (target_screen_name))
            continue
    
        print(u"%s(%s)をブロックしました。" % (user.name,user.screen_name))
        

def unlock(consumer_key, consumer_secret, token, token_secret, user_name, num_digits=3):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)
                         
    api = tweepy.API(auth)
    
    for i in range(10**(num_digits - 1)):
    
        target_screen_name = user_name + str(i).zfill(num_digits)
    
        try:
            user = api.get_user(screen_name=target_screen_name)
            api.create_block(target_screen_name)
        
        except:
            print(u"%sは存在しないか何らかの理由でブロック解除できませんでした。" % (target_screen_name))
            continue
            
        print(u"%s(%s)のブロックを解除しました。" % (user.name,user.screen_name))

    
def main(opt):
    
    if opt.unlock:
        unlock(consumer_key=opt.consumer_key, 
               consumer_secret=opt.consumer_secret, 
               token=opt.token, 
               token_secret=opt.token_secret, 
               user_name=opt.user_name,
               num_digits=opt.num_digits) 
        
    elif not opt.unlock:
        spam_block(consumer_key=opt.consumer_key, 
                   consumer_secret=opt.consumer_secret, 
                   token=opt.token, 
                   token_secret=opt.token_secret, 
                   user_name=opt.user_name,
                   num_digits=opt.num_digits) 
                   
    exit(0)
    

if __name__ == '__main__':
    main(options.parse_args())