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

## Execução
Basta rodar o script Python, que irá automaticamente buscar sua localização e exibir o clima atual, além da previsão para os próximos dias.

```bash
python script.py

```
O script detecta a sua localização automaticamente e busca o clima para sua cidade. Caso o BeautifulSoup não consiga obter as informações desejadas, o ```Selenium``` é utilizado como fallback para buscar os dados diretamente no site ```tempo.com.```

## Exemplo de Saída
```bash
Essa é sua localização!
Cidade: São Paulo
Região: São Paulo
País: BR

Localização: São Paulo
Horário: Sexta-feira 10:00 AM
Temperatura Atual: 25°C
Condição: Ensolarado

Previsão para os próximos dias:
Sábado: Máxima de 27°C, Mínima de 18°C - Condição: Parcialmente Nublado
Domingo: Máxima de 30°C, Mínima de 20°C - Condição: Ensolarado
```
## Notas
- O código primeiro tenta obter os dados climáticos usando ```BeautifulSoup``` para realizar scraping no Google.

- Caso o ```BeautifulSoup``` não consiga encontrar os dados, o Selenium é ativado para acessar diretamente o site ```tempo.com``` e buscar as informações.

- O código também formata o nome da cidade para URLs de maneira adequada, removendo acentos e espaços.

## Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar o projeto 🚀🚀🚀.