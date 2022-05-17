import pyodbc
msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS']

print(f'MS-ACCESS: {msa_drivers}')