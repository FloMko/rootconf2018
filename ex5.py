# -*- coding: utf-8 -*-
import csv


def input_read():
    input_dict = csv.DictReader(open("shkib.csv"))
    return(input_dict)


def prepare_dict(input_dict):
    prod_dict = {rows['src_user']: {'output_byte':0, 'count':0} for rows in input_dict}
    return(prod_dict)


def count_dict(prod_dict):
    gen_dict = input_read()
    for rows in gen_dict:
        src_user = rows['src_user']
        prod_dict.get(src_user)['count'] +=1
    return prod_dict



def traff_dict(prod_dict):
    gen_dict = input_read()
    for rows in gen_dict:
        src_user = rows['src_user']
        prod_dict.get(src_user)['output_byte'] +=int(rows['output_byte'])
    return prod_dict


def find_max_count(prod_dict):
    timer = 0
    max_count = 0
    max_count_name = ''
    max_count_list = list()
    while timer < 6:
        for item in prod_dict:
            if prod_dict[item].get('count') > max_count:
                max_count_name = item
                max_count = prod_dict[item].get('count')
        max_count_list.append(max_count_name)
        prod_dict.pop(max_count_name)
        timer +=1
        max_count_name = ''
        max_count = 0
    return max_count_list


def find_max_bytes(prod_dict):
    timer = 0
    max_count = 0
    max_count_name = ''
    max_count_list = list()
    while timer < 6:
        for item in prod_dict:
            if prod_dict[item].get('output_byte') > max_count:
                max_count_name = item
                max_count = prod_dict[item].get('output_byte')
        max_count_list.append(max_count_name)
        prod_dict.pop(max_count_name)
        timer +=1
        max_count_name = ''
        max_count = 0
    return max_count_list


def generate_answer():
    prod_dict = prepare_dict(input_read())
    count_prod_dict = count_dict(prod_dict)
    traff_prod_dict = traff_dict(count_prod_dict)
    # print(find_max_count(traff_prod_dict))
    with open('ex5_out.txt', mode='w') as outfile:
        outfile.write(
            '# Поиск 5ти пользователей, сгенерировавших наибольшее\
             количество запросов')
        outfile.write(''.join(find_max_count(traff_prod_dict)))
        outfile.write(
            '# Поиск 5ти пользователей, отправивших наибольшее\
             наибольшее количество данных')
        outfile.write(''.join(find_max_bytes(traff_prod_dict)))


if __name__ == '__main__':
    generate_answer()

