#!/usr/bin/env python3
"""Convert diabettech_article.md to WordPress block HTML (diabettech_article.html)."""
import re, html
md=open('diabettech_article.md').read(); lines=md.split('\n'); title=lines[0].lstrip('# ').strip()
body='\n'.join(lines[1:]).strip()
for a,b in [ ("TuneMyBG is an Android app", "[TuneMyBG](https://play.google.com/store/apps/details?id=com.adamkowalczyk.tunemybg) is an Android app"),
 ("the advice my own network published in January", "the advice [my own network published in January](https://abcd.care/dtn/resource/current/dtn-uk-statement-large-language-models)"),
 ("posted as preprints [preprint links]", "posted as preprints [here](STUDY-PREPRINT-URL) and [here](COMMENTARY-PREPRINT-URL), with archived copies on [medRxiv](MEDRXIV-URL) and [Zenodo](ZENODO-URL)")]:
    body=body.replace(a,b)
fig='''<!-- wp:image {"align":"wide","sizeSlug":"full","linkDestination":"media"} -->
<figure class="wp-block-image alignwide size-full"><img src="UPLOAD-fig_funky.png-TO-MEDIA-LIBRARY-AND-PASTE-URL-HERE" alt="Barcode chart: one cell per conversation for eleven language models showing the maximum insulin on board limit each proposed on the same record; DeepSeek's sensitivity factors from 30 to 180; and Gemini 3.6 Flash's headline recommendation flipping between target and basal across fifty conversations."/><figcaption class="wp-element-caption">Same record, same prompts, a fresh conversation each time. Each cell is one conversation; the app's check accepted every coloured cell.</figcaption></figure>
<!-- /wp:image -->'''
def inline(t):
    t=html.escape(t, quote=False); return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
paras=[p for p in body.split('\n\n') if p.strip()]
out=[f'<!-- wp:paragraph {{"className":"standfirst"}} -->\n<p class="standfirst">{inline(paras[0].strip())}</p>\n<!-- /wp:paragraph -->']
for p in paras[1:]:
    if p.startswith('## '):
        h=p[3:].strip()
        if h.startswith('Which universe'): out.append(fig)
        out.append(f'<!-- wp:heading -->\n<h2 class="wp-block-heading">{html.escape(h, quote=False)}</h2>\n<!-- /wp:heading -->')
    else: out.append(f'<!-- wp:paragraph -->\n<p>{inline(p.strip())}</p>\n<!-- /wp:paragraph -->')
open('diabettech_article.html','w').write(f'<!-- Title (enter in the post title field): {html.escape(title, quote=False)} -->\n\n'+'\n\n'.join(out)+'\n')
print('blocks', len(out))
