from distutils.core import setup, Extension
import numpy.distutils.misc_util

# Adding OpenCV to project
# ************************

# Adding sources of the project
# *****************************

SOURCES = ["../cpp_utils/cloud/cloud.cpp",
             "neighbors/neighbors.cpp",
             "wrapper.cpp"]

module = Extension(name="radius_neighbors",
                    sources=SOURCES)


setup(ext_modules=[module], include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs())








