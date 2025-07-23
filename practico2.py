from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.skyscanner.es")

time.sleep(5)

# Aceptar cookies si aparece
try:
    cookie_button = driver.find_element(By.ID, "acceptCookieButton")
    cookie_button.click()
except:
    pass

# Escribir origen
from_input = driver.find_element(By.ID, "fsc-origin-search")
from_input.clear()
from_input.send_keys("Madrid")
time.sleep(1)
from_input.send_keys(Keys.RETURN)

# Escribir destino
to_input = driver.find_element(By.ID, "fsc-destination-search")
to_input.clear()
to_input.send_keys("Londres")
time.sleep(1)
to_input.send_keys(Keys.RETURN)

# Hacer clic en el botón de buscar
search_button = driver.find_element(By.CLASS_NAME, "BpkButtonBase_bpk-button__F-rxV")
search_button.click()

print("Buscando vuelos...")
time.sleep(15)  # Tiempo para que carguen los resultados

# Scraping de resultados
print("\n=== Resultados de vuelos ===\n")

# Extrae solo las primeras 5 ofertas visibles
ofertas = driver.find_elements(By.CLASS_NAME, "EcoTicketWrapper_itinerary__text__Nphke")

for i, oferta in enumerate(ofertas[:5]):
    print(f"Oferta {i+1}:")
    print(oferta.text)
    print("-" * 30)

driver.quit()
