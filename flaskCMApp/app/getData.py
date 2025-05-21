import json
import requests


def get_data(apiURL):
    getData = requests.get(apiURL)

    if getData.status_code == 200:
        jsonData = getData.json()
    else:
        print(f"Error retrieving data, {getData.status_code}")
    
    jd_data = json.dumps(jsonData)
    jl_data = json.loads(jd_data)

    return(jl_data)