Hi All!

Thanks for collaborating on this phone scraping tool. I was surprised that I couldn't find a clean open-source solution online so here we go.
<br>

The tool reliably pumps out phone numbers given a URL. Here is a running list of to-do items to improve the tool:
<br>
• Make it so that results show on one line per website to make it easier to upload to CRM <br>
• Use proper redirect for header so that it detects HTTP vs HTTPS and goes to the correct one, provides cert for SSL if needed <br>
• De-duplicate results so that matching results are excluded <br>
• Make it ignore the first row of a file so that we can use files and retain the column titles. <br>

Stretch goals: <br>
• Translating it into JavaScript to make it a tad easier throw into full web applications. <br>
• building out the API/DB Models to request and save results. <br>

