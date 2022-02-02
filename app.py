from pathlib import Path
from datetime import date, datetime

# path of the files
our_files = Path(r'C:\Users\Admin\Downloads\Test_Folder')

# looping through each file
for file in our_files.iterdir():
    
    if file.name != '.DS_Store' and file.is_file():
        
        directory = file.parent
        exten = file.suffix

        old_name = file.stem

        region, doc_type, old_date = old_name.split('-')

        old_date = datetime.strptime(old_date, '%Y%b%d')

        date = old_date.strftime("%Y-%m-%d")
        
        new_name = f'{date} - {region} - {doc_type}{exten}'
        month = old_date.strftime('%B')

        new_path = our_files.joinpath(month)

        if not new_path.exists():
            new_path.mkdir()
        new_file_path = new_path.joinpath(new_name)

        file.rename(new_file_path)    
