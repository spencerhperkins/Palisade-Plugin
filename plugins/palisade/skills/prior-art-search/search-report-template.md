# Prior-art search report template

Output layout for the `prior-art-search` skill. Replace every bracketed value. Use the citation format from `patent-search-fundamentals` in every citation cell.

---

## Target

- **Mode:** [Invalidity / Novelty / Gap]
- **Target:** US [number], "[title]", [applicant] (or: invention disclosure, "[short name]")
- **Claims searched:** [claim numbers, or "search statement drafted for this search, not a proposed claim"]
- **Cutoff:** [date], [basis, for example "effective filing date, priority to application [number]" or "planned filing date"]
- **Excluded as same specification:** [patent numbers, or "None found"]

| Limitation | Claim language | Notes |
|---|---|---|
| 1[pre] | "[verbatim claim text]" | [Preamble may be limiting because ...] |
| 1[a] | "[verbatim claim text]" | |
| 1[b] | "[verbatim claim text]" | **Point of novelty.** |
| 1[c] | "[verbatim claim text]" | [Means-plus-function; corresponding structure: "[quotation]" ([citation])] |

## Results summary

[n] X, [n] Y, and [n] A candidates. Limitations with no candidate: [labels, or "None"].

## Candidates

| Rank | Patent | Title | Applicant | Filed | Granted | Cat. | Limitations | Best passage |
|---|---|---|---|---|---|---|---|---|
| 1 | US [number] | [title] | [applicant] | [date] | [date] | X | all of claim [n] | "[verbatim quotation]" ([citation]) |
| 2 | US [number] | [title] | [applicant] | [date] | [date] | Y | 1[a], 1[b] | "[verbatim quotation]" ([citation]) |
| 3 | US [number] | [title] | [applicant] | [date] | [date] | A | 1[pre] | "[verbatim quotation]" ([citation]) |

**Flags:** [for example, "Rank 2 is commonly owned with the target and qualifies only by filing date; check whether the common-ownership exception applies."]

## Coverage matrix

| Limitation | Rank 1 | Rank 2 | Rank 3 |
|---|---|---|---|
| 1[pre] | Yes | Yes | Yes |
| 1[a] | Yes | Yes | |
| 1[b] | Yes | Yes | |
| 1[c] | Partial | | |

## Novelty read-out

Novelty mode only. One block per draft claim or search statement.

- **Anticipation risk:** [Rank [n] appears to read on claim [n], or "No X candidate found"]
- **Obviousness risk:** [Ranks [n] and [n] together cover every limitation; possible reason to combine: [one line]]
- **Distinguishing limitations:** [labels]: no candidate found discloses them.
- **Focus for claim drafting:** "[verbatim disclosure passage]" adds distance from Rank [n] because [reason].

## Search log

| Round | Tool | Query | Filters | Useful results |
|---|---|---|---|---|
| 1 | Semantic, claims returned | [claim 1 text, or short description] | Filed before [date] | [n]: [patent numbers, with the claims that recite target limitations, for example "US 9,123,456 (cl. 1, 4, 9)"] |
| 2 | Patent lookup, spec mined | US [number] | — | Limitations found: [labels] |
| 3 | Keyword | [terms] | Filed before [date] | [n]: [patent numbers] |
| 4 | Semantic + applicant, claims returned | [query] | Applicant "[name]", filed before [date] | [n]: [patent numbers] |

## Next steps

- [Invalidity: chart ranks [n] with `/invalidity` or the `chart` skill.]
- [Novelty: review ranks [n] in full; claim-scope questions for the drafter: [questions].]
- [Gap search suggested for limitation [label].]

## Coverage note

This search covered only US granted patents from 2005 on. Published applications, foreign patents, non-patent literature, and older US patents were not searched. Relevant art may exist outside that coverage, especially for targets with early effective filing dates. It is research, not legal advice, and should be reviewed by a registered patent practitioner.
