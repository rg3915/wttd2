import names
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from fixtures.gen_random_values import gen_doc, gen_phone
from gen_random_values import gen_doc, gen_phone


first_name = names.get_first_name()
last_name = names.get_last_name()
name = '{} {}'.format(first_name, last_name)

email = '{}.{}@example.com'.format(first_name[0].lower(), last_name.lower())


page = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
page.get('http://localhost:8000/inscricao/')


search = page.find_element_by_id('id_name')
search.send_keys(name)
time.sleep(1)

search = page.find_element_by_id('id_cpf')
search.send_keys(gen_doc())
time.sleep(1)

search = page.find_element_by_id('id_email')
search.send_keys(email)
time.sleep(1)

search = page.find_element_by_id('id_phone')
search.send_keys(gen_phone())
time.sleep(2)

button = page.find_element_by_id('id_submit')
button.click()

# page.quit()
