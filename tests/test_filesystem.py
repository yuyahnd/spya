from spya import filesystem as fs
import os

def test_paths():
    path = fs.paths('.', 'tests')
    assert path == '.' + os.path.sep + 'tests'

def test_exists():
    assert True == fs.exists(__file__)

def test_isfile():
    assert True == fs.isfile(__file__)

def test_isdir():
    dirname = fs.dirname(__file__)
    assert True == fs.isdir(dirname)

def test_dirname():
    dirname = os.path.dirname(__file__)
    assert dirname == fs.dirname(__file__)

def test_basename():
    assert 'test_filesystem.py' == fs.basename(__file__)

def test_filename():
    assert 'test_filesystem' == fs.filename(__file__)

def test_extension():
    assert '.py' == fs.extension(__file__)
