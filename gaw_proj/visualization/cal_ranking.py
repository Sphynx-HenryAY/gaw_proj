from collections import Counter

from functools import reduce

from ..tmpl import struc_tmpl, data_tmpl

from ..settings.searching import base_rvs_kws

from ..settings import Rank_Data
from typing import List, Dict

def render_content( tmpl, ctx ):
    render_mark = "{{ %s }}"

    for k in ctx:
        tmpl = tmpl.replace( render_mark % k, str( ctx.get( k ) ) )

    return tmpl

# Counter data was saved at abstract in rank data
def render_ranking_content(
        rank_data_list : List[ Rank_Data ]
        , num_get : int = None
        , rvs_kws : List[ str ] = []
    ) -> str:

    num_get = num_get if num_get else len( rank_data_list )

    total_abstract = reduce( lambda x, y: x + y, [ e[ "abstract" ] for e in rank_data_list ] )
    for e in base_rvs_kws + rvs_kws:
        total_abstract.pop( e, 0 )

    total_most_common = total_abstract.most_common( num_get )


    ctt_list = []
    for each in rank_data_list:

        each[ "struc" ] = render_content( struc_tmpl, { "link" : each[ "link" ] } )


        for e in base_rvs_kws + rvs_kws:
            each[ "abstract" ].pop( e, 0 )

        kw_ranking_data = []
        for word, _ in total_most_common:
        
            kw_ranking_data.append( render_content(
                data_tmpl 
                , { "kw" : word
                    , "score" : each[ "abstract" ].get( word, 0 )
                }
            ) )

        ctt_list.append( render_content( each[ "struc" ], { "kw_ranking_data" : ",".join( kw_ranking_data ) } ) )

    return ",".join( ctt_list )

