import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import unicodedata

response = requests.get('https://ipinfo.io')
data = response.json()

city = data['city']
region = data['region']
country = data['country']

print(f"Essa é sua localização!")
print(f"Cidade: {city}")
print(f"Região: {region}")
print(f"País: {country}")

def remover_acentos(texto):
    texto = texto.replace(" ", "-").lower()
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    return ''.join(c for c in texto_normalizado if not unicodedata.combining(c))

city_formated = remover_acentos(city)

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
        horario = soup.find('div', attrs={'id': 'wob_dts'}).text
        
        print(f"Localização: {city}")
        print(f"Horário: {horario}")
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
        print("Não foi possível encontrar informações climáticas para a cidade especificada utilizando o bs4. Vamos utilizar o Selenium!")
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-extensions")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print(f"Acessando o site: Tempo.com")
        driver.get(f"https://www.tempo.com/{city_formated}.htm")

        time.sleep(5)

        # print(f"""{driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[1]/span/span[1]').text} - {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[1]/span/span[2]').text}
        # Máxima: {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[1]/span/span[4]/span[1]').text}
        # Minima: {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[1]/span/span[4]/span[3]').text}
        # """)
        print(f"""{driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[2]/span/span[1]').text} - {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[2]/span/span[2]').text}
        Máxima: {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[2]/span/span[4]/span[1]').text}
        Minima: {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[2]/span/span[4]/span[3]').text}
        """)
        print(f"""{driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[3]/span/span[1]').text} - {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[3]/span/span[2]').text}
        Máxima: {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[3]/span/span[4]/span[1]').text}
        Minima: {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[3]/span/span[4]/span[3]').text}
        """)
        print(f"""{driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[4]/span/span[1]').text} - {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[4]/span/span[2]').text}
        Máxima: {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[4]/span/span[4]/span[1]').text}
        Minima: {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[4]/span/span[4]/span[3]').text}
        """)
        print(f"""{driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[5]/span/span[1]').text} - {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[5]/span/span[2]').text}
        Máxima: {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[5]/span/span[4]/span[1]').text}
        Minima: {driver.find_element(By.XPATH, '/html/body/main/div[2]/section/section[2]/div/ul/li[5]/span/span[4]/span[3]').text}
        """)

        driver.quit()

# Exemplo de uso
# city = input("Digite sua cidade: ")
get_weather(city)
