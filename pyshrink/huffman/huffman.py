#!/usr/bin/python3
# Huffman Encoding for string
import sys
from ..compressor import Compressor

class Node():
    def __init__(self, char, score = 0):
        self.char = char
        self.score = score
        self.left = None
        self.right = None
    
    def set_left(self, left):
        self.left = left
        self.score += left.score

    def set_right(self, right):
        self.right = right
        self.score += right.score

    def get_score(self):
        return self.score

    def get_short_char(self):
        return self.short_char

    def set_short_char(self, short_char):
        self.short_char = short_char

def sortbyvalue(lists):
    return sorted(lists, key=lambda x:x.get_score())

def huffman_encode(string):
    # encoding a string into huffman
    # get frequencies of each character
    chars = list(string)
    freq = [Node(v, chars.count(v)) for v in set(chars)]

    freq = sortbyvalue(freq)

    # generate huffman tree
    while len(freq) != 1:
        # get first item and add it to root
        left = freq.pop(0)
        right = freq.pop(0)

        new_node = Node('$')
        new_node.set_left(left)
        new_node.set_right(right)
        
        freq.append(new_node)
        freq = sortbyvalue(freq)

    # generate mapping table
    hash_table = {}

    def visit_nodes(root, char):
        if root is not None:
            root.set_short_char(char)
            visit_nodes(root.left, char + '0')
            visit_nodes(root.right, char + '1')
            if root.left is None and root.right is None:
                hash_table[root.char] = char

    visit_nodes(freq[0], '1')

    # encode string
    encoded_string = ""
    for char in chars:
        encoded_string += hash_table[char]
    
    return encoded_string, hash_table

def huffman_decodeS(string, hashtable):
    decoded_string = ""
    while string:
        for k in hashtable:
            if string.startswith(hashtable[k]):
                decoded_string += k
                string = string[len(hashtable[k]):]
    return decoded_string

def huffman_decode(string, hashtable):
    decoded_string = bytearray()
    while string:
        for k in hashtable:
            if string.startswith(hashtable[k]):
                decoded_string.append(k)
                string = string[len(hashtable[k]):]
    return decoded_string

class Huffman(Compressor):

    def encode(self, file_path, save_path):
        self.file_path = file_path
        self.save_path = save_path

        file_handler = open(file_path, 'rb')
        data = file_handler.read()
        file_handler.close()

        save_handler = open(save_path, 'wb')

        enc, hash_table = huffman_encode(data)
        self.hash_table = hash_table

        byte_data = self._to_Bytes(enc)
        save_handler.write(byte_data)

    def decode(self, file_path, save_path):
        src = open(file_path, 'rb')
        tgt = open(save_path, 'wb')
        
        data = src.read()
        data = bin(int.from_bytes(data, byteorder='big'))[2:]

        dec = huffman_decode(data, self.hash_table)
        tgt.write(dec)



    


