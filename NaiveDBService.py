import os 
import json
import rpyc
import logging
import socket
# import psutil

class NaiveDBService(rpyc.Service):
    # hosts precisam ter hostnames unicos
    ALIASES = ["NAIVEDB" + socket.gethostname()]
    def __init__(self):
        pass
    
    def exposed_search_file(self, file_name, expression):
        print("search_expression")
        '''Search a substring and return a list with the first 100 occurrences and total occurrences'''
        MAX_ITEMS = 10 #limite de resultados
        results = list()
        count = 0
        expression = expression.upper()
        fd = open(file_name)
        for line in fd:
            line = json.loads(line)
            if isinstance(line['title'], str):
                if expression in line['title'].upper():
                    if count < MAX_ITEMS:
                        results.append(line)
                    count += 1
                continue
            if isinstance(line['maintext'], str):
                if expression in line['maintext'].upper():
                    if count < MAX_ITEMS:
                        results.append(line)
                    count += 1
        fd.close()
        message = 'Total de resultados: ' + str(count) + '\n\n'
        for item in results:
            title = item['title'] if isinstance(item['title'], str) else 'SEM TITULO'
            description = item['description'] if isinstance(item['description'], str) else 'SEM DESCRIÇÃO'
            url = item['url'] if isinstance(item['url'], str) else 'SEM LINK'
            message += 'Título: ' + title + '\n' + 'Descrição: ' + description + '\n' + 'URL: ' + url + '\n\n'
        return message

    
    def exposed_persist_file(self, file_name, chunk):
        with open(file_name, 'ab') as f:
            f.write(chunk)
    
    def exposed_file_list():
        return [x for x in os.listdir() if x.endswith('.jsonl')]

    def send_stats():
        pass# return psutil.cpu_percent()



    def on_connect(self, conn):
        pass
    def on_disconnect(self, conn):
        pass