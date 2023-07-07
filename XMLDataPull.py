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

	#Find The BOM
	for file in os.listdir(source):
		with open("utf32le.file", "rb") as file:
			beginning = file.read(4)
			# The order of these if-statements is important
			# otherwise UTF32 LE may be detected as UTF16 LE as well
			if beginning == b'\x00\x00\xfe\xff':
				print("UTF-32 BE")
			elif beginning == b'\xff\xfe\x00\x00':
				print("UTF-32 LE")
			elif beginning[0:3] == b'\xef\xbb\xbf':
				print("UTF-8")
			elif beginning[0:2] == b'\xff\xfe':
				print("UTF-16 LE")
			elif beginning[0:2] == b'\xfe\xff':
				print("UTF-16 BE")
			else:
				print("Unknown or no BOM")
	for file in os.listdir(result):
		if file.endswith(".xml"):
			doc = open(f"{result}/{file}", encoding='utf-8').read()
			minidom = xml.dom.minidom.parse(f"{result}/{file}")
			# ebb: minidom.parse appears to read in a file path rather than an open file
			print("miniDom parsing: ", minidom)
			print("Sall Good")

			# ebb: I'm sending minidom and g1, as well as the XML document in open read mode so you can experiment with
			# either continuing minidom, or using SaxonC for pulling info for hdf5
			#dumpXML(minidom, g1, doc)

