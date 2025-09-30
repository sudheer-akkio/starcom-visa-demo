import os
import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Add the parent directory to the path so we can import from src
sys.path.append(str(Path(__file__).parent))
sys.path.append(str(Path(__file__).parent / 'data-warehouse-sdk'))

from src.data_dictionary.DataDictionaryManager import DataDictionaryManager
from src.utils import load_data_files

root_path = Path(__file__).parent

schema_path = root_path / 'data_schemas'

data_path = root_path / "data"

files = [str(data_path / f) for f in os.listdir(str(data_path)) if f.endswith('.csv')]

for file in files:

    print(f"Generating data dictionary for {file}")

    data_sample = pd.read_csv(file, nrows=10000, index_col=None, low_memory=False)
    data_sample.columns = data_sample.columns.str.lower().str.replace(r'[ ()\[\]]', '_', regex=True).str.replace(r'_+', '_', regex=True).str.strip('_')
    # Handle duplicate column names by appending _2, _3, etc.
    seen_columns = {}
    new_columns = []
    
    for col in data_sample.columns:
        if col in seen_columns:
            seen_columns[col] += 1
            new_col = f"{col}_{seen_columns[col]}"
        else:
            seen_columns[col] = 1
            new_col = col
        new_columns.append(new_col)
    
    data_sample.columns = new_columns

    # data_sample = load_data_files(data_folder=data_path, file_suffix=".csv", read_chunk_size=10000000)
    # filename, data_sample = next(data_sample)

    table_name = file.split('/')[-1].split('.')[0]

    # Initialize DataDictionaryManager with sample data
    manager = DataDictionaryManager(
        data_dictionary_path=schema_path,
        data_sample=data_sample
    )

    results = manager.generate_data_dictionary(table_name=table_name)

# files = []

# file_paths = [str(schema_path / f) for f in files]
# table_names = []

# # TODO: Need to manage class definition on how to handle multiple table names / schemas as lists when generating data dictionaries - do you loop in the class our outside?
# manager = DataDictionaryManager(data_dictionary_path=str(schema_path))

# for i in range(len(file_paths)):
#     print(f"Generating data dictionary for {table_names[i]}")
#     manager.table_name = [table_names[i]]

#     results = manager.generate_data_dictionary(from_csv=file_paths[i])
