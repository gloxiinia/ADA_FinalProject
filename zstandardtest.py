
import zstandard as zstd
import sys
import time
from matplotlib import image
import os

#IMAGE
#using matplotlib to get the image into binary

img = image.imread("testFiles/kirby.jpg")

#--------------------------------------------------------------------------------------------------#

#TEXT FILE

print("-------------------TXT FILE----------------------")
with open('testFiles/theraven.txt', 'rb') as infile:
    with open('testFiles/theraven.zst', 'wb') as outfile:
        outfile.write(zstd.compress(infile.read()))

with open('testFiles/theraven.zst', 'rb') as infile:
    with open('testFiles/theravenAfterzst.txt', 'wb') as outfile:
        outfile.write(zstd.decompress(infile.read()))

#file size comparison

#original
file_stats = os.stat("testFiles/theraven.txt")
print("Original file:")
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#compressed
file_stats = os.stat("testFiles/theraven.zst")
print("Compressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#decompressed
file_stats = os.stat("testFiles/theravenAfterzst.txt")
print("Decompressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#--------------------------------------------------------------------------------------------------#

#CSV FILE

print("-------------------CSV FILE----------------------")
with open('testFiles/movies.csv', 'rb') as infile:
    with open('testFiles/movies.zst', 'wb') as outfile:
        outfile.write(zstd.compress(infile.read()))

with open('testFiles/movies.zst', 'rb') as infile:
    with open('testFiles/moviesAfterzst.csv', 'wb') as outfile:
        outfile.write(zstd.decompress(infile.read()))

#file size comparison

#original
file_stats = os.stat("testFiles/movies.csv")
print("Original file:")
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#compressed
file_stats = os.stat("testFiles/movies.zst")
print("Compressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#decompressed
file_stats = os.stat("testFiles/moviesAfterzst.csv")
print("Decompressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#--------------------------------------------------------------------------------------------------#

#PDF FILE

#compression
print("-------------------PDF FILE----------------------")
with open('testFiles/covidindo.pdf', 'rb') as infile:
    with open('testFiles/covidindo.zst', 'wb') as outfile:
        outfile.write(zstd.compress(infile.read()))

#decompression
with open('testFiles/covidindo.zst', 'rb') as infile:
    with open('testFiles/covidindoAfterzst.pdf', "wb") as outfile:
        outfile.write(zstd.decompress(infile.read()))

#file size comparison

#original
file_stats = os.stat("testFiles/covidindo.pdf")
print("Original file:")
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#compressed
file_stats = os.stat("testFiles/covidindo.zst")
print("Compressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#decompressed
file_stats = os.stat("testFiles/covidindoAfterzst.pdf")
print("Decompressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#--------------------------------------------------------------------------------------------------#

#JSON FILE

print("-------------------JSON FILE----------------------")
#compression
with open('testFiles/example_2.json', 'rb') as infile:
    with open('testFiles/example_2.zst', 'wb') as outfile:
        outfile.write(zstd.compress(infile.read()))

#decompression
with open('testFiles/example_2.zst', 'rb') as infile:
    with open('testFiles/example_2Afterzst.json', "wb") as outfile:
        outfile.write(zstd.decompress(infile.read()))

#file size comparison

#original
file_stats = os.stat("testFiles/example_2.json")
print("Original file:")
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#compressed
file_stats = os.stat("testFiles/example_2.zst")
print("Compressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')

#decompressed
file_stats = os.stat("testFiles/example_2Afterzst.json")
print("Decompressed file:")
print(f'file size in Bytes is {file_stats.st_size}')
print(f'file size in MegaBytes is {file_stats.st_size / (1024 * 1024)}\n')
