
import sys
from plasTeX.TeX import TeX

#from plasTeX.Renderers.XHTML import Renderer
#Renderer().render(TeX(file=sys.argv[-1]).parse())

doc = TeX(file=sys.argv[-1]).parse()
for i in doc:
    print i



  tex = TeX()
    tex.input(open('foo.tex','r'))
    for token in tex:
        print token

        
