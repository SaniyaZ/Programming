import requests
import codecs
import os
path = 'D:\\PYTHON\\hw\\vk\\'    
os.chdir(path)
if 'output' not in os.listdir():
    os.mkdir('output')
search_link = 'https://api.vk.com/method/users.search'
search_pars = {
    'access_token': 'dad046e01b2ab9f769f7c9676ff2cd73bc2674dc5a8ed8fa40089156db7ebc56483305a39403c87f07d88',
    'count': 200,
    'city': 138,
    'country': 1,
    'fields': 'bdate, sex, occupation'
}


def get_users(users_search, parameters):
    """
    Requests user data for a given set of parameters.
    """
    users = requests.get(users_search, params=parameters)
    data = users.json()
    return data


def save_users_info(users_data):
    """
    Write users metadata to a .csv file
    """
    f_out = codecs.open('metadata.csv', 'w', 'utf-8')
    f_out.write('first_name; last_name; sex; bdate; uid; occupation\n')
    keys = ['first_name', 'last_name', 'sex', 'bdate', 'uid', 'occupation']
    for i in users_data['response'][1:search_pars['count']]:
        mass = ''
        for key in keys:
            if key in i.keys():
                if key != 'occupation':
                    mass += str(i[key]) + ';'
                else:
                    mass += str(i[key]['name']) + '\n'
            else:
                if key == 'occupation':
                    mass += 'NONE\n'
                else:
                    mass += 'NONE; '
        f_out.write(mass)
    f_out.close()


def save_wall_info(users_data, output_dir):
    """
    Write wall posts to a .txt file
    """
    for i in range(1, len(users_data['response'])):
        perid = users_data['response'][i]['uid']
        get_meth = 'https://api.vk.com/method/wall.get'
        wall_parameters = {
            'owner_id': perid,
            'count': 10,
            'filter': 'owner'
        }
        save_posts = requests.get(get_meth, params=wall_parameters)
        posts = save_posts.json()
        f_out = codecs.open(output_dir + str(perid) + '.txt', 'w', 'utf-8')
        try:
            for post in posts['response'][1:]:
                cleared = post['text'].replace('<br>', '\n')
                if cleared != '':
                    f_out.write('НОВЫЙ ПОСТ:\n')
                    f_out.write(cleared + '\n')
                    f_out.write('\n')
                else:
                    os.remove(output_dir + perid + '.txt')
        except:
            continue

info = get_users(search_link, search_pars)
save_users_info(info)
save_wall_info(info, path+'output\\')

