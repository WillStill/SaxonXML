import os
import xml.dom.minidom
from pathlib import Path

from saxonche import PySaxonProcessor

with PySaxonProcessor(license=False) as proc:
	print(proc.version)
	xsltproc = proc.new_xslt30_processor()
	source = "data"
	xslt = "DataXSLT.xsl"
	result = "output"
	executable = xsltproc.compile_stylesheet(stylesheet_file=xslt)
	print(type(executable))
	# With compile_stylesheet() we get a PyXSLTExecutable object and can do more with that using advanced Saxon features
	executable.set_initial_match_selection(file_name="data/data.xml")
	# set a dummy file here, but it does have to be a well-formed XML document
	executable.apply_templates_returning_value(base_output_uri=Path('.', result, 'output').absolute().as_uri())
	# See examples at https://www.saxonica.com/saxon-c/documentation12/index.html#!samples/samples_python

	for file in os.listdir(result):
		if file.endswith(".xml"):
			doc = open(f"{result}/{file}", encoding='utf-8').read()
			minidom = xml.dom.minidom.parse(f"{result}/{file}")
			# ebb: minidom.parse appears to read in a file path rather than an open file
			print(doc)
			print("miniDom parsing: ", minidom)

