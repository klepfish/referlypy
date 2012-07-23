referlypy
=========

Python/Django library for Refer.ly's API

Sample Usage:

import referlypy
data = referlypy.create_account('test@test.com')
print data['account_id']