
import sys
from plasTeX.TeX import TeX

#from plasTeX.Renderers.XHTML import Renderer
#Renderer().render(TeX(file=sys.argv[-1]).parse())

doc = TeX()

doc.input(open(sys.argv[-1], 'r'))

for i in doc:
    print i
    

#doc = TeX(file=sys.argv[-1]).parse()

#tex = TeX()
#tex.input(open('foo.tex','r'))
#for token in tex:
#    print token

        
