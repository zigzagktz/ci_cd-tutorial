import requests

def my_function(event, context):
    result = requests.get('https://api.github.com')
    print(result)
    return result
