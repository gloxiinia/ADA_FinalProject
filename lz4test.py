import lz4.frame
from matplotlib import image
import time
import sys
import os

#IMAGE
#using matplotlib to get the image into binary

img = image.imread("testFiles/kirby.jpg")

#TEXT FILE

f=open("testFiles/theraven.txt", "rb")

if f.mode == 'rb':
    book = f.read()
else:
    print("File cannot be read, sorry!")


#TEST TIME FOR TEXT FILE
st = time.time()

cdata = lz4.frame.compress(book)

et = time.time()
elapsed_time = et - st

print('Execution time:', elapsed_time, 'seconds')


print("The size of the compressed file is:", sys.getsizeof(cdata))

decomdata = lz4.frame.decompress(cdata)

print("The size of the decompressed file is:", sys.getsizeof(decomdata))

#CSV FILE

print("-------------------CSV FILE----------------------")
with open('testFiles/movies_metadata.csv', 'rb') as infile:
    with open('testFiles/movies_metadata.lz4', 'wb') as outfile:
        outfile.write(lz4.frame.compress(infile.read()))

with open('testFiles/movies_metadata.lz4', 'rb') as infile:
    with open('testFiles/movies_metadataAfterlz4.csv', 'wb') as outfile:
        outfile.write(lz4.frame.decompress(infile.read()))

#PDF FILE

print("-------------------PDF FILE----------------------")
with open('testFiles/covidindo.pdf', 'rb') as infile:
    with open('testFiles/covidindo.lz4', 'wb') as outfile:
        outfile.write(lz4.frame.compress(infile.read()))

with open('testFiles/covidindo.lz4', 'rb') as infile:
    with open('testFiles/covidindoAfterlz4.pdf', "wb") as outfile:
        outfile.write(lz4.frame.decompress(infile.read()))

#JSON FILE

print("-------------------JSON FILE----------------------")
#compression
with open('testFiles/example_2.json', 'rb') as infile:
    with open('testFiles/example_2.lz4', 'wb') as outfile:
        outfile.write(lz4.frame.compress(infile.read()))

#decompression
with open('testFiles/example_2.lz4', 'rb') as infile:
    with open('testFiles/example_2Afterlz4.json', "wb") as outfile:
        outfile.write(lz4.frame.decompress(infile.read()))

#file size comparison

#original
file_stats = os.stat("testFiles/example_2.json")
print("Original file:")
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')

#compressed
file_stats = os.stat("testFiles/example_2.lz4")
print("Compressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')

#decompressed
file_stats = os.stat("testFiles/example_2Afterlz4.json")
print("Decompressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')



