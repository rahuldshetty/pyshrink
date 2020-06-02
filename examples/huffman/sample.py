from pyshrink import Huffman

file = 'test.txt'
save = 'save.txt'
dec = 'dcde.txt'

huffman = Huffman()
huffman.encode(file, save)
huffman.compare()
huffman.decode(save, dec)

print("Status:", open(file,'r').read() == open(dec, 'r').read())