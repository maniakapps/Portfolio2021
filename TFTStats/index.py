from .connector import *

api_key = open("api.txt").read()
n_c = Connect(api_key,"la1")
print(n_c.region)