# nlp_python_package

Developed by Afnanurrahim Ansari (c) 2023

## How To Use this package

Install the package

```python
!pip install nlp-text-preprocessor
```

import the library

```python
import nlp_lib
from nlp_lib import preprocessor
```

Now you can use all the functionalities in the package

```python
preprocessor.remove_emoji('I loved that joke 😂')
#output : I loved that joke 

preprocessor.replace_emoji('I loved that joke 😂')
#output : I loved that joke laughing

preprocessor.remove_html_tags('<head><title>Title of web page</title></head><body>HTML web page contents </body>')
#output : Title of web pageHTML web page contents 

preprocessor.remove_special_char('Th@is #is &a samp^le text')
#output : This is a sample text

preprocessor.replace_abbreviations("lmao , lol , p.m")
#output : laugh my ass off , laughing out loud , after midday

preprocessor.replace_contraction("They aren't doing any kinda work")
#output : they are not doing any kind of work

preprocessor.WordSegment('Thisisasampletext').segment_list()
#output : ['this', 'is', 'a', 'sample', 'text']

```

For getting dictionary of data used use the following commands
```python
preprocessor.abbreviations()

#output : {'$': 'dollar','4ao': 'for adults only','a.m': 'before midday','a3': 'anytime anywhere anyplace','acct': 'account',...}

preprocessor.contractions()

#output : {"aren't": 'are not',"can't": 'cannot',"couldn't": 'could not',"didn't": 'did not',...}

preprocessor.emojis()

#output: {'😂': 'laughing','😍': 'love','😭': 'crying'...}

```

