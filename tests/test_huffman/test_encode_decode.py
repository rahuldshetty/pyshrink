from pyshrink import huffman_encode, huffman_decodeS, Huffman
import sys

def test_encode_decode():
    sample = 'helllo abcdddd' 
    enc, table = huffman_encode(sample)
    enc_bits = Huffman._to_Bytes(enc)
    dec_bits = bin(int.from_bytes(enc_bits, byteorder='big'))[2:]
    dec = huffman_decodeS(enc, table)
    assert dec == sample