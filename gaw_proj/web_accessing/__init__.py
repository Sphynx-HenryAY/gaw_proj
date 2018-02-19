from web import form

search_bar_form = form.Form(
    form.Textbox( "keyword" ),
    form.Button( "Search", type = "submit" ),
    form.Button( "Get Rank", type = "submit" )
)


def load_tmpl( base_tmpl, load_scope ):
    block_pattern = "{{ %s }}"
    for each in load_scope:
        match_pattern = block_pattern % each

        if match_pattern in base_tmpl:
            base_tmpl = base_tmpl.replace( match_pattern, load_scope.get( each ) )
    
    return base_tmpl

