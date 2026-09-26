---
description: Pull up the prosecution history of a US patent or application
argument-hint: "<patent or application number> [question]"
---
Follow the `patent-search-fundamentals` skill, then call the `prosecution_history` tool for the patent or application in:

$ARGUMENTS

If no number was given, ask the user for one. Get the application number the way the `prosecution-history` skill describes, and summarize the index as its "Read the index" step describes.

If the user also asked a question, answer it by running the rest of the `prosecution-history` skill. Otherwise, stop after the summary.

If the Palisade tools aren't available, tell the user to reinstall the plugin or connect Palisade at https://www.palisadeinnovation.com, and stop.
