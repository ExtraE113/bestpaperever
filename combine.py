from PyPDF2 import PdfFileMerger

pdfs = ['Sigbovik_22.pdf', 'page0.pdf', 'page1.pdf', 'page2.pdf', 'page3.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
	merger.append(pdf)

merger.write("result.pdf")
merger.close()
