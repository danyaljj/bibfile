from pybtex.database import parse_file

# make sure the file is valid and the keys are not duplicate
bib_data = parse_file('ref.bib')

for entries in bib_data.entries.keys():

  # make sure they have "authors"
  for author in bib_data.entries[entries].persons['author']:
    print(f" * {entries} -> {author}")

  # make sure they have "year"
  year = bib_data.entries[entries].fields['year']
  print(f" * {entries} -> {year}")
