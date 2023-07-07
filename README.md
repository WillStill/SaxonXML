# SaxonXML

## Process
When the python script 'XMLDataPull.py' is run, it should:
1. Create a SaxonC XSLT Processor
1. Transform all the XML from 'Data' directory
1. Output new XML in 'output' directory
1. and Find any BOM from the source XML files

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
