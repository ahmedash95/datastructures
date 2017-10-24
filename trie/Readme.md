# Trie datastructure

A very simple trie implementation in Python 2.7 with auto-complete feature

## How to use

```py
import Trie

t = Trie.Trie()

t.add("foo")
t.add("foobar")
t.add("foobaz")
t.add("bar")

t.get_by_prefix("foo")
"""
 Result
    [0] foo
    [1] foobar
    [2] foobaz
"""
```