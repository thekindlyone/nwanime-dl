# # coding: utf-8
import pickle
table=pickle.load(open('mirror_table.p'))
html='''<ol>{}</ol>'''.format('\n'.join(['''<li><a href="{}">{}</a></li>'''.format(v,k) for k,v in table.items()]))
open('table.html','w').write(html)

