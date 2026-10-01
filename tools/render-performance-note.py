"""Render the approved Week 2 Markdown using Pandoc 3.9 and the site's layout."""
from pathlib import Path
import html
import re
import subprocess

root = Path(__file__).resolve().parents[1]
source = root / 'study-notes/microprocessor/performance-and-yield.md'
target = source.with_suffix('.html')
text = source.read_text()
title = text.splitlines()[0].removeprefix('# ')
content = subprocess.check_output([
    'pandoc', '-f', 'gfm', '-t', 'html5', '--wrap=none',
    '--syntax-highlighting=none', str(source)
], text=True)
start = '<h2 id="contents">Contents</h2>'
end = '<h2 id="1-software-defines-the-work-that-the-machine-executes">'
assert content.count(start) == content.count(end) == 1
content = content.replace(start, '<nav class="toc-box" aria-labelledby="table-of-contents">\n<h2 id="table-of-contents">Contents</h2>', 1)
content = content.replace(end, '</nav>\n' + end, 1)
position = content.index('</h1>') + len('</h1>')
dates = '\n<p class="article-dates">Created <time datetime="2026-10-01">1 October 2026</time> · Last edited <time datetime="2026-10-01">1 October 2026</time></p>'
content = content[:position] + dates + content[position:]
pre_labels = iter([
    'C addition statement', 'Average cycles per instruction calculation',
    'One gigahertz clock waveform', 'CPU time equations',
    'Instruction throughput equation', 'Instruction throughput cross-check',
    'Single CPU timeline', 'Single CPU throughput', 'Two CPU timeline',
    'Two CPU throughput', 'Instruction class cycle equations',
    'Required clock rate derivation', 'Execution time fractions',
    'Amdahl speedup equations', 'Small and large die yield illustration',
    'Discarded die area comparison', 'Chiplets tested before package assembly',
    'Eight compute units with one faulty unit', 'Two enabled compute unit configurations',
])
def accessible_pre(match):
    return match.group(0).replace('<pre', '<pre role="region" tabindex="0" aria-label="' + next(pre_labels) + '"', 1)
content = re.sub(r'<pre\b[^>]*>', accessible_pre, content)
assert next(pre_labels, None) is None
table_labels = iter([
    'Computer classes', 'Decimal number prefixes', 'Performance measures',
    'Processor clock rates and CPI', 'Processor instruction throughput',
    'Cycles and instructions in ten seconds', 'Runtime for a fixed instruction count',
    'Instruction class CPI and counts', 'Compiled program cycle totals',
    'Required new processor clock rates', 'Multiplication speedup time breakdown',
])
def accessible_table(match):
    return '<div class="table-scroll" role="region" tabindex="0" aria-label="' + next(table_labels) + '">\n' + match.group(0) + '\n</div>'
content = re.sub(r'<table\b[^>]*>.*?</table>', accessible_table, content, flags=re.S)
assert next(table_labels, None) is None
page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="CPU time, instruction count, CPI, throughput, Amdahl's law, and how chiplets and harvesting reduce manufacturing waste.">
  <title>{html.escape(title)} — Microprocessor — Jack Byun</title>
  <link rel="stylesheet" href="../../style.css?v=20260930-layout">
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>
  <header class="site-header"><div class="wrap">
    <a class="brand" href="../../">Jack Byun</a>
    <nav aria-label="Main navigation"><a href="../">Study Notes</a> <a href="../../projects/">Projects</a> <a href="../../contributions/">Upstream Contributions</a></nav>
  </div></header>
  <main class="wrap article" id="content">
    <p class="breadcrumbs"><a href="../">Study Notes</a> / <a href="./">Microprocessor</a></p>
{content}
    <aside class="reference-box" aria-label="Source and attribution">
      <p class="reference-label"><strong>Reference</strong></p>
      <p><a href="https://dl.acm.org/doi/book/10.5555/3027670">https://dl.acm.org/doi/book/10.5555/3027670</a></p>
    </aside>
  </main>
  <footer><div class="wrap">© 2026 Jack Byun</div></footer>
</body>
</html>
'''
target.write_text(page)
print(f'Rendered {target.name} ({len(page.encode())} bytes)')
