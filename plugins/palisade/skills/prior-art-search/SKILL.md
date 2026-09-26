---
name: prior-art-search
description: Runs an iterative prior-art search of US granted patents. It starts with semantic search that returns each result's claims, reads those full claim sets to choose which specifications to mine, then runs keyword searches of specification text with date and applicant filters. It handles invalidity searches against the claims of an issued patent, novelty and patentability searches for an invention disclosure or draft claims, and gap searches for secondary references. Use it when the user wants prior art, a novelty or patentability search, or references for claim limitations missing from a primary reference. The chart skill and the /invalidity command run this skill for their searching.
---

# Prior-art search

Find the closest prior art to a set of claim limitations, rank it, and record how it was found so the search can be checked and repeated.

Follow `patent-search-fundamentals` for the search tools, dates, citations, claim language, and output rules. This skill does not restate them.

## Modes

| Mode | Target | Date cutoff | Called by |
|---|---|---|---|
| **Invalidity** | Claims of an issued US patent | The target's effective filing date | `/invalidity`, `chart`, or a direct request |
| **Novelty** | An invention disclosure or draft claims | The planned filing date, or today if none is given | A direct request |
| **Gap** | Specific limitations missing from a primary reference | Same cutoff as the calling search | `chart`, or a follow-up to either mode above |

Choose the mode from the input. If the input is a patent number, use invalidity mode. If it is prose or claim text with no patent number, use novelty mode. When another skill calls this one, it names the mode.

In every mode, filter on application date before the cutoff, as described under date filters in `patent-search-fundamentals`.

## Workflow

### 1. Set up the target

**Invalidity mode:**

1. Retrieve the target patent. Copy each claim to be searched word for word, and for dependent claims copy every claim they depend on.
2. Record the target's effective filing date. This is the cutoff.
3. Note the target's applicant and inventors, and any related patents that share its specification (parents, continuations, divisionals). Those related patents are excluded from the results.

**Novelty mode:**

1. If the user gave draft claims, use them. If not, write one claim-style statement of the invention from the disclosure and label it "search statement drafted for this search, not a proposed claim".
2. Set the cutoff to the planned filing date if the user gave one, otherwise today.

**Gap mode:** take the limitations, primary reference, and cutoff from the caller, and go straight to step 4, running only the searches for those limitations.

### 2. Break the claim into limitations

1. Split each claim into labeled limitations, keeping the claim's exact words, and add the flags for preambles, defined terms, and means-plus-function terms, all as described under claim language in `patent-search-fundamentals`.
2. Identify the likely **point of novelty**: the limitation or combination the target presents as new. Look at the summary, the stated problem, and how the claims differ from the art described in the background. Weight the search toward it.

Callers such as `chart` reuse this limitation table.

### 3. Build the search vocabulary

Mine the target's specification (or the disclosure) for the words the art is likely to use:

- The claim's own terms.
- Synonyms and alternative terms the specification uses for the same thing.
- Terms the specification defines, and the ordinary terms they replace.
- Terms for the problem solved and the benefit claimed.
- Older or more generic terms for the same component. Earlier art often uses different vocabulary than the target.

Group the vocabulary by limitation. Terms the target coined are usually useless for search; replace them with functional descriptions. Round 1 adds to this vocabulary from the claims of the results.

### 4. Search in rounds

Apply the date filter to every query, and keep a search log.

**Round 1: semantic search, with claims returned.**

Run every semantic query with claims returned. Do not start with claim table search. It returns no claim text, so it gives you nothing to judge which results are worth reading or whose specifications to mine.

Queries:

- The full text of each independent claim being searched.
- A rewritten version of claim 1 in plainer, more generic claim language.
- Each limitation or pair of limitations that carries the point of novelty, phrased as a short claim.
- The limitations the target's key dependent claims add, phrased as short claims.
- In novelty mode, also the disclosure's summary of the invention, phrased as a claim.

Read the claims that come back:

1. Read each result's full returned claim set, not just claim 1. Semantic search ranks on claim 1, but a result's dependent claims and later independent claims often recite limitations its claim 1 leaves out. Together they show how much of the target the result's disclosure is likely to cover.
2. For each result, note which of the target's limitations its claims recite, with the claim number, for example "US 9,123,456, claims 1, 4, and 9".
3. Add the terms the results' claims use for the target's elements to the vocabulary from step 3.

**Round 2: mine the specifications the claims point to.**

1. Shortlist the results whose claim sets:
   - recite the point of novelty in any claim, independent or dependent;
   - recite several of the target's limitations across claim 1 and its dependents;
   - claim the same problem or component in different vocabulary.
   Leave off results whose claims share only the general field.
