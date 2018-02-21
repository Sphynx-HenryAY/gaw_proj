from typing import List, Dict
from ..settings import Rank_Data, base_rvs_kws
from ..tmpl import struc_tmpl, data_tmpl

from . import render_content

from collections import Counter

from functools import reduce

# abstract is sizable, multi-processing could be applied
# the resulting Counter obj is so powerful and can be accumulated!
def indexing( abstract: str, rvs_kws : List[ str ] ) -> Dict[ str, int ]:
    word_occ = Counter( abstract.split( " " ) )
    for kw in rvs_kws:
        word_occ.pop( kw )

    return word_occ

# Counter data was saved at abstract in rank data
def render_ranking_content(
        rank_data_list : List[ Rank_Data ]
        , get_num : int
        , rvs_kws : List[ str ] = None
    ) -> str:


    ctt_list = []


    total_abstract = reduce( lambda x, y: x + y, [ e[ "abstract" ] for e in rank_data_list ] )
    for e in base_rvs_kws + rvs_kws:
        total_abstract.pop( e, 0 )

    total_most_common = total_abstract.most_common( get_num )


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

