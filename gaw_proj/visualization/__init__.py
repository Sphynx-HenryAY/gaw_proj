from functools import reduce

def render_content( tmpl, ctx ):
    render_mark = "{{ %s }}"

    for k in ctx:
        tmpl = tmpl.replace( render_mark % k, str( ctx.get( k ) ) )

    return tmpl

