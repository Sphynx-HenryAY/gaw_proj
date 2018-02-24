from typing import List
from ..settings import Rank_Data


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


def return_search_content( rank_data : List[ Rank_Data ] ) -> "<str> modified by html tags" :
    for each in rank_data:
        each[ "link" ] = "<a href='%s'>Click</a>"%each[ "link" ]

    return join_rank_data( rank_data ).replace( "\n", "<br/>" )

