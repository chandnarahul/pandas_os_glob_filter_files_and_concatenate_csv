import os
import glob
import pandas as pd

data_folder_path = (r'C:\Users\imrah\Downloads\AReM')

for file_or_directory in os.listdir(data_folder_path):
    print(file_or_directory)
    
    if os.path.isdir(file_or_directory):
        directory = file_or_directory
        
        concatenate_to_file = directory+"_concatenated.csv"
        
        if os.path.isfile(concatenate_to_file):
            os.remove(concatenate_to_file)
        
        for csv_file in glob.glob(directory+"/*.csv"):
            print (csv_file)
            colum_names=['1','2','3','4','5','6','7']
            data_frame = pd.read_csv(csv_file, sep=',', header=None, skiprows=5, names=colum_names)
            data_frame.to_csv(concatenate_to_file, index=False, encoding='utf-8-sig', mode='a')