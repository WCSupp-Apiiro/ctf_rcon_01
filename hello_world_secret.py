import requests

def hello_world_with_secret():
  """
  This function sends a GET request to an API endpoint with a hardcoded secret key.
  """
  url = "https://api.example.com/data" 
  headers = {"Authorization": "Bearer MY_SUPER_SECRET_KEY"} 
  response = requests.get(url, headers=headers)
  print(response.text)

if __name__ == "__main__":
  hello_world_with_secret()
