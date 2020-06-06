import os

class FileHandler :
    def __init__(self) :
        pass

    def read(self, filename) :
        cwd = os.getcwd()
        data_path = os.path.abspath(os.path.join(cwd, os.pardir, 'test'))
        filename_path = os.path.join(data_path, filename + '.txt')
        f = open(filename_path, 'r')
        container = []
        text = f.readlines()
        for i in range(len(text)) :
            line = text[i].strip('\n').split(' ')
            for j in range(len(line)) :
                if (line[j] == '#') :
                    line[j] = 0
                else :
                    line[j] = int(line[j])
            container.append(line)
        f.close()
        return container

    def write(self, filename, text) :
        cwd = os.getcwd()
        data_path = os.path.abspath(os.path.join(cwd, os.pardir, 'result'))
        filename_path = os.path.join(data_path, filename + '.txt')
        f = open(filename_path, 'w')
        f.write(text)
        f.close()