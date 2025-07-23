from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Simular una búsqueda de vuelo desde Madrid a Londres en eDreams usando Selenium. No extraeremos los datos (eso se hace en el caso 2), solo automatizaremos el proceso de reserva como si fuéramos un usuario.



# Inicializar navegador
driver = webdriver.Chrome()
driver.get("https://www.edreams.es/")

# Espera para que cargue todo (incluye cookies)
time.sleep(5)

# Aceptar cookies si aparece
try:
    cookie_btn = driver.find_element(By.ID, "didomi-notice-agree-button")
    cookie_btn.click()
except:
    pass

# Seleccionar origen
origen = driver.find_element(By.NAME, "origin")
origen.clear()
origen.send_keys("Madrid")
time.sleep(2)
origen.send_keys(Keys.RETURN)

# Seleccionar destino
destino = driver.find_element(By.NAME, "destination")
destino.clear()
destino.send_keys("Londres")
time.sleep(2)
destino.send_keys(Keys.RETURN)

# Puedes dejar la fecha por defecto

# Hacer clic en el botón de buscar
buscar = driver.find_element(By.CLASS_NAME, "searchbox-submit-button")
buscar.click()

# Esperar a que cargue la página de resultados
print("Buscando vuelos...")
time.sleep(10)

print("Automatización completada.")
driver.quit()
