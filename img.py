
from flask import request
img_path = './path/to/img'
url = 'http://www.example.com/api/img_data'
files = {'file': ('image.jpg', open(img_path, 'rb'), 'image/jpeg')}
r = request.post(url, files=files)
print(r.text)