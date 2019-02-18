import pytest
import os
import shutil

from analyzer import clone_github as gh


@pytest.fixture(scope='function')
def resources_setup(request):
    from_url = 'https://github.com/srgmatveev/kud'
    to_path = 'lalala'
    git_hub = gh.CloneGitHub(from_url=from_url, to_path=to_path)
    def teardown_sub():
        if os.path.isdir(os.path.abspath(to_path)):
            shutil.rmtree(os.path.abspath(to_path))
    request.addfinalizer(teardown_sub)
    return git_hub


def test_github_init_dir_path(resources_setup):
    g_h = resources_setup
    g_h.init_dir_path()
    assert g_h.to_path ==  os.path.abspath(g_h.to_path)
    g_h.to_path = None
    g_h.init_dir_path()
    assert g_h.to_path ==  os.path.abspath('tmp')

def test__github_init_copy_dir1():
    to_path = os.path.abspath('tmp')
    if os.path.isdir(to_path):
        shutil.rmtree(to_path)
    gh.CloneGitHub.init_catalog_to_copy_git(path=to_path)
    assert os.path.isdir(to_path) == True
    shutil.rmtree(to_path)

def test_github_init_copy_dir2():
    to_path = os.path.abspath('/tata')
    with pytest.raises(Exception):
        gh.CloneGitHub.init_catalog_to_copy_git(path=to_path)
    

def test_clone_from_git_hub(resources_setup):
    g_h =resources_setup
    tmp_str = str(g_h.clone())
    assert '<git.Repo' in tmp_str
    assert f'{g_h.to_path}' in tmp_str