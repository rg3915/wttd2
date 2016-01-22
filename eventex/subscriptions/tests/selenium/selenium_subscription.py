import names
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from gen_random_values import gen_cpf, gen_phone


first_name = names.get_first_name()
last_name = names.get_last_name()
name = '{} {}'.format(first_name, last_name)

email = '{}.{}@example.com'.format(first_name[0].lower(), last_name.lower())


page = webdriver.Firefox()
page.maximize_window()
time.sleep(0.5)
# page = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
page.get('http://localhost:8000/inscricao/')
time.sleep(0.5)

fields = [['id_name', name],
          ['id_cpf', gen_cpf()],
          ['id_email', email],
          ['id_phone', gen_phone()]]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])
    # time.sleep(0.5)

button = page.find_element_by_id('id_submit')
button.click()

page.quit()
