from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
from Cython.Compiler.Options import get_directive_defaults
directive_defaults = get_directive_defaults() 
directive_defaults['linetrace'] = True
directive_defaults['binding'] = True


# get the annotated file as well
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True

ext_modules = [
    Extension("matMul",
              sources=["matMul.pyx"],
              include_dirs=[numpy.get_include()],
              define_macros=[('CYTHON_TRACE', '1')],
              libraries=[]), 
    
]
setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)

