import os
import hashlib


class CompareFiles(object):
    """Compare files in folder and delete dublicate"""

    def __init__(self, floder_main, folder_new, buffer_size = 8192):
        """Constructor"""
        self.floder_main = floder_main + '\\'
        self.folder_new = folder_new + '\\'
        self.buffer_size = buffer_size

    def hash_folder_main(self):
        """Hash folder main"""
        self.hash_main = set()

        for dirpath, dirnames, filenames in os.walk(self.floder_main):
            # перебрать файлы
            for filename in filenames:
                # self.hash_main.add(os.path.join(dirpath, filename))
                # self.hash_main.add(os.path.join(self.floderMain, filename))
                self.hash_main.add(self.get_hash_md5(os.path.join(self.floder_main, filename)))

    def get_hash_md5(self, filename):
        with open(filename, 'rb') as f:
            m = hashlib.md5()
            while True:
                data = f.read(self.buffer_size)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()

    def check_folder_new(self):
        self.dublicate_files = set()
        for dirpath, dirnames, filenames in os.walk(self.folder_new):
            # перебрать файлы
            for filename in filenames:
                fileHash = self.get_hash_md5(os.path.join(self.folder_new, filename))
                if fileHash in self.hash_main:
                    self.dublicate_files.add(os.path.join(self.folder_new, filename))

    def check_and_remove_folder_new(self):
        self.dublicate_files = set()
        for dirpath, dirnames, filenames in os.walk(self.folder_new):
            # перебрать файлы
            for filename in filenames:
                fileHash = self.get_hash_md5(os.path.join(self.folder_new, filename))
                if fileHash in self.hash_main:
                    self.remove_dublicate_files(os.path.join(self.folder_new, filename))

    def remove_dublicate_files(self):
        for file in self.dublicate_files:
            os.remove(file)

    def find_dublicate_in_folder(self, folder):
        self.dict_files = {}
        val = []
        for dirpath, dirnames, filenames in os.walk(folder):
            # перебрать файлы
            for filename in filenames:
                file = os.path.join(folder, dirpath)
                file = os.path.join(file, filename)
                fileHash = self.get_hash_md5(file)

                val = self.dict_files.get(fileHash, [])
                val.append(file)
                self.dict_files[fileHash] = val

    def remove_dublicate_in_folder(self):
        for key in self.dict_files:
            if len(self.dict_files.get(key, [])) > 1:
                for file in self.dict_files.get(key, [])[1:]:
                    os.remove(file)
