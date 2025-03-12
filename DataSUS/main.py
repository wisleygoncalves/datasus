from GetZip import GetZipDataSUS
from ExtractFiles import ExtractFiles
from GetFile import GetFile
from Transformexcel import Transformexcel

class DataSUS(object):
    def __init__(self):
        print('\nArmazenando dados da base de dados DataSUS\n')
    
    def get_zip_datasus(self):
        gzds = GetZipDataSUS()
        gzds.get_zip_datasus()
    
    def extract_files(self):
        ef = ExtractFiles()
        ef.control_extract_file()
    
    def get_file(self):
        gf = GetFile()
        gf.get_file_tercerizados()
    
    def transform_excel(self):
        te = Transformexcel()
        te.transform_excel()

def main():
    ds = DataSUS()
    ds.get_zip_datasus()
    ds.extract_files()
    ds.get_file()
    ds.transform_excel()

if '__main__' == __name__:
    main()