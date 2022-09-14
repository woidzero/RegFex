<div align="center" style="font-family: monospace;">
<img src="https://github.com/woidzero/regfex/blob/main/icon.png?raw=true">

<h2>RegFex</h2>
<p>Python module for get regular expressions from .re files</p>

<a href="https://pypi.org/project/regfex/"><img src="https://img.shields.io/badge/pypi-0.0.1-fff?style=for-the-badge"></a>
<a href="https://github.com/woidzero/regfex/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-GPL_3.0-fff?style=for-the-badge"></a>
<a href="https://python.org/"><img src="https://img.shields.io/badge/python-3.x-fff?style=for-the-badge"></a>
</div>

<br>

## Installation
> `Linux`
> ```
>  python3 -m pip install regfex
> ```
> `Windows`
> ```
>  pip install regfex
> ```

<br>

## Using 
> `main.py`
> ```python
> import regfex
> 
> expression = regfex.loadFile("expressions.re").getKey("expr1")
> print(expression)
> ```
> `expressions.re`
> ```python
> expr1: (?<=\.) {2,}(?=[A-Z])
> ```
> Output
> ```bash
> (?<=\.) {2,}(?=[A-Z])
> ```

<br>

## Support

For support, email <a href="mailto://contact@woidzero.xyz">contact@woidzero.xyz</a> or join Discord - <a href="https://discord.gg/bD2uaxkqQW">Tacet Community</a>
