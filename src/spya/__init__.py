from spya import filesystem as fs

def paths(path, *pathnames):
    """Concatenate and return paths."""
    return fs.paths(path, *pathnames)

def exists(path):
    """Returns whether the path exists."""
    return fs.exists(path)

def isfile(path):
    """Returns whether the path is a file."""
    return fs.isfile(path)

def isdir(path):
    """Returns whether the path is a directory."""
    return fs.isdir(path)

def dirname(path):
    """Returns the directory component of a pathname."""
    return fs.dirname(path)

def basename(filepath):
    """Returns the final component of a pathname."""
    return fs.basename(filepath)

def filename(filepath):
    """Returns the final component of a filename."""
    return fs.filename(filepath)

def extension(filepath):
    """Returns the final component of a file extension."""
    return fs.extension(filepath)

def getsize(filepath):
    """Return the size of a file."""
    return fs.getsize(filepath)
