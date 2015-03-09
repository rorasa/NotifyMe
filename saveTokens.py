# saveTokens module

import os.path

def saveAccessToken(access_token):
    f = open('access_token','w')
    f.write(str(access_token))
    f.close()
    # print "save access_token"

def saveAccessTokenSecret(access_token_secret):
    f = open('access_token_secret','w')
    f.write(str(access_token_secret))
    f.close()
    # print "save access_token_secret"

def saveTokens(access_token, access_token_secret):
    saveAccessToken(access_token)
    saveAccessTokenSecret(access_token_secret)

def loadAccessToken():
    try:
        f = open('access_token','r')
        access_token = f.readline()
    except IOError:
        print "Unable to open file"
        return None
    else:
        f.close()
        return access_token
    # need some integrity check for token here

def loadAccessTokenSecret():
    try:
        f = open('access_token_secret','r')
        access_token_secret = f.readline()
    except IOError:
        print "Unable to open file"
        return None
    else:
        f.close()
        return access_token_secret
    # need some integrity check for token here

def loadTokens():
    access_token = loadAccessToken()
    access_token_secret = loadAccessTokenSecret()
    return access_token, access_token_secret
