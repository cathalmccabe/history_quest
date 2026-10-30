import json,re,pathlib
root=pathlib.Path(__file__).parent
js=(root/'questions.js').read_text()
q=json.loads(js.removeprefix('window.BUILTIN_QUESTIONS=').rstrip(' \n;'))
assert len(q)>=100
assert len({x['id'] for x in q})==len(q)
assert all(x['year'] and x['precision'] in ('day','year') for x in q)
assert all(x['day'] and x['month'] if x['precision']=='day' else x['day'] is None for x in q)
assert len({x['category'] for x in q})>=8
for f in ['index.html','style.css','app.js','questions.js','sw.js','manifest.webmanifest','icons/icon-192.png','icons/icon-512.png']:
 assert (root/f).exists(),f
print(f'PASS: {len(q)} cards, {len({x["category"] for x in q})} categories; app assets present')
