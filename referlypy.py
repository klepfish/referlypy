import urllib2
import base64
from django.conf import settings

def make_request(endpoint, data):
	req = urllib2.Request('https://refer.ly/api/120701/'+endpoint, urllib2.urlencode(data))
	req.add_header('Accept', 'application/json')
	base64string = base64.encodestring('%s:%s' % (settings.REFERLY_KEY, settings.REFERLY_SECRET)).replace('\n', '')
	req.add_header("Authorization", "Basic %s" % base64string)
	
	res = urllib2.urlopen(req)
	data = res.read()
	
	return data
	
def create_account(email):
	data = {}
	data['email'] = email
	return make_request('accounts', data)

def list_links(count = None, page = None):
	data = {}
	if count is not None:
		data['count'] = count
	if page is not None:
		data['page'] = page

	return make_request('links', data)

def create_link(url, account_id = None):
	data = {}
	data['url'] = url
	if account_id is not None:
		data['account_id'] = account_id

	return make_request('links', data)
	
def add_reward(visit_id, amount, earned_on, payable_on, vendor_external_id = None):
	data = {}
	data['visit_id'] = visit_id
	data['amount'] = amount
	data['earned_on'] = earned_on
	data['payable_on'] = payable_on
	if vendor_external_id is not None:
		data['vendor_external_id'] = vendor_external_id

	return make_request('rewards', data)

def list_rewards(account_id = None, link_id = None):	
	data = {}
	if account_id is not None:
		data['account_id'] = account_id
	if link_id is not None:
		data['link_id'] = link_id

	return make_request('rewards', data)	