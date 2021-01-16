# pyfuck: a Brainfuck interpretor

```python
>>> import bf
>>> bf.evaluate("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
'Hello World!'
```

Oh and you can also enter some inputs.

```python
>>> bf.evaluate(",>,[------------------------------------------------<]>[->+<]>++++++++++++++++++++++++++++++++++++++++++++++++.", inp="23") # This script will add the two digits given in string input
'5'
```

That's it. Enjoy.. getting your brain fucked, I guess?
