---
description: Search for prior art against a US patent's claims and chart the strongest references
argument-hint: "<patent number> [claim numbers] [vs <references>]"
---
Follow the `patent-search-fundamentals` skill, then run the `chart` skill as an invalidity chart on:

$ARGUMENTS

The `chart` skill runs `prior-art-search` in invalidity mode to find references, unless the user asks to chart only the references they named. If the user asks only for a search, run `prior-art-search` in invalidity mode and stop.

If the Palisade tools aren't available, tell the user to reinstall the plugin or connect Palisade at https://www.palisadeinnovation.com, and stop.
