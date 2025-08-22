import os 
from database import con,cur
def create_user():
    os.system('clear')
    new_data='''
    INSERT INTO users (firstname, lastname, ide_number, email)
    values('sarita', 'gomez', '2312', 'saritajatherinegomez@gmail.com'),
'''
    con.exacaute(new_data)
    con.comit()
    print(':::User has been created sucessfully:::')
create_user()

