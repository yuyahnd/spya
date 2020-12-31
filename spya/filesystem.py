import os

def paths(path, *pathnames):
    """
    Join two or more pathname components, inserting '/' as needed.
    If any component is an absolute path, all previous path components
    will be discarded.  An empty last part will result in a path that
    ends with a separator.
    """
    return os.path.join(path, *pathnames)

def exists(path):
    """
    Test whether a path exists.  Returns False for broken symbolic links.
    """
    return os.path.exists(path)

def isfile(path):
    """
    Test whether a path is a regular file.
    """
    return os.path.isfile(path)

def isdir(path):
    """
    Return true if the pathname refers to an existing directory.
    """
    return os.path.isdir(path)

def dirname(path):
    """
    Returns the directory component of a pathname.
    """
    return os.path.dirname(path)

def basename(filepath):
    """
    Returns the final component of a pathname.
    """
    return os.path.basename(filepath)

def filename(filepath):
    """
    Returns the final component of a filename.
    """
    basename = os.path.basename(filepath)
    return os.path.splitext(basename)[0]

def extension(filepath):
    """
    Returns the final component of a file extension.
    """
    basename = os.path.basename(filepath)
    return os.path.splitext(basename)[1]
