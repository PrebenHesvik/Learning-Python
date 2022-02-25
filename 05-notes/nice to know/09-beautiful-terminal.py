from rich.console import Console
from rich.text import Text
from rich.theme import Theme
from rich.traceback import install
from rich.table import Table
from rich.markdown import Markdown
from rich.progress import track
import time

install()

console = Console()
console.print(f"Let's do some math: 2 + 2 = {2 + 2}")
console.print({'a': [1, 2, 3], 'b': {'c': 5}}, style='bold')
console.print('This is some bold text in red', style='bold underline red')
console.print('This is some bold text in red on white background', style='bold underline red on white')
console.print('[bold]This [cyan]is[/] some text.[/]')

# text
text = Text('Hello, World')
text.stylize('bold magenta', 0, 6)
console.print(text)

# Theme
custom_theme = Theme({'success': 'green', 'error': 'bold red'})
console = Console(theme=custom_theme)
console.print('Operation successful', style='success')
console.print('Operation failed', style='error')
console.print('Operation [error]failed[/error]')

# Emoji
console.print(':thumbs_up: File downloaded')

# console log
console = Console()
for i in range(3):
    console.log(f'Doing important stuff...{i}')
    time.sleep(.2)
    
def add(x, y):
    console.log('Adding two numbers', log_locals=True)
    return x + y
    
add(1, 3)
add(2, 3)
#add(13, 'hello')

# Table
table = Table(title='Star Wars Movies')
table.add_column('Released', style='cyan')
table.add_column('Title', style='magenta')
table.add_column('Box Office', justify='right', style='green')

table.add_row('Dec 20, 2019', 'Star Wars: The Ris of Skywalker', '$952,110,690')
table.add_row('May 25, 2018', 'Solo: A Star Wars Story', '$393,151,347')

console = Console()
console.print(table)

# Markdown

MARKDOWN = """
## This is an H2 heading
Rich can do a pretty **decent** job rendering markdown.

1. List item
    * list sub item
2. Another list item
"""
console = Console()
md = Markdown(MARKDOWN)
console.print(md)

# progress bar
for i in track(range(10), description='Processing...'):
    print(f'working {i}')
    time.sleep(0.5)