import requests

for x in range(1, 50):
    url = requests.get(f"https://halofilmes.com/genero/terror/page/{x}/")
    if url.status_code == 200:
        print("-" * 20)
        print(f"Page {x} is accessible.")
        print(url.url)
    else:
        print(f"Page {x} is not accessible. Status code: {url.status_code}")  

