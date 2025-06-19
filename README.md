
# Verificador de Páginas - Gênero Terror (HaloFilmes)

Este script em Python utiliza a biblioteca `requests` para verificar se páginas do gênero **terror** do site [halofilmes.com](https://halofilmes.com) estão acessíveis (código de status HTTP 200).

## 🚀 Funcionalidade

- Itera da página 1 até a 49.
- Para cada página, faz uma requisição HTTP.
- Exibe se a página está acessível ou não.
- Exibe o status e a URL acessada.

## 🧪 Requisitos

- Python 3.x
- Biblioteca `requests`

### Instalação da biblioteca `requests`:

```bash
pip install requests
```

## 📜 Código

```python
import requests

for x in range(1, 50):
    url = requests.get(f"https://halofilmes.com/genero/terror/page/{x}/")
    if url.status_code == 200:
        print("-" * 20)
        print(f"Page {x} is accessible.")
        print(url.url)
    else:
        print(f"Page {x} is not accessible. Status code: {url.status_code}")
```

## 🧠 Observações

- O script é útil para verificar se uma sequência de páginas existe ou está online.
- Pode ser adaptado para raspagem de dados (web scraping) futuramente, com bibliotecas como `BeautifulSoup`.

## ⚠️ Aviso

Este script apenas faz requisições `GET` para fins educativos. Sempre respeite os **termos de uso** e o **robots.txt** de qualquer site antes de fazer raspagens em larga escala.
