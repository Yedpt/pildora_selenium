# 🧪 Selenium: Qué es y para qué sirve

## 📌 ¿Qué es Selenium?

**Selenium** es un conjunto de herramientas de código abierto que permite la automatización de pruebas en aplicaciones web a través de diferentes navegadores. Permite simular la interacción del usuario con una página web: hacer clic, escribir, navegar entre páginas, etc.

> 🗣️ _Selenium is an open-source tool suite for automating web browser interactions. It allows testers and developers to simulate user actions in web applications, such as clicking buttons, filling out forms, and navigating pages._

---

## 🌟 Principales características

- ✅ **Multiplataforma**: Funciona en Windows, macOS y Linux.
- 🌐 **Multinavegador**: Soporta Chrome, Firefox, Edge, Safari, entre otros.
- 🧪 **Automatización de pruebas**: Ideal para pruebas funcionales y de regresión.
- 💻 **Soporte para múltiples lenguajes**: Java, Python, C#, JavaScript, Ruby, etc.
- 🔄 **Integración con otras herramientas**: Jenkins, TestNG, Maven, JUnit, etc.
- 🤖 **Simulación real de usuario**: Interacción directa con el navegador como si fuera un usuario real.

---

## 🎯 ¿Para qué sirve Selenium?

Selenium se utiliza principalmente para:

- Automatizar pruebas de interfaces web.
- Validar que los elementos y flujos de una aplicación funcionan correctamente.
- Simular la experiencia del usuario para detectar errores en tiempo de desarrollo.
- Ejecutar pruebas de forma continua (CI/CD) en distintos entornos y navegadores.

> 🗣️ _Selenium is used to automate web application testing, simulate user behavior, validate UI workflows, and run tests across multiple browsers and platforms._

---

## 🛠️ Herramientas de Selenium

### 🔹 Selenium IDE

- Es una extensión para navegadores (Chrome/Firefox).
- Permite grabar, editar y reproducir pruebas sin necesidad de programar.
- Ideal para principiantes o pruebas rápidas.
- Exporta pruebas a distintos lenguajes como Java o Python.

### 🔹 Selenium Remote Control

> ⚠️ _Selenium RC está obsoleto, fue reemplazado por WebDriver._

- Permitía escribir pruebas en varios lenguajes de programación.
- Funcionaba como un servidor intermedio que controlaba el navegador.
- Era más complejo y lento comparado con WebDriver.

---

📚 _Siguiente paso: aprender Selenium WebDriver, el estándar actual para pruebas automáticas avanzadas._

___
#Propuesta para práctica

# 🏖️ Alerta de Vacaciones con Selenium

## Historia

Los miembros del grupo **P5** están exhaustos. Después de semanas sin descanso, solo piensan en una cosa:  
**playa, sol y desconexión**.  
Pero no quieren pagar más de la cuenta, así que han tenido una idea brillante:

> 🔧 Automatizar la búsqueda de ofertas de viaje en la web de **Viajes El Corte Inglés** con **Python + Selenium**.

---

## 🚀 Objetivo

Crear un script que acceda automáticamente a la web, busque un destino (ej: *Málaga*), y revise los precios.  
Si detecta una ganga (por ejemplo, un viaje por menos de 150 €), lanza una **alerta**.

---

## 🧰 Requisitos

Asegúrate de tener Python instalado, y luego instala las siguientes librerías:

```bash
pip install selenium
pip install webdriver-manager

🛠️ Paso a paso

1. Importar librerías
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
2. Iniciar el navegador y abrir la web
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.viajeselcorteingles.es/")
time.sleep(5)
3. Aceptar cookies (si aparecen)
try:
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    time.sleep(1)
except:
    pass
4. Escribir el destino deseado
destino = driver.find_element(By.ID, "autocomplete-destination")  # ID puede cambiar
destino.clear()
destino.send_keys("Málaga")
time.sleep(2)

buscar_btn = driver.find_element(By.CSS_SELECTOR, ".search-button")  # Ajustar selector real
buscar_btn.click()
time.sleep(5)
5. Extraer precios de la página de resultados
precios = driver.find_elements(By.CLASS_NAME, "price")  # Ajustar al HTML actual

for p in precios:
    print(p.text)
6. Detectar precios bajos y lanzar alerta
for p in precios:
    precio_str = p.text.replace("€", "").replace(".", "").strip()
    if precio_str.isdigit():
        precio = int(precio_str)
        if precio < 150:
            print("💥 ¡ALERTA! Oferta encontrada por solo:", precio, "€")
7. Cerrar el navegador
driver.quit()
🎉 Resultado

Tu script vigila los precios por ti, como un agente secreto de vacaciones.
Mientras el resto del mundo refresca la página sin éxito, tú te enteras primero cuando aparece una oferta irresistible.

💡 Nota

La estructura del sitio web puede cambiar, así que es posible que necesites actualizar los selectores (By.ID, By.CLASS_NAME, etc.).
Puedes ejecutar este script cada cierto tiempo automáticamente con una tarea programada (como cron en Linux o el programador de tareas en Windows).
¡Felices vacaciones, P5! 🏖️🐚🌞


