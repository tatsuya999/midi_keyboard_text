import bz2,io

target_file = "enwiktionary-20210520-pages-articles-multistream.xml.bz2"

size = 1024 * 1024  # 1MB
with open(target_file, "rb") as f:
    decompressor = bz2.BZ2Decompressor()
    slen = 0
    data = b''
    while data or (data := f.read(size)):
        len1 = len(data)
        decompressor.decompress(data)
        data = decompressor.unused_data
        slen += len1 - len(data)
        if decompressor.eof:
            print(slen)
            slen = 0
            decompressor = bz2.BZ2Decompressor()
