import requests
from bs4 import BeautifulSoup
import numpy as np
import logging
import csv
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from time import sleep
from random import randint
def extract_data(url, city):
    response = requests.get(url, timeout=20)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = {}
    try:
        result['name'] = soup.select('.venue-name-box h1')[0].get_text().lstrip(' ').rstrip(' ')
    except IndexError:
       result['name'] = None
    result['nameEN'] = url.split('/')[3]
    result['city'] = city
    
    try:
        result['rate'] = soup.select('.rate span')[0].get_text().lstrip(' ').rstrip(' ')
    except IndexError:
        result['rate'] = None
    info = soup.select('.infolist li span')
    result['address'] = info[0].get_text().lstrip('\r\n ').rstrip('\r\n ')
    result['phone']   = info[1].get_text().lstrip('\r\n ').rstrip('\r\n ')
    try:
        result['time'] = info[2].get_text().lstrip('\r\n ').rstrip('\r\n ').split()[3]
    except IndexError:
        result['time'] = None

    rate = soup.select('.rates-list li span div')
    result['quality_rate'] = rate[0].get('data-rateit-value')
    result['service_rate'] = rate[1].get('data-rateit-value')
    result['w_to_p_ratio'] = rate[2].get('data-rateit-value')
    result['decor_rate']   = rate[3].get('data-rateit-value')
    
    # Features
    features = soup.select('.venue-features-box span')
    features_list = []
    for index in range(len(features)):
        features_list.append(features[index].get_text())
    result['features'] = features_list
    
    return result


def scrape(url, logger, city, number):
    
    logger.info('Starting to scrape the page [{}]'.format(url))
    results = []
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
    except HTTPError as http_err:
        logger.error('HTTP error occurred: {}'.format(http_err))
        return results
    except ConnectionError as conn_err:
        logger.error('Connection error occurred: {}'.format(conn_err))
        return results
    except Timeout as timeout_err:
        logger.error('Timeout error occurred: {}'.format(timeout_err))
        return results
    except RequestException as req_err:
        logger.error('Request error occurred: {}'.format(req_err))
        return results
    
    print(f'response = {response.status_code}  city = {city}   page = {number}')
    soup = BeautifulSoup(response.text, 'html.parser')
    new_links = soup.select('.restaurant-list-container div a')
    
    for i in range(len(new_links)):
        try:
            new_url = new_links[i].get('href')
            results.append(extract_data(f'https://fidilio.com{new_url}', city))
            logger.info('city={city} page={number} scraped successfully.')
        except:
            logger.warning(f'Failed to extract data from city={city} page={number}')

    return results

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(filename='fidilio.log', filemode='w', format='%(asctime)s %(levelname)s: %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    city = ['shiraz']#, 'tehran', 'isfahan', 'mashhad', 'tabriz', 'kish', 'ghom', 'arak', 'ahwaz','sabzevar', 'urmia', 'zanjan', 'qazvin', 'hamedan'
        #, 'karaj', 'kerman', 'bandarabbas' ]
    pages_end = [49, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1]     
    pages_end = [2]
    all_results = []
    for index, value in enumerate(city):
        for number in range(pages_end[index]):
                url = f'https://fidilio.com/coffeeshops/in/{value}/?p={number}'
                Coffee_list = scrape(url, logger, value, number)
                all_results.extend(Coffee_list)
                #sleep for random time between 2 to 5 seconds
                time_milisec = randint(2000,5000)
                time_sec = time_milisec / 1000
                print("time sleep=",time_sec)
                sleep(time_sec)
    with open('Coffee.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'nameEN', 'city', 'rate', 'address', 'phone', 'time', 'quality_rate', 'service_rate', 'w_to_p_ratio', 'decor_rate', 'features'])
        writer.writeheader()
        for co_dic in all_results:
            writer.writerow(co_dic)