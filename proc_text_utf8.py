# encoding: utf8
from stanford_corenlp_pywrapper.sockwrap import SockWrap

proc = SockWrap("ssplit")
print(proc.parse_doc(u"Ivan Meštrović"))