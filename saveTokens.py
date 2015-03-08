# saveTokens module

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
