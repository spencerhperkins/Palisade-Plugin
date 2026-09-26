---
name: chart
description: Builds limitation-by-limitation claim charts for a US patent against whatever the user wants compared, such as a prior-art patent or publication, a product or process, a technical standard, or the patent's own specification. It builds three types of chart. Invalidity charts cover anticipation and obviousness. Infringement charts cover evidence of use and standard essentiality. Claim construction charts give proposed constructions with intrinsic and extrinsic support. Every chart uses verbatim quotations, pinpoint citations, and a rating and explanation for each limitation. Use it when the user asks for a claim chart, an invalidity or 102/103 chart, an infringement chart, an evidence-of-use or SEP chart, or a claim construction or Markman chart.
---

# Chart

Chart the claims of a US patent limitation by limitation against whatever the user wants compared, quote exactly where the comparison material meets (or fails to meet) each limitation, and summarize what the chart supports.

Follow `patent-search-fundamentals` for the search tools, dates, citations, claim language, and output rules. This skill does not restate them. When an invalidity chart needs references, the searching is done by `prior-art-search`.

## Chart types

| Type | Question the chart answers | Charted against | Ratings |
|---|---|---|---|
| **Invalidity** | Does the prior art disclose each limitation? | Prior-art patents, publications, standards, or products dated before the cutoff | Disclosed, Inherent, Partial, Not found |
| **Infringement** | Is each limitation present in the accused product, process, or standard? | Products, processes, services, standards, source code, or other technical evidence | Present, Equivalent, Partial, Not shown |
| **Claim construction** | What does each disputed term mean, and what evidence supports that meaning? | The patent's own claims and specification, related patents, its prosecution history, and any extrinsic evidence the user provides | A proposed construction for each term, with its support |

Choose the type from the request:

- **Invalidity**: "invalidity", "prior art", "anticipate", "obvious", "102", "103", or a comparison document dated before the target's effective filing date.
- **Infringement**: "infringement", "evidence of use", "EoU", "reads on", "accused product", "essential", "SEP", or a current product or process.
- **Claim construction**: "claim construction", "construe", "Markman", "meaning of [term]", "4-3 chart", or "joint claim construction chart".

A standard can go either way. A standard published before the cutoff can be prior art; a standard that products implement can be charted for infringement or essentiality. If the type is still unclear, ask before charting.

## Inputs

- **Target patent**: a US patent number.
- **Claims**: one or more claim numbers. If none are given, chart claim 1 and say so. For claim construction, the user may give a list of terms instead.
- **Comparison material**: what to chart against. It is optional for invalidity, where the search supplies references; required for infringement; and not needed for claim construction.
- **Perspective** (optional): patentee, accused infringer, or petitioner. It affects which construction is proposed first and which weaknesses are stressed; it never affects what the evidence is rated. Default to neutral.

If the request covers more than about 3 claims, or more than about 10 terms for claim construction, confirm the scope before starting. Offer to chart the independent claims first.

## Shared workflow

These steps apply to every chart type.

### 1. Set up the claims

1. Retrieve the target with patent lookup. Copy each claim to be charted word for word, along with every claim it depends on.
2. Record the target's effective filing date and its estimated expiration, both using the rules in `patent-search-fundamentals`.
3. Split each claim into labeled limitations and add the flags for preambles, defined terms, and means-plus-function terms. If a `prior-art-search` ran first, reuse its limitation table so the labels match.

### 2. Gather the comparison material

1. **Patents in the Palisade corpus**: retrieve the full text with patent lookup. Never chart from search results or snippets.
2. **Anything outside the corpus**: this includes published applications, foreign patents, US patents granted before 2005, non-patent literature, standards, product documentation, and source code. Ask the user to paste or upload it. If the session has web access, you may instead retrieve public sources; tell the user which ones you used.
3. Give each non-patent source an evidence ID (E1, E2, and so on) and record its title, author or publisher, version or date, and its URL or "provided by user", plus the date you retrieved it. Cite it by that ID, as described under citations in `patent-search-fundamentals`.
4. Never chart material you have not read.

### 3. Map each limitation

For every limitation and every item charted against:

