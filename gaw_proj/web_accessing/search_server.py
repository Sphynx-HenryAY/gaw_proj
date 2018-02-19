from time import time as get_time

import web
from web import form

from . import search_bar_form, load_tmpl



urls = [
    "/", "index"
    , "/(search|google)", "search"
    , "/rank", "rank"
]


class index:
    def GET( self ):
        base_tmpl = web.template.render( "templates/base.html" )
        f = search_bar_form()
        return base_tmpl.register( f )


class search:
    def GET( self, name ):
        start_time = get_time()
        kwargs = web.input()
        base_tmpl = web.template.render( "templates/base.html" )

        if not kwargs:
            f = search_bar_form()
            return base_tmpl.register( f )
        
        kw = kwargs.kw
        
        num_get = kwargs.get( "num_get", "20" )
        num_get = int( num_get ) if num_get and num_get.isdigit() else 20

        content = """
            Time spent: %fs
            <br/>
            <br/>
            %s
            <br/>
        """
        
        base_tmpl = load_tmpl( base_tmpl, globals() )
        html_tmpl = load_tmpl( base_tmpl, locals() )

        from .. import search as search_func, show as show_func
        return html_tmpl % ( get_time() - start_time, show_func( search_func( kw, num_get ), "web" ) )


class rank:
    def GET( self ):
        kws = web.input( kw = [] )
        return ", ".join( kws.kw )


class WebPortApp( web.application ):
    def run( self, port = 9999, *middleware ):
        func = self.wsgifunc( *middleware )
        return web.httpserver.runsimple( func, ( "0.0.0.0", port ) )


def start_server( port = 9999 ):
    app = WebPortApp( urls, globals() )
    app.run( port = port )


if __name__ == "__main__":
    start_server( 9999 )
