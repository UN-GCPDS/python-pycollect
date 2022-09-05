from pycollect import GEDevice, GEDecode, database

# Read the file
file = open(database.RAWS_ABSPATH[0], 'rb')
data = file.read()
file.close()

data = data[:10000]

decode = GEDecode(data)

print("Buffer size: {} bytes".format(len(decode.BUFFER)))
print("Modules detected: {}".format(decode.MODULES))
print("Modules active: {}".format(decode.MODULES_ACTIVE))


print(decode.DATA_SUBRECORD)

# pyplot.plot