import requests
url=('https://rgb-classifier-api.herokuapp.com/api/')
r=int(input('enter r:'))
g=int(input('enter g:'))
b=int(input('enter b:'))
result = requests.post(url,json=[{'r':r,'g':g,'b':b}])
arr=result.json()
print(arr)
