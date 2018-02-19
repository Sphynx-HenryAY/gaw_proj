

from typing import List, Dict


bs_parser_lib = "html5lib"

headers = {
    "user-agent" : "Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.89 Safari/537.36"
    , "charset" : "utf-8"
}


Rank_Data = List[ Dict[ str, str ] ]
rank_data = {
    "rank" : int
    , "title" : str
    , "link" : str
    , "abstract" : str
}
