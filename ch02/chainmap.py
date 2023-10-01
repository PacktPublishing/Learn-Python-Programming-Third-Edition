# chainmap.py

from collections import ChainMap
default_connection = {'host': 'localhost', 'port': 4567}
connection = {'port': 5678}
conn = ChainMap(connection, default_connection) # map creation
print(conn['port'])  # port is found in the first dictionary

print(conn['host'])  # host is fetched from the second dictionary

print(conn.maps)  # we can see the mapping objects

conn['host'] = 'packtpub.com'  # let's add host
print(conn.maps)

del conn['port']  # let's remove the port information
print(conn.maps)

print(conn['port'])  # now port is fetched from the second dictionary

print(dict(conn))  # easy to merge and convert to regular dictionary