# Bibfile 

The standardized bib file used for writing our papers.
To add new items to the file, send a pull-request with your additions to `bib.ref`.
The repository automatically styles and sorts the items.

## Tagging Papers (Khashabi papers)

Papers authored by Daniel Khashabi have a `tags` field with topic labels used for filtering on the publication page. Valid tags:

`Reasoning`, `Evaluation`, `Model Training`, `Safety`, `Retrieval`, `AI + Humans`, `AI for Science`, `Agents`, `Interpretability`, `Grounding`, `Multimodal`, `Multilingual`, `Long-context`, `Embodied`

When adding a new Khashabi paper, run the following Claude Code slash command to assign tags automatically:

```
/tag-papers <bibtex-key>
```

Or run it without arguments to process all untagged Khashabi papers:

```
/tag-papers
```