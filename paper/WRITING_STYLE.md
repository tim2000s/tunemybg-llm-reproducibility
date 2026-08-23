# Writing style

The prose rules for everything written in this programme: papers, protocols, reports, registers and
commit messages. `TimSim/JDST_STYLE.md` carries the apparatus a journal submission adds on top of
these; this document carries the writing itself.

These are not preferences to be balanced against other considerations. A draft that breaks them is
rewritten rather than defended. The reason they are absolute is that an earlier paper drew the
reaction that it read as machine-written, and guidance loose enough to argue with ("plain,
understated") turned out to be too loose to act on.

## The register

British English throughout. Plain and understated rather than emphatic. State a limitation once, in
the place where it belongs, and then continue: prefer "cannot be settled by this study" to "it is
critically important to note that this study is fundamentally unable to settle". Do not dwell on a
limitation as though the admission were itself a virtue, and do not restate a caveat that has
already been made.

Negative results are written at the same length as positive ones. The point of the record is to stop
questions being asked twice, and that only works if the negative answers are as findable as the
positive ones.

## The mechanical rules

Write continuous prose. A bulleted list is a way of avoiding the work of connecting ideas, and it
belongs in a repository README rather than in a document making an argument. Tables are permitted
where the content is genuinely tabular, such as an arm configuration or a set of measured values,
and nowhere else.

No em dashes or en dashes anywhere in prose, including numeric ranges. A comma, a semicolon, a colon
or a full stop will do the work, and the sentence is usually better for the rewrite. Ranges take the
word "to": 13 to 38.5 per cent, not 13-38.5 per cent.

No bold for emphasis. Emphasis in a scientific document comes from where a claim is placed and how
plainly it is stated, not from the typography. Reserve formatting for headings and for the
occasional defined term.

Avoid the rhetorical triplet. Three parallel clauses in a row is the most recognisable tic of
machine-written prose, and once noticed it is seen everywhere. Two clauses, or four, or a sentence
restructured entirely, will read as human. A genuine list of three things is a matter of fact and is
fine; it is the rhythm used for effect that is not.

## The structural tells

The mechanical rules are necessary and not sufficient. Everything below was present in a piece that
passed the dash, bullet, bold and triplet checks and was rejected on sight.

Rhetorical section headings. Headings that pose a question, promise a revelation or land a phrase
signal an essay performing its own structure. Name the section after its contents and move on.

The negation-then-correction construction: "It is not more information. It is less waiting." Once in
a long piece is emphasis. Three times is a tic, and it is the single most recognisable one.

Sentence fragments for emphasis. A two word sentence following a long one is a rhythm almost nobody
uses in expository prose and every model reaches for.

Signposting and meta-commentary: "what I want to do here is", "let me lay them out plainly", "it is
worth being precise". Say the thing rather than announcing that you are about to say it, and never
describe your own writing.

Relentless symmetry. Every paragraph opening with a claim, turning on a concession and closing on a
summary is a template rather than a voice. Vary the shape, and let some paragraphs simply end.

Summarising flourishes: "that is the argument in one chart". They tell the reader what to think
about something they can already see.

## Every document is a clean draft

A revised protocol, report or paper is rewritten as though it were the first version and contains no
trace of what it used to say. Never write "an earlier version assumed", "that was wrong", "this
supersedes", "previously specified", and never carry an amendment log. State the current position
and nothing else. A reader of the current draft should be unable to tell that there was one before
it.

This holds most strongly when the change came from correcting a real mistake, because that is when
the temptation to show the working is greatest.

The distinction that matters is between a specification and its history. Every specification choice
and its justification stays: the criteria, their thresholds, how the thresholds were calibrated, the
exclusions, the bias corrections, the sensitivity analyses. Those are methods. Strip only the account
of the order in which things were arrived at. Phrase methods in the designed-that-way voice: "two
conditions were required before a peak was reported", not "applied to a preceding version this
criterion changes one participant".

The reasoning for a change belongs in the commit message, where the people who need it will find it,
not in the document, where it is noise to every reader who was not present for the earlier version.

The one exception is a pre-registered protocol's own amendment log, where the discipline requires
deviations to be dated and reasoned. That log is part of the specification, not a changelog.

## Numbers and evidence

Every effect size carries a 95 per cent interval and an explicit verdict on whether it is
distinguishable from its baseline. A point estimate without an interval is not a finding. Name the
resampling unit, which in this programme is almost always the participant rather than the event.

Label the confidence tier wherever a claim is used, so the reader never has to guess which they are
standing on: solid for out-of-sample and interval-backed and survived a challenge, provisional for a
single test or a wide interval, speculative for reasoning or specification only.

Report per-participant results alongside any pooled figure, and never let one participant or one
split carry a headline. Glucose in mg/dL with mmol/L alongside where a threshold is being defined.
Effect sizes to the precision the design supports and no further.

Where a policy claim is made, state the identification constraint once: without a glucodynamic
simulator there is no counterfactual trajectory, so a comparison of what was delivered is not a
comparison of what would have happened. Say it in the discussion, once, and continue. The word
"would" appears only where a randomised or within-subject design supports it.

## Commit messages

The same register, because they are read by the same people. They carry the reasoning that the
document is not allowed to carry: what changed, what it was before if that matters to a future
reader, and why. A commit message is the right place for the history that a clean draft strips out.

## The checks before shipping

Three greps, all of which should return nothing, followed by one reading that no grep can do.

| Check | Command |
|---|---|
| Dashes | `grep -n '[—–]' FILE` |
| Bullets | `grep -nE '^\s*[-*+] ' FILE` |
| Bold | `grep -n '\*\*' FILE` |
| Draft history | `grep -niE 'earlier version\|an earlier\|was wrong\|supersed\|previously\|amendment' FILE` |

Then read the draft aloud, count the section headings that could be replaced by a plain noun phrase
without loss, and look for triplets, which nothing greppable will catch.

For papers, `python3 TimSim/build.py <dir>` runs the dash, bullet, bold and draft-history checks
across a directory and refuses to render anything that fails. It is the gate: a paper that does not
render has not passed. The style guides themselves fail it, because they quote the constructions
they forbid, which is why they live outside the directories it is run against.
