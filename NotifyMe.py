from rauth import OAuth1Service
from saveTokens import saveTokens
import webbrowser


print("Hi")
print("Initiating OAuth")

class TwitterService:
    def create_service(self):
        self.twitter = OAuth1Service(
            consumer_key = "lpoFF3SyAcZzLNkOtnKx1Jue9",
            consumer_secret = "AyacUUlN72C3JR5nvKffdlHYLbnfwCuIFW26bYP6VkyFA5YzPB",
            name='twitter',
            access_token_url='https://api.twitter.com/oauth/access_token',
            request_token_url='https://api.twitter.com/oauth/request_token',
            authorize_url='https://api.twitter.com/oauth/authorize',
            base_url='https://api.twitter.com/1/' )

    def request_access(self):
        self.request_token, self.request_token_secret = self.twitter.get_request_token()

        print "request_token:"
        print self.request_token
        print "\nrequest_token_secret:"
        print self.request_token_secret

        authorize_url = self.twitter.get_authorize_url(self.request_token)

        print "\nAuthorisation url:"
        print authorize_url

        webbrowser.open(authorize_url)

    def get_access_token(self):
        pin = raw_input('Enter PIN from browser: ')
        self.session = self.twitter.get_auth_session(self.request_token,
                                                self.request_token_secret,
                                                method='POST',
                                                data={'oauth_verifier': pin})

        access_token = self.session.access_token
        access_token_secret = self.session.access_token_secret
        saveTokens(access_token,access_token_secret)

        print "Authorised successful\n"
        print "access_token:"
        print access_token
        print "\naccess_token_secret:"
        print access_token_secret


twitterService = TwitterService()
twitterService.create_service()
twitterService.request_access()
twitterService.get_access_token()
