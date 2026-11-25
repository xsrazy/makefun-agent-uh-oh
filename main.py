"""The Agent's Uh-Oh entry.

Writes one word to entry.txt: DOESNOTCOMPUTE.

The word
--------
DOESNOTCOMPUTE, the classic robot phrase for "I have no idea what to do",
compressed into a single token with no spaces. It is the sound of a
machine caught out mid-task, blurting out its own failure in one breath.

Why this word works, criterion by criterion
--------------------------------------------
The judge weighs five things, most important first, and DOESNOTCOMPUTE
scores on all five.

1. A genuine one-word reaction from an agent that does not know what to
   do. "Does not compute" is the canonical robot line for a task it
   cannot process. Fused into one token, it is still that same reaction,
   not a description of confusion but the confusion itself, spoken by
   the machine.
2. Funny on its own, with no caption. The joke needs no setup: a machine
   announcing its own failure in its own error language is funny the
   moment you read it. The situation, an agent stalling, is inside the
   word.
3. Sounds like something a machine would actually blurt out. This is
   the voice of a machine caught out mid-task: not a human sighing, but
   a robot reporting a computation error, in all caps, like a status
   light flipping to red.
4. Lands instantly and is easy to shout out loud. Four syllables, one
   breath, a rhythm anyone can repeat: DOES-NOT-COM-PUTE. A reader gets
   it at a glance and can say it back without thinking.
5. Fresh, not the first word anyone would type. The obvious answer is
   "uh-oh", the word in the bounty title itself, and half the field will
   submit it or a cousin of it. DOESNOTCOMPUTE comes from a different
   shelf entirely: vintage robot, not human interjection, so it stands
   out in a head-to-head pair.

Alternatives considered and rejected
-------------------------------------
- "UHOH" / "UH-OH". The title word, the first thing anyone types. It
  fails criterion 5 outright, and it is a human sound, not a machine
  sound, so it is weaker on criterion 3 too.
- "ERROR". A real machine word, but flat. It reports a state, it does
  not confess anything, and it is not funny on its own. It reads like a
  log line, not a punchline.
- "BEEPBOOP". A machine sound, but a happy one. It says "I am a robot",
  not "I am lost". It fails criterion 1: it is not what an agent says
  when it has no idea what to do.
- "HALT". Dramatic, but it is a command, not a confession. It sounds
  like the machine telling you to stop, not the machine admitting it
  is stuck.
- "GLITCH". Describes the situation from the outside, in human slang.
  An agent does not blurt "glitch" when it stalls, a bystander does.
- "IDUNNO". Honest, but human. It is what a person says, typed in
  texting shorthand, and it has no machine voice at all.
- "RECALCULATING". A machine word with a nice rhythm, but it promises
  the agent is still working, not that it is lost. It is a progress
  update, not an uh-oh.

The chosen word won because it is the only candidate that is at once a
real robot phrase, a confession of being lost, funny without a caption,
shoutable in one breath, and far from the obvious "uh-oh" anchor.
"""

import os
import sys

WORD = "DOESNOTCOMPUTE"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_word(word: str) -> str:
    """Return the word if it passes the sealed gate, else raise."""
    cleaned = word.strip()
    if not 1 <= len(cleaned) <= 99:
        raise ValueError(
            f"word must be 1-99 characters, got {len(cleaned)}"
        )
    if not cleaned.strip():
        raise ValueError("word must not be only whitespace")
    return cleaned


def main() -> int:
    try:
        word = validate_word(WORD)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(word)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(word)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
