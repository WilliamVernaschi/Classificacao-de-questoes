from bs4 import BeautifulSoup
import requests
import pickle
from time import sleep

DEFAULT_URL = 'https://www.stoodi.com.br/exercicios/'
STOODI_URL = 'https://www.stoodi.com.br'

all_subjects = ['fisica', 'matematica', 'quimica', 'biologia', 'literatura', 'gramatica'\
,'historia', 'geografia', 'filosofia', 'sociologia', 'artes', 'ingles', 'espanhol']

def URL_to_soup(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    return soup


def href_from_soup(text):
    URL = text.find('a')
    question_URL = URL.get('href')

    return question_URL


questions_URL_list = list()

for subject in all_subjects:

    module_URLs = list()
    
    soup = URL_to_soup(DEFAULT_URL + subject)
    module_list = soup.find_all('li', 'exercise')

    for module in module_list:

        module_URL = STOODI_URL + href_from_soup(module) 
        module_URLs.append(module_URL)
    
    for URL in module_URLs:
        
        soup = URL_to_soup(URL)
    
        # Looks for the navigation bar to go to the next page
        # (If there's only one page, there's no navigation bar)
        pagination = soup.find('nav', 'pagination--secondary')

        if pagination != None: #If there is more than one page:
            pagination_numbers = pagination.find_all('li')
            number_of_pages = int(pagination_numbers[-2].text)
            for i in range(1, number_of_pages + 1):
                page_URL = f'{URL}?page={str(i)}'
                soup = URL_to_soup(page_URL)
                question_list = soup.find_all('li', 'questionItem')
                
                for question in question_list:
                    question_URL = STOODI_URL + href_from_soup(question)
                    questions_URL_list.append(question_URL)
                    print(question_URL)
        else:
            question_list = soup.find_all('li', 'questionItem')

            for question in question_list:
                question_URL = STOODI_URL + href_from_soup(question)
                questions_URL_list.append(question_URL)
                print(question_URL)          

with open('questions_url.pickle', 'wb') as pickle_out:
    pickle.dump(questions_URL_list, pickle_out)
