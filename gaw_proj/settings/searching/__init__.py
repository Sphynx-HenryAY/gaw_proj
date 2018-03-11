from . import baidu, google

bs_parser_lib = "html5lib"

headers = {
    "user-agent" : "Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.89 Safari/537.36"
    , "charset" : "utf-8"
}

base_rvs_kws = [ "to","and","a","is","for","in","of","the","your"
    ,"that", "on", "by", "on", "an", "from", "", "you", "use"
    , "more", "-", "than", "·", "are", "or", "can", "with"
    , "using", "&", "this", "it", ",", ".", "\""
]

shortcuts = {
    "google" : google
    , "baidu" : baidu
}

default_search_engine = "google"
