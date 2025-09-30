import os
import sys
from pathlib import Path

# Get the project root (parent of examples directory)
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.data_dictionary.DataDictionaryManager import DataDictionaryManager

table_names = ["template"]
dd_path = project_root / "data_schemas"

manager = DataDictionaryManager(table_names, str(dd_path))

schemas = manager.load_data_dictionary(warehouse_type="snowflake")

for table_name, schema in schemas.items():
    print(f"Table: {table_name}")
    print(f"Table Comment: {schema.table_comment}")
    print(f"Column Comments: {schema.column_comments}")
    print(f"Column Data Types: {schema.column_datatypes}")





