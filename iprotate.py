'''
Rotating IP addresses is a common technique used in web scraping or 
accessing APIs that may have rate limits or restrictions.
One way to achieve this is by using a pool of proxies and rotating 
through them for each request.

'''


import requests
from itertools import cycle

def make_request(url, proxy_pool):
    try:
        
        proxy = next(proxy_pool)
        print(f"Using proxy: {proxy}")

        # Send a GET request through the proxy
        response = requests.get(url, proxies={'http': proxy, 'https': proxy})

        
        print(f"Response from {url}:\n{response.text}")

    except requests.RequestException as e:
        print(f"Error making request: {e}")

if __name__ == '__main__':
    # Set the URL to request
    target_url = 'http://www.example.com'

    # pool of proxy addresses
    proxies = [
        'http://proxy1.example.com:8080',
        'http://proxy2.example.com:8080',
        'http://proxy3.example.com:8080',
        
    ]

    proxy_pool = cycle(proxies)

   
    for _ in range(5):
        make_request(target_url, proxy_pool)
