import tracemalloc
import lz4.frame

tracemalloc.start()

with open('test_files/kirby.jpg', 'rb') as infile:
    with open('lz4_test_files/kirby.lz4', 'wb') as outfile:
        outfile.write(lz4.frame.compress(infile.read()))

img_com_snapshot = tracemalloc.take_snapshot()

print("================ IMG COMPRESSION SNAPSHOT =================")
for stat in img_com_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('lz4_test_files/kirby.lz4', 'rb') as infile:
    with open('lz4_test_files/kirbyAfterlz4.jpg', 'wb') as outfile:
        outfile.write(lz4.frame.decompress(infile.read()))

img_decom_snapshot = tracemalloc.take_snapshot()

print("\n================ IMG DECOMPRESSION SNAPSHOT =================")
for stat in img_decom_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('test_files/theraven.txt', 'rb') as infile:
    with open('lz4_test_files/theraven.lz4', 'wb') as outfile:
        outfile.write(lz4.frame.compress(infile.read()))

txt_com_snapshot = tracemalloc.take_snapshot()

print("\n================ TXT COMPRESSION SNAPSHOT =================")
for stat in txt_com_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('lz4_test_files/theraven.lz4', 'rb') as infile:
    with open('lz4_test_files/theravenAfterlz4.txt', 'wb') as outfile:
        outfile.write(lz4.frame.decompress(infile.read()))

txt_decom_snapshot = tracemalloc.take_snapshot()

print("\n================ TXT DECOMPRESSION SNAPSHOT =================")
for stat in txt_decom_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('test_files/imdb_movies.csv', 'rb') as infile:
    with open('lz4_test_files/imdb_movies.lz4', 'wb') as outfile:
        outfile.write(lz4.frame.compress(infile.read()))
csv_com_snapshot = tracemalloc.take_snapshot()

print("\n================ CSV COMPRESSION SNAPSHOT =================")
for stat in csv_com_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('lz4_test_files/imdb_movies.lz4', 'rb') as infile:
    with open('lz4_test_files/imdb_moviesAfterlz4.csv', 'wb') as outfile:
        outfile.write(lz4.frame.decompress(infile.read()))

csv_decom_snapshot = tracemalloc.take_snapshot()

print("\n================ CSV DECOMPRESSION SNAPSHOT =================")
for stat in csv_decom_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('test_files/covidindo.pdf', 'rb') as infile:
    with open('lz4_test_files/covidindo.lz4', 'wb') as outfile:
        outfile.write(lz4.frame.compress(infile.read()))

pdf_com_snapshot = tracemalloc.take_snapshot()

print("\n================ PDF COMPRESSION SNAPSHOT =================")
for stat in pdf_com_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('lz4_test_files/covidindo.lz4', 'rb') as infile:
    with open('lz4_test_files/covidindoAfterlz4.pdf', "wb") as outfile:
        outfile.write(lz4.frame.decompress(infile.read()))

pdf_decom_snapshot = tracemalloc.take_snapshot()

print("\n================ PDF DECOMPRESSION SNAPSHOT =================")
for stat in pdf_decom_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('test_files/example_2.json', 'rb') as infile:
    with open('lz4_test_files/example_2.lz4', 'wb') as outfile:
        outfile.write(lz4.frame.compress(infile.read()))

json_com_snapshot = tracemalloc.take_snapshot()

print("\n================ JSON COMPRESSION SNAPSHOT =================")
for stat in json_com_snapshot.statistics("lineno"):
    print(stat)

tracemalloc.clear_traces()

with open('lz4_test_files/example_2.lz4', 'rb') as infile:
    with open('lz4_test_files/example_2Afterlz4.json', 'wb') as outfile:
        outfile.write(lz4.frame.decompress(infile.read()))

json_decom_snapshot = tracemalloc.take_snapshot()

print("\n================ JSON DECOMPRESSION SNAPSHOT =================")
for stat in json_decom_snapshot.statistics("lineno"):
    print(stat)