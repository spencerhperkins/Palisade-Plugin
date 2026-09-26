# Palisade

Palisade is an MCP server that provides vector search capabilities to frontier lab products, including Claude and ChatGPT.  Palisade searches granted US patents from 2005-present using vector search and an efficient HNSW indexing strategy. Laslty, pre-built, but fully customizable workflows for analyzing prior art, invalidity, patentability, freedom to operate, infringement, portfolio review, due diligence, and landscapes.

## Install

In Claude Code, run:

```
/plugin marketplace add spencerhperkins/palisade-plugin
/plugin install palisade@palisade
```

Then run `/mcp`, select Palisade, and sign in in your browser. If Palisade doesn't appear in `/mcp`, restart Claude Code.

To use only the search engine manually, see [palisadeinnovation.com](https://www.palisadeinnovation.com).

## What you get

| Command | Skill | What it does |
|---|---|---|
| (used by all commands) | `patent-search-fundamentals` | Shared reference for every skill: how the search tools work and how to write queries for them, prior-art date rules, patent term, citation format, claim language, and output rules. |
| `/invalidity` | `chart`, `prior-art-search` | Searches for prior art against the claims of a US patent and charts the strongest references, limitation by limitation, with the anticipation and obviousness grounds the chart supports. |
| `/chart` | `chart` | Builds a limitation-by-limitation claim chart of any type: invalidity against a reference, infringement against a product, process, or standard, or claim construction of disputed terms. |
| (no command) | `prior-art-search` | Iterative prior-art search. It reads the full claim sets that semantic search returns to decide which specifications to mine, then follows up with keyword and applicant searches. It does the searching for `/invalidity`, and also runs novelty searches on an invention disclosure or draft claims when asked directly. |
| (no command) | `prosecution-history` | Reads the file wrapper of any US application live from the USPTO Open Data Portal. It lists every paper with the statutes and claims each office action rejected, then pulls only the papers the question needs, such as claim amendments, remarks, or reasons for allowance. `chart` uses it for prosecution disclaimer and estoppel. |

## Example prompts

- `/invalidity US 10,XXX,XXX claim 1`
- `/invalidity US 10,XXX,XXX claims 1-5 vs US 9,XXX,XXX, US 8,XXX,XXX`
- `/chart US 10,XXX,XXX claim 1 invalidity vs US 9,XXX,XXX`
- `/chart US 10,XXX,XXX claims 1 and 12 infringement vs a smart thermostat that learns occupancy from phone location`
- `/chart US 10,XXX,XXX claim 1 infringement vs 3GPP TS 38.331, Release 16`
- `/chart US 10,XXX,XXX claim construction of "substantially aligned" and "control module"`
- `Run a novelty search on: a wearable sensor that estimates hydration from sweat conductivity and adjusts a reminder schedule`
- `What did the applicant argue to overcome the 103 rejections in the prosecution of US 10,XXX,XXX?`

## Coverage and limits

Palisade's search corpus covers US granted patents from 2005 to the present, and nothing else. It does not include published applications, foreign patents, non-patent literature, standards, product information, or legal status (such as maintenance, expiration, assignment, or litigation history). A search that finds nothing in Palisade does not mean no prior art exists. Prosecution histories are read live from the USPTO Open Data Portal for any US application; papers that are not available as text can't be read.

Infringement charts rely on product or standard evidence that you provide or that the session retrieves from public sources. Claim construction charts use the patent's own claims, specification, and prosecution history, plus any PTAB or extrinsic evidence you provide. Confirm expiration, maintenance, and ownership separately before relying on any result.

## Privacy

Your queries and the text you submit are sent to the Palisade server and to your model provider. See the [Palisade data policy](https://www.palisadeinnovation.com/data) for how that data is handled. Do not submit confidential material you are not permitted to share.

## Not legal advice

Palisade is a research tool. Its output is not legal advice, may be incomplete or wrong, and does not replace review by a registered patent practitioner. Read the full [disclaimer](DISCLAIMER.md) before relying on any result.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[Apache-2.0](LICENSE)