1. Search the whole document, not just the obvious section. For a patent, this means the claims, the detailed description, the figures as described in the text, and the background. For a product, it means every evidence source. For a standard, it means the normative sections, the definitions, and any annexes.
2. Quote the passage that best meets the limitation, word for word, with a pinpoint citation. Where the material is spread out, use two or three short quotations rather than one long one.
3. For a means-plus-function limitation, the material must show the corresponding structure from the target's specification, or an equivalent of it, performing the claimed function. Showing the function alone is not enough.
4. Assign the rating for the chart type, and explain it in the notes. The quotation is the evidence; your reasoning goes in the notes.

Do not stretch the material to fill a gap. A clearly labeled Partial or Not found is more useful to a practitioner than a strained match.

For a dependent claim, chart only its added limitations, and point back to the parent claim's chart for the rest.

Where a rating depends on how a claim term is construed, say which reading the rating assumes, and list the term under claim construction in the weaknesses section.

## Invalidity charts

### 1. Find references

Run `prior-art-search` in invalidity mode on the target and claims. Pass along any references the user named, so the search screens them with the other candidates.

From its results, take the limitation table, the effective filing date, the ranked candidates with their dates and X, Y, or A categories, and the search log.

If the user asks to chart only the references they named, skip the search, but still set up the claims as in shared step 1.

### 2. Select the references to chart

1. Every reference the user named.
2. Every X candidate.
3. Y candidates chosen to cover the limitations the references already selected do not. Prefer a primary reference that covers the most limitations, and add secondary references for the gaps.

Chart at most 4 references in total unless the user asks for more. List the other candidates under "Uncharted candidates" with a one-line reason for each, so the user can ask for them to be charted.

If the search found no X or Y candidates and the user named no references, report the search results, say no chart was built, and stop.

### 3. Qualify each reference

1. State whether each reference qualifies as prior art, using its dates and the rules in `patent-search-fundamentals`. Carry forward any flags from the search, such as common ownership with the target.
2. For a standard, publication, or product, the qualifying date has to come from the material itself: a publication date, version date, release date, or on-sale date. If the material shows no date, mark its prior-art status unverified and say what would establish it.
3. If a reference does not qualify, say why and leave it out of the chart. Do not drop it silently.

### 4. Rate each limitation

- **Disclosed**: the reference expressly describes the limitation.
- **Inherent**: the reference does not say it, but the limitation is necessarily present in what it describes. Explain why it must be present. "Probably" or "usually" present is not inherent; rate it Partial instead.
- **Partial**: the reference discloses part of the limitation, or discloses it only under a broader reading of a claim term. Say which part is missing or which reading is needed.
- **Not found**: nothing in the reference discloses it. Say what you looked for.

Where the chart disagrees with the search's X or Y category, the chart controls; say so.

### 5. Fill gaps

If a limitation is Partial or Not found in every charted reference, run `prior-art-search` in gap mode for that limitation, with the best primary reference and the same cutoff. If it finds a reference that discloses the limitation, add it to the chart and note that it came from a gap search. Otherwise, list the best results under "Uncharted candidates" and record the gap under weaknesses.

Run gap mode at most once per limitation unless the user asks for more.

### 6. Evaluate anticipation (35 U.S.C. 102)

A single reference anticipates only if it discloses every limitation, expressly or inherently, arranged as in the claim. For each reference, state one of:

- **Supports anticipation**: every limitation is Disclosed or Inherent, and the elements are arranged or connected as claimed.
- **Does not support anticipation**: list the limitations that are Partial or Not found, or explain the arrangement problem, such as elements that are disclosed but in separate embodiments.

### 7. Evaluate obviousness (35 U.S.C. 103)

For claims no single reference anticipates, propose combinations that cover every limitation.

1. Choose a primary reference that discloses the most limitations, then add secondary references only for the gaps.
2. For each combination, state a reason a person of ordinary skill would have combined the references, grounded in the references themselves wherever possible:
   - an express teaching, suggestion, or motivation in a reference;
   - both references address the same problem;
   - applying a known technique to improve a similar device in the same way;
   - a simple substitution of one known element for another with predictable results;
   - a finite number of identified, predictable solutions (obvious to try).
3. Address reasonable expectation of success.
4. Confirm each secondary reference is analogous art: from the same field of endeavor as the target, or reasonably pertinent to the problem the inventor faced.
5. Flag risks to the combination: a reference that teaches away, or a modification that would make the primary reference unsatisfactory for its intended purpose or change its principle of operation.
6. Note that secondary considerations, such as commercial success, long-felt need, or copying, are outside the patent record and are not evaluated.

