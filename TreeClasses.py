# Directiry Tree
# RetrO_13th
# github.com/RetrO-13th

import pathlib
import os

class DirectoryTree:
    def __init__(self, dir: str, extention=None, dir_only=False) -> None:
        self.create_tree = _TreeGenerator(dir, extention, dir_only)

    def show(self) -> str:
        tree = self.create_tree.create_tree()

        for dir in tree:
            print(dir)

    @property
    def direction(self):
        return self.create_tree._direction

class _TreeGenerator:

    PIP = "|"
    ELBOW = "└───"
    TEE = "├───"
    PIPE_PREFIX = "|   "
    SPACE_PREFIX = "    "

    def __init__(self, dir: str, extention=None, dir_only=False) -> None:
        self._root_dir = pathlib.Path(dir)
        self._extention = extention
        self._dir_only = dir_only
        self._tree = ["\n"]

    @property
    def _direction(self):
        return f"{self._root_dir}{os.sep}"

    def create_tree(self) -> str:
        self._tree_head()
        self._tree_body(self._root_dir)

        return self._tree

    def _tree_head(self) -> None:
        self._tree.append(self._direction)
        self._tree.append(self.PIP)

    def _tree_body(self, dir: str, prefix="") -> None:
        paths = self._dir_selector(dir)
        paths_len = len(paths)

        for index, path in enumerate(paths):
            connector = self.ELBOW if index == paths_len - 1 else self.TEE

            if path.is_dir():
                self._dir(path, index, paths_len, connector, prefix)
            else:
                self._file(path, connector, prefix)

    def _dir_selector(self, dir: str) -> None:
        paths = dir.iterdir()

        if self._extention is not None:
            paths = self._select_extention(paths)
            return paths
        elif self._dir_only:
            paths = [path for path in paths if path.is_dir()]
            return paths

        return sorted(paths, key=lambda path: path.is_file())

    def _select_extention(self, paths) -> list:
        ex_list = []

        for path in paths:
            if path.is_file() and str(path).endswith(f".{self._extention}"):
                ex_list.append(path)
            elif path.is_dir():
                files = list(pathlib.Path(str(path)).glob(f"*.{self._extention}"))
                if files != []:
                    ex_list.append(path)

        return sorted(ex_list, key=lambda path: path.is_file())

    def _dir(self, path: str, index: int, paths_len: int, connector: str, prefix:str) -> None:
        self._tree.append(f"{prefix}{connector} {path.name}{os.sep}")
        
        if index != paths_len - 1:
            prefix += self.PIPE_PREFIX
        else:
            prefix += self.SPACE_PREFIX

        self._tree_body(path, prefix=prefix)
        self._tree.append(prefix.rstrip())

    def _file(self, path: str, connector: str, prefix: str) -> None:
        self._tree.append(f"{prefix}{connector} {path.name}")
