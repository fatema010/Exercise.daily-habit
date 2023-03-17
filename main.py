import requests
from datetime import datetime
TOKEN = "123456789"
USERNAME = "ummefatema"
GRAPH = "graph1"
pixela_endpoint ="https://pixe.la/v1/users"

user_params = {"token":TOKEN,
               "username":USERNAME,
                "agreeTermsOfService":"yes",
                "notMinor":"yes"}

#response = requests.post(url=pixela_endpoint,json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {"id":GRAPH,
                "name":"Daily hour calculation",
                "unit":"hour",
                "type":"int",
                "color":"ajisai"}
headers = {"X-USER-TOKEN":TOKEN}
#print(response.text)
another_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()

configuration = {"date":today.strftime("%Y%m%d"),
                 "quantity":"2",
                 }



#response = requests.post(url=another_endpoint,json=configuration,headers=headers)
#print(response.text)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"
new_config = {"quantity":input("How many hours did you study today?")}
response = requests.put(url=update_endpoint,json=new_config,headers = headers)
print(response.text)