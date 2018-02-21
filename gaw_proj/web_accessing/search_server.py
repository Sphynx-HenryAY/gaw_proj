from time import time as get_time

import web
from . import search_bar_form
from ..searching.google import perform as search_func
from ..visualization.pretty_rank_data import prettify as show_func
from ..visualization.cal_ranking import render_ranking_content as rank_func

from ..tmpl import ranking_content


urls = [
    "/", "index"
    , "/(search|google)", "search"
    , "/ranking", "ranking"
]

template = web.template.render( "gaw_proj/web_accessing" )

class index:
    def GET( self ):
        return base.base( { "search_bar_form" : search_bar_form } )

class search:
    def GET( self, name ):
        start_time = get_time()

        kwargs = web.input()

        if not kwargs:
            raise web.seeother( "/" )
        
        kw = kwargs.kw
        
        num_get = kwargs.get( "num_get", "20" )
        num_get = int( num_get ) if num_get and num_get.isdigit() else 20


        ctx = { 
            "search_bar_form" : search_bar_form
            , "content" : show_func( search_func( kw, num_get ), "goog" )
            , "proc_time" : get_time() - start_time
        }

        return template.base( ctx )


class ranking:
    def GET( self ):
        start_time = get_time()

        # the first key word is the searching kw
        # the rest would be treated as reverse kw to clear meaningless wordings
        kwargs = web.input()
        if not kwargs.kw:
            return "Would you please input a keyword"

        kws = [ e.strip() for e in kwargs.kw.split( "," ) ]
        
        num_get = kwargs.get( "num_get", "10" )
        num_get = int( num_get ) if num_get and num_get.isdigit() else 10

        ctx = {
            "search_bar_form" : search_bar_form
            , "content" : ranking_content
            , "rank_data_list" : rank_func( 
                search_func( kws[ 0 ], num_get, is_indexing = True )
                , num_get
                , kws[ 1 : ] 
            ) 
            , "proc_time" : get_time() - start_time
        }

        return template.base( ctx )


class WebPortApp( web.application ):
    def run( self, port = 9999, *middleware ):
        func = self.wsgifunc( *middleware )
        return web.httpserver.runsimple( func, ( "0.0.0.0", port ) )


def start_server( port = 9999 ):
    app = WebPortApp( urls, globals() )
    app.run( port = port )


