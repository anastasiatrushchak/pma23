import requests

url = 'http://localhost:5000/websites'

new_website = {'title': 'New Website', 'description': 'New Description'}
response = requests.post(url, json=new_website)
print(f'Response: {response.status_code}, {response.json()}')
for website in requests.get(url).json():
    print(website)
website_id = 1
updated_website = {'title': 'Updated Website'}
response = requests.patch(f'{url}/{website_id}', json=updated_website)
print("\nUpdated website:")
for website in requests.get(url).json():
    print(website)
