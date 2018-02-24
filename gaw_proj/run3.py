from .settings import Rank_Data
from typing import List

def search_func( 
        kw : "<str> : keyword"
        , num_get : "<int> : target number of result in list" = 20
        , is_indexing : bool = False
        , engine: "<str> : search engine with default google" = "google"
    ) -> List[ Rank_Data ] :

    from .searching import search
    return search( kw, num_get, is_indexing, engine )

def show_func(
        rank_data : Rank_Data
        , return_type = None
    ) -> "<str> in json format or joined by new line" :

    from .visualization import prettify
    return prettify( rank_data, return_type )

def render_rank_func(
        rank_data_list : List[ Rank_Data ]
        , num_get : int = None
        , rvs_kws : List[ str ] = []
    ) -> str:
    
    from .visualization.cal_ranking import render_ranking_content
    return render_ranking_content( rank_data_list, num_get, rvs_kws )

def website_func( port = 9999 ):
    from .web_accessing.search_server import start_server
    return start_server( port )
