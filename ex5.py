# -*- coding: utf-8 -*-
import csv


def input_read():
    input_dict = csv.DictReader(open("shkib.csv"))
    return(input_dict)


def prepare_dict(input_dict):
    prod_dict = {rows['src_user']: {'output_byte':0, 'count':0} for rows in input_dict}
    return(prod_dict, input_dict)



def find_max_queue(prod_dict, input_dict):
    for rows in input_dict:
        return None


def generate_answer():
    prod_dict, input_dict = prepare_dict(input_read())
    with open('ex5_out.txt', mode='w') as outfile:
        outfile.write(
            '# Поиск 5ти пользователей, сгенерировавших наибольшее\
             количество запросов')
        outfile.write(find_max_queue(prod_dict, input_dict))


if __name__ == '__main__':
    generate_answer()
