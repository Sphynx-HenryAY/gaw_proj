# keep this file capable with python2

def get_arg( args, index, default = None ):
    return args[ index ] if index < len( args ) else default

def todigit( arg, default = None ):
    return int( arg ) if arg and arg.isdigit() else default


def base_search( args, show_method = "" ):

    from gaw_proj.run3 import search_func, show_func

    kw = get_arg( args, 2, "" )
    num_get = todigit( get_arg( args, 3 ), 10 )
    engine = get_arg( args, 4, default = "google" )

    is_indexing = False
    if show_method == "rank":
        is_indexing = True

    show_func( search_func( kw, num_get, is_indexing, engine ), show_method )


def pre_search( args ):
    base_search( args )

def pre_rank( args ):
    base_search( args, "rank" )


def pre_website( args ):
    from gaw_proj.run3 import website_func
    website_func( todigit( get_arg( args, 2 ), 9999 ) )


if __name__ == "__main__":
    map_func = { k.replace( "pre_", "" ) : globals()[ k ] for k in globals() if "pre_" in k }

    import sys
    args = sys.argv
    if len( args ) > 2:
        map_func.get( get_arg( args, 1 ), pre_search )( args )

    print( "finished" )
