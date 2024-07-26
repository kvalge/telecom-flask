from flask import request


def save_conclusions(source_page, text):
    with open('data_insight/conclusions.txt', 'a') as file:
        file.write(source_page + text + '\n')
