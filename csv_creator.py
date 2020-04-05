from bs4 import BeautifulSoup
import requests
import pickle
import threading
import csv
from time import sleep



def URL_to_soup(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    return soup


def add_to_query(query_part):
    global full_query

    try:
        for part in query_part:
            full_query += ' '
            full_query += part.text
    except Exception as e:
        print(e)
        full_query += ''


with open('questions_URL.pickle', 'rb') as questions_URL:
    questions_URL = pickle.load(questions_URL)


number_of_questions = len(questions_URL)
questions_dict = dict()

for index, URL in enumerate(questions_URL):
    
    print(f'{index}/{number_of_questions - 1}')

    question_query = None
    
    page_soup = URL_to_soup(URL)
    question_query = page_soup.find('div', 'query')

    if question_query is None:
        print('Looking for question query...')
        page_soup = URL_to_soup(URL)
        question_query = page_soup.find('div', 'query')
    
    if question_query is None:
        continue
    
    full_query = ''
    
    query_part = list(question_query.find_all(['h2', 'p', 'div'], recursive=False))
    add_to_query(query_part)
    full_query = full_query.strip()
    
    module_title = str(page_soup.find_all('h1'))[5:-6] #<-- [5:-6] removes the tags

    subject_name = URL.split('/')
    subject_name = subject_name[4].capitalize()

    module_title = module_title.split(' ')
    module_title = module_title[2:]
    module_title = ' '.join(module_title)
    
    #questions_dict.setdefault(subject_name, {module_title: []}) #if questions_dict[subject_name] does not exist, create one with the value of {module_title: []}
    #questions_dict[subject_name].setdefault(module_title, []) 
    with open ('questions_csv.csv', 'a', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='@')

        if index == 0:
            csv_writer.writerow(['Nome da matéria', 'Nome do módulo', 'Pergunta'])

        csv_writer.writerow([subject_name, module_title, full_query])


    print(f'{subject_name}@{module_title}@{full_query}')
    #questions_dict[subject_name][module_title].append(full_query)
    


#with open('questions_dict.pickle', 'wb') as pickle_out:
#    pickle.dump(questions_dict, pickle_out)
    
        
