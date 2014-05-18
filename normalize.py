# encoding: utf-8

import fileinput
import re

RE_URL = re.compile(r'^https?://.*$')
RE_MENTION = re.compile(r'^@\w+')
RE_JUNKTUATION = re.compile(r'^(\w*)(?:-|—|:|&gt;|&lt;|&amp;)+$|^(?:-|:|&gt;|&lt;|&amp;)+(\w*)$')
RE_AT = re.compile(r'^(.*)@(.*)$')
RE_WITH = re.compile(r'^w/$')
RE_PIC = re.compile(r'^\[pic\]:$')
RE_HASHTAG = re.compile(r'^#(\w+)$')

seen_ht = {}
def next_ht(tag):
  if tag not in seen_ht:
    n = len(seen_ht)
    seen_ht[tag] = n
  else:
    n = seen_ht[tag]
  return n

def needs_punc(string):
  return string[-1] not in ('.', '?', '!')

for line in fileinput.input():
  line = line.strip()
  tokens = line.split(' ')
  norm_tokens = []
  for token in tokens:
    if RE_URL.match(token):
      norm_tokens.append('T_URL')
      continue
    elif RE_MENTION.match(token):
      norm_tokens.append(token[1].upper() + token[2:])
    elif RE_PIC.match(token):
      norm_tokens.append('T_PIC')
    else:
      junk_md = RE_JUNKTUATION.match(token)
      if junk_md:
        word = junk_md.group(1) or junk_md.group(2)
        if word:
          norm_tokens.append(word)
        continue

      # at_md = RE_AT.match(token)
      # if at_md:
      #   word = ''
      #   if at_md.group(1):
      #     word += at_md.group(1)
      #   word += 'at'
      #   if at_md.group(2):
      #     word += at_md.group(2)
      #   norm_tokens.append(word)
      #   continue

      if RE_WITH.match(token):
        norm_tokens.append('with')
        continue

      ht_md = RE_HASHTAG.match(token)
      if ht_md:
        # This would put the word without the hashtag
        # norm_tokens.append(ht_md.group(1))
        
        # But actually, hashtags are largely nonsense, so normalize them away.
        norm_tokens.append('HT%04d' % next_ht(ht_md.group()))
        continue
      
      # Finally if nothing matches, append the token itself
      norm_tokens.append(token)

  add_punc = needs_punc(line)
  print(' '.join(norm_tokens) + ('.' if add_punc else ''))
