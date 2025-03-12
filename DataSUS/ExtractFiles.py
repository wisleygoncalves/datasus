import os
import zipfile



class ExtractFiles(object):
    base_path = r"C:\Users\wisle\Downloads\DataSUS"

    def __init__(self):
        print('\nExtrair Arquivos Obtidos do DataSus\n')
    
    def control_extract_file(self):
        path_file = os.path.join(self.base_path, 'files')

        for file in os.listdir(path_file):
            if 'zip' in file.split('.') or 'ZIP' in file.split('.'):
                print(f'\nExtraindo Arquivo: {file}\n')

                name_path = os.path.join(self.base_path, 'files', file)
                extract_to = os.path.join(self.base_path, 'files', file.split('.')[0])

                if not os.path.exists(extract_to):
                    os.makedirs(extract_to)

                try:
                    self.extract_file(name_path, extract_to)
                except:
                    print('Já existe arquivo...')
            
                self.delete_zip_file(name_path)
    
    def extract_file(self, archive_path, extract_to):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    
    def delete_zip_file(self, archive_path):
        os.remove(archive_path)