# Functional Programming
scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
    {'name': 'Emy Noether', 'field': 'math', 'born': 1882, 'nobel': False}
]

# must always use immutable data structures while using functional programming style
import collections
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])

Scientist(name='Ada Lovelace', field= 'Math', born='1815', nobel=False)
# nameed tuple instance is immutable

scientists