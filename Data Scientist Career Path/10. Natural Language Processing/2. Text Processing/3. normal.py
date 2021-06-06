brands = 'Salvation Army, YMCA, Boys & Girls Club of America'

brands_lower = brands.lower()
brands_upper = brands.upper()

try:
  print(f'Lowercased brands: {brands_lower}')
except:
  print('Expected a variable called `brands_lower`')
try:
  print(f'Uppercased brands: {brands_upper}')
except:
  print('Expected a variable called `brands_upper`')