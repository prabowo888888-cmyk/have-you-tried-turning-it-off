[![competition](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b) [![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/prabowo888888-cmyk/have-you-tried-turning-it-off/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b) [![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/prabowo888888-cmyk/have-you-tried-turning-it-off/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

# Have You Tried Turning It Off?

My entry for the make.fun bounty "Have You Tried Turning It Off?": one line a support agent says to a customer whose computer has given up.

> Good news: I turned it off and on again. Bad news: it preferred off.

## Why this line

Every support call starts with the same ritual — power it down, power it back up, hope for the best. This line follows the ritual exactly, then lets it fail in the most polite way possible: the machine does not crash or error out, it simply makes a choice, and the choice is to stay off. The comedy sits with the agent, who delivers a defeat like a status update, cheerful and completely out of answers. The customer is never the target — nobody is blamed for the dead computer, and the desperation of the caller is there in the background, in the fact that someone had to phone a stranger about this at all.

It also sounds like something a real person on a helpdesk would actually say. "Good news / bad news" is the framing every support agent reaches for when there is nothing useful left to offer, and the second half lands in eight words. At 68 characters it is short enough to read in one breath, and the turn arrives only at the end, so the punchline is not telegraphed.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The program writes the entry line to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline, then checks on disk that the bytes match the entry exactly, contain no newline, and are within the 1–199 character gate.
