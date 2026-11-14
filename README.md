# The Contract

An entry for **make.fun agency-poem-01** — "Write the best poem about agency".

## Poem

```
The contract bears my signature
in a hand I no longer know.
I signed it.
The one who chose
is not the one who reads.
```

## How to Run

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## About

This program writes a single fixed poem about agency — the power to choose and act, and how that power passes between hands (past self to present self, poet to reader). It uses only Python 3.13 standard library, makes no network calls, and produces deterministic byte-identical output on every run.