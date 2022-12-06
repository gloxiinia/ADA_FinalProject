
import zstandard as zstd
import sys
import time

data = b"asdkfj;lkasdfasf"

from matplotlib import image

img = image.imread("testFiles/kirby.jpg")

st = time.time()

cctx = zstd.ZstdCompressor()

cdata = cctx.compress(img)

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')


print("The size of the compressed file is:", sys.getsizeof(cdata))
#print(cdata)

decomdata = zstd.decompress(cdata)

print("The size of the decompressed file is:", sys.getsizeof(decomdata))

with open('testFiles/credits.csv', 'rb') as infile:
    with open('testFiles/credits.zst', 'wb') as outfile:
        outfile.write(zstd.compress(infile.read()))

with open('testFiles/covidindo.pdf', 'rb') as infile:
    with open('testFiles/covidindo.zst', 'wb') as outfile:
        outfile.write(zstd.compress(infile.read()))

with open('testFiles/covidindo.zst', 'rb') as infile:
    with open('testFiles/covidindoAfterzstd.pdf', 'wb') as outfile:
        outfile.write(zstd.decompress(infile.read()))

with open('testFiles/credits.zst', 'rb') as infile:
    with open('testFiles/creditsAfterzst.csv', 'wb') as outfile:
        outfile.write(zstd.decompress(infile.read()))
