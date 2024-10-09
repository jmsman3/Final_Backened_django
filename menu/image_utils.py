import requests
from Food_Project import settings

def upload_image_to_imgbb(image_file):
    api_key = '59c029e1206724ae1f2e3c30d278d10f'  
    url = 'https://api.imgbb.com/1/upload'
    payload = {
        'key'  : settings.IMGBB_API_KEY,
        'image': image_file.read(),
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json().get('data', {}).get('url')
    return None
