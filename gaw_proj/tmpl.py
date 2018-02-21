
struc_tmpl = """
{
    type: "stackedColumn100",
    name: "{{ link }}",
    showInLegend: true,
    dataPoints: [
            {{ kw_ranking_data }}
    ]
}
"""

data_tmpl = """{ label: "{{ kw }}", y: {{ score }} }"""

ranking_content = """
<p>
    Remove column by adding column label after target keyword, e.g:<br/>
    <b><i>Keyword: target keyword,unwanted column,unwanted again</i></b><br/>
    so, "unwanted column" and "unwanted again" columns will be removed.
</p>
<p>
    Get more keywords and website by inputing a integer in Result Number, default 10.
</p>
"""
