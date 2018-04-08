from urllib.request import urlopen, Request
from urllib.parse import urlencode

from collections import Counter

import json
from bs4 import BeautifulSoup

from typing import List

from ..settings import Rank_Data
from ..settings.searching import *

def get_rank( 
        rank_data : Rank_Data
        , page_ctt : "<str> : decoded 'page content' return from website"
        , is_indexing : bool = False
        , ctt_cls = None
        , special_func = {}
    ) -> "<str> DUPL : existing record signal" or "<int> 0 : normal exit" :

    start_index = len( rank_data )

    s = BeautifulSoup( page_ctt, bs_parser_lib )
    blk_tag, blk_cls = ctt_cls.get( "ctt_block" )
    abst_tag, abst_cls = ctt_cls.get( "ctt_abstract" )
    ttl_tag, ttl_cls = ctt_cls.get( "ctt_title" )
    link_tag, link_cls = ctt_cls.get( "ctt_link" )

    for ctt_block in s.find_all( blk_tag, class_ = blk_cls ):
        b = ctt_block

        abstract = b.find( abst_tag, class_ = abst_cls )
        abstract = abstract.text if abstract else "__NO_ABSTRACT__"

        if is_indexing:
            if abstract == "__NO_ABSTRACT__":
                continue

            abstract = Counter( abstract.lower().split( " " ) )
            for e in base_rvs_kws:
                abstract.pop( e, 0 )

        title = b.find( ttl_tag, class_ = ttl_cls )
        title = title.text if title else "__NO_TITLE__"

        data = {
            "rank" : len( rank_data )
            , "title" : title
            , "link" : b.a.attrs.get( "href")
            , "abstract" : abstract
        }

        
        for each in set( special_func ) & set( data ):
            special_result = special_func[ each ]( ctt_block )
            data[ each ] = special_result if special_result else data[ each ]

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
        , query_ele = None
        , cls = None
        , special_func = {}
    ) -> Rank_Data :

    if not query_ele:
        raise Exception( "Please assign a query_ele" )

    query_url = query_ele.get( "url", "" )
    query_kwa = query_ele.get( "kwa", {} )

    begin_wd  = query_ele.get( "begin_wd", "" )

    req = Request( query_url + urlencode( query_kwa ), headers = headers )
    page_ctt = urlopen( req ).read().decode( "utf8" )

    rank_data = []
    get_rank( rank_data, page_ctt, is_indexing, cls, special_func )

    while len( rank_data ) < num_get:
        query_kwa.update( { begin_wd : len( rank_data ) } )

        req = Request( query_url + urlencode( query_kwa ), headers = headers )
        page_ctt = urlopen( req ).read().decode( "utf8" )

        exit_code = get_rank( rank_data, page_ctt, is_indexing, cls, special_func )

        if exit_code and exit_code in [ "END", "DUPL" ]:
            break

    return rank_data[ : num_get ]


