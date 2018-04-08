from urllib.request import *
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from gaw_proj.settings.searching import shortcuts as sc
from gaw_proj.settings.searching import *
from gaw_proj.settings import *
engine = default_search_engine
#engine = "baidu"
def get_bs( kw, engine ):
    qs = sc[ engine ].settings[ "query" ]
    if engine == "baidu":
        qs[ "kwa" ][ "wd" ] = kw
    else:
        qs[ "kwa" ][ "oq" ] = qs[ "kwa" ][ "q" ] = kw
    print( qs )
    req = Request( qs[ "url" ] + urlencode( qs[ "kwa" ] ), headers=headers )
    page_ctt = urlopen( req ).read().decode( "utf8" )
    return BeautifulSoup( page_ctt, bs_parser_lib )


ctt_cls = sc[ engine ].settings[ "cls" ]
blk_tag, blk_cls = ctt_cls.get( "ctt_block" )
abst_tag, abst_cls = ctt_cls.get( "ctt_abstract" )
ttl_tag, ttl_cls = ctt_cls.get( "ctt_title" )
link_tag, link_cls = ctt_cls.get( "ctt_link" )
blocks = get_bs( "python", engine ).find_all( blk_tag, class_ = blk_cls )


