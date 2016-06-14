"""Downloader to retrieve useful resources."""
import os
import urllib.request

from utils import definitions


class Downloader:
    """Downloads resources in the appropriate folders"""

    def get(self, url=None, directory=None, filename=None):
        """
        Retrieves a resource and saves it.

        Retrieves a resource at the specified url and saves it in the given
        location.
        """

        if not os.path.isdir(directory):
            raise NotADirectoryError("'" + directory + "' does not exists")

        if os.path.exists(os.path.join(directory, filename)):
            raise FileExistsError("'" + filename + "' already exists")

        return urllib.request.urlretrieve(url, os.path.join(directory, filename))


class MovielensDownloader(Downloader):
    """Specialised downloader for the Movielens dataset"""

    baseUrl = 'http://files.grouplens.org/datasets/movielens/'

    sizes = {
        '100K': 'ml-100k.zip',
        '1M': 'ml-1m.zip',
        '10M': 'ml-10m.zip',
        '20M': 'ml-20m.zip'
    }

    url = None
    fileName = None

    def setsize(self, size):
        """Sets the size and initialises the url and fileName values."""
        if size not in self.sizes:
            raise ValueError("'" + size + "' is not acceptable. Acceptable: " + str(self.sizes.keys()))
        else:
            self.fileName = self.sizes[size]
            self.url = self.baseUrl + self.fileName

    def __init__(self, size=None):
        """Initializer"""
        if not size:
            size = '1M'

        self.setsize(size)

    def get(self, url=None, directory=None, filename=None):
        """Retrieves the movielens dataset and saves it among the resources"""
        super(MovielensDownloader, self).get(self.url, definitions.resourcesDirectory, self.fileName)
