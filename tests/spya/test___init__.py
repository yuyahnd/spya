import spya
from os import path as op

def test_paths():
    path = spya.paths('.', 'tests')
    assert path == '.' + op.sep + 'tests'

def test_exists():
    assert True == spya.exists(__file__)

def test_isfile():
    assert True == spya.isfile(__file__)

def test_isdir():
    dirname = spya.dirname(__file__)
    assert True == spya.isdir(dirname)

def test_dirname():
    dirname = op.dirname(__file__)
    assert dirname == spya.dirname(__file__)

def test_basename():
    assert 'test___init__.py' == spya.basename(__file__)

def test_filename():
    assert 'test___init__' == spya.filename(__file__)

def test_extension():
    assert '.py' == spya.extension(__file__)

def test_getsize():
    assert spya.getsize(__file__) is not None
