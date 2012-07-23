referlypy
=========

Python/Django library for Refer.ly's API

Installation:

Set REFERLY_KEY and REFERLY_SECRET in your settings.py

Sample Usage:

```python
import referlypy
data = referlypy.create_account('test@test.com')
print data['account_id']
```