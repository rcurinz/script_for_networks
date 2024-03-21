import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import datetime

def setup_driver():
    # Configura el WebDriver para Edge
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    return driver


def search_and_save(driver, date, url, filename):
    # Construye la URL de búsqueda
    search_url = f"https://www.google.com/search?q=site:{url}&tbs=cdr:1,cd_min:{date},cd_max:{date}&sec_act=d"

    # Abre la URL
    driver.get(search_url)

    # Espera a que se cargue la página
    driver.implicitly_wait(5)  # Espera implícita de 5 segundos

    # Recupera los resultados de búsqueda
    results = driver.find_elements(By.CSS_SELECTOR, "div.g")

    # Abre el archivo para guardar los resultados
    with open(filename, 'a', encoding='utf-8') as file:
        for result in results:
            # Extrae el título, URL y descripción de cada resultado
            title = result.find_element(By.CSS_SELECTOR, "h3").text
            description = result.find_element(By.CSS_SELECTOR, "div.VwiC3b").text
            # Guarda los detalles en el archivo
            file.write(f"Fecha: {date}\nTítulo: {title}\nDescripción: {description}\n------\n")
    time.sleep(5)

def main():
    driver = setup_driver()  # Inicializa el navegador

    """
    24horas	18/07/2023
    biobio	26/10/2023
    CHVnoticias	29/03/2023
    CNN	1/09/2023
    Cooperativa	24/10/2023
    El Mercurio	15/02/2023
    EMOL 4/03/2023
    La Tercera	26/10/2023
    T13	20/07/2023
    """

    # Define las fechas de inicio y fin
    d1 = datetime.date(2023, 10, 26)
    d2 = datetime.date(2024, 3, 20)

    # Genera la lista de fechas
    days = [d1 + datetime.timedelta(days=x) for x in range((d2 - d1).days + 1)]

    # Lista de sitios web para buscar
    medios = ["www.biobiochile.cl","www.cnnchile.com","www.cooperativa.cl","www.emol.com","www.lun.com","www.elmostrador.cl","www.24horas.cl","www.ahoranoticias.cl","www.latercera.com","www.t13.cl","digital.elmercurio.com","www.elciudadano.cl","www.theclinic.cl","www.cnn.com","www.chvnoticias.cl","www.lacuarta.com","www.eldinamo.cl"]
    medios = ["www.biobiochile.cl"]
    for m in medios:
        filename = f"resultados/resultados_{m.replace('.', '_')}.txt"
        for day in days:
            date_str = day.strftime("%m-%d-%Y")  # Formato de fecha para la URL de búsqueda
            search_and_save(driver, date_str, m, filename)

    #driver.quit()  # Cierra el navegador al final del proceso
    while 1:
        time.sleep(5)


if __name__ == '__main__':
    main()
