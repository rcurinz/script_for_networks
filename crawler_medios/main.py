from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service

# Configura el WebDriver para Edge
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

# Abre Google
driver.get("http://www.google.com")

# Encuentra el cuadro de búsqueda
search_box = driver.find_element("name", "q")

# Escribe en el cuadro de búsqueda y presiona Enter
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

# Espera un momento para que los resultados se carguen
driver.implicitly_wait(5) # Espera implícita de 5 segundos

# Ahora puedes procesar los resultados de la página como necesites
# Por ejemplo, imprimir el título de la página para confirmar que los resultados se han cargado
print(driver.title)

# No olvides cerrar el navegador al final
driver.quit()
