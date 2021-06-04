love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for love in love_maybe_lines:
  love_maybe_lines_stripped.append(love.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)