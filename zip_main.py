import zipfile

lines = []
with zipfile.ZipFile('Resampling-M6-FD-B01.log.0.zip', 'r') as zipf:
  print('zip file has these archives: {}'.format(zipf.namelist()))
  with zipf.open(zipf.namelist()[0]) as f:
    for line in f:
      lines.append(line)
      print(line)
      break
print('done')