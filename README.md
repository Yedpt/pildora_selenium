# 🚀 Píldora de Selenium

## 📖 Introducción

**Selenium** es un conjunto de herramientas de automatización de navegadores web que permite controlar un navegador de forma automática mediante código, simulando la interacción humana con páginas web.

### ✨ Características principales

- 🌐 **Open Source** y **multiplataforma**
- 🔧 Compatible con navegadores populares (Chrome, Firefox, Safari, Edge)
- 💻 Soporte para múltiples lenguajes de programación
- 🎯 Simulación realista de interacciones de usuario

---

## 🎯 ¿Para qué sirve Selenium?

### 🧪 **Automatización de Pruebas Funcionales (Testing)**
- Simula el comportamiento real del usuario
- Verificación de funcionamiento correcto de aplicaciones web
- Ideal para **testing end-to-end**
- Pruebas de regresión automatizadas

### 🕷️ **Web Scraping**
- Extracción de datos de páginas con contenido dinámico
- Manejo de JavaScript y AJAX
- Útil cuando herramientas como `requests` o `BeautifulSoup` no son suficientes

**Ejemplos de scraping:**
- Plataformas como Amazon, YouTube, LinkedIn
- Datos que aparecen tras interacciones específicas
- Contenido cargado dinámicamente

### 🔄 **Integración CI/CD**
- Compatible con Jenkins, GitHub Actions, GitLab CI
- Ejecución automática de tests tras cambios en el código
- Integración en pipelines de desarrollo

### ⚡ **Automatización de Tareas Repetitivas**
- Completar formularios automáticamente
- Login automático en aplicaciones
- Descarga masiva de archivos
- Búsquedas y navegación programada

---

## 🛠️ Herramientas Principales

### 🎬 **Selenium IDE**
> Herramienta visual para grabación y reproducción de pruebas

**Características:**
- 📹 **Grabación automática** de interacciones
- 🚫 **Sin programación** requerida
- ▶️ **Modo de reproducción** para validar pruebas
- 📤 **Exportación de código** a múltiples lenguajes

**Ideal para:** Testers sin experiencia en programación

### 🚗 **WebDriver**
> Biblioteca para control programático detallado de navegadores

**Características:**
- 🎭 **Automatización realista** de acciones de usuario
- 🌍 **Soporte multi-navegador**
- 🎛️ **Control total:** ventanas emergentes, cookies, formularios
- 📸 Capturas de pantalla y pruebas dinámicas
- 👻 **Modo Headless** para ejecución sin interfaz gráfica

**Ideal para:** Pruebas automatizadas complejas y validación de flujos completos

### 🕸️ **Selenium Grid**
> Ejecución paralela de pruebas en múltiples entornos

**Características:**
- ⚡ **Ejecución paralela** en diferentes máquinas
- 🌐 **Multi-navegador** y **multi-SO** simultáneo
- 📈 **Escalabilidad** para grandes suites de pruebas

**Ideal para:** Equipos que necesitan ejecutar pruebas masivas

---

## 🌐 Navegadores Compatibles

| Navegador | Driver Requerido | Disponibilidad |
|-----------|------------------|----------------|
| 🟢 **Google Chrome** | ChromeDriver | Todas las plataformas |
| 🟠 **Mozilla Firefox** | GeckoDriver | Todas las plataformas |
| 🔵 **Microsoft Edge** | EdgeDriver | Todas las plataformas |
| 🍎 **Safari** | SafariDriver | Solo macOS |
| 🎭 **Opera** | ChromiumDriver | Limitado |

> **Nota:** Cada navegador requiere su driver específico que actúa como puente entre Selenium y el navegador.

---

## 📋 Requisitos Técnicos

### ✅ **Requisitos Básicos**
- 🐍 Lenguaje de programación instalado (Python, Java, JavaScript, etc.)
- 🚗 Driver del navegador correspondiente
- 📦 Selenium instalado (`pip install selenium` para Python)
- 🌐 Navegador compatible en versión actual/estable
- 💻 Editor de código (VSCode, PyCharm, IntelliJ, etc.)

### ⚙️ **Configuración Adicional**
- Variables de entorno configuradas (opcional)
- Driver ubicado en PATH del sistema o directorio del proyecto
- Permisos de ejecución en sistemas Unix/Linux

---

## 🚀 Ventajas de Selenium

- ✅ **Gratuito y Open Source**
- ✅ **Amplia comunidad** y documentación
- ✅ **Flexibilidad** en lenguajes de programación
- ✅ **Integración** con frameworks de testing
- ✅ **Soporte activo** y actualizaciones constantes
- ✅ **Estándar de la industria** para automatización web

---

## 📚 Casos de Uso Avanzados

### 🎯 **Testing Avanzado**
- Pruebas de carga y rendimiento
- Validación de responsividad
- Testing de compatibilidad cross-browser
- Pruebas de accesibilidad automatizadas

### 🔍 **Monitoreo y Alertas**
- Monitoreo continuo de sitios web
- Detección automática de errores
- Alertas por cambios inesperados
- Validación de SLA de aplicaciones

### 📊 **Análisis y Reporting**
- Generación automática de reportes
- Integración con herramientas de BI
- Métricas de rendimiento automatizadas
- Dashboards de salud de aplicaciones

---

## 🤝 Contribuir

¿Tienes sugerencias o mejoras para esta píldora de Selenium? 

- 🐛 Reporta bugs o problemas
- 💡 Propón nuevas funcionalidades
- 📖 Mejora la documentación
- 🧪 Comparte casos de uso interesantes



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

Asegúrate de tener Python instalado, y luego instala las siguiente:

```bash
git clone REPO_URL
------------------------------
cd pildora_selenium
------------------------------
python -m venv hotel_env
------------------------------
hotel_env\Scripts\activate
------------------------------
pip install -r requirements.txt
------------------------------
python hotel_scraper.py

---
