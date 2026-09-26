---
description: Build a limitation-by-limitation claim chart for invalidity, infringement, or claim construction
argument-hint: "<patent number> [claim numbers] [invalidity | infringement | construction] [vs <reference, product, or standard>]"
---
Follow the `patent-search-fundamentals` skill, then run the `chart` skill on:

$ARGUMENTS

Choose the chart type as the `chart` skill describes. If the type is still unclear, ask the user before charting.

If the Palisade tools aren't available, tell the user to reinstall the plugin or connect Palisade at https://www.palisadeinnovation.com, and stop.
