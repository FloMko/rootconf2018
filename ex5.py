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


def find_max_queue(prod_dict):
    return count_sorted[:4] 


def generate_answer():
    prod_dict = prepare_dict(input_read())
    count_d
    with open('ex5_out.txt', mode='w') as outfile:
        outfile.write(
            '# Поиск 5ти пользователей, сгенерировавших наибольшее\
             количество запросов')
        outfile.write(find_max_queue(prod_dict))


if __name__ == '__main__':
    generate_answer()

