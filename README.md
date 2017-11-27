Hi All!

Thanks for collaborating on this phone scraping tool. I was surprised that I couldn't find a clean open-source solution online so here we go.

The tool reliably pumps out phone numbers given a URL. Here is a running list of to-do items to improve the tool:

• Make it so that results show on one line per website to make it easier to upload to CRM
• Use proper redirect for header so that it detects HTTP vs HTTPS and goes to the correct one, provides cert for SSL if needed
• De-duplicate results so that matching results are excluded
• Make it ignore the first row of a file so that we can use files and retain the column titles.

Stretch goals:
• Translating it into JavaScript to make it a tad easier throw into full web applications.
• building out the API/DB Models to request and save results.

