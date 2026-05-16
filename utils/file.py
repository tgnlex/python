import json 
def readonly(filename):
    """Open a file with readonly permissions."""
    with open(filename, "r") as file: 
        return file;

def getFile(filename):
    """Open a file with write permissions."""
    with open(filename, "w") as file:
        return file 

def readFile(filename): 
    """Read content from a file."""
    file = readonly(filename) 
    return file.read()

def readJson(filename):
    """ Read from a json file"""
    data = readFile(filename)
    return json.dumps(data)


def printFile(filename):
    """Read a file and print its content to console"""
    data = readFile(filename)
    return print(data)


def writeFile(filename, data):
    """Write to a file."""
    file = getFile(filename)
    file.write(data)


def writeJson(filename, data):
    """Write to a json file."""
    writeFile(filename, json.dumps(data))
