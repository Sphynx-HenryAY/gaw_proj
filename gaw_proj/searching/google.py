from urllib.request import urlopen, Request
from urllib.parse import urlencode

from collections import Counter

from bs4 import BeautifulSoup

from ..ctt_cls_name import google_cls
from ..settings import headers, bs_parser_lib, Rank_Data


def google_get_rank( 
        page_ctt : "<str> : decoded 'page content' return from website"
        , rank_data : Rank_Data = []
        , is_indexing : bool = False
    ) -> "<str> DUPL : existing record signal" or "<int> 0 : normal exit" :

    start_index = len( rank_data )

    s = BeautifulSoup( page_ctt, bs_parser_lib )
    for ctt_block in s.find_all( "div", class_ = google_cls.get( "ctt_blk", "rc" ) ):
        b = ctt_block

        abstract = b.find_all( "span", class_ = google_cls.get( "ctt_abst", "st" ) )
        abstract = abstract[ 0 ].text if abstract else "__NO_ABSTRACT__"

        if is_indexing:
            abstract = Counter( abstract.lower().replace( "\"", "" ).replace( ".", "" ).replace( ",", "" ).split( " " ) )

        data = {
            "rank" : len( rank_data )
            , "title" : b.a.contents[ 0 ]
            , "link" : b.a.attrs.get( "href")
            , "abstract" : abstract
        }

        if data not in rank_data:
            rank_data.append( data )
        else:
            return "DUPL"

    if len( rank_data ) == start_index:
        return "END"

    return 0


def perform( 
        kw : "<str> : keyword"
        , num_get : "<int> : target number of result in list" = 20
        , is_indexing : bool = False
    ) -> Rank_Data :

    gs_url = "https://www.google.com.hk/search?"
    gs_kwa = { 
        "ie" : "UTF-8" 
        , "q" : kw
        , "hl" : "en"
    }
    rank_data = []


    req = Request( gs_url + urlencode( gs_kwa ), headers = headers )
    page_ctt = urlopen( req ).read().decode( "utf8" )

    google_get_rank( page_ctt, rank_data, is_indexing )


    while len( rank_data ) < num_get:
        gs_kwa.update( { "start" : len( rank_data ) } )

        req = Request( gs_url + urlencode( gs_kwa ), headers = headers )
        page_ctt = urlopen( req ).read().decode( "utf8" )

        exit_code = google_get_rank( page_ctt, rank_data, is_indexing )

        if exit_code and exit_code in [ "END", "DUPL" ]:
            break

    return rank_data[ : num_get ]


