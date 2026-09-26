# Chart templates

Output layouts for the `chart` skill: one for each chart type. Replace every bracketed value. Use the citation format from `patent-search-fundamentals` in every citation cell.

---

# Invalidity chart

## Scope

- **Target patent:** US [number], "[title]"
- **Claims charted:** [claim numbers]
- **Effective filing date:** [date], [basis, for example "priority to application [number]"]

| Ref | Reference | Title | Source | Search cat. | Qualifying date(s) | Qualifies? |
|---|---|---|---|---|---|---|
| A | US [number] | [title] | Search | X | [dates] | Yes, [basis] |
| B | US [number] | [title] | User | Y | [dates] | Yes, [basis] |
| C | US [number] | [title] | Gap search, 1[b] | Y | [dates] | Yes, [basis] |
| D | E1: [standard or publication, version] | [title] | User | — | [date shown on the document] | [Yes, [basis] / Unverified: [reason]] |

**Excluded:** [reference and reason, or "None"]

## Search summary

`prior-art-search` ran [n] queries over [n] rounds and found [n] X, [n] Y, and [n] A candidates. The full log is at the end of this chart.

## Summary matrix

| Limitation | Ref A | Ref B |
|---|---|---|
| 1[pre] | Disclosed | Disclosed |
| 1[a] | Disclosed | Partial |
| 1[b] | Not found | Disclosed |
| 1[c] | Inherent | Not found |

## Detailed chart: claim [n]

| Limitation | Claim language | Ref A | Ref B |
|---|---|---|---|
| 1[pre] | "[verbatim claim text]" | **Disclosed.** "[verbatim quotation]" ([citation]) | **Disclosed.** "[verbatim quotation]" ([citation]) |
| 1[a] | "[verbatim claim text]" | **Disclosed.** "[verbatim quotation]" ([citation]) | **Partial.** "[verbatim quotation]" ([citation]). Missing: [what is missing]. |
| 1[b] | "[verbatim claim text]" | **Not found.** Searched for [terms and concepts]. | **Disclosed.** "[verbatim quotation]" ([citation]) |
| 1[c] | "[verbatim claim text]" | **Inherent.** "[verbatim quotation]" ([citation]). Necessarily present because [reason]. | **Not found.** Searched for [terms and concepts]. |

For more than three references, use one table per reference instead, with columns: Limitation, Claim language, Disclosure, Rating, Notes.

For a dependent claim, start the table with: "Includes all limitations of claim [parent]; see that chart." Then chart only the added limitations.

## Proposed grounds

| Ground | Claims | Statute | References |
|---|---|---|---|
| 1 | [claims] | 35 U.S.C. 102 | Ref [X] |
| 2 | [claims] | 35 U.S.C. 103 | Ref [X] in view of Ref [Y] |

**Ground 2 rationale.** [Primary reference] discloses [limitations]. [Secondary reference] supplies [limitation]. A person of ordinary skill would have combined them because [reason, with a quotation and citation from the references where possible]. Expectation of success: [reason]. Analogous art: [same field of endeavor, or reasonably pertinent to the problem of ...].

## Weaknesses and open issues

- **Gaps:** [limitation]: [Partial or Not found] in all references.
- **Claim construction:** [term]: [readings and which one the chart depends on].
- **Means-plus-function:** [term]: [corresponding structure in the target, and whether the references disclose it or an equivalent].
- **Combination risks:** [teaching away, change in principle of operation, or unsatisfactory for intended purpose].
- **Not evaluated:** secondary considerations of non-obviousness.

## Uncharted candidates

Other results from the search and any gap searches. Ask to have any of them charted.

| Patent | Title | Search cat. | Limitations | Why not charted |
|---|---|---|---|---|
| US [number] | [title] | Y | 1[a], 1[b] | [for example, "covers the same limitations as Ref A less closely"] |

## Search log

[The search log table from `prior-art-search`, including any gap-mode queries.]

## Coverage note

This chart is based only on the references listed above. Palisade searched only US granted patents from 2005 on, so published applications, foreign patents, and non-patent literature were not searched unless the user provided them. A limitation marked Not found may still be disclosed in art outside that coverage. It is research, not legal advice, and should be reviewed by a registered patent practitioner.

---

# Infringement chart

## Scope

- **Target patent:** US [number], "[title]"
- **Claims charted:** [claim numbers]
- **Estimated expiration:** [date], [basis; "before term adjustment, term extension, terminal disclaimer, or lapse for unpaid maintenance fees" unless the adjustment is stated on the patent]
- **Accused item(s):** [maker, product or process, model, version]
- **Representative product:** [None, or "[item] charted as representative of [items], as confirmed by the user"]

