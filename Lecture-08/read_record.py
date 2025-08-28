import struct

with open("records.bin",'rb') as file:
    data = file.read(struct.calcsize('i20sif'))
    records = struct.unpack('i20sif', data)
    records = (records[0], records[1].decode().strip('\x00'),records[2],records[3])
    print(f"ID: {records[0]}, name:{records[1]}, Age:{records[2]}, GPA:{records[3]}")