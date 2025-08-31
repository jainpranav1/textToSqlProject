import json

DATASET_PATH = "evaluation_examples/examples/tables.json"

def grab_table_information():
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    for database in data:
                
        print(f"Database: {database['db_id']}")
        print()

        tables = [{
            "table_name": table,
            "column_names": [],
            "column_types": [],
            "primary_key": None, # there are no composite primary keys in the dataset
            "foreign_keys": []
        } for table in database['table_names']]


        for i in range(len(database['column_names'])):

            columnName = database['column_names'][i][1]
            columnType = database['column_types'][i]
            tableIndex = database['column_names'][i][0]

            if tableIndex < 0:
                continue

            tables[tableIndex]["column_names"].append(columnName)
            tables[tableIndex]["column_types"].append(columnType)

            if i in database['primary_keys']:
                tables[tableIndex]["primary_key"] = columnName

            if i in [fk[0] for fk in database["foreign_keys"]]:
                tables[tableIndex]["foreign_keys"].append(columnName)

        for table in tables:
            print(f"Table: {table['table_name']}")
            print("Columns:")
            
            numColumns = len(table['column_names'])

            for i in range(numColumns):
                columnName = table['column_names'][i]
                columnType = table['column_types'][i]
                print(f" - {columnName} ({columnType})")

            if table['primary_key'] != None:
                print(f"Primary Key: {table['primary_key']}")

            if len(table['foreign_keys']) > 0:
                print("Foreign Keys:")
                for fk in table['foreign_keys']:
                    print(f" - {fk}")

            print()


        print("===================================")

if __name__ == "__main__":
    grab_table_information()