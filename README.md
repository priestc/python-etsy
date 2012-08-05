Usage
=====

Initialization
--------------
    >>> from etsy import Etsy
    >>> e = Etsy(consumer_key, consumer_secret)

Get info for user
-----------------
    >>> e.get_user_info('priestc')
    {u'count': 1,
     u'pagination': {},
     u'params': {u'user_id': u'priestc'},
     u'results': [{u'creation_tsz': 1338405910,
       u'feedback_info': {u'count': 0, u'score': None},
       u'login_name': u'priestc',
       u'referred_by_user_id': None,
       u'user_id': 22138099}],
     u'type': u'User'}

Searching for users
-------------------
    >>> e.find_user('william')
    {u'count': 27956,
     u'pagination': {u'effective_limit': 25,
      u'effective_offset': 0,
      u'effective_page': 1,
      u'next_offset': 25,
      u'next_page': 2},
     u'params': {u'keywords': u'william',
      u'limit': 25,
      u'offset': 0,
      u'page': None},
     u'results': [{u'creation_tsz': 1320715538,
       u'feedback_info': {u'count': 0, u'score': None},
       u'login_name': u'almostbohemian',
       u'referred_by_user_id': None,
       u'user_id': 17479899},
      {u'creation_tsz': 1335125907,
       u'feedback_info': {u'count': 0, u'score': None},
       u'login_name': u'Blawesomes',
       u'referred_by_user_id': None,
       u'user_id': 21276820},
      {u'creation_tsz': 1339310987,
       u'feedback_info': {u'count': 0, u'score': None},
       u'login_name': u'cityfleet',
       u'referred_by_user_id': None,
       u'user_id': 22385428},
      {u'creation_tsz': 1321655636,
       u'feedback_info': {u'count': 2, u'score': 100},
       u'login_name': u'way2easy4ron',
       u'referred_by_user_id': None,
       ...
       
Authenticating with OAuth
-------------------------

    >>> e.get_auth_url(permissions=['email_r', 'listings_r'])
    {'oauth_token': u'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
     'oauth_token_secret': u'XXXXXXXXXX',
     'url': u'https://www.etsy.com/oauth/signin?oauth_consumer_key=...'}
    
The user then is redirected to the URL (you must save the `oauth_token` and `oauth_token_secret` for later in step two.

The list of all permissions can be found [here.](http://www.etsy.com/developers/documentation/getting_started/oauth#section_permission_scopes)

Once the user click the link and authenticates your app, the user then copy/pastes the *verification code* back to your app

    >>> e.get_auth_token(verification_code, oauth_token, oauth_token_secret)
    {'oauth_token': u'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
     'oauth_token_secret': u'XXXXXXXXXXXX'}

The new `oauth_token` and `oauth_token_secret` are permanent and should be stored
in a database for use in all subsequent api requests that require authentication.