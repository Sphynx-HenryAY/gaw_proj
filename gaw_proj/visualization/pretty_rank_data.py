from typing import List
from ..settings import Rank_Data


type_print  = "print"
type_join   = "join"
type_json   = "json"
type_web    = "goog"

def prettify(
        rank_data : Rank_Data
        , return_type : "<str> trigger" = None
    ) -> "<str> in json format or joined by new line" :

    return {
        type_print  : print_rank_data
        , type_join : join_rank_data
        , type_json : json_rank_data
        , type_web  : return_search_content
    }.get( return_type, print_rank_data )( rank_data )


def print_rank_data( rank_data : Rank_Data ) -> "<str> print rank_data" :
    connect_rank_data( rank_data, pretty_func = print )


def join_rank_data( rank_data : Rank_Data ) -> "<str> join rank_data" :
    data_list = []
    connect_rank_data( rank_data, pretty_func = data_list.append )

    return "\n".join( data_list )


def connect_rank_data( rank_data : Rank_Data, pretty_func ):

    for data_dict in rank_data:

        pretty_func( data_dict.pop( "title", "TITLE_LOST" ) )

        for k in sorted( data_dict ):
            pretty_func( "%s : %s"%( k, str( data_dict[ k ] ) ) )

        pretty_func( "" )


def json_rank_data( rank_data : Rank_Data ) -> "<str> joined by new line" :

    from json import dumps
    return dumps( rank_data )


def return_search_content( rank_data : Rank_Data ) -> "<str> modified by html tags" :
    for each in rank_data:
        each[ "link" ] = "<a href='%s'>Click</a>"%each[ "link" ]
        each[ "abstract" ] = each[ "abstract" ]

    return join_rank_data( rank_data ).replace( "\n", "<br/>" )

