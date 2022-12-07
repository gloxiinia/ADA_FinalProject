import tracemalloc
import zstandard as zstd

tracemalloc.start()

with open('test_files/kirby.jpg', 'rb') as infile:
    with open('zst_test_files/kirby.zst', 'wb') as outfile:
        outfile.write(zstd.compress(infile.read()))

img_com_snapshot = tracemalloc.take_snapshot()

print("================ IMG COMPRESSION SNAPSHOT =================")
for stat in img_com_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('zst_test_files/kirby.zst', 'rb') as infile:
    with open('zst_test_files/kirbyAfterzst.jpg', 'wb') as outfile:
        outfile.write(zstd.decompress(infile.read()))

img_decom_snapshot = tracemalloc.take_snapshot()

print("\n================ IMG DECOMPRESSION SNAPSHOT =================")
for stat in img_decom_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('test_files/theraven.txt', 'rb') as infile:
    with open('zst_test_files/theraven.zst', 'wb') as outfile:
        outfile.write(zstd.compress(infile.read()))

txt_com_snapshot = tracemalloc.take_snapshot()

print("\n================ TXT COMPRESSION SNAPSHOT =================")
for stat in txt_com_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('zst_test_files/theraven.zst', 'rb') as infile:
    with open('zst_test_files/theravenAfterzst.txt', 'wb') as outfile:
        outfile.write(zstd.decompress(infile.read()))

txt_decom_snapshot = tracemalloc.take_snapshot()

print("\n================ TXT DECOMPRESSION SNAPSHOT =================")
for stat in txt_decom_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('test_files/imdb_movies.csv', 'rb') as infile:
    with open('zst_test_files/imdb_movies.zst', 'wb') as outfile:
        outfile.write(zstd.compress(infile.read()))
csv_com_snapshot = tracemalloc.take_snapshot()

print("\n================ CSV COMPRESSION SNAPSHOT =================")
for stat in csv_com_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('zst_test_files/imdb_movies.zst', 'rb') as infile:
    with open('zst_test_files/imdb_moviesAfterzst.csv', 'wb') as outfile:
        outfile.write(zstd.decompress(infile.read()))

csv_decom_snapshot = tracemalloc.take_snapshot()

print("\n================ CSV DECOMPRESSION SNAPSHOT =================")
for stat in csv_decom_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('test_files/covidindo.pdf', 'rb') as infile:
    with open('zst_test_files/covidindo.zst', 'wb') as outfile:
        outfile.write(zstd.compress(infile.read()))

pdf_com_snapshot = tracemalloc.take_snapshot()

print("\n================ PDF COMPRESSION SNAPSHOT =================")
for stat in pdf_com_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('zst_test_files/covidindo.zst', 'rb') as infile:
    with open('zst_test_files/covidindoAfterzst.pdf', "wb") as outfile:
        outfile.write(zstd.decompress(infile.read()))

pdf_decom_snapshot = tracemalloc.take_snapshot()

print("\n================ PDF DECOMPRESSION SNAPSHOT =================")
for stat in pdf_decom_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('test_files/example_2.json', 'rb') as infile:
    with open('zst_test_files/example_2.zst', 'wb') as outfile:
        outfile.write(zstd.compress(infile.read()))

json_com_snapshot = tracemalloc.take_snapshot()

print("\n================ JSON COMPRESSION SNAPSHOT =================")
for stat in json_com_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('zst_test_files/example_2.zst', 'rb') as infile:
    with open('zst_test_files/example_2Afterzst.json', 'wb') as outfile:
        outfile.write(zstd.decompress(infile.read()))

json_decom_snapshot = tracemalloc.take_snapshot()

print("\n================ JSON DECOMPRESSION SNAPSHOT =================")
for stat in json_decom_snapshot.statistics("lineno"):
    print(stat)