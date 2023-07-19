# SaxonXML

## Process
When the python script 'XMLDataPull.py' is run, it should:
1. Create a SaxonC XSLT Processor
1. Transform all the XML from 'Data' directory
1. Output new XML in 'output' directory

## Error

However, the current code does not work with the SaxonC-HE 12.3.0 library. It returns the error

```
Error on line 1 column 1 of data:
  SXXP0003   Error reported by XML parser: Content is not allowed in prolog.: Content is not
  allowed in prolog.
Traceback (most recent call last):
  File "C:\Users\still\Documents\GitHub\SaxonXML\XMLDataPull.py", line 12, in <module>
    output = xsltproc.transform_to_file(source_file=source, stylesheet_file=xslt, output_file=result)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "python_saxon\saxonc.pyx", line 1300, in saxonche.PyXslt30Processor.transform_to_file
saxonche.PySaxonApiError: org.xml.sax.SAXParseException; systemId: file:///C:/Users/still/Documents/GitHub/SaxonXML/data; lineNumber: 1; columnNumber: 1; Content is not allowed in prolog.. Line number: -1
```

The line that is producing the error: 
```python
output = xsltproc.transform_to_file(source_file=source, stylesheet_file=xslt, output_file=result)
```
This can be worked around by using the SaxonC-HE 12.0.0 library.


## Solution

The line that produced the error: 
```python
output = xsltproc.transform_to_file(source_file=source, stylesheet_file=xslt, output_file=result)
```

In SaxonC-HE 12.1-12.3, the `transform_to_file()` function was changed in how it worked. The function does not require a source document as an arguement. The XSLT developed for this repo specifies a collection of XML documents in a directory, so removing a source arguement meant it could still be found by the XSLT. However, the XSLT run through SaxonC-HE 12.3 (in contrast to oXygen) was attempting to feed the function a directory. This would not return an error, but instead return a `NoneType` object.

The solution we found was to use another function other than `transform_to_file()`. The solution we found was to replace `output = xsltproc.transform_to_file(source_file=source, stylesheet_file=xslt, output_file=result)` with the current code:
```python
executable = xsltproc.compile_stylesheet(stylesheet_file=xslt)
print(type(executable))
# With compile_stylesheet() we get a PyXSLTExecutable object and can do more with that using advanced Saxon features
executable.set_initial_match_selection(file_name="data/data.xml")
# set a dummy file here, but it does have to be a well-formed XML document
executable.apply_templates_returning_value(base_output_uri=Path('.', result, 'output').absolute().as_uri())
# See examples at https://www.saxonica.com/saxon-c/documentation12/index.html#!samples/samples_python
```
This code also prevents a need for the XSLT to be changed.
