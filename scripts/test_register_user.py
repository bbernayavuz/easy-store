import requests
from pprint import pprint

def client(): 
    credentials = {
         "username":"by4",
        "password1":"brnyvz123",
        "password2":"brnyvz123",
        "email": "dort@b.com",
    }

    response = requests.post(
        url= 'http://127.0.0.1:8000/dj-rest-auth/registration/',
        data=credentials,
    )
    print('status code:', response.status_code)

    return response.json()

if __name__ == '__main__':
    client()