2. Retrieve each shortlisted patent with patent lookup, starting with the one whose claims cover the most limitations. Mine up to about 10 specifications per round.
3. In each specification, find the passages that describe the limitations its claims recite, then look for the limitations they do not. A claim that recites a feature is a strong sign that the specification describes it in detail. Record the best passage for each limitation, with a pinpoint citation.
4. Take new vocabulary from the specifications: their terms for the same components, and the art they describe in their own backgrounds.

**Round 3: keyword search of specifications.**

- For each limitation, run keyword searches that combine its most distinctive terms and synonyms, including the vocabulary from rounds 1 and 2. Start narrow (several terms that must co-occur), then broaden.
- Give priority to limitations that no shortlisted specification covered.
- Search the problem-and-solution vocabulary: art that solved the same problem, even in a different device, often supplies motivation to combine.
- Keyword hits match specification text but may claim something unrelated. Read a hit's claims before deciding how much of its specification to mine.

**Round 4: applicant search.**

Combine the applicant filter with semantic search with claims returned, and read the returned claims as in round 1.

- The target's own applicant. Its earlier patents are often the closest art. Some of them may be excepted from prior art by common ownership if they qualify only by their filing date; record this as something to check, and do not exclude them yourself.
- Competitors the user names.
- Any applicant that appears several times in rounds 1 to 3.

**Further rounds: iterate.**

1. Rerun semantic search with claims returned, and keyword search, using the new vocabulary.
2. Read the returned claims, and mine the specifications of any new results that meet the round 2 shortlist test.
3. For each limitation that no candidate yet covers, run searches for that limitation alone.

Stop when two rounds in a row add no new X or Y candidates (see step 5), when every limitation is covered by at least one candidate, or after six rounds. Report what remains uncovered.

### 5. Screen and rank the candidates

For each candidate worth keeping:

1. Retrieve it and check whether it qualifies as prior art under the date rules in `patent-search-fundamentals`. Record its application and grant dates and any exception to flag.
2. Exclude the target itself and any patent that shares its specification.
3. Read its full claim set and the specification passages you mined. Identify which limitations it discloses, with a short verbatim quotation and pinpoint citation for the best passage. A limitation recited only in its claims counts as disclosed, but cite the specification passage that supports it where there is one.
4. Assign a category:
   - **X**: appears to disclose every limitation of at least one claim on its own. Candidate for anticipation.
   - **Y**: discloses the point of novelty or several key limitations. Useful alone for obviousness or combined with another reference.
   - **A**: relevant background. Discloses individual limitations or the general field.

Categories are screening judgments, not charted findings. `chart` confirms them limitation by limitation.

Rank X before Y before A, and within a category by how many limitations the candidate covers and how closely.

### 6. Novelty read-out (novelty mode only)

For each draft claim or search statement:

1. **Anticipation risk**: name any X candidate and the claim it appears to read on.
2. **Obviousness risk**: name the Y candidates, or pairs of them, that together cover every limitation, with a one-line reason a person of ordinary skill might combine them.
3. **Distinguishing limitations**: the limitations, or combinations, that no candidate covers. These are where the disclosure appears to differ from the art found.
4. **Focus for claim drafting**: which details in the disclosure, not yet in the claims or search statement, add the most distance from the closest art. Point to the disclosure's own words; do not draft claims unless the user asks.

Never state that an invention is novel or patentable. Say what the search found, for example "no candidate found discloses limitation 1[c]."

## Output

Use the layout in [search-report-template.md](search-report-template.md):

1. **Target**: mode, target, claims, cutoff, and the limitation table with the point of novelty and any flags.
2. **Results summary**: the number of X, Y, and A candidates, and any limitations that no candidate covers.
3. **Candidates**: a ranked table with dates, category, limitations covered, and the best passage for each.
4. **Coverage matrix**: limitations against the top candidates.
5. **Novelty read-out**: novelty mode only, as described in step 6.
6. **Search log**: every query with its tool, filters, and yield, and every specification mined.
7. **Next steps**: for invalidity, which candidates to chart with `chart`; for novelty, which references to review in full and any claim-scope questions for the drafter; plus any gap searches worth running.
8. **Coverage note**: the note from `patent-search-fundamentals`, adding that for targets with early effective filing dates much of the relevant art may predate the corpus.

When another skill calls this one, return the same content for the caller to use; do not repeat the full report in the caller's output unless the user asks.

## Rules

- Follow the output rules in `patent-search-fundamentals`.
- Finding nothing does not mean no prior art exists. Say so whenever a limitation is uncovered.
