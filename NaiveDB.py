import os 
import json
import rpyc
import logging

class NaiveDBService(rpyc.Service):
    ALIASES = ['NAIVEDB'] # mudar para nome do nó
    def __init__(self):
        pass

    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        pass

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        pass
    
    def exposed_search_expression(self, expression: str):
        logging.info("search_expression from ")
        '''Search a substring and return a list with the first 100 occurrences and total occurrences'''
        MAX_ITEMS = 10
        results = list()
        count = 0
        expression = expression.upper()
        jsonl_files = [file for file in os.listdir() if file.endswith('.jsonl')]
        for jsonl_file in jsonl_files:
            file_descriptor = open(jsonl_file)
            for line in file_descriptor:
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
            file_descriptor.close()
        message = 'Total de resultados: ' + str(count) + '\n\n'
        for item in results:
            title = item['title'] if isinstance(item['title'], str) else 'SEM TITULO'
            description = item['description'] if isinstance(item['description'], str) else 'SEM DESCRIÇÃO'
            url = item['url'] if isinstance(item['url'], str) else 'SEM LINK'
            message += 'Título: ' + title + '\n' + 'Descrição: ' + description + '\n' + 'URL: ' + url + '\n\n'
        return message
    
    
    def extract_from_gz():
        '''Extract the downloaded .gz files. gzip must be installed'''
        gz_files = [file for file in os.listdir() if file.endswith('.gz')]
        for gz_file in gz_files:
            os.system('gzip -d ' + gz_file)
    
    def exposed_upload_file(self, file_name, file_data):
        with open(file_name, 'ab') as f:
            f.write(file_data)
