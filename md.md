# Markdown Examples

## Basic Stuff

### Emphasis

This word is *italicized*, _underscores_ also work

### Strong emphasis

This word is **bold** and *markup __can__ be nested*.

### Code inline

Call the `function_name` function.

### Code blocks

Look at this output:

```
$ ls /usr/
bin        lib        libexec
```

Look at this code:

```python
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

### Blockquotes

Lincoln said:

> Four-score and seven years ago, our fathers
> brought forth on this continent a new nation,
> conceived in Liberty, and dedicated to the
> proposition that all men are created equal.

## Lists

### Numbered

1. First ordered list item
1. Another item
1. Actual numbers don't matter

### Bullets

* First unordered list item
* Another item
* And another item

### Nested

1. First outer
   * First inner
   * Second inner
2. Second outer
3. Third outer

## Links

### URLs

<!-- note: Classic Markdown doesn't auto-link URLs. -->

URLs make links: http://python.org.

### Inline

[Inline link](http://python.org)
for brevity.

### Indirect

[Indirect link][indirect]
for readability.

[indirect]: http://python.org


## Headers

### Headers

<!-- parse-headers-off -->

# First Header

## Second Header

### Third Header

#### Fourth Header

<!-- parse-headers-on -->


## Images

### Images

![Image of Xsy](xsy_150.png)


## Notes etc

### Notes

Markdown has no specialized syntax for notes.

### Footnotes

Extended Markdown supports footnotes[^1].

[^1]: The footnote will mostly be displayed in the bottom
no matter where you define it, hence _the name_.

### Warnings

Markdown has no specialized syntax for warnings.
