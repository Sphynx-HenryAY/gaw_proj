from ..settings import Rank_Data
from .pretty_rank_data import *
from .cal_ranking import render_ranking_content


type_print  = "print"
type_join   = "join"
type_json   = "json"
type_search = "search"
type_rank   = "rank"

def prettify(
        rank_data : Rank_Data
        , return_type : "<str> trigger" = None
    ) -> str :

    return {
        type_print      : print_rank_data
        , type_join     : join_rank_data
        , type_json     : json_rank_data
        , type_search   : return_search_content
        , type_rank     : render_ranking_content
    }.get( return_type, print_rank_data )( rank_data )
