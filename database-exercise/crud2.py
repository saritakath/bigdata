import os
from database import con, cur
def create_user():
    os.system('clear')
    fname = input('Enter your firtsname')
    lname = input('Enter your lastname')
    ide_num = input('Enter your ident.number:')
    email = input('Enter your email:')
    new_data=f'''
        insert into users (firstname, lastname, ide_number, email)
        values('{fname}','{lname}','{ide_num}','{email}')
    '''
    con.execute(new_data)
    con.commit()
    print("user has been created sucessfully!")
create_user()
def list_users():
    os.system('clear')
    users_data_query='''
        select
        id
        fristname
        email
        ide_number
        case when
        
        SELECT * FROM users;
        '''
    cur.execute(users_data_query)
    data=cur.fetchall()
    print(data)
list_users()


