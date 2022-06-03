from pybtex.database import parse_file

# make sure the file is valid and the keys are not duplicate
bib_data = parse_file('ref.bib')

for entry in bib_data.entries.keys():

  # make sure they have "authors"
  for author in bib_data.entries[entry].persons['author']:
    print(f" * {entry} -> {author}")

    # TODO: bib entry name should not have "-"
    assert "-" not in entry, entry

    # TODO: bib entry name should have first author name
    # TODO: bib entry name should have publication year
    # TODO: bib entry name should have a keyword from title

  # make sure they have "year"
  year = bib_data.entries[entry].fields['year']
  print(f" * {entry} -> {year}")




# TODO: make sure the entries are sorted according to time

# formatted_entries = bib_data.to_string('bibtex')
# print(formatted_entries)
