
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

cls = {
    "google" : {
        "ctt_block" : ( "div", "rc" )
        , "ctt_abstract" : ( "span", "st" )
        , "ctt_title" : ( "h3", "r" )
        , "ctt_link" : ( "cite", "_Rm" )
    }
    , "baidu" : {
        "ctt_block" : ( "div", "c-result" )
        , "ctt_abstract" : ( "div", "c-abstract" )
        , "ctt_title" : ( "h3", "c-title" )
        , "ctt_link" : ( "span", "c-showurl" )
    }
}

query_settings = {
    "google" : {
        "url"   : "https://www.google.com.hk/search?"
        , "kwa" : { 
            "q"     : None
            , "oq"  : None
            , "ie"  : "UTF-8" 
            , "hl"  : "en"
            , "btnG": "Search"
        }
        , "begin_wd" : "start"
    }
    , "baidu" : {
        "url"   : "http://m.baidu.com/s?"
        , "kwa" : { 
            "wd"    : None
            , "ie"  : "UTF-8" 
            , "hl"  : "en"
        }
        , "begin_wd" : "pn"
    }
}

default_search_engine = "google"
