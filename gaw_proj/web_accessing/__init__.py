from web import form

search_bar_form = form.Form(
    form.Textbox( "kw", description = "Keyword:" )
    , form.Textbox( "num_get", description = "Result Number:" )

    , form.Dropdown('selection', [ ('search', 'Search'), ('ranking', 'Get Rank') ])
    , form.Button( "get_type", type = "submit", html = "Submit" )
)


