#! /usr/bin/env python3

from gaw_proj import search, show, web
import sys

# avoid index error
def get_arg( args, index, default = None ):
    return args[ index ] if index < len( args ) else default

def todigit( arg, default = None ):
    return int( arg ) if arg and arg.isdigit() else default

def pre_search( args ):
    kw = get_arg( args, 2, "" )

    num_get = todigit( get_arg( args, 3 ), 10 )

    show( search( kw, num_get ) )


def pre_web( args ):
    port = todigit( get_arg( args, 2 ), 9999 )

    web( port )


if __name__ == "__main__":
    map_func = {
        "search" : pre_search
        , "web" : pre_web
    }

    args = sys.argv
    if len( args ) > 2:
        map_func.get( get_arg( args, 1 ), "search" )( args )
    print( "finished" )
