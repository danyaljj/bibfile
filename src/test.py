from pybtex.database import parse_file

# make sure the file is valid and the keys are not duplicate
bib_data = parse_file('ref.bib')

for entry in bib_data.entries.keys():
  # make sure they have "authors"
  for author in bib_data.entries[entry].persons['author']:
    print(f" * {entry} -> {author}")
#     # TODO: bib entry name should have first author name
#     # TODO: bib entry name should have publication year
#     # TODO: bib entry name should have a keyword from title

  # make sure they have "year"
  year = bib_data.entries[entry].fields['year']
  print(f" * {entry} -> {year}")

# find and raise duplicate article names
all_keys = list(bib_data.entries.keys())
repeated_entries = []
for idx, entry in enumerate(all_keys):
  for entry2 in all_keys[idx+1:]:
    if bib_data.entries[entry].fields['title'].lower().strip() == bib_data.entries[entry2].fields['title'].lower().strip():
      repeated_entries.append(f" * WARNING: {entry} and {entry2} have the same title")

# if len(repeated_entries) > 0:
#   print("\n".join(repeated_entries))
#   raise Exception("There are duplicate article names")


import bibtexparser

with open('ref.bib') as bibtex_file:
  bib_database = bibtexparser.load(bibtex_file)