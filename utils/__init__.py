import os
from datetime import date


list_files_folders = os.listdir()

folder_name = "data"

if folder_name not in list_files_folders:
    print("📂 Creating folder")
    os.mkdir(folder_name)


# specify the columns list
COLUMNS_LIST = ['kenteken', 'merk', 'handelsbenaming', 
                'datum_tenaamstelling', 'eerste_kleur', 
                'catalogusprijs']

# specify the data types
DF_DTYPES = {'kenteken': str,
             'merk': str,
             'handelsbenaming': str,
             'datum_tenaamstelling': date,
             'eerste_kleur': str,
             'catalogusprijs': float}

# specify the column names
DF_COLNAMES = {'handelsbenaming': 'model',
               'eerste_kleur': 'kleur'}