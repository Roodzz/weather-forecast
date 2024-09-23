import requests
from bs4 import BeautifulSoup

response = requests.get('https://ipinfo.io')
data = response.json()

city = data['city']
region = data['region']
country = data['country']

print(f"Essa é sua localização!")
print(f"Cidade: {city}")
print(f"Região: {region}")
print(f"País: {country}")

def get_weather(city):
    url = f"https://www.google.com/search?q=clima+{city.replace(' ', '+')}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    try:
        temp = soup.find('span', attrs={'id': 'wob_tm'}).text
        condition = soup.find('span', attrs={'id': 'wob_dc'}).text
        # location = soup.find('div', attrs={'id': 'wob_loc'}).text
        time = soup.find('div', attrs={'id': 'wob_dts'}).text
        
        print(f"Localização: {city}")
        print(f"Horário: {time}")
        print(f"Temperatura Atual: {temp}°C")
        print(f"Condição: {condition}")

        forecast_days = soup.find_all('div', attrs={'class': 'wob_df'})
        
        print("\nPrevisão para os próximos dias:")
        
        for day in forecast_days:
            day_name = day.find('div', attrs={'class': 'vk_lgy'}).text
            max_temp = day.find('span', attrs={'class': 'wob_t', 'style': 'display:inline'}).text
            min_temp = day.find_all('span', attrs={'class': 'wob_t', 'style': 'display:none'})[0].text
            condition_day = day.find('img')['alt']
            
            print(f"{day_name}: Máxima de {max_temp}°C, Mínima de {min_temp}°C - Condição: {condition_day}")
            

    except AttributeError:
        print("Não foi possível encontrar informações climáticas para a cidade especificada.")

# Exemplo de uso
# city = input("Digite sua cidade: ")
get_weather(city)