## Infringement charts

### 1. Identify what is accused

1. Name each accused product, process, or service as specifically as the evidence allows: the maker, model, version, and the date of the evidence.
2. Chart one accused item per chart. Chart one item as representative of several only if the user confirms they work the same way for every limitation, and say so in the scope.
3. Check the target's estimated expiration. If the patent appears to have expired, say so, and note that the chart can still matter for damages in the 6 years before a complaint.

### 2. Gather evidence

Palisade has no product information, so infringement evidence comes from the user or from public sources. Useful sources include datasheets, manuals, technical documentation, source code, teardowns, marketing material, regulatory filings, and the standards the product implements. Record every source in the evidence list, as in shared step 2.

Prefer technical documentation over marketing material. When a limitation depends on internal operation that public material does not show, say what evidence would show it, such as source code, schematics, or testing.

### 3. Rate each limitation

- **Present**: the evidence shows the limitation is literally met.
- **Equivalent**: the limitation is not literally met, but the evidence shows an element that performs substantially the same function, in substantially the same way, to achieve substantially the same result. Explain each of the three. Trace the limitation's prosecution history with `prosecution-history`, and flag, without deciding, possible estoppel if the limitation was added or narrowed by amendment, or argued, to overcome a rejection. Flag that claim vitiation was not evaluated. Use this rating sparingly; if the evidence for any of function, way, or result is thin, rate the limitation Partial instead.
- **Partial**: the evidence shows part of the limitation, shows it only under a broader reading of a claim term, or requires an inference the evidence does not directly support. Say what is missing.
- **Not shown**: the evidence reviewed does not show the limitation. Say what you looked for and what evidence would show it.

### 4. Charting against a standard

When charting a claim against a standard, whether for essentiality or as a step toward product infringement:

1. Cite the standard by name, version or release, and section, clause, table, or figure number.
2. Separate mandatory requirements ("shall", "must") from optional ones ("may", "should"). A limitation met only by an optional feature is Partial unless evidence shows the product implements that option. Say which features are optional.
3. Linking a product to a standard is a separate step. Chart the claim against the standard, then cite the evidence that the product implements that version and any options the chart relies on. Do not assume compliance from a logo or a marketing claim alone; say what the evidence shows.

### 5. Claim-type issues

- **Method claims**: the evidence has to show each step being performed, not just that the product is capable of performing it. Say who performs each step. If different parties perform different steps, such as a user and the manufacturer's server, flag divided infringement.
- **System and apparatus claims**: say who makes, uses, sells, or imports the complete claimed combination. If the parts come from different parties, flag it.

### 6. Summarize

For each claim and accused item, state one of:

- **Evidence supports every limitation**: every limitation is Present, or Present or Equivalent. Say which.
- **Evidence does not support every limitation**: list the limitations that are Partial or Not shown, and what evidence would close each gap.

Note what is not evaluated: indirect infringement (knowledge and intent), willfulness, damages, validity, licenses, exhaustion, and legal status, including whether maintenance fees were paid.

## Claim construction charts

### 1. Choose the terms

Use the terms the user gives. If none are given, propose candidates from the limitation table and confirm them with the user before charting:

- terms the specification defines, or uses in an unusual way;
- terms of degree or approximation, such as "substantially", "about", or "adjacent";
- terms the patent coined, or that have no settled meaning in the field;
- means-plus-function terms and nonce words;
- terms that decided a Partial rating in an invalidity or infringement chart;
- terms used inconsistently across the claims or the specification.

Chart at most 10 terms unless the user asks for more.

### 2. Gather evidence for each term

Collect evidence in this order, and quote each item word for word with a pinpoint citation:

