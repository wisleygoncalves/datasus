import os
import shutil

class GetFile(object):
    base_path = r"C:\Users\wisle\Downloads\DataSUS"

    def __init__(self):
        print('\nObtendo os arquivos SERVTERC.txt\n')
        
    def get_file_tercerizados(self):
        path_file = os.path.join(self.base_path, 'files')

        for root, dir, files in os.walk(path_file):
            if 'SERVTERC.txt' in files:
                old_file = os.path.join(root, 'SERVTERC.txt')
                new_file = os.path.join(root, f"SERVTERC_{root.split('\\')[-1]}.txt")
                os.rename(old_file, new_file)

                if os.path.exists(new_file):
                    shutil.copy(new_file, path_file)
                    

                shutil.rmtree(root)  