import web
from web import form

from ..run3 import *
from ..tmpl import ranking_content, index_content
from ..settings.searching import *

from time import time as get_time


template = web.template.render( "gaw_proj/web_accessing" )

search_bar_form = form.Form(
    form.Textbox( "kw", description = "Keyword:" )
    , form.Textbox( "num_get", description = "Result Number:" )
    , form.Dropdown( "functions", [ ( "search", "Search" ), ( "ranking", "Get Rank" ) ] )
    , form.Dropdown( "engine", [ ( "google", "Google" ), ( "baidu", "Baidu" ) ] )#, ( "hybrid", "Hybrid" )
)


def get_query():
    kwargs = web.input()

    if not kwargs or not kwargs.kw:
        raise web.seeother( "/Request_Received_BUT/You need to input at least a key word" )
        
    """
        when Searching  : only the first one would be searched
        when Ranking    : the first keyword would be the searching kw
                            and the rest would be treated as stop word
    """
    kws = [ e.strip() for e in kwargs.kw.split( "," ) ]
    
    num_get = kwargs.get( "num_get", "10" )
    num_get = int( num_get ) if num_get and num_get.isdigit() else 10

    if num_get > 50 :
        raise web.seeother( "/Request_Received_BUT/DANGEROUS & FORBIDDEN!" )

    engine = kwargs.get( "engine", default_search_engine )

    return kws, num_get, engine


class index:
    def GET( self ):
        return template.base( { 
            "search_bar_form" : search_bar_form 
            , "content" : index_content
        } )

class search:
    def GET( self, name ):
        start_time = get_time()

        kws, num_get, engine = get_query()

        rank_data = search_func( kws[ 0 ], num_get, False, engine )
        content = show_func( rank_data, "search" )

        ctx = { 
            "search_bar_form" : search_bar_form
            , "content" : content
            , "proc_time" : get_time() - start_time
        }

        return template.base( ctx )


class ranking:
    def GET( self ):
        start_time = get_time()

        kws, num_get, engine = get_query()

        rank_data = search_func( kws[ 0 ], num_get, True, engine )
        rank_data_list = render_rank_func( rank_data, num_get, kws[ 1: ] )

        ctx = {
            "search_bar_form" : search_bar_form
            , "content" : ranking_content
            , "rank_data_list" : rank_data_list
            , "proc_time" : get_time() - start_time
        }

        return template.base( ctx )

class empty:
    def GET( self, name = "This", msg = "" ):
        return """
<html>
<head>
<style>
    h1 {
        font-size: 80px;
        margin-top: 80px;
        margin-bottom: 20px;
    }
</style>
</head>
<body align="center">
    <h1> 404 </h1>
    <h2> No No No No No </h2>
    <h3> %s <h3>
    <hr/>
</body>
</html>
"""% ( "<i>%s</i>"%msg if msg else "<i>%s</i> page is not acceeeeeeeeessible"%name )

class WebPortApp( web.application ):
    def run( self, port = 9999, *middleware ):
        func = self.wsgifunc( *middleware )
        return web.httpserver.runsimple( func, ( "0.0.0.0", port ) )

urls = [
    "/", "index"
    , "/(search|google)", "search"
    , "/ranking", "ranking"
    , "/(.*)/(.*)", "empty"
]

def start_server( port = 9999 ):
    app = WebPortApp( urls, globals() )
    app.run( port = port )


