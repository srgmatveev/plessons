from analyzer.i_clone_repo import iCloneRepo
import os
import shutil
from git import Repo


class CloneGitHub(iCloneRepo):

    def __init__(self, from_url=None, to_path=None):
        self.from_url = from_url
        self.to_path = to_path
        self.init_dir_path()
        self.init_catalog_to_copy_git(path=self.to_path)

    def init_dir_path(self):
        if self.to_path is None or not self.to_path:
            dir_name = 'tmp'
            self.to_path = os.path.abspath(dir_name)
        else:
            self.to_path = os.path.abspath(self.to_path)

    @staticmethod
    def init_catalog_to_copy_git(path=None):
        '''Recreate dir where copy repo'''
        if os.path.isdir(path):
            shutil.rmtree(path)
        os.mkdir(path)

    def clone(self):
        return Repo.clone_from(self.from_url, self.to_path)
