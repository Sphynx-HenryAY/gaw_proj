import json

settings = {
    "cls": {
        "ctt_block" : ( "div", "c-result" )
        , "ctt_abstract" : ( "", "c-abstract" )
        , "ctt_title" : ( "h3", "c-title" )
        , "ctt_link" : ( "span", "c-showurl" )
    }
    , "query" : {
        "url"   : "http://m.baidu.com/s?"
        , "kwa" : { 
            "wd"    : None
            , "ie"  : "UTF-8" 
            , "hl"  : "en"
        }
        , "begin_wd" : "pn"
    }
    , "special" : {
        "link" : lambda b: json.loads( b.attrs.get( "data-log" ).replace( "'", '"' ) ).get( "mu" )
    }
}
