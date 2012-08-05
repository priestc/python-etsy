import urllib
from urlparse import unquote, parse_qs
import json
import logging
import requests
from oauth_hook import OAuthHook

log = logging.getLogger(__name__)

#from django.conf import settings
class settings(object):
    ETSY_CONSUMER_KEY = 'oe2opawvwhzw1t0rpnx59ljn'
    ETSY_SHARED_SECRET = 'z30f562ecw'

class Etsy(object):
    """
    Represents the etsy API
    """
    url_base = "http://openapi.etsy.com/v2/"
    
    class EtsyError(Exception):
        pass
    
    def __init__(self, consumer_key, consumer_secret):
        self.params = {}
        self.consumer_key = consumer_key
        oah = OAuthHook(consumer_key=consumer_key, consumer_secret=consumer_secret)
        self.client = requests.session(hooks={'pre_request': oah})
    
    def get_user_info(self, user):
        """
        Get basic info about a user, pass in a username or a user_id
        """
        endpoint = 'users/%s' % user
        self.params = {'api_key': self.consumer_key}
        response = self.execute(endpoint)
        return json.loads(response.text)
    
    def find_user(self, keywords):
        endpoint = 'users'
        self.params = {'api_key': self.consumer_key, 'keywords': keywords}
        response = self.execute(endpoint)
        return json.loads(response.text)
    
    def get_auth_url(self, permissions=[]):
        """
        """
        endpoint = 'oauth/request_token'
        if permissions:
            self.params = {'scope': " ".join(permissions)}
        response = self.execute(endpoint)
        return parse_qs(response.text)['login_url'][0]
    
    def execute(self, endpoint, method='get'):
        querystring = urllib.urlencode(self.params)
        url = "%s%s" % (self.url_base, endpoint)
        if querystring:
            url = "%s?%s" % (url, querystring)

        response = getattr(self.client, method)(url)
        
        if response.status_code > 201:
            e = response.text
            code = response.status_code
            raise self.EtsyError('API returned %s response: %s' % (code, e))
        return response

def make_my_etsy():
    key = settings.ETSY_CONSUMER_KEY
    secret = settings.ETSY_SHARED_SECRET
    return Etsy(key, secret)