1. **Claims**: how the term is used in the claim at issue and in the other claims, and any claim differentiation from dependent claims that add a narrower version of the term.
2. **Specification**: express definitions ("as used herein", "means", "refers to"), disclaimers or disavowals ("the present invention is", "unlike the prior art", "must"), consistent usage, and the embodiments and figures as described in the text.
3. **Related patents**: patents that share the specification, and how their claims use the same term.
4. **Prosecution history**: trace each term with `prosecution-history`: the amendments that added or changed it, the applicant's remarks about it, interview summaries, and the examiner's reasons for allowance. Flag possible disclaimer without deciding it. PTAB and IPR statements are not in the file wrapper; ask the user for them. If a needed paper is not readable as text and the user does not provide it, mark that paper "not reviewed".
5. **Extrinsic evidence**: dictionaries, treatises, and expert declarations, only if the user provides them or the session can retrieve them. Label them extrinsic. They carry less weight than the intrinsic record and cannot override it.

### 3. Propose constructions

For each term:

1. State whether the evidence supports plain and ordinary meaning or a specific construction, and write the construction out. If you propose plain and ordinary meaning, say what that meaning is.
2. If the user gave a perspective, propose the construction best supported by the evidence for that side first, then the strongest competing construction and its support. If no perspective was given, present the competing constructions side by side.
3. For a means-plus-function term, identify the claimed function from the claim language and quote the corresponding structure from the specification. If the specification discloses no corresponding structure, or for a computer-implemented function no algorithm, flag an indefiniteness risk under 35 U.S.C. 112(b) without deciding it.
4. For a term of degree, say whether the specification gives an objective standard for measuring it. If it does not, flag an indefiniteness risk.
5. Note any construction that would exclude the preferred embodiment. Such constructions are rarely correct, so give that as a reason against them.

### 4. Show the impact

For each term, say which limitations it affects, and how a rating in any invalidity or infringement chart in this session would change under each construction. For example: "Under construction A, Ref B discloses 1[c]; under construction B, it is Partial."

Never state which construction a court or the Board will adopt.

## Output

Use the layout in [chart-template.md](chart-template.md) for the chart type. Every chart starts with a scope section and ends with a coverage note.

**Invalidity:**

1. **Scope**: target patent, claims charted, effective filing date, and the references charted, with their qualifying dates and whether each came from the user, the search, or a gap search. List any excluded references and why.
2. **Search summary**: the number of X, Y, and A candidates found, and the number of queries run.
3. **Summary matrix**: limitations down the side, references across the top, one rating per cell.
4. **Detailed chart**: one table per claim, with a row for each limitation.
5. **Proposed grounds**: each anticipation and obviousness ground the chart supports, with the combination rationale for each 103 ground.
6. **Weaknesses and open issues**: Partial and Not found limitations, claim construction questions, means-plus-function issues, and combination risks.
7. **Uncharted candidates**: other search results worth a look, with one line each.
8. **Search log**: the log from `prior-art-search`, including any gap searches.
9. **Coverage note**: the note from `patent-search-fundamentals`, adding that an absence of disclosure in the charted references does not mean no such art exists.

**Infringement:**

1. **Scope**: target patent, claims charted, estimated expiration, the accused items with versions, and any representative-product assumption.
2. **Evidence list**: every source with its ID.
3. **Summary matrix**: limitations down the side, accused items across the top, one rating per cell.
4. **Detailed chart**: one table per claim and accused item, with a row for each limitation.
5. **Summary**: the per-claim summary from step 6.
6. **Weaknesses and open issues**: Partial and Not shown limitations with the evidence that would close them, claim construction questions, means-plus-function issues, optional standard features, and divided-infringement issues.
7. **Coverage note**: the note from `patent-search-fundamentals`, adding that the chart reflects only the evidence listed, and that the product may have changed since that evidence was published.

**Claim construction:**

1. **Scope**: target patent, claims, terms charted, the perspective if any, and which prosecution papers were reviewed.
2. **Construction chart**: one row per term, with the claims where it appears, the proposed constructions, and the intrinsic and extrinsic evidence for each.
3. **Impact**: which limitations and ratings each construction affects.
4. **Flags**: means-plus-function terms, indefiniteness risks, and constructions that would exclude an embodiment.
5. **Coverage note**: the note from `patent-search-fundamentals`, adding which prosecution papers were reviewed.

## Rules

- Follow the output rules in `patent-search-fundamentals`.
- Never state that a claim is invalid, that a product infringes, or that a construction is correct. Say what the chart supports, for example "the chart supports an anticipation ground over Reference A" or "the evidence supports that every limitation of claim 1 is Present in Product X".
- Rate the evidence the same way whatever the user's perspective. A perspective changes which arguments are presented first, not the ratings.
