Why?
====

To make it easier to interact with the Etsy API in Python.

Usage
=====

Initialization
--------------
    >>> from etsy import Etsy
    >>> e = Etsy(consumer_key, consumer_secret) # gotten from signing up at etsy.com/developers

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

Showing listings
----------------

Listings are items that are for sale on the site.

    >>> e.show_listings(color='#FF00FF')
    {u'count': 15,
     u'pagination': {u'effective_limit': 25,
      u'effective_offset': 0,
      u'effective_page': 1,
      u'next_offset': None,
      u'next_page': None},
     u'params': {u'category': None,
      u'color': u'#FF0000',
      u'color_accuracy': u'5',
      u'geo_level': u'city',
      u'keywords': None,
      u'lat': None,
      u'limit': 25,
      u'location': None,
      u'lon': None,
      u'materials': None,
      u'max_price': None,
      u'min_price': None,
      u'offset': 0,
      u'page': None,
      u'sort_on': u'created',
      u'sort_order': u'down',
      u'tags': None},
     u'results': [{u'brightness': 99,
       u'category_id': 69152465,
       u'category_path': [u'Patterns', u'Handmade'],
       u'creation_tsz': 1343606971,
       u'currency_code': u'USD',
       u'description': u'This listing is for...',
       u'ending_tsz': 1354165200,
       u'featured_rank': 0,
       u'hue': 0,
       u'is_black_and_white': False,
       u'is_supply': None,
       u'last_modified_tsz': 1343606971,
       u'listing_id': 55489116,
       u'materials': [u'pdf email pattern', u'beads', u'needles and thread'],
       u'num_favorers': 4,
       u'occasion': None,
       u'original_creation_tsz': 1283592254,
       u'price': u'35.00',
       u'quantity': 1,
       u'recipient': None,
       u'saturation': 100,
       u'shop_section_id': 6766997,
       u'state': u'active',
       u'state_tsz': 1323227794,
       u'style': None,
       u'tags': [u'beading',
        u'beadweaving',
        u'peyote',
        u'bracelet',
        u'cuff',
        u'snow leopard',
        u'blue',
        u'red',
        u'white',
        u'grey',
        u'dust team',
        u'ebw team'],
        ...
    

Authenticating with OAuth
-------------------------
    >>> e.get_auth_url(permissions=['email_r', 'listings_r'])
    {'oauth_token': u'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
     'oauth_token_secret': u'XXXXXXXXXX',
     'url': u'https://www.etsy.com/oauth/signin?oauth_consumer_key=...'}
    
The user then is redirected to the URL (you must save the `oauth_token` and `oauth_token_secret` for later in step two).

The list of all permissions can be found [here.](http://www.etsy.com/developers/documentation/getting_started/oauth#section_permission_scopes)

Once the user click the link and authenticates your app, the user then copy/pastes the *verification code* back to your app

    >>> e.get_auth_token(verification_code, oauth_token, oauth_token_secret)
    {'oauth_token': u'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
     'oauth_token_secret': u'XXXXXXXXXXXX'}

The new `oauth_token` and `oauth_token_secret` are permanent and should be stored
in a database for use in all subsequent api requests that require authentication.

Making authenticated requests
-----------------------------

When instantiating the Etsy object, include the `oauth_token` and `oauth_token_secret` along with the `consumer_key` and `consumer_secret`:

    >>> from etsy import Etsy
    >>> e = Etsy(consumer_key, consumer_secret, oauth_token, oauth_token_secret)

Now you have access to all authentication only methods, as well as the magic `__SELF__` identifier:

    >>> e.get_user_info('__SELF__') 
    {u'count': 1,
     u'pagination': {},
     u'params': {u'user_id': u'__SELF__'},
     u'results': [{u'creation_tsz': 1344140248,
       u'feedback_info': {u'count': 0, u'score': None},
       u'login_name': u'priestc',
       u'primary_email': u'nbvfour@gmail.com',
       u'referred_by_user_id': None,
       u'user_id': 14888663}],
     u'type': u'User'}

Notice the addition of the `primary_email` field, this is because this user authenticated with the app using the `'email_r'` permission.