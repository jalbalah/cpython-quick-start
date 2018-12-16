# cpython-quick-start
Basic script to compile Python code into optimized c++ code

module.pyx  --  includes all the Python code to compile into C++ code
build.sh    --  script that builds module.pyx so you can call `from module import <function/etc.>`
setup.py    --  build file
test.py     --  runs profiling


<br/><br/>
WINDOWS:
Make sure you install the correct version of visual studio
To determine which VS version: run `python`
<br/> See: https://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat
