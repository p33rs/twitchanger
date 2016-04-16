import yaml, twitter, random, sys

f = open(sys.path[0] + '/config.yml', 'r')
c = yaml.load(f.read())

api = twitter.Api(consumer_key=c['consumer_key'],
    consumer_secret=c['consumer_secret'],
    access_token_key=c['access_token_key'],
    access_token_secret=c['access_token_secret'])

name = random.choice(c['names'])
api.UpdateProfile(name=name)

