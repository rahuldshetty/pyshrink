from pyshrink import huffman_encode, huffman_decodeS, Huffman
import sys
sample = 'helllo abcdddd' 

enc, table = huffman_encode(sample)
enc_bits = Huffman._to_Bytes(enc)

print("Encoding:", enc, table, enc_bits)

dec_bits = bin(int.from_bytes(enc_bits, byteorder='big'))[2:]

dec = huffman_decodeS(enc, table)
print("Decoding:",dec_bits, dec)