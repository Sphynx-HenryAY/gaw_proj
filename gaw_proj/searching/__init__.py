from ..searching_settings import *

from ..settings import Rank_Data
from typing import List

from .base_func import perform

def search( 
        kw : "<str> : keyword"
        , num_get : "<int> : target number of result in list" = 20
        , is_indexing : bool = False
        , engine : str = "google"
    ) -> List[ Rank_Data ] :

    if engine == "baidu":
        setting = query_settings.get( "baidu" )
        setting[ "kwa" ][ "wd" ] = kw
    else:
        setting = query_settings.get( "google" )
        setting[ "kwa" ][ "q" ] = setting[ "kwa" ][ "oq" ] = kw

    return perform( kw, num_get, is_indexing, setting, cls.get( engine ) )

