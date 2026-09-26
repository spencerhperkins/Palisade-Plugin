---
name: prosecution-history
description: Reads the prosecution history (file wrapper) of any US patent application, live from the USPTO Open Data Portal. It lists every paper first, with its category, the statutes and claims each office action rejected, the rounds of action and response, and whether the paper is readable as text, then pulls only the papers the question needs. Use it when the user asks about an application's prosecution, office actions, rejections, amendments, applicant arguments, interviews, or reasons for allowance, or when a claim construction or infringement chart needs prosecution disclaimer or estoppel evidence.
---

# Prosecution history

Read the file wrapper of a US application and pull only the papers that answer the question, with every quotation traced to the paper it came from.

Follow `patent-search-fundamentals` for citations, claim language, and output rules. This skill does not restate them.

## Tools

| Tool | Returns | Use it for |
|---|---|---|
| **`prosecution_history`** | Every paper in the file wrapper, with its category, the statutes and claims each office action rejected, the rounds of action and response, and whether the paper is readable as text | Always call it first, to plan which papers to read |
| **`prosecution_document_text`** | The text of specific papers | Reading the papers the question needs |

Both come live from the USPTO Open Data Portal and work for any US application, not just the patents in the Palisade corpus. That includes pending and abandoned applications and patents granted before 2005.

`prosecution_document_text` selects papers in one of two ways:

- **By `document_ids`** taken from the `prosecution_history` list. Use this when you already know which papers you want.
- **By category**, such as `claims`, `claim_amendments`, `rejections`, `remarks`, `interviews`, or `allowance`, with `which` set to `latest`, `all`, or `first`.

For one statute of an office action, pass `section`, for example `section: "103"`, instead of pulling the whole action.

## Workflow

### 1. Identify the application

Take the application or patent number from the user or the calling skill. If the tool needs an application number and you have only a patent number in the corpus, get the application number from patent lookup. For a continuation or divisional, prosecution of the parent can also matter; say so, and read the parent's history only if the question needs it.

### 2. Read the index

Call `prosecution_history` and summarize it before pulling any text:

- the rounds of action and response, in order, with dates;
- for each office action, the statutes and claims rejected;
- interviews, and the notice of allowance or final disposition;
- any paper that is not readable as text.

For a question about the history as a whole, such as "how many rejections did it get?" or "which statutes were raised?", the index may be enough. Answer from it and stop.

### 3. Pull only what the question needs

Choose the narrowest request that answers the question:

| Question | Pull |
|---|---|
| What claims issued, or what are the pending claims? | `claims`, `latest` |
| What claims were originally filed? | `claims`, `first` |
| How did the claims change, and when? | `claim_amendments`, `all` |
| What art did the examiner apply against the claims? | `rejections`, with `section: "102"` or `"103"`, for the round that matters |
| Were there 101 or 112 rejections, and on what grounds? | `rejections`, with `section: "101"` or `"112"` |
| What did the applicant argue to get around the art? | `remarks` for the response to that rejection, plus the `claim_amendments` filed with it |
| Why was it allowed? | `allowance`, `latest` |
| What was agreed in an interview? | `interviews` |
| Where does a pending application stand now? | `rejections`, `latest`, and `remarks`, `latest` |

Use the index to target a round with `document_ids` rather than pulling `all` when only one round matters. Pull `all` only when the question depends on the whole sequence, such as tracing how one limitation entered the claims.

### 4. Trace a limitation or term

When a chart or the user needs the history of one limitation or claim term, typically for prosecution disclaimer in claim construction or amendment-based estoppel in an equivalents analysis:

1. Find the round where the limitation was added or narrowed: compare `claim_amendments` across rounds, or `claims` `first` against `latest`.
2. Pull the rejection that prompted the amendment, using `section` for the statute involved.
3. Pull the `remarks` filed with the amendment, and quote every statement about the limitation or term, word for word.
4. Pull any `interviews` summaries from that round, and the reasons for allowance if they mention the limitation.
5. Report what the record shows: the original language, the amended language, the rejection it responded to, and the applicant's statements. Flag possible disclaimer or estoppel without deciding it.

### 5. Papers that are not readable as text

If a paper the question needs is not readable as text, say which paper it is (category and date), and ask the user to provide its text if it matters. Never describe the contents of a paper you could not read.

## Output

1. **Application**: the application number, the patent number if granted, the title if shown, and the current status.
2. **Prosecution summary**: the rounds of action and response from the index, with the statutes and claims rejected in each.
3. **Answer**: the answer to the user's question, with verbatim quotations from the papers read, each cited to its paper.
4. **Papers read**: every paper pulled, by category and date, and any needed paper that was not readable as text.
5. **Coverage note**: the note from `patent-search-fundamentals`, adding which papers were read and that any paper not listed was not reviewed.

When another skill calls this one, return the same content for the caller to use; do not repeat the full summary in the caller's output unless the user asks.

## Rules

- Follow the output rules in `patent-search-fundamentals`.
- Pull only what the question needs. The file wrapper of a long prosecution is large, and reading all of it wastes context without improving the answer.
- Quote the examiner and the applicant as written. Keep the examiner's statements and the applicant's arguments clearly attributed, and never merge them.
- An examiner's rejection is not a finding that the claims are unpatentable, and an allowance is not a finding that they are valid. Report what each paper says.
- Never state that prosecution disclaimer or estoppel applies. Say what the record shows and flag the issue.
