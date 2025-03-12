import pandas as pd
import os

class Transformexcel(object):
    colspecs = [(0, 18), (18, 23), (23, 83), (83, None)]  
    colnames = ["CO_MUNCO_CNES", "TSERCLA", "NO_FANTASIA", "CODIGO_ENIGMATICO"]

    base_path = r"C:\Users\wisle\Downloads\DataSUS"
    
    def __init__(self):
        print('\nTrasformando para Excel\n')
    
    def transform_excel(self):
        path_file = os.path.join(self.base_path, 'files')

        for file in os.listdir(path_file):
            if 'txt' in file.split('.'):
                name_file = os.path.join(path_file, file)
                name_file_excel = os.path.join(path_file, f'{file.split('.')[0]}.xlsx')

                df = pd.read_fwf(name_file, colspecs=self.colspecs, names=self.colnames, dtype=str)

                print('\n', df.head(), '\n')

                df.to_excel(name_file_excel, index=False)
                os.remove( name_file )
               
