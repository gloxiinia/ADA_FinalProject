import lz4.frame
from matplotlib import image
import time
import sys
import os

#IMAGE
#using matplotlib to get the image into binary

img = image.imread("testFiles/kirby.jpg")

#--------------------------------------------------------------------------------------------------#

#TEXT FILE

print("-------------------TXT FILE----------------------")
with open('testFiles/theraven.txt', 'rb') as infile:
    with open('testFiles/theraven.lz4', 'wb') as outfile:
        outfile.write(lz4.frame.compress(infile.read()))

with open('testFiles/theraven.lz4', 'rb') as infile:
    with open('testFiles/theravenAfterlz4.txt', 'wb') as outfile:
        outfile.write(lz4.frame.decompress(infile.read()))

#file size comparison

#original
file_stats = os.stat("testFiles/theraven.txt")
print("Original file:")
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#compressed
file_stats = os.stat("testFiles/theraven.lz4")
print("Compressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#decompressed
file_stats = os.stat("testFiles/theravenAfterlz4.txt")
print("Decompressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#--------------------------------------------------------------------------------------------------#

#CSV FILE

print("-------------------CSV FILE----------------------")
with open('testFiles/movies.csv', 'rb') as infile:
    with open('testFiles/movies.lz4', 'wb') as outfile:
        outfile.write(lz4.frame.compress(infile.read()))

with open('testFiles/movies.lz4', 'rb') as infile:
    with open('testFiles/moviesAfterlz4.csv', 'wb') as outfile:
        outfile.write(lz4.frame.decompress(infile.read()))

#file size comparison

#original
file_stats = os.stat("testFiles/movies.csv")
print("Original file:")
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#compressed
file_stats = os.stat("testFiles/movies.lz4")
print("Compressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#decompressed
file_stats = os.stat("testFiles/moviesAfterlz4.csv")
print("Decompressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#--------------------------------------------------------------------------------------------------#

#PDF FILE

#compression
print("-------------------PDF FILE----------------------")
with open('testFiles/covidindo.pdf', 'rb') as infile:
    with open('testFiles/covidindo.lz4', 'wb') as outfile:
        outfile.write(lz4.frame.compress(infile.read()))

#decompression
with open('testFiles/covidindo.lz4', 'rb') as infile:
    with open('testFiles/covidindoAfterlz4.pdf', "wb") as outfile:
        outfile.write(lz4.frame.decompress(infile.read()))

#file size comparison

#original
file_stats = os.stat("testFiles/covidindo.pdf")
print("Original file:")
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#compressed
file_stats = os.stat("testFiles/covidindo.lz4")
print("Compressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#decompressed
file_stats = os.stat("testFiles/covidindoAfterlz4.pdf")
print("Decompressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#--------------------------------------------------------------------------------------------------#

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
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#compressed
file_stats = os.stat("testFiles/example_2.lz4")
print("Compressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#decompressed
file_stats = os.stat("testFiles/example_2Afterlz4.json")
print("Decompressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')



# #TEST TIME FOR TEXT FILE
# st = time.time()

# cdata = lz4.frame.compress(book)

# et = time.time()
# elapsed_time = et - st

# print('Execution time:', elapsed_time, 'seconds')


# print("The size of the compressed file is:", sys.getsizeof(cdata))

# decomdata = lz4.frame.decompress(cdata)

# print("The size of the decompressed file is:", sys.getsizeof(decomdata))
