"""quick test to see if we can read Illustrator files"""

import os
from collections import Counter
from minecart import Document, Shape


pdfpath = os.path.join(os.path.dirname(__file__), 'ai-files-are-pdfs.ai')
doc = Document(open(pdfpath, 'rb'))
page = doc.get_page(0)


shapes = page.shapes
print len(shapes), 'shapes'

counter = Counter(tuple(shape.fill.color.as_rgb()) for shape in shapes)
print 'by fill color:', ', '.join('%d rbg%s' % (v,k) for k,v in counter.iteritems())

