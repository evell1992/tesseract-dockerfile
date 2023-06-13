import requests

files = {'png': ('0.png', open('0.png', 'rb'), 'image/png', {'Expires': '0'})}
response = requests.post('http://127.0.0.1:9999/png_to_text', files=files)
print(response.text)
