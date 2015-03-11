from notifyme_social import TwitterService
import sys

number_argv = len(sys.argv)

if number_argv <2:
    print "Please select a service"
    sys.exit()

if sys.argv[1] == 'twitter':
    print "Selecting twitter service"

    if number_argv < 3:
        print "Please give NotifyMe a command (Expected command arguments)"
    elif sys.argv[2] == 'login':
        print "Logging in"

        twitterService = TwitterService()
        twitterService.create_service()
        twitterService.request_access()
        print "Please authorise NotifyMe on the Twitter website"
        twitterService.get_access_token()
        print "Logged in successfully"
    elif sys.argv[2] == 'post':
        if number_argv > 3:
            text = str(sys.argv[3])

            twitterService = TwitterService()
            twitterService.create_service()
            twitterService.resume_session()
            twitterService.post_status(text)

            print "Posted "+text+" to twitter"
        else:
            print "No text to post. Sorry."
