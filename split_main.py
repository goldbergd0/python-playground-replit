name = 'this_is_exactly_what_im_thinking_s12345_e039485151_c163049723745'

split_n = name.split('_')
for s in split_n:
  is_time = s.startswith('s') and len(s) > 1 and s[1:].isdigit()
  if is_time:
    print(s[1:])