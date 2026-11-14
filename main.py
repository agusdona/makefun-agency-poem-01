"""Agency poem entry: writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8)."""

import os

POEM = """Four Cents

My father tuned pianos forty years
and left the E above middle C a hair
flat. Not wrong, he said. Just his.
He set it the way he set his watch.

Tonight an agent tuned the hall
in nine minutes: eighty-eight strings
to zero, a green tick on every pin.
Backstage I asked it to put the flat back.

His flat, forty years, the one note
he hummed while thinking, the only one
that was truly his. I wanted that one
back in the hall.

The agent asked me to hum it.
It could tune anything except a memory.
My father is dead. I hummed his note:
four cents flat, a guess, a pitch
I mostly wished. It held me
like a hand on the back of my neck.

At the interval I sat at the keys
and heard what I'd asked for:
everything true but the one note
I'd chosen in the dark, holding,
less sure than he would have been,
and mine."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
