# A simplified markdown parser.

# *hello* -> <b>hello</b>
# _hello_ -> <i>hello</i>
# #hello  -> <h1>hello</h1>

# *some string            -> *some string
# *some string*lol*       -> <b>some string</b>lol*
# *some_string*again_     -> <b>some_string</b>again_
# *some* _string_         -> <b>some</b> <i>string</i>
# some *string_again_     -> some *string<i>again</i>
# some#string*once_again* -> some#string<b>once_again</b>
# #string_stuff_          -> <h1>string_stuff_</h1>

# NESTED MATCHES:
# *some_string_* -> <b>some_string_</b>
# #some _string_ -> <h1>some _string_</h1

# EMPTY MATCHES:
# hello ** world  -> hello ** world
# hello **world*  -> hello *<b>world</b>
# hello **world** -> hello *<b>world</b>*

# OTHER:
# *some*string** -> <b>some</b>string**
# hello ***world*** -> hello **<b>world</b>**
# hello ****world**** -> hello ***<b>world</b>***
# hello ***hello* -> hello **<b>word</b>
# hello ****hello* -> hello ***<b>word</b>
# # -> #

# Rules:
# - Match until closing special character. If no closing character, ignore.
# - The '#' special character must be the first character. It matches until EOL.
# - Once there is a match, clear stack up until matching special character.
# - Ignore nested matches, and take the outermost match.
# - Ignore any special characters immediately followed by itself.


def parse(s):
  tags = {
    '*': ('<b>', '</b>'),
    '_': ('<i>', '</i>')
  }
  
  new = ''
  if s:
    if s[0] == '#' and len(s) > 1:
      return f'<h1>{s[1:]}</h1>'
    i = 0
    lastIndex = 0
    while i < len(s):
      letter = s[i]
      if letter in tags:
        nextIndex = i + s[i+1:].find(letter) + 1
        if nextIndex != i and nextIndex != i + 1: # There is a closing special char.
          match = s[i+1:nextIndex]
          new += s[lastIndex:i]
          new += f'{tags[letter][0]}{match}{tags[letter][1]}'
          i += nextIndex - i + 1
          lastIndex = i
      i += 1
    new += s[lastIndex:]

  return new

if __name__ == '__main__':
  # Run simple tests.
  assert(parse('*hello*') == '<b>hello</b>')
  assert(parse('_hello_') == '<i>hello</i>')
  assert(parse('#hello') == '<h1>hello</h1>')

  assert(parse('*some string') == '*some string')
  assert(parse('*some string*lol*') == '<b>some string</b>lol*')
  assert(parse('*some_string*again_') == '<b>some_string</b>again_')
  assert(parse('*some* _string_') == '<b>some</b> <i>string</i>')
  assert(parse('some *string_again_') == 'some *string<i>again</i>')
  assert(parse('some#string*once_again*') == 'some#string<b>once_again</b>')
  assert(parse('#string_stuff_') == '<h1>string_stuff_</h1>')

  assert(parse('*some_string_*') == '<b>some_string_</b>')
  assert(parse('#some _string_') == '<h1>some _string_</h1>')

  assert(parse('hello ** world') == 'hello ** world')
  assert(parse('hello **world*') == 'hello *<b>world</b>')
  assert(parse('hello **world**') == 'hello *<b>world</b>*')

  assert(parse('*some*string**') == '<b>some</b>string**')
  assert(parse('hello ***world***') == 'hello **<b>world</b>**')
  assert(parse('hello ****world****') == 'hello ***<b>world</b>***')
  assert(parse('hello ***world*') == 'hello **<b>world</b>')
  assert(parse('hello ****world*') == 'hello ***<b>world</b>')

  print('All tests passed!!!')
