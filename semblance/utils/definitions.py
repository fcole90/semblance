import os

workDirectoryName = 'semblance-workdir'
resourcesDirectoryName = 'resources'

workDirectory = os.path.join(os.path.expanduser('~'), workDirectoryName)
resourcesDirectory = os.path.join(workDirectory, resourcesDirectoryName)
