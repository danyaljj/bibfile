# Tag Khashabi Papers

Your task is to assign topic tags to one or more papers by Daniel Khashabi in `ref.bib`.

## Instructions

1. If the user specified a BibTeX key (e.g. `/tag-khashabi-papers zhang2026AgentOdyssey`), process only that entry. Otherwise, find all entries authored by "Daniel Khashabi" or "Khashabi, Daniel" whose `tags` field is either missing or contains only `selected` (i.e., no topic tags yet assigned).

2. For each target entry, read its `title`, `abstract` (if present), and any other available fields to understand the paper's content.

3. Assign **all applicable** tags from the following list to the `tags` field:

   - `Reasoning`
   - `Evaluation`
   - `Model Training`
   - `Safety`
   - `Retrieval`
   - `AI + Humans`
   - `AI for Science`
   - `Agents`
   - `Interpretability`
   - `Grounding`
   - `Multimodal`
   - `Multilingual`
   - `Long-context`
   - `Embodied`

4. Preserve any existing tags already in the field (e.g. `selected`). Add the new topic tags alongside them. Use comma-separated values inside the `tags = {...}` field.

5. For each paper, briefly explain which tags you assigned and why, so the user can verify your choices.

6. After processing all papers, apply the edits to `ref.bib` and offer to commit and push.
