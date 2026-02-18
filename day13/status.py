import requests

'''def get_status_code():
    url= "https://api.github.com"
    
    response= requests.get(url)
    print("Status Code:", response.status_code)
    print("Header Information:", response.headers)
    print("Response JSON:", response.json())

get_status_code() '''

'''def get_user_details(username):
    url = f"https://api.github.com/users/{username}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        print(f"User Name: {user_data['login']}")
        print(f"Public Repos: {user_data['public_repos']}")
    else:
        print(f"Error: Unable to fetch details for user '{username}'.") 

get_user_details("octocat")'''

'''import requests 
url = "https://api.github.com" 
response = requests.get(url) 
print("---- HTTP RESPONSE DETAILS ----") 
print("Status Code:", response.status_code) 
print("Response Headers:") 
for key, value in response.headers.items():     print(f"{key} : {value}") 
print("\nResponse Body:") 
print(response.text) '''


import requests 
base_url = "https://api.example.com/users" 
# GET 
get_response = requests.get(base_url) 
print("GET Status:", get_response.status_code) # POST 
post_data = {"name": "Jhilik", "role": "Trainer"} 
post_response = requests.post(base_url, json=post_data) 
print("POST Status:", post_response.status_code) 
# PUT 
put_data = {"name": "Jhilik Barman", "role": "Senior Trainer"} 
put_response = requests.put(f"{base_url}/1", json=put_data) 
print("PUT Status:", put_response.status_code) 
# PATCH 
patch_data = {"role": "Lead Trainer"} 
patch_response = requests.patch(f"{base_url}/1", json=patch_data) 
print("PATCH Status:", patch_response.status_code) 
# DELETE 
delete_response = requests.delete(f"{base_url}/1") 
print("DELETE Status:", delete_response.status_code) 