## Evidence list

| ID | Source | Publisher | Version or date | Location | Retrieved |
|---|---|---|---|---|---|
| E1 | [title] | [publisher] | [version or date] | [URL, or "provided by user"] | [date] |
| E2 | [standard name] | [standards body] | [release] | [URL, or "provided by user"] | [date] |

## Summary matrix

| Limitation | [Accused item 1] | [Accused item 2] |
|---|---|---|
| 1[pre] | Present | Present |
| 1[a] | Present | Partial |
| 1[b] | Equivalent | Not shown |

## Detailed chart: claim [n], [accused item]

| Limitation | Claim language | Evidence | Rating | Notes |
|---|---|---|---|---|
| 1[pre] | "[verbatim claim text]" | "[verbatim quotation]" ([E1, p. n]) | **Present** | [explanation] |
| 1[a] | "[verbatim claim text]" | "[verbatim quotation]" ([E2, § n.n]) | **Present** | [Mandatory ("shall") in E2; product implements [release] per E1, p. n.] |
| 1[b] | "[verbatim claim text]" | "[verbatim quotation]" ([E1, p. n]) | **Equivalent** | Function: [..]. Way: [..]. Result: [..]. Prosecution history: [amendment or argument on this limitation, cited / none found]; estoppel not decided. Vitiation not evaluated. |
| 1[c] | "[verbatim claim text]" | None found. Searched for [terms and concepts] in E1–E[n]. | **Not shown** | Would be shown by [source code, teardown, testing]. |

For a dependent claim, start the table with: "Includes all limitations of claim [parent]; see that chart." Then chart only the added limitations.

## Summary

- **Claim [n], [accused item]:** [Evidence supports every limitation (Present / Present or Equivalent)] or [Evidence does not support limitations [labels]; would be closed by [evidence]].

## Weaknesses and open issues

- **Gaps:** [limitation]: [Partial or Not shown], and the evidence that would close it.
- **Claim construction:** [term]: [readings and which one the chart depends on].
- **Means-plus-function:** [term]: [corresponding structure in the target, and whether the evidence shows it or an equivalent].
- **Standards:** [optional features the chart relies on, and the evidence the product implements them].
- **Who performs:** [divided infringement or multiple-party issues].
- **Not evaluated:** indirect infringement, willfulness, damages, validity, licenses, exhaustion, and legal status.

## Coverage note

This chart reflects only the evidence listed above, and the accused item may have changed since that evidence was published. Palisade has no product information, legal status, or ownership records, and the prosecution history was reviewed only as listed in the notes. It is research, not legal advice, and should be reviewed by a registered patent practitioner.

---

# Claim construction chart

## Scope

- **Target patent:** US [number], "[title]"
- **Claims:** [claim numbers]
- **Terms charted:** [n], [from the user / proposed and confirmed]
- **Perspective:** [Patentee / Accused infringer / Petitioner / Neutral]
- **Prosecution history:** [Appl. No. [number]; papers reviewed: [types and dates] / Not reviewed]

## Construction chart

| Term | Claims | Construction | Intrinsic evidence | Extrinsic evidence |
|---|---|---|---|---|
| "[term]" | [1, 7, 12] | **Proposed:** [construction, or "plain and ordinary meaning: [meaning]"]<br>**Competing:** [construction] | **Supports proposed:** "[verbatim quotation]" ([citation]); claim differentiation from claim [n]: "[verbatim claim text]"<br>**Supports competing:** "[verbatim quotation]" ([citation]) | [E1: "[verbatim quotation]" ([citation]), or "None provided"] |
| "[means for ...]" | [n] | **Function:** "[claim language]"<br>**Structure:** "[verbatim quotation]" ([citation]), and equivalents | "[verbatim quotation]" ([citation]) | [..] |

## Impact

| Term | Limitations | Under proposed | Under competing |
|---|---|---|---|
| "[term]" | 1[c] | [Ref A: Disclosed; Product X: Present] | [Ref A: Partial; Product X: Not shown] |

## Flags

- **Indefiniteness risk:** [term]: [no corresponding structure or algorithm disclosed / no objective standard for a term of degree].
- **Excludes an embodiment:** [construction] would exclude [embodiment], "[verbatim quotation]" ([citation]).
- **Prosecution history:** [term]: [amendment, remark, or reason for allowance, quoted and cited, and any possible disclaimer flagged], or [papers not readable as text that should be checked].

## Coverage note

This chart used only the target patent, related patents in Palisade, and any material the user provided. The prosecution history was [reviewed only as listed in the scope / not reviewed]. It does not predict which construction a court or the Board will adopt. It is research, not legal advice, and should be reviewed by a registered patent practitioner.
