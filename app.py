import yaml, twitter, random

f = open('config.yml', 'r')
c = yaml.load(f.read())
print c

api = twitter.Api(consumer_key=c['consumer_key'],
    consumer_secret=c['consumer_secret'],
    access_token_key=c['access_token_key'],
    access_token_secret=c['access_token_secret'])

name = random.choice(c['names'])
api.UpdateProfile(name=name)
