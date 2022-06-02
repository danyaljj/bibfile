from pybtex.database import parse_file
bib_data = parse_file('../ref.bib')

for author in bib_data.entries['Knuth:TB8-1-14'].persons['author']:
  print(unicode(author))
