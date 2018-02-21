
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
    <b>Usage of Ranking:</b>Remove column by adding column label after target keyword, e.g:<br/>
    <b>   <i>Keyword: target keyword,unwanted column,unwanted again</i></b><br/>
    so, "unwanted column" and "unwanted again" columns will be removed.
</p>
<p>
    Get more keywords and website by inputing a integer in Result Number, default 10.
</p>
"""

index_content = """
<style>
    b {
        font-size : 28px;
    }
</style>
<p>
    This site contains two main functions:
    <ol>
        <li>
            Searching Functions
        </li>
        <li>
            Ranking Functions
        </li>
    </ol>
</p>
<p>
    <b>Searching Functions</b> is basically a function that grab content from search engine,<br/>
    which is now only google is available. And then extract and reformat to show. This is a <br/>
    function that could be used to reduce traffic produced; and be possible to get as much as <br/>
    result if wanted; besides, it could be used by mainlander to obtain google search somehow.
</p>
<p>
    <b>Ranking Functions</b> is a function that also grab content from search engine, and <br/>
    perform word frequency analysis on website abstract. This could be used to show how your<br/>
    website is different from the others according to the brief introduction in search result.<br/>
    Display order could be a multiplyer of word occurence to show different kind of impact.
</p>
<br/>
<br/>
<p>
    <b>Usage of Searching:</b> come on, it is so easy.
</p>
""" + ranking_content
