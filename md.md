# Markdown Examples

## Basic Stuff

### Emphasis

*emphasis*

### Strong emphasis

**emphasis**

### Code inline

Call the `function_name` function.

### Code blocks

Look at this code:

```
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

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
