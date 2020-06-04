import os
import abc


class Compressor:
    '''
    Super class with definitions for creating custom compression encoding/decoding programs.
    '''
    def __init__(self):
        self.save_path = None
        self.file_path = None
        pass

    @abc.abstractclassmethod
    def encode(self, file_path, save_path):
        '''
        This method encodes the data and returns the compressed string.
        '''
        return

    @abc.abstractclassmethod
    def decode(self, data, params):
        '''
        This method decodes the compressed data back to original.
        '''
        return

    @staticmethod
    def _to_Bytes(data):
        return int(data, 2).to_bytes((len(data) + 7) // 8, byteorder='big')

    @staticmethod
    def _from_Bytes(data):
        return bin(int.from_bytes(data, byteorder='big'))[2:]

    def compare(self):
        '''
        Parameters:
        -----------

        file_path (str) : Path to the file which needs to be compressed
        '''
        file_path, save_path = self.file_path, self.save_path
        a = os.path.getsize(file_path)
        b = os.path.getsize(save_path)
        print("Source File:", file_path, "Size:", a, "BYTES")
        print("Compressed File:", save_path, "Size:", b, "BYTES")
        print("Compression Ratio:", 100*((a-b)/a) )
