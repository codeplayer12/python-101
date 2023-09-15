import requests

x = requests.get('http://httpbin.org/get')

print(x.headers)
print(x.headers['Server'])
print(x.status_code)

if x.status_code == 200:
	print("Success")
elif x.status_code == 404:
	print("Not Found")

print(x.elapsed)
print(x.cookies)

# print(x.content)
# print(x.text)

# x = requests.get('http://httpbin.org/get', params={'id':1})

# print(x.url)
# x = requests.get('http://httpbin.org/get?id=2')

# print(x.url)

# x = requests.get('http://httpbin.org/get', params={'id':3}, headers={'Accept':'application/json', 'testheader':'test'})
# print(x.text)
# x = requests.delete('http://httpbin.org/delete', params={'id':3}, headers={'Accept':'application/json', 'testheader':'test'})
# print(x.text)
# x = requests.post('http://httpbin.org/post', data={'id':3}, headers={'Accept':'application/json', 'testheader':'test'})
# print(x.text)



# files = {'file': open('google.png','rb')}
# x = requests.post('http://httpbin.org/post', files=files)
# print(x.text)


# x = requests.get("http://httpbin.org/get", auth=('username', 'password'))
# print(x.text)


# By default request will make a redirection except for head

# x = requests.get("http://github.com", allow_redirects=False)
# print(x.headers)
# x = requests.get("http://httpbin.org/get", timeout=1)
# print(x.content)

x = requests.get("http://httpbin.org/cookies", cookies={"a":"b"})
print(x.content)

x = requests.Session()
x.cookies.update({"a":"b"})
print(x.get("http://httpbin.org/cookies").text)

print(x.get("http://httpbin.org/cookies").json())


x = requests.get("URL")
with open('google2.png', 'wb') as f:
	f.write(x.content)