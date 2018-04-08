from ..settings.searching import shortcuts as sc

from ..settings import Rank_Data
from typing import List

from .base_func import perform

def search( 
        kw : "<str> : keyword"
        , num_get : "<int> : target number of result in list" = 20
        , is_indexing : bool = False
        , engine : str = "google"
    ) -> List[ Rank_Data ] :

    query = sc[ engine ].settings[ "query" ]

    if engine == "baidu":
        query[ "kwa" ][ "wd" ] = kw
    else:
        query[ "kwa" ][ "q" ] = query[ "kwa" ][ "oq" ] = kw

    return perform(
        kw
        , num_get
        , is_indexing
        , query
        , sc[ engine ].settings[ "cls" ]
        , sc[ engine ].settings.get( "special", {} )
    )

