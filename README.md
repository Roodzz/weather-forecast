# Projeto de Web Scraping e Consulta de Clima (Weather Forecast)

Este projeto demonstra o uso de algumas bibliotecas poderosas de Python para obter informações de clima e localização. Ele utiliza as bibliotecas `requests`, `BeautifulSoup`, e `Selenium` para realizar web scraping e interagir com websites, além de consultar a localização do usuário usando a API do `ipinfo.io`.

## Funcionalidades

- Consulta a localização do usuário (cidade, região, país) utilizando a API do `ipinfo.io`.
- Busca a previsão do tempo atual para a cidade do usuário usando o `Google` ou, caso necessário, utilizando o `Selenium` para acessar o site `tempo.com`.
- Remoção de acentos em strings para formatação adequada de URLs.

## Tecnologias Utilizadas

- **requests**: Para realizar requisições HTTP e obter a localização atual do usuário.
- **BeautifulSoup**: Para realizar web scraping no Google e buscar dados de clima.
- **Selenium**: Como alternativa para obter dados de clima diretamente do site `tempo.com` caso o web scraping falhe.
- **WebDriver Manager**: Para gerenciar o driver do Chrome automaticamente no Selenium.
- **Unicodedata**: Para remover acentos de strings e formatar textos.

## Como Usar

### Pré-requisitos

- Python 3.x
- Instalar as dependências do projeto:

```bash
pip install requests beautifulsoup4 selenium webdriver_manager
```
