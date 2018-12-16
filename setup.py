

from distutils.core import setup
from Cython.Build import cythonize


if __name__ == '__main__':
    setup(name='app', ext_modules=cythonize("module.pyx"))
