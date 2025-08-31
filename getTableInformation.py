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
            "column_types": []
        } for table in database['table_names']]


        for i in range(len(database['column_names'])):
            columnName = database['column_names'][i][1]
            columnType = database['column_types'][i]
            tableIndex = database['column_names'][i][0]
            tables[tableIndex]["column_names"].append(columnName)
            tables[tableIndex]["column_types"].append(columnType)

        for table in tables:
            print(f"Table: {table['table_name']}")
            print("Columns:")
            
            numColumns = len(table['column_names'])

            for i in range(numColumns):
                column = table['column_names'][i]
                columnType = table['column_types'][i]
                print(f" - {column} ({columnType})")
            print()


        print("===================================")


    
        # for table in enumerate(database['table_names'], 1):

        #     print(f"  Table {j}: {table}")
        
        
        # print(f"Table {i}: {table['table_name']}")
        # print("Columns:")
        # for column in table['column_names']:
        #     print(f" - {column[1]}")
        # print()

if __name__ == "__main__":
    grab_table_information()