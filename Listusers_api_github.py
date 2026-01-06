import requests
#The requests library provides simple functions for various HTTP methods like get, put, post etc

response =requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#request.get method provides json data of the api provided

#print(response.json())
output = response.json()
#storing the response in json dictionary format

#traversing the dictionary and getting the list of users
for i in range(len(output)):
    print(output[i]["user"]["login"])


"""
output:
nem0z
ankit98040
sreeram-venkitesh
ShaanveerS
HueCodes
Tanner-Gladson
SergeyKanzhelev
SergeyKanzhelev
natasha41575
pravk03
richabanker
petern48
lalitc375
koobfoo
lalitc375
thc1006
huww98
thc1006
KyungHwanKim-devs
kkkkun
ERJavier
apratinav-intuit
itzPranshul
nohy6630
neolit123
Chunxia202410
SataQiu
KyungHwanKim-devs
wold9168
olamilekan000

"""