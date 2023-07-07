import xml.dom.minidom
import os
from saxonche import PySaxonProcessor


with PySaxonProcessor(license=False) as proc:
	print(proc.version)
	xsltproc = proc.new_xslt30_processor()
	source = "data"
	xslt = "DataXSLT.xsl"
	result = "output"
	output = xsltproc.transform_to_file(source_file=source, stylesheet_file=xslt, output_file=result)

	for file in os.listdir(result):
		if file.endswith(".xml"):
			doc = open(f"{result}/{file}", encoding='utf-8').read()
			minidom = xml.dom.minidom.parse(f"{result}/{file}")
			# ebb: minidom.parse appears to read in a file path rather than an open file
			print(doc)
			print("miniDom parsing: ", minidom)

