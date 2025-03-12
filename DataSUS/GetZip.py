import requests
from bs4 import BeautifulSoup
import os
import shutil

class GetZipDataSUS(object):
    url = "http://cnes2.datasus.gov.br/Mod_Download_De_Para_Terceiros.asp?VComp=202502&varTipo=2"
    base_path = r"C:\Users\wisle\Downloads\DataSUS"

    def __init__(self):
        print('\nManipulando Arquivos da Base de Dados\n')

    def get_zip_datasus(self):
        shutil.rmtree(os.path.join(self.base_path, 'files'))

        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            href = link["href"]

            res = requests.get(href, verify=False)
            name_file = href.split('?')[-1].split('=')[-1]
            
            print(f'\nManipulando Arquivo: {name_file}\n')

            self.save_file(res, name_file)
    
    def save_file(self, res, name_file):
        path_file = os.path.join(self.base_path, 'files')
        name_path = os.path.join(self.base_path, 'files', name_file)

        if not os.path.exists(path_file):
            os.makedirs(path_file)

        with open(name_path , "wb") as f:
            for chunk in res.iter_content(chunk_size=8192):
                f.write(chunk)



    