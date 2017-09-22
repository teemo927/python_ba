import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
a = r.status_code
print(r.url)
print(a)
# 200
b = r.headers['content-type']
print(b)
# 'application/json; charset=utf8'
c = r.encoding
print(c)
# 'utf-8'
d = r.text
print(d)
# u'{"type":"User"...'
e = r.json()
print(e)
# {u'private_gists': 419, u'total_private_repos': 77, ...}
