# cpython-quick-start
```
./build.sh
```
```
python test.py
```

# Overview

Basic script to compile Python code into optimized c++ code
<br/>module.pyx  --  includes all the Python code to compile into C++ code
<br/>build.sh    --  script that builds from module.pyx so you can call `from module import <function/etc.>`
<br/>setup.py    --  build file
<br/>test.py     --  runs profiling


<br/><br/>
WINDOWS:
Make sure you install the correct version of visual studio
To determine which VS version:
```
python
```
e.g. 
```
python
Python 3.5.6 |Anaconda, Inc.| (default, Aug 26 2018, 16:05:27) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Check the version listed, then download the according VS version:
```
MSC v.1000 -> Visual C++ 4.x        
MSC v.1100 -> Visual C++ 5          
MSC v.1200 -> Visual C++ 6          
MSC v.1300 -> Visual C++ .NET       
MSC v.1310 -> Visual C++ .NET 2003  
MSC v.1400 -> Visual C++ 2005  (8.0)
MSC v.1500 -> Visual C++ 2008  (9.0)
MSC v.1600 -> Visual C++ 2010 (10.0)
MSC v.1700 -> Visual C++ 2012 (11.0)
MSC v.1800 -> Visual C++ 2013 (12.0)
MSC v.1900 -> Visual C++ 2015 (14.0)
MSC v.1910 -> Visual C++ 2017 (15.0)
MSC v.1911 -> Visual C++ 2017 (15.3)
MSC v.1912 -> Visual C++ 2017 (15.5)
MSC v.1913 -> Visual C++ 2017 (15.6)
MSC v.1914 -> Visual C++ 2017 (15.7)
MSC v.1915 -> Visual C++ 2017 (15.8)
MSC v.1916 -> Visual C++ 2017 (15.9)  
```
<br/> See: https://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat
