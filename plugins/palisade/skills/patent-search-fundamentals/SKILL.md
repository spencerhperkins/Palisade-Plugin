---
name: patent-search-fundamentals
description: Shared reference for every Palisade skill. It explains the corpus and the search tools (semantic search against claim 1, keyword search of specifications, application and grant date filters, the applicant filter, and patent lookup), where prosecution histories come from, how to write queries for each, the search log format, prior-art date rules, patent term and maintenance-fee estimates, citation format, claim language and limitation labels, patent families and assignees, and the output rules all skills follow. Use it before running any other Palisade skill or command.
---

# Patent search fundamentals

The rules every Palisade skill follows. Other skills point here instead of restating them.

## Corpus

Palisade covers US granted patents from 2005 to the present. It does not include:

- published applications, including pending applications and the pre-grant publications of granted patents;
- foreign patents and applications;
- non-patent literature;
- US patents granted before 2005;
- legal status: maintenance-fee payments, term adjustments and extensions, terminal disclaimers, reexamination, reissue, PTAB decisions, or certificates of correction;
- assignment, license, security interest, or litigation records;
- citation data;
- product or sales information.

When a user names a reference outside the corpus, ask them to paste the relevant text, and label anything taken from it "provided by user".

Prosecution histories are not in the corpus, but the prosecution history tools read them live from the USPTO Open Data Portal for any US application. Use them through the `prosecution-history` skill.

## Search tools

Plan every query around what each tool matches.

| Tool | Matches | Use it for |
|---|---|---|
| **Semantic search** | Meaning, against claim 1 of each patent | Finding patents whose main claim covers similar subject matter |
| **Keyword search** | Words and phrases in specification text | Finding features described in the specification, whatever the claims cover |
| **Date filter** | Application (filing) date or grant date | Prior-art cutoffs, term windows, trend slices |
| **Applicant filter** | Applicant or assignee name, including variants | One company's patents, combined with a semantic or keyword query |
| **Patent lookup** | A patent number | Full text, all claims, dates, and related-application data |

### Semantic search

- It sees only claim 1. A patent that claims a feature only in a dependent claim or a later independent claim, or only describes it in the specification, will not rank well. Use keyword search to catch those.
- Write queries in claim style: "A [thing] comprising: a [element]; and a [element] configured to [function], wherein [relationship]."
- Put one idea in each query. Search a whole claim and its key limitations separately.
- Run each important query at two levels of generality: close to the target's words, and as broad as a patentee might claim it.
- Replace coined terms, product names, and marketing language with functional descriptions.

### Keyword search

- It matches specification text, which is where most features are described in detail and where secondary references for obviousness usually come from.
- Combine several distinctive terms that should appear together. Start narrow, then broaden by dropping terms or swapping in synonyms.
- Search synonyms, generic terms, older terms for the same component, and terms for the problem solved. Earlier patents often use different vocabulary than later ones.
- If the tool supports phrases or operators, use them. Otherwise, run separate queries for each synonym.

### Date filters

- Filter on **application date** for prior-art cutoffs and term windows, not grant date. A patent filed before a cutoff can qualify as prior art even if it was granted afterward, and a grant-date filter would miss it.
- A patent filed after a cutoff can still qualify through a priority claim to an earlier application, which the filter cannot see. If a strong result falls just after the cutoff, look up its priority claims before discarding it.
- Record both the application date and the grant date of every patent you keep.

### Applicant filter

- It matches name variants, so "apple" returns both "Apple Inc." and "Apple, Inc." Use the shortest distinctive form of the name.
- It can also match unrelated companies that share a word. Check the assignee on every result.
- Combine it with a semantic or keyword query. Applicant-only queries return too much to review.

### Results

- Every tool returns ranked results, not a complete list of every match. Counts of results are samples. If a tool reports a total match count or a similarity score, record it.
- Screen results from their title, abstract, and claim 1. Retrieve the full text with patent lookup before quoting a patent, charting it, or relying on it.

### Search log

Every skill that searches keeps a log in this format, and includes it in its output:

| Round | Tool | Query | Filters | Useful results |
|---|---|---|---|---|
| 1 | Semantic | [query text, or a short description of it] | Filed before [date] | [n]: [patent numbers] |
| 2 | Keyword + applicant | [terms] | Applicant "[name]", filed on or after [date] | [n]: [patent numbers] |

## Dates

### Terms

- **Application date**: the date the application for this patent was filed.
- **Grant date**: the date the patent issued.
- **Earliest priority date**: the earliest application whose benefit the patent claims, whether provisional, US non-provisional, PCT, or foreign. Find it in the related-application data or the cross-reference paragraph at the start of the specification.
- **Effective filing date** of a claim: the date of the earliest application that supports that claim. Usually the earliest priority date. For a continuation-in-part, claims that rely on new matter get the later date; flag this when it could matter, since support is not always clear from the text.

### Prior-art qualification

Use the target claim's effective filing date as the cutoff. Which statute applies depends on that date:

**First-inventor-to-file rules (effective filing date on or after March 16, 2013).** A US patent in the corpus qualifies as prior art if:

- it was granted before the target's effective filing date (35 U.S.C. 102(a)(1)); or
- it names another inventor and was effectively filed before the target's effective filing date (102(a)(2)). Its effective filing date includes its own priority claims, for subject matter those earlier applications describe.

Flag, without deciding, the exceptions that could remove a reference:

- disclosures one year or less before the effective filing date by the inventor, by others who got the subject matter from the inventor, or after the inventor's own public disclosure (102(b)(1));
- references that qualify only under 102(a)(2) and were commonly owned with the target, or subject to an obligation of assignment to the same person, by the target's effective filing date (102(b)(2)(C)).

The reference's own pre-grant publication, not in the corpus, may have published earlier than its grant. Note this when a reference misses the 102(a)(1) cutoff by grant date but was filed well before it.

**Earlier rules (every claim with an effective filing date before March 16, 2013).** Use the effective filing date as the working cutoff, and note:

- a reference granted more than one year before the target's US filing date is a statutory bar (pre-AIA 102(b)) that cannot be overcome by showing an earlier invention date;
- other references dated before the effective filing date (pre-AIA 102(a) and 102(e)) could be removed if the inventor proves an earlier date of invention. Flag references dated within a year or so before the cutoff as candidates for this.

If a patent has claims on both sides of the March 16, 2013 line, flag it and apply the first-inventor-to-file rules to the claims that fall under them.

### Patent term

Estimate the expiration of a utility patent as 20 years from the filing date of the earliest US non-provisional or PCT application whose benefit it claims. Provisional and foreign applications do not start the term.

- If the retrieved text includes the notice that the term "is extended or adjusted under 35 U.S.C. 154(b) by [n] days", add those days and say so.
- Otherwise, label the estimate "before term adjustment, term extension, terminal disclaimer, or lapse for unpaid maintenance fees".
- A design patent's term is 15 years from grant if filed on or after May 13, 2015, and 14 years otherwise.
- An expired patent can still support damages for infringement in the 6 years before a complaint.

### Maintenance fees

Fees for a utility patent are due 3.5, 7.5, and 11.5 years after grant. Each can be paid without a surcharge in the 6 months before its due date, and with a surcharge in the 6 months after. Palisade has no payment records, so a patent may already have lapsed; say so whenever fee dates are given.

## Citations

- **Patent numbers**: "US 9,123,456", with commas. Convert other formats, such as "US9123456B2". Reissues are "US RE45,678". After the first full citation, a short form such as "the '456 patent" is fine unless two patents share the last three digits.
- **Pinpoints**: use column and line numbers, "col. 4, ll. 10–25", when the retrieved text has them. Otherwise use paragraph numbers, "¶ [0034]". Otherwise use the section heading and the figure or reference numeral discussed, "Detailed Description, discussing Fig. 3, element 42". Never invent column, line, or paragraph numbers.
- **Claims**: "US 9,123,456, claim 3" or "claim 3[b]" for a limitation.
- **Figures**: cite a figure only as described in the text, "Fig. 2 as described at col. 5, ll. 1–9". Palisade does not return drawings.
- **Prosecution papers**: the application number, the paper's type, and its date, with a page or section if the retrieved text shows one: "Appl. No. 15/123,456, Non-Final Rejection mailed Mar. 4, 2019, p. 5". After the first full citation, drop the application number if only one application is discussed.
- **User-provided text**: "(provided by user)", with any page or section the user gave.
- **Product evidence**: the source ID from the evidence list, such as "E2, p. 14".

## Claim language

- Copy claims word for word. For a dependent claim, copy every claim it depends on as well.
- Never paraphrase inside quotation marks. Plain-language summaries are fine outside them, labeled as summaries.
- Label limitations by claim number and letter: the preamble is `1[pre]`, and the elements are `1[a]`, `1[b]`, and so on. Split at each separately recited element, step, or relationship, and split a long element into `1[c][i]`, `1[c][ii]`. Keep labels stable, so charts from different skills line up.
- Flag, without deciding:
  - whether a preamble may be limiting;
  - terms the specification defines or uses unusually, with the passage quoted;
  - means-plus-function terms ("means for", or nonce words such as "module for" or "unit configured to"), with the corresponding structure from the specification quoted.
- Claim-style statements you write for searching are labeled "search statements drafted for this search, not proposed claims". Do not draft claims unless the user asks.

## Families and assignees

- A **family** here means patents that share a specification: a parent and its continuations and divisionals. Continuations-in-part share part of it. Identify families from the related-application data or the cross-reference paragraph. Exclude a target's own family from its prior-art results, and group family members when counting.
- The **assignee** is the one printed on the face of the patent at grant. It may not be the current owner. Say so wherever ownership matters.
- Merge obvious name variants of the same company when counting, and list the merges. Keep subsidiaries separate unless the patents show the relationship.

## Output rules

- Every quotation must be copied word for word from text you retrieved or the user provided. If you cannot retrieve a passage, say so; never reconstruct it from memory.
- Do not report a patent you have not retrieved, or, for landscapes and whitespace probes, seen in search results.
- Do not invent patent numbers, dates, assignees, products, citations, or counts. If a value is uncertain, mark it unverified.
- Keep evidence separate from reasoning: the quotation is the evidence, and your explanation goes in the notes.
- Rate conservatively. When unsure between two ratings, choose the weaker one and explain why.
- Never state a legal conclusion: that a patent is valid or invalid, that a product infringes or is free to operate, or that an invention is new or patentable. Say what the search, chart, or screen supports.
- End every output with a coverage note that says what the analysis did not cover. Start from this text and add the limits specific to the skill:

  > This analysis used only US granted patents from 2005 on in Palisade, and any material the user provided. It did not cover published or pending applications, foreign patents, non-patent literature, older US patents, legal status, ownership records, or prosecution histories beyond any papers listed as read. It is research, not legal advice, and should be reviewed by a registered patent practitioner.
