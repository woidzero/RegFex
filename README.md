# RegFex
Python module for get regular expressions from .re files</p>

## Installation
> `Linux`
> ```
>  python3 -m pip install regfex
> ```
> `Windows`
> ```
>  pip install regfex
> ```

## Using 
> ```python
> import regfex
> 
> expression = regfex.loadFile("expressions.re").getKey("expr1")
> print(expression)
> ```
> ```css
> expr1: (?<=\.) {2,}(?=[A-Z])
> ```
> Output
> ```bash
> (?<=\.) {2,}(?=[A-Z])
> ```

## Support

For support, email <a href="mailto://contact@woidzero.xyz">contact@woidzero.xyz</a> or join Discord - <a href="https://discord.gg/bD2uaxkqQW">Tacet Community</a>
