from urllib.request import urlopen, Request
from urllib.parse import urlencode

from collections import Counter

import json
from bs4 import BeautifulSoup

from typing import List
from ..settings import Rank_Data

from ..searching_settings import *

def get_rank( 
        page_ctt : "<str> : decoded 'page content' return from website"
        , rank_data : Rank_Data
        , is_indexing : bool = False
        , ctt_cls = None
    ) -> "<str> DUPL : existing record signal" or "<int> 0 : normal exit" :

    start_index = len( rank_data )

    s = BeautifulSoup( page_ctt, bs_parser_lib )
    blk_tag, blk_cls = ctt_cls.get( "ctt_block" )
    abst_tag, abst_cls = ctt_cls.get( "ctt_abstract" )
    ttl_tag, ttl_cls = ctt_cls.get( "ctt_title" )
    link_tag, link_cls = ctt_cls.get( "ctt_link" )

    for ctt_block in s.find_all( blk_tag, class_ = blk_cls ):
        b = ctt_block

        abstract = b.find_all( abst_tag, class_ = abst_cls )
        abstract = abstract[ 0 ].text if abstract else "__NO_ABSTRACT__"

        if is_indexing:

            if abstract == "__NO_ABSTRACT__":
                continue

            abstract = Counter( abstract.lower().split( " " ) )
            for e in base_rvs_kws:
                abstract.pop( e, 0 )

        title = b.find_all( ttl_tag, class_ = ttl_cls )
        link = b.attrs.get( "data-log" )
        link = json.loads( link.replace( "'", '"' ) ).get( "mu", "" ) if link else b.a.attrs.get( "href")

        data = {
            "rank" : len( rank_data )
            , "title" : title[ 0 ].text if title else "__NO_TITLE__"
            , "link" : link
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
        , query_setting = None
        , cls = None
    ) -> Rank_Data :

    if not query_setting:
        raise Exception( "Please assign a query_setting" )

    query_url = query_setting.get( "url", "" )
    query_kwa = query_setting.get( "kwa", {} )

    begin_wd  = query_setting.get( "begin_wd", "" )

    req = Request( query_url + urlencode( query_kwa ), headers = headers )
    page_ctt = urlopen( req ).read().decode( "utf8" )


    rank_data = []
    get_rank( page_ctt, rank_data, is_indexing, cls )

    while len( rank_data ) < num_get:
        query_kwa.update( { begin_wd : len( rank_data ) } )

        req = Request( query_url + urlencode( query_kwa ), headers = headers )
        page_ctt = urlopen( req ).read().decode( "utf8" )

        exit_code = get_rank( page_ctt, rank_data, is_indexing, cls )

        if exit_code and exit_code in [ "END", "DUPL" ]:
            break

    return rank_data[ : num_get ]


