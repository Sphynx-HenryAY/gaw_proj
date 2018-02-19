from .settings import Rank_Data

def search( 
        kw : "<str> : keyword"
        , num_get : "<int> : target number of result in list" = 20
        , engine: "<str> : search engine with default google" = "google"
    ) -> Rank_Data :
    
    from .searching.google import perform 
    return perform( kw, num_get )

def show(
        rank_data : Rank_Data
        , return_type = None
    ) -> "<str> in json format or joined by new line" :

    from .visualization.pretty_rank_data import prettify
    return prettify( rank_data, return_type )

def web( port = 9999 ):
    from .web_accessing.search_server import start_server
    return start_server( port )
