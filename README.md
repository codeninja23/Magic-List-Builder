Hi All!

Thanks for collaborating on this phone scraping tool. I was surprised that I couldn't find a clean open-source solution online so here we go.
<br>

The tool reliably pumps out phone numbers given a URL. Here is a running list of to-do items to improve the tool:
<br>
• Use proper redirect for header so that it detects HTTP vs HTTPS and goes to the correct one, provides cert for SSL if needed <br>
• De-duplicate results so that matching results are excluded <br>

Stretch goals: <br>
• Translating it into JavaScript to make it a tad easier throw into full web applications. <strong>Coming soon!</strong><br>
• building out the API/DB Models to request and save results. <br>

After you download, run in shell with the following comand: <strong>python3.6 phoneSiteQuery.py</strong>

