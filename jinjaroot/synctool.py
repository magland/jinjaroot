import os

class FileGroup:
    def __init__(self, file_name: str):
        self._file_name = file_name
        self._file_paths = []
        self._distinct_file_groups = []
    def add_file(self, file_path: str):
        self._file_paths.append(file_path)
        found = False
        for g in self._distinct_file_groups:
            if _has_same_content(g[0], file_path):
                g.append(file_path)
                found = True
                break
        if not found:
            self._distinct_file_groups.append([file_path])
        if len(self._distinct_file_groups) == 0:
            self._distinct_file_groups.append([self._])
    def num_files(self):
        return len(self._file_paths)
    def num_distinct_file_groups(self):
        return len(self._distinct_file_groups)
    def display(self):
        print('==============================================================')
        print(self._file_name)
        for g in self._distinct_file_groups:
            print('****************************************************')
            for p in g:
                print(p)
        print('==============================================================')
        print('')

def _has_same_content(path1: str, path2: str):
    with open(path1, 'r') as f:
        c1 = f.read()
    with open(path2, 'r') as f:
        c2 = f.read()
    return c1 == c2

class SyncTool:
    def __init__(self):
        self._file_groups = {}
    def scan_dir(self, dirpath: str):
        fnames = os.listdir(dirpath)
        for fname in fnames:
            if not _excluded(fname):
                file_path = f'{dirpath}/{fname}'
                if os.path.isfile(file_path):
                    if fname.endswith('.j2') or (os.path.isfile(file_path + '.sync')):
                        if fname not in self._file_groups:
                            self._file_groups[fname] = FileGroup(fname)
                        self._file_groups[fname].add_file(file_path)
                elif os.path.isdir(file_path):
                    if fname == '.jinjaroot':
                        self.scan_jinjaroot_dir(dirpath=file_path, relpath='.jinjaroot')
                    else:
                        self.scan_dir(file_path)
    def scan_jinjaroot_dir(self, dirpath: str, relpath: str):
        fnames = os.listdir(dirpath)
        for fname in fnames:
            if not _excluded(fname):
                file_path = f'{dirpath}/{fname}'
                name = relpath + '/' + fname
                if os.path.isfile(file_path):
                    if name not in self._file_groups:
                        self._file_groups[name] = FileGroup(name)
                    self._file_groups[name].add_file(file_path)
                elif os.path.isdir(file_path):
                    self.scan_jinjaroot_dir(dirpath=file_path, relpath=name)
    def report(self):
        file_group_names = sorted(list(self._file_groups.keys()))
        for name in file_group_names:
            g: FileGroup = self._file_groups[name]
            if g.num_distinct_file_groups() > 1:
                g.display()

def _excluded(fname):
    return fname in ['__pycache__', 'node_modules', '.git']

def synctool():
    s = SyncTool()
    s.scan_dir('.')
    s.report()
