from os import path as op

def paths(path, *pathnames):
    """
    Join two or more pathname components, inserting '/' as needed.
    If any component is an absolute path, all previous path components
    will be discarded.  An empty last part will result in a path that
    ends with a separator.
    """
    return op.join(path, *pathnames)

def exists(path):
    """
    Test whether a path exists.  Returns False for broken symbolic links.
    """
    return op.exists(path)

def isfile(path):
    """
    Test whether a path is a regular file.
    """
    return op.isfile(path)

def isdir(path):
    """
    Return true if the pathname refers to an existing directory.
    """
    return op.isdir(path)

def dirname(path):
    """
    Returns the directory component of a pathname.
    """
    return op.dirname(path)

def basename(filepath):
    """
    Returns the final component of a pathname.
    """
    return op.basename(filepath)

def filename(filepath):
    """
    Returns the final component of a filename.
    """
    basename = op.basename(filepath)
    return op.splitext(basename)[0]

def extension(filepath):
    """
    Returns the final component of a file extension.
    """
    basename = op.basename(filepath)
    return op.splitext(basename)[1]

def getsize(filepath):
    """
    Return the size of a file.
    """
    return op.getsize(filepath)
