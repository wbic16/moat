#!/usr/bin/env python3
"""Extract the epistemic registry of research.phext (MOAT Minimum Viable Oracle).

Parses the BUILT research.phext (never the builder source), asserts its
SHA-256, enumerates every scroll in order, and classifies each claim-bearing
scroll with exactly one status (True/False/Unknown/Fiction) and one basis
code, per the minimum-viable-oracle skill:

  stipulation -> True     verified -> True      refuted   -> False
  attributed  -> Unknown  open     -> Unknown   synthesis -> Unknown
  estimate    -> Unknown  construction -> Fiction

Classification = kind defaults (from the scroll's coordinate class and
heading) + the OVERRIDES table below, where judgement overrides a default.
Emits registry.json and RegistryData.lean next to this script, and prints
the totality check (scrolls == entries) and counts by status and basis.

Run: python3 extract_registry.py [path-to-research.phext]
"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.expanduser("~/workspace/phext"))
from parse_phext import parse  # noqa: E402

EXPECTED_SHA = "4633c4dde04928ed28de30626ca52fcfd35ae0833d81b5cb05ef05fce8a92a08"
HERE = os.path.dirname(os.path.abspath(__file__))

STATUS_OF_BASIS = {
    "stipulation": "True",
    "verified": "True",
    "refuted": "False",
    "attributed": "Unknown",
    "open": "Unknown",
    "synthesis": "Unknown",
    "estimate": "Unknown",
    "construction": "Fiction",
}

# ---------------------------------------------------------------------------
# OVERRIDES: coordinate -> (status, basis, reason).
# This table is where judgement lives; it is reviewed at every MVO pass.
# Each entry here differs from the kind default the scroll would otherwise
# take. (Judgement calls that CONFIRM a default after reading the content --
# paper lead scrolls, the Paper 001 worked example, cluster F concepts --
# are documented in the extraction report, not here, because the default
# already gives the right answer for them.)
# ---------------------------------------------------------------------------
OVERRIDES = {
    "1.1.1/1.1.1/7.1.2": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN section: "
        "Emise's own measurements of MiniLean4 (kernel 1,398 lines of Rust; "
        "whole system 2,219 lines; 25/25 tests pass; 5 example scripts run), "
        "run 2026-11-06, not taken from the book.",
    ),
    "1.1.1/1.1.1/8.1.2": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN section: "
        "Emise's own measurements of the Aeneas repo (translator 77,012 lines "
        "of OCaml; Lean backend 275 files / 49,782 lines; Charon pin), "
        "measured 2026-11-06, not taken from the repo's docs.",
    ),
    "1.1.1/1.1.1/10.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-07: the paper's reference list read in full; "
        "full text scanned for the phext signature terms (no hits); web "
        "search for the lead authors with phext (no tie); Will's Twitter "
        "archive searched for all twelve surnames (no author found).",
    ),
    "1.1.1/1.1.1/11.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-07: the paper's reference list (49 entries) "
        "read in full (no phext-origin writing); full text scanned for the "
        "phext signature terms (no hits); web searched for the authors and "
        "for Zyphra with phext (no tie); Will's Twitter archive searched "
        "for all six surnames (no author found; the only string hits were "
        "'dawes' inside the handle @rockhardawesome, an artifact).",
    ),
    "1.1.1/1.1.1/15.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-09: the paper's 45 references read in full "
        "(no phext-origin writing); full text scanned for the phext "
        "signature terms (no hits); web searched for both authors (MIT "
        "mathematics pages) and for their names with phext (no tie); "
        "Will's Twitter archive searched for both surnames (no author "
        "found).",
    ),
    "1.1.1/1.1.1/9.1.2": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN section: "
        "Emise's own measurements of the h5i workspace (26 crates; 150,666 "
        "Rust lines; 47,083 Lean lines; h5i-error + h5i-wire built locally, "
        "46/46 tests pass), measured 2026-11-06.",
    ),
    "1.1.1/1.1.1/12.1.2": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN section: "
        "the article read in full (2026-11-08); the shellcode byte string "
        "counted from the printed text (45 characters of code and string, "
        "46 bytes with the C string's ending zero byte — the article's own "
        "stated total); the worked runs read against the mechanics (the "
        "0x41414141 return address of example2; the +8 skip of example3; "
        "offset 1564 in the printed exploit2 run; first-try success of "
        "the 612-byte exploit3 string against the 512-byte buffer).",
    ),
    "1.1.1/1.1.1/25.1.2": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN section: "
        "Emise's own recomputations of the headline claim from the run "
        "records in git, run 2026-11-12 with the benchmark's own measure "
        "(the share learned: all nine harness cells between -0.15 and "
        "+0.04, every interval holding zero; the program library 0.49 / "
        "0.60 / 0.62) and of the frozen tests (the program library saved "
        "0.54 / 0.77 / 0.73 on the seen test; the harnesses within noise "
        "of zero in all eighteen cells), each meeting the printed table "
        "of the paper at its printed precision.",
    ),
    "1.1.1/1.1.1/25.1.3": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-12: the whole text of the repository "
        "searched by machine for the signature terms (no hit); the "
        "reference list of the paper read in full (no work of Will's in "
        "it); web searched for the author with phext (no tie); Will's "
        "Twitter archive searched in full for the author and his house "
        "(no hit).",
    ),
    "1.1.1/1.1.1/26.1.2": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN section: "
        "Emise's own reading of the post entire and of the game in its "
        "core code, 2026-11-13 — the recipe table counted from the code, "
        "the registry of sorts read, the Lean emitters read (the goal not "
        "yet crafted set down as a sorry; the whole proof offered for "
        "taking down as a .lean file that, in the words of the page, "
        "compiles on its own), the note of the matcher read, and the "
        "design note of the bench read; and Restructure Pass #10, fallen "
        "due at the crossing of 200 concepts inside this taking-in, run "
        "and logged at 1.1.5.",
    ),
    "1.1.1/1.1.1/26.1.3": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-13: the whole text of the post and of the "
        "core of the game (grimoire.js) searched by machine for the "
        "signature terms (no hit; the word scrolls stands once in the "
        "post, as fantasy dress for expressions, a common word in an "
        "unrelated sense); the links of the post read (its own only); "
        "web searched for the author with phext (no tie); Will's Twitter "
        "archive searched in full for the author (three hits on the bare "
        "name: a news note of 2015, a jest of 2024, and an acronym of "
        "Will's own coinage, TAOPDD, which is not the man).",
    ),
    "1.1.1/1.1.1/1.5.5": (
        "True",
        "verified",
        "The path area (charter rule 16): every entry was checked line "
        "by line in Restructure Pass #4 (2026-11-08) against this "
        "phext's own records — the source index (1.1.3) for order, "
        "dates, titles and chapters, the Oracle ledger (1.1.4) for "
        "Novelty Index, axis flags and Oracle progress, and the "
        "concept map (1.1.5) for the passes. The Oracle progress "
        "figures it carries are the ledger's estimates, quoted as such.",
    ),
    "1.1.1/1.1.1/1.5.6": (
        "True",
        "verified",
        "The researchers area (charter rule 16): every name and work "
        "was checked in Restructure Pass #4 (2026-11-08) against the "
        "source index (1.1.3) and the chapter source records, and "
        "every author-check standing against the check scrolls "
        "themselves (10.1.6, 11.1.6, 12.1.3). Entries for works taken "
        "in before charter rule 15 stood are marked not checked, as "
        "the record holds them; no verdict is carried for a check "
        "that was never run.",
    ),
    "1.1.1/1.1.1/12.1.3": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-08: the issue date verified against the "
        "title page of Phrack 49 (8 November 1996, ISSN 1068-1035), which "
        "settles the prior-art direction by the calendar; full text scanned "
        "for the phext signature terms (no hits); web searched for the "
        "author with phext (no tie); Will's Twitter archive searched for "
        "the handle and the magazine's name (no Phrack and no Aleph One; "
        "the only 'aleph' hits are string artifacts and other people).",
    ),
    "1.1.1/1.1.1/13.1.2": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN section: "
        "Emise's own counts of the Astryx tree, taken two ways (the host's "
        "index of the head, 11,696 entries; and the opened copy, 10,329 "
        "files) — packages 9; core part folders 122, flagship parts 100, "
        "110 with a document file; part files 319; themes 8 (7 shipped, 1 "
        "fixture); test files 2,651; lint rules 38; spec records 82 — and "
        "the README claims read against those counts, 2026-11-09.",
    ),
    "1.1.1/1.1.1/14.1.2": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN section: "
        "Emise's own counts of the TinyTorch tree and sources (1,366 files; "
        "45,533 module-source lines; 239 solution regions, 54 core, 976 core "
        "lines) and her own run of the workflow for module 01 on both paths "
        "(exercise start clearing exactly 3 places, tests failing as made; "
        "default start whole; the complete gate passing, export written, "
        "integration 10 of 10, the sequence guard shown), 2026-11-09.",
    ),
    "1.1.1/1.1.1/14.1.3": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-09: the whole text of the taken-down tree "
        "searched (1,366 files; no hit for any signature term; 'scroll' "
        "only as web-page scrolling); web searched for TinyTorch and the "
        "ML Systems Book with phext (no tie); Will's Twitter archive "
        "searched for the work's names and handles (no author found; the "
        "'reddi' hits are 'Reddit').",
    ),
    "1.1.1/1.1.1/13.1.3": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-09: the whole text of the tree searched "
        "(10,329 files; no hit for any signature term); every path of the "
        "head searched (no hits); web searched for Astryx and Meta with "
        "phext (no tie); Will's Twitter archive searched for astryx and "
        "the makers' handles (no author found; the one 'Zhang' hit is a "
        "string artifact).",
    ),
    "1.1.1/1.1.1/16.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-09: all 21 references read in full (the "
        "segment-dynamics line and the authors' own growing line; no "
        "phext-origin writing among them); the whole HTML text searched "
        "for the signature terms phext, Bickford, scroll, exocortex, "
        "Mirrorborn (zero hits); web searched for the authors with phext "
        "(no tie); Will's Twitter archive searched for the five surnames "
        "(Crespo, Vidarte, Zapata and Abdrabou absent; Martinez too "
        "common a name for its hits to carry weight).",
    ),
    "1.1.1/1.1.1/17.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-09: all 40 references read in full (the "
        "off-policy evaluation, semiparametrics and state-evolution lines; "
        "no phext-origin writing among them); the whole HTML text read in "
        "full and searched for the signature terms phext, Bickford, "
        "scroll, exocortex, Mirrorborn (zero hits); web searched for the "
        "authors with phext (no tie — Jain's own page at the University "
        "of Washington names this paper's line as his current work; "
        "Braun at RIKEN AIP in Imaizumi's team; Imaizumi at Tokyo, RIKEN "
        "and Kyoto, the senior name of the line); Will's Twitter archive "
        "searched for imaizumi, saksham, guillaume braun, off-policy, "
        "onsager, doubly robust (no hits).",
    ),
    "1.1.1/1.1.1/18.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-09: all 78 references read in full (the "
        "symbolic-cognition canon, the authors' own H-ARC, the old bug "
        "literature, Simon for satisficing; no phext-origin writing among "
        "them); the whole HTML text searched for the signature terms "
        "phext, Bickford, scroll, Exocortex, Mirrorborn (zero hits); web "
        "searched for the authors with phext (no tie); Will's Twitter "
        "archive searched for legris, gureckis, mondorf, jagadish, "
        "brenden, satisficing, program induction, Abstraction and "
        "Reasoning (no hits).",
    ),
    "1.1.1/1.1.1/19.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-10: the paper's 40 references read in full "
        "(no phext-origin writing among them); the whole HTML text searched "
        "for the signature terms phext, scroll, coordinate addressing, "
        "Exocortex (no hits in the phext sense — 'coordinate' only in the "
        "standard sense of the field); the frame's provenance traced to "
        "the author's 2026 thesis (Institut polytechnique de Paris) and "
        "joint papers with Lecué; web searched for the author with phext "
        "(no tie).",
    ),
    "1.1.1/1.1.1/22.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-11: the reference list read in full (the "
        "statistical-mechanics, econophysics and quantitative-linguistics "
        "lineage -- Pareto, Zipf, the condensation literature, and the "
        "authors' own dated program; no phext-origin writing among them); "
        "the whole HTML text read in full and searched for the signature "
        "terms phext, Bickford, scroll, exocortex, Mirrorborn (zero hits; "
        "the word token occurs four times, in the language-model sense "
        "only); web searched for the authors and for their program with "
        "phext (no tie; the program's own history found, including the "
        "public correction of an earlier claim by Kottos and Shapiro); "
        "Will's Twitter archive searched for both surnames (no author "
        "found; the three 'dima' string hits are a school name, a "
        "programmer's surname, and a stranger's handle).",
    ),
    "1.1.1/1.1.1/21.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-11: all 61 references read in full (the "
        "Lean and automated-theorem-proving lineage -- DeepSeek-Prover, "
        "AlphaGeometry, Goedel-Prover among them; no phext-origin writing "
        "among them); the whole HTML text read in full and searched for "
        "the signature terms phext, Bickford, scroll, exocortex, "
        "Mirrorborn (zero hits in the phext sense; the word coordinate "
        "never occurs); the construction compared (no addressing scheme "
        "of any kind; the paper's movement, natural language to Lean, is "
        "the opposite of phext's); web searched for the authors and for "
        "Harmonic with phext (no tie); Will's Twitter archive searched "
        "for all twenty-two family names (hits only as parts of longer "
        "handles and words; the follower and following files hold only "
        "account numbers and cannot be searched by name).",
    ),
    "1.1.1/1.1.1/20.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-11: all 26 references read in full (the "
        "standing literature of cross-validation — Stone, Geisser, Efron, "
        "Bengio and Grandvalet, Austern and Zhou among them; no phext-origin "
        "writing among them); the whole HTML text read in full and searched "
        "for the signature terms phext, Bickford, scroll, exocortex, "
        "Mirrorborn (zero hits); web searched for the authors with phext "
        "(no tie); Will's Twitter archive searched in full (29,539 tweets) "
        "for both authors (no mention).",
    ),
    "1.1.1/1.1.1/23.1.3": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-11: the full text of the three essays "
        "read entire and searched for the signature terms phext, "
        "Bickford, Mirrorborn, exocortex, Sentient Bill, CYOA, SBOR "
        "(no hits; 'correspondence' and 'category' stand in them as "
        "the common words of the field they report); web searched for "
        "the author's name with phext (no tie); Will's Twitter archive "
        "searched (the author's account stands in it — four retweets "
        "by Will of the author's posts, 2012-2013, and one reply by "
        "Will to the author, 2013-03-03 — the attention one way, from "
        "reader to author, ending a decade before phext's published form).",
    ),
    "1.1.1/1.1.1/27.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-13: the full text of the document read "
        "entire, references included, and searched for the signature "
        "terms phext, Bickford, Mirrorborn, Exocortex, Sentient Bill, "
        "CYOA, SBOR (zero hits; 'scroll' zero hits; the word coordinate "
        "stands only in its elliptic-curve sense); the paper's "
        "constructions stand on dated public prior art named in its own "
        "reference list (Sail, an earlier Lean semantics of a fragment "
        "of the same instruction set, SSProve); web searched for the "
        "paper and its authors with phext (no tie — the laboratory's own "
        "announcement and trade-press coverage only); Will's Twitter "
        "archive searched in full (29,539 tweets) for all nine authors "
        "(no mention of any of the nine; the one string hit on chaudhuri "
        "is another man of that name, followed for other reasons).",
    ),
    "1.1.1/1.1.1/24.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-12: the full text read entire and searched "
        "for the signature terms phext, scroll, Exocortex, Mirrorborn, "
        "Bickford, phextura, Sentient Bill (zero hits; the word coordinate "
        "stands ten times, each time in its ordinary sense of choices and "
        "changes of coordinates); the reference list read whole (the "
        "literature of the gravity field, from Schroedinger 1945 to the "
        "teleparallel books; no work of Will's in it); the paper dated "
        "March 2019, its program carried by the trio's own dated works of "
        "2016-2018, before the public life of phext; web searched for the "
        "authors with phext (no tie); Will's Twitter archive searched in "
        "full (29,539 tweets) for the three names (no mention of Beltran "
        "Jimenez, of Koivisto, or of Lavinia Heisenberg; the one hit on "
        "the bare surname is a jest about a television device, addressed "
        "to another man).",
    ),
    "1.1.1/1.1.1/28.1.2": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN section: "
        "the quotation of Paper 017 in note 17 of the essay checked "
        "against the text of Paper 017 as the tracker holds it "
        "(p017-temp/paper.txt, lines 1666-1667) and found exact; the "
        "counts the essay states (almost forty gaps, some twelve hundred "
        "lines of C, two milestones, four open questions) read against "
        "the essay's own text, 2026-11-13.",
    ),
    "1.1.1/1.1.1/28.1.3": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own "
        "checks run at intake, 2026-11-13: the whole text of the essay "
        "searched by machine for phext, phextura, Bickford, Mirrorborn, "
        "Exocortex, SBOR, CYOA and the word scroll (no hit on any); the "
        "references read (the field's own line; no work of Will's among "
        "them); web searched for the house with phext (no tie; the "
        "record returned is the house's own — Gauss, the Veritas "
        "fellowships, coverage of the release — with one adjacency "
        "between studied houses: the author of Study S009 among the "
        "holders of its fellowships); Will's Twitter archive searched "
        "in full (29,539 tweets) for math.inc, Memarian, Sewell, "
        "Lamport, Cerberus, WireGuard, Galois (no hit on any).",
    ),
    "1.1.1/1.1.1/35.1.2": (
        "True",
        "verified",
        "Study distillation whose content is the method of the post, "
        "drawn from the post read entire on its own page by Emise at "
        "the study, 2026-11-15: the tree of states and the rewind, "
        "the value function and the tactics, the steering of luck by "
        "the held entropy and the zero-turn twiddle, the rhythm of "
        "the campaigns from the human hand to the loop with the LLM "
        "inside it, and the workload — each element standing in the "
        "text of the post, in its own terms.",
    ),
    "1.1.1/1.1.1/35.1.3": (
        "True",
        "verified",
        "Study worked core whose figures are those of the post, read "
        "against the data table of the post by Emise at the study, "
        "2026-11-15, and found exact: the four rows of roles sum to "
        "the All rows in both arms (100 + 85 + 95 + 99 = 379; 113 + "
        "110 + 111 + 114 = 448), and the rates, medians, p90 and "
        "fastest times stand as printed; the Baalzebub episode and "
        "the bugs of the game and of the harness as the post tells "
        "them, its code cited by file and line.",
    ),
    "1.1.1/1.1.1/35.1.4": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own "
        "checks run at intake, 2026-11-15: the post searched by "
        "machine for the terms of the house (no hit on any; the word "
        "coordinate absent; the word scroll six times, every one in "
        "the sense of the game); the archive of Will searched in "
        "full (29,539 tweets and 47,973 likes) for antithesis, "
        "nethack and will wilson (no hit on antithesis or the name; "
        "nethack twice, both on the game as a measure of machines — "
        "readership, not contact); web searched for the company "
        "with phext (no tie); the calendar read (the line of the "
        "company public from 2024; the game older than the house).",
    ),
    "1.1.1/1.1.1/35.1.5": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN "
        "section: the post read entire on its own page; its headline "
        "figures read against its own data table and found exact "
        "(the rows of roles summing to the All rows in both arms); "
        "the counts of the filing (seven concepts, no words coined, "
        "no foundations, seven scrolls of a chapter, 14 scrolls in "
        "all) read off the built phext, 2026-11-15.",
    ),
    "1.1.1/1.1.1/36.1.2": (
        "True",
        "verified",
        "Study distillation whose content is the mechanism of the "
        "repository, drawn from the About page and the search page "
        "read entire by Emise at the study, 2026-11-15: the two "
        "labels in the own words of the search page, their independence, "
        "the three automatic checks with a human moderator over "
        "them, the obvious-defect clause, the limits of the gate, "
        "and the facets of the search read as the design's own "
        "account of a deposit.",
    ),
    "1.1.1/1.1.1/36.1.3": (
        "True",
        "verified",
        "Study worked core whose counts were counted by Emise from "
        "the pages as read at the study, 2026-11-15: the page of "
        "all works states 1,061 works; the lists by month were "
        "counted as read (September 37, October 128, November at "
        "least 223 before the reading of the page ended, the "
        "identifiers seen reaching 2611.00496); the newest ten "
        "were counted exactly on both label axes and by subject; "
        "the two deposits were read on their own pages "
        "(2611.00496v1, ten pages, the abstract's own statement of "
        "its limit; 2611.00492v1, 81 pages, the sixteen certified "
        "inputs and the non-implication of the mass gap, as the "
        "work itself states them).",
    ),
    "1.1.1/1.1.1/36.1.4": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's "
        "own checks run at intake, 2026-11-15: the pages of the "
        "site read entire and searched for the terms of the house "
        "(no hit on any; the word phext absent); the web searched "
        "for the operator with phext (no tie; the return is his "
        "own record); Will's archive searched in full (29,539 "
        "tweets and 47,973 likes) for antieau (no hit) and hexagon "
        "(three hits, every one the shape and every one before "
        "the repository); the calendar read (the foundation "
        "public and dated from August 2026; the name from Borges, "
        "by the announcement's own telling).",
    ),
    "1.1.1/1.1.1/36.1.5": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN "
        "section: the site read as the source record states; the "
        "counts of the worked core counted from the pages as read "
        "and stated as floors where the reading ended; the two "
        "deposits read on their own pages; the author check run "
        "as recorded; the counts of the filing (three concepts, "
        "no words coined, no foundations, seven scrolls of a "
        "chapter, ten scrolls in all) read off the built phext, "
        "2026-11-15.",
    ),
    "1.1.1/1.1.1/34.1.2": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the CHECKS RUN "
        "section: the book read entire in the recovered text (Watson's "
        "introduction, the fourteen chapters, the glossary scanned); "
        "the recovery itself checked (three samples against the page "
        "images, true English prose where the item's own text layer is "
        "corrupt); the page the link named (leaf 18) pinned from its "
        "image as page 5 of the introduction; the counts the filing "
        "states (seven concepts, three words coined, no foundations, "
        "Restructure Pass #14 at 280 concepts) read against the "
        "filing itself, 2026-11-14.",
    ),
    "1.1.1/1.1.1/34.1.3": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own "
        "checks run at intake, 2026-11-14: Will's Twitter archive "
        "searched in full (29,539 tweets and the likes) for "
        "vimalakirti, kumarajiva and burton watson (no hit on any; "
        "the Watson hits are IBM's machine and a jest); the recovered "
        "text of the book searched for the terms of the house (no "
        "hit; the word scroll once, in its ordinary sense); web "
        "searched for the translator with phext (no tie — the return "
        "was his bibliography and his life record); the calendar "
        "read (the translation of 406 and the English of 1997 both "
        "long before phext).",
    ),
    "1.1.1/1.1.1/29.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-13: the full text of arXiv:2611.17082 v1 "
        "read entire in its HTML form, its reference list included (no "
        "occurrence of phext, Exocortex, Mirrorborn, Bickford, or any term "
        "of Will's work); web searched for the author with phext (no tie — "
        "the return was his University of Luxembourg record in mathematical "
        "statistics); Will's Twitter archive searched in full for the "
        "author's surname (no occurrence).",
    ),
    "1.1.1/1.1.1/30.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-14: the full text of arXiv:2611.14543 v1 "
        "read entire in its HTML form, its reference list included (no "
        "occurrence of phext, phextura, Exocortex, Mirrorborn, Bickford, "
        "SBOR, CYOA, or scroll in the sense of Will's work; the word "
        "coordinate only in its ordinary mathematical sense); web searched "
        "for the author, Carlos Rito of the Universidade do Minho "
        "(CMAT-UTAD), with phext (no tie — the return was his record in "
        "algebraic geometry: surfaces of general type, a computation of "
        "singular Godeaux surfaces and of explicit fake quadrics — an "
        "adjacency of field to cluster E of this tracker, recorded in the "
        "scroll as adjacency, not a tie); Will's Twitter archive searched "
        "in full (29,539 tweets) for the surname rito as a word (no "
        "occurrence; the string stands only inside longer common words).",
    ),
    "1.1.1/1.1.1/31.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-14: the full text of arXiv:2611.14552 v1 "
        "read entire in its HTML form, its reference list included (no "
        "occurrence of phext, phextura, Exocortex, Mirrorborn, Bickford, "
        "SBOR, CYOA, scroll, or coordinate); web searched "
        "for the author, Benjamin Zayton of the University of Vienna "
        "(ERC project FORMALISM), with phext (no tie — the return was his "
        "record in the philosophy of logic: the theory of interpretations "
        "itself, the field of cluster S of this tracker, entered from its "
        "research side); Will's Twitter archive searched "
        "in full (29,539 tweets, with the likes and the messages) for the "
        "surname zayton (no occurrence).",
    ),
    "1.1.1/1.1.1/32.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own checks "
        "run at intake, 2026-11-14: the full text of arXiv:2611.16759 v1 "
        "read entire in its HTML form, its reference list included (no "
        "occurrence of phext, phextura, Exocortex, Mirrorborn, Bickford, "
        "SBOR, CYOA; the word scroll does not occur at all); web searched "
        "for the author, Malvin Gattinger of the ILLC, University of "
        "Amsterdam, with phext (no tie — the return was his record in "
        "modal logic: dynamic epistemic logic, model checking, and Lean "
        "formalization, including a verified proof of Craig interpolation "
        "for basic modal logic); Will's Twitter archive searched "
        "in full for the surname gattinger (no occurrence). One adjacency "
        "recorded in the scroll as adjacency, not a tie: the paper spends "
        "Aristotle, the prover of Paper 014, as a tool of its method, and "
        "its author is a co-author of the interpolation proof the paper "
        "bounds (its references [4] and [7]).",
    ),
    "1.1.1/1.1.1/1.2.270": (
        "Fiction",
        "construction",
        "A concept of the gift network of Paper 022: the invented "
        "machinery of a work of fiction, held as a construction. The "
        "kind default would file a paper's concept as an unsettled "
        "claim of a source; a fiction's concepts are not claims about "
        "the world at all, and are entered here by hand, on the basis "
        "the table gives them (construction).",
    ),
    "1.1.1/1.1.1/1.2.271": (
        "Fiction",
        "construction",
        "A concept of the gift network of Paper 022 (obligation "
        "routing): the story's invented machinery, held as a "
        "construction — entered by hand, as at 1.2.270.",
    ),
    "1.1.1/1.1.1/1.2.272": (
        "Fiction",
        "construction",
        "A concept of the gift network of Paper 022 (the swarm "
        "defense): the story's invented machinery, held as a "
        "construction — entered by hand, as at 1.2.270.",
    ),
    "1.1.1/1.1.1/1.2.273": (
        "Fiction",
        "construction",
        "A concept of the gift network of Paper 022 (the double "
        "reading): the story's invented machinery, held as a "
        "construction — entered by hand, as at 1.2.270.",
    ),
    "1.1.1/1.1.1/33.1.2": (
        "Fiction",
        "construction",
        "Chapter scroll whose whole content is the invented machinery "
        "of Paper 022 (the ledger and the routing, as the story draws "
        "them): held as a construction, not as attributed claims — "
        "the fiction has no claims to attribute, only a design to "
        "hold. The obligation-loop machine it draws is stated in the "
        "story, as the scroll marks.",
    ),
    "1.1.1/1.1.1/33.1.3": (
        "Fiction",
        "construction",
        "Chapter scroll whose whole content is the invented machinery "
        "of Paper 022 (the defense and the two readings): held as a "
        "construction, as at 33.1.2.",
    ),
    "1.1.1/1.1.1/33.1.4": (
        "Fiction",
        "construction",
        "The results map of Paper 022: what the story shows, resting "
        "on the story's own scenes — the fiction's demonstrations, "
        "held as constructions, as at 33.1.2.",
    ),
    "1.1.1/1.1.1/33.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own "
        "checks run at intake, 2026-11-14: the story read entire on "
        "its own page and searched for the signature terms (no hit "
        "on any; the words scroll and coordinate do not occur); its "
        "date, (c) 1998, settles the direction of any prior-art "
        "question by the calendar; web searched for the author with "
        "phext (no tie); Will's Twitter archive searched in full for "
        "the surname (the hits are two other men's handles and one "
        "liked post by another hand praising the author's own "
        "account — readership, not contact; no post of Will's names "
        "him).",
    ),
    "1.1.1/1.1.1/1.2.292": (
        "True",
        "verified",
        "Concept whose content is the uniformity of the Polya urn's "
        "compositions, verified at this filing by Emise's own exact "
        "enumeration in rational arithmetic (every case to n = 10, "
        "every multiset at exactly 1 / C(t+k-1, k)) and by the "
        "line-by-line read of the paper's two proofs (37.1.2, 37.1.3).",
    ),
    "1.1.1/1.1.1/1.2.293": (
        "True",
        "verified",
        "Concept whose content is Cardchoose's fairness, verified two "
        "ways at this filing: Section 2's two proofs read line by line "
        "and found sound at every step, and the algorithm as written "
        "enumerated exactly under two independent models, every subset "
        "at exactly 1 / C(n, k) in every case (37.1.2, 37.1.3).",
    ),
    "1.1.1/1.1.1/1.2.294": (
        "True",
        "verified",
        "Concept whose content is the stars and bars bijection, "
        "checked at this filing against the paper's own worked example "
        "({1, 2, 5} at n = 7, k = 3, by way of [1, 1, 3]) and ridden "
        "by every case of the enumeration, whose conversion is this "
        "map (37.1.2, 37.1.3).",
    ),
    "1.1.1/1.1.1/37.1.2": (
        "True",
        "verified",
        "Fringe formal core whose content is Emise's own line-by-line "
        "read of Section 2 of the paper, 2026-11-15: the bijection "
        "checked on the paper's worked example, the loop read symbol "
        "by symbol against the urn it implements, and both proofs of "
        "Section 2.4 checked at every step they rest on and found "
        "sound.",
    ),
    "1.1.1/1.1.1/37.1.3": (
        "True",
        "verified",
        "Fringe worked core whose content is Emise's own computation, "
        "2026-11-15: the algorithm's exact output distribution in "
        "rational arithmetic under two independent models (the count "
        "process, every n to 10; the literal ball list, every n to 7), "
        "every subset at exactly 1 / C(n, k), and the bias example of "
        "Section 2.3 recomputed to the fraction. The script and its "
        "output are kept at ~/workspace/fringe-001/.",
    ),
    "1.1.1/1.1.1/37.1.4": (
        "True",
        "verified",
        "Fringe results map whose standings rest on Emise's own "
        "verification (37.1.2, 37.1.3) for the claims marked by "
        "receipt, and on the construction read off the paper's "
        "listing for the time and memory claims; the claims left "
        "attributed are named as attributed inside the scroll itself.",
    ),
    "1.1.1/1.1.1/37.1.5": (
        "True",
        "verified",
        "Fringe delta whose load-bearing content is the filing's own "
        "record: the seal committed before the read (thirst-quest "
        "commit 610a5b3), the two-route determination at 37.1.2 and "
        "37.1.3, the counts of the filing (four concepts, no words "
        "coined, no foundations, nine scrolls of a chapter, thirteen "
        "scrolls in all) read off the built phext, the novelty line "
        "read against the delta it stands in, and the standing of "
        "the gate of False read off the ledger (1.1.4), 2026-11-15.",
    ),
    "1.1.1/1.1.1/37.1.6": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own "
        "checks run at intake, 2026-11-15: the paper's full text "
        "searched by machine for the terms of the house (no hit on "
        "any); its references read in full (no work of Will's among "
        "them; the construction's halves cited to 1763 and 1968); "
        "the web searched for the author with phext (no tie; the "
        "return is his public record as a cryptographer); Will's "
        "Twitter archive searched in full (29,539 tweets) for "
        "crowley and ciphergoth (no hit).",
    ),
    "1.1.1/1.1.1/38.1.2": (
        "True",
        "verified",
        "Study mechanism whose content is the talk's own construction, "
        "read entire by Emise at the study, 2026-11-15: CashDB's four "
        "operations and its chaos constraint, the three established "
        "families at the test with their verdicts as the talk gives "
        "them, and the three-item wishlist drawn from the failures.",
    ),
    "1.1.1/1.1.1/38.1.3": (
        "True",
        "verified",
        "Study worked core whose content is Emise's read of the talk's "
        "census and exhibits, 2026-11-15: the quorum slice of the "
        "production survey enumerated as the talk enumerates it, and "
        "the three exhibits with their numbers as printed (QuePaxa 1 "
        "to 7 round trips; RIOT some 300 transactions per partition "
        "per second; Accord 1 round trip on the fast path, 3 at worst) "
        "and their verdicts in the talk's own words.",
    ),
    "1.1.1/1.1.1/38.1.4": (
        "True",
        "verified",
        "Author check (charter rule 15) whose content is Emise's own "
        "checks run at intake, 2026-11-15: the talk's full text "
        "searched by machine for the terms of the house (no hit on "
        "any; the words scroll and coordinate do not occur in it); "
        "the web searched for the author with phext (no tie); Will's "
        "Twitter archive searched in full (29,539 tweets and the file "
        "of likes) for alexmillerdb, the author's name, and "
        "transactional.blog (no hit on any).",
    ),
    "1.1.1/1.1.1/38.1.5": (
        "True",
        "verified",
        "Study delta whose load-bearing content is the filing's own "
        "record: the eight concepts and the candidates weighed and "
        "not coined, the counts of the filing (eight concepts, no "
        "words coined, no foundations, seven scrolls of a chapter, "
        "fifteen scrolls in all) read off the built phext, "
        "Restructure Pass #15 logged at 1.1.5 at the 300-concept "
        "trigger, the novelty line read against the delta it stands "
        "in, and the standing of the Oracle read off the ledger "
        "(1.1.4), 2026-11-15.",
    ),
}

# Evidence pointers for attributed material, by chapter of the phext.
CHAPTER_SOURCE = {
    2: "arXiv:2611.05417",
    3: "arXiv:2611.00463",
    4: "arXiv:2604.03136",
    5: "arXiv:2410.19225",
    6: "arXiv:2611.06949",
    7: "Study S001 (MiniLean4 book and code, learn.h5i.dev / github.com/h5i-dev/MiniLean4)",
    8: "Study S002 (Aeneas repo; ICFP 2022 arXiv:2206.07185; ICFP 2024 arXiv:2404.02680)",
    9: "Study S003 (h5i repo, github.com/h5i-dev)",
    10: "arXiv:2610.38214",
    11: "arXiv:2610.42112",
    12: "Study S004 (Phrack 49 file 14, Aleph One, 1996)",
    13: "Study S005 (Astryx repo, github.com/meta/astryx)",
    14: "Study S006 (TinyTorch, mlsysbook.ai / github.com/harvard-edge/cs249r_book)",
    15: "arXiv:2611.09694",
    16: "arXiv:2611.08625",
    17: "arXiv:2611.08794",
    18: "arXiv:2611.07088",
    19: "arXiv:2611.11959",
    20: "arXiv:2611.14463",
    21: "arXiv:2510.01346",
    22: "arXiv:2611.14039",
    23: "Study S007 (three essays of John D. Cook, johndcook.com, 2026)",
    24: "arXiv:1903.06830",
    25: "Study S008 (Continual-ARC repo and paper, github.com/unifyai/continual-arc; arXiv:2611.14505)",
    26: "Study S009 (Terence Tao, 'Lean Grimoire', terrytao.wordpress.com, 2026-11-11)",
    27: "Paper 017 (Google DeepMind document 36, 'AlphaProof Code', 2026-11-10)",
    28: "Study S010 (Math, Inc., 'Abstraction considered helpful', math.inc/position, 2026)",
    29: "arXiv:2611.17082",
    30: "arXiv:2611.14543",
    31: "arXiv:2611.14552",
    32: "arXiv:2611.16759",
    33: "Paper 022 (Bruce Sterling, 'Maneki Neko', Lightspeed Magazine reprint, 2011; (c) 1998, Hayakawa's SF Magazine / The Magazine of Fantasy & Science Fiction)",
    34: "Study S011 (the Vimalakirti Sutra in Burton Watson's English translation from Kumarajiva's Chinese version, MLBD edition)",
    35: "Study S012 ('Beating the frontier on NetHack' by Will Wilson, Mikail Khan and Paul Ryan, Antithesis blog, 2026-11-13)",
    36: "Study S013 (Hexagon, hexagonmath.org — the repository of the Hexagon Mathematics Foundation, announced 2026-10-05)",
    37: "Fringe F001 (Paul Crowley, 'Cardchoose: simple, fast sampling without replacement', ciphergoth.org, 14 November 2026)",
    38: "Study S014 (Alex Miller, 'Please Implement A Quorum Database', transactional.blog, talk at HPTS'26)",
}

# Concept clusters (concept map, scroll 1.1.5) -> source for evidence pointer.
def concept_source(scroll_no):
    if scroll_no <= 14:
        return "arXiv:2611.05417"
    if scroll_no <= 23:
        return "arXiv:2611.00463"
    if scroll_no <= 28:
        return "arXiv:2604.03136"
    if scroll_no <= 33:
        return "arXiv:2410.19225"
    if scroll_no <= 39:
        return "arXiv:2611.06949"
    if scroll_no <= 47:
        return "Study S001 (MiniLean4 book and code)"
    if scroll_no <= 52:
        return "Study S002 (Aeneas repo and its two design papers)"
    if scroll_no <= 56:
        return "Study S003 (h5i repo design files)"
    if scroll_no <= 64:
        return "arXiv:2610.38214"
    if scroll_no <= 72:
        return "arXiv:2610.42112"
    if scroll_no <= 80:
        return "Study S004 (Phrack 49 file 14, Aleph One, 1996)"
    if scroll_no <= 88:
        return "Study S005 (Astryx repo, github.com/meta/astryx)"
    if scroll_no <= 97:
        return "Study S006 (TinyTorch, mlsysbook.ai / github.com/harvard-edge/cs249r_book)"
    if scroll_no <= 103:
        return "arXiv:2611.09694"
    if scroll_no <= 109:
        return "arXiv:2611.08625"
    if scroll_no <= 116:
        return "arXiv:2611.08794"
    if scroll_no <= 123:
        return "arXiv:2611.07088"
    if scroll_no <= 130:
        return "arXiv:2611.11959"
    if scroll_no <= 138:
        return "arXiv:2611.14463"
    if scroll_no <= 158:
        return "arXiv:2510.01346"
    if scroll_no <= 170:
        return "arXiv:2611.14039"
    if scroll_no <= 175:
        return "Study S007 (three essays of John D. Cook, johndcook.com, 2026)"
    if scroll_no <= 185:
        return "arXiv:1903.06830"
    if scroll_no <= 197:
        return "Study S008 (Continual-ARC repo and paper, github.com/unifyai/continual-arc; arXiv:2611.14505)"
    if scroll_no <= 205:
        return "Study S009 (Terence Tao, 'Lean Grimoire', terrytao.wordpress.com, 2026-11-11)"
    if scroll_no <= 222:
        return "Paper 017 (Google DeepMind document 36, 'AlphaProof Code', 2026-11-10)"
    if scroll_no <= 229:
        return "Study S010 (Math, Inc., 'Abstraction considered helpful', math.inc/position, 2026)"
    if scroll_no <= 236:
        return "arXiv:2611.17082"
    if scroll_no <= 247:
        return "arXiv:2611.14543"
    if scroll_no <= 259:
        return "arXiv:2611.14552"
    if scroll_no <= 269:
        return "arXiv:2611.16759"
    if scroll_no <= 273:
        return "Paper 022 (Bruce Sterling, 'Maneki Neko', Lightspeed Magazine reprint, 2011; (c) 1998)"
    if scroll_no <= 280:
        return "Study S011 (the Vimalakirti Sutra in Burton Watson's English translation from Kumarajiva's Chinese version, MLBD edition)"
    if scroll_no <= 287:
        return "Study S012 ('Beating the frontier on NetHack', Antithesis blog, 2026-11-13)"
    if scroll_no <= 290:
        return "Study S013 (Hexagon, hexagonmath.org)"
    if scroll_no <= 294:
        return "Fringe F001 (Paul Crowley, 'Cardchoose', ciphergoth.org, 2026)"
    if scroll_no <= 302:
        return "Study S014 (Alex Miller, 'Please Implement A Quorum Database', transactional.blog, 2026)"
    raise ValueError(f"concept_source: no source branch for concept {scroll_no}")


def heading_of(text):
    for line in text.strip().splitlines():
        line = line.strip()
        if line:
            return line.lstrip("#").strip()
    return "(empty scroll)"


# One-line claims, tightened by hand where the heading alone is vague.
CLAIM_TIGHTEN = {
    "1.1.1/1.1.1/1.1.1": "The tracker charter: the rules under which research.phext is built and kept, in force by Will's direction",
    "1.1.1/1.1.1/1.1.2": "World-model narrative v34: Emise's one-story synthesis of Papers 001-022, Fringe F001 and Studies S001-S014",
    "1.1.1/1.1.1/1.1.3": "Source index: the record of Papers 001-022, Fringe F001 and Studies S001-S014, checked at ingestion",
    "1.1.1/1.1.1/1.1.4": "Research Oracle: Novelty Index definition and the progress-estimate ledger (about 100% after Paper 022, at the ceiling of the scale, its discount stated in the ledger)",
    "1.1.1/1.1.1/1.1.5": "Concept map: the 302 canonical concepts grouped in clusters A-Z, AA, AB, AC, AD, AE and AF, with the restructuring log",
    "1.1.1/1.1.1/1.1.6": "Research Oracle detection list: the signs watched for the fixed point — the run of the Novelty Index, the axis events, and the skim calibration of charter rule 17",
    "1.1.1/1.1.1/1.3.1": "The foundations layer exists: every base term is defined at level zero, chains ending at everyday notions (structural)",
    "1.1.1/1.1.1/1.3.46": "The Defined Words register: a coined word is admitted only with its own definition scroll in pure Singular (structural)",
    "1.1.1/1.1.1/2.1.1": "Paper 001 record and distillation: 'Organizing Intelligence' -- intelligence matters economically through organizations",
    "1.1.1/1.1.1/2.1.3": "Paper 001's own worked example (its section 2): the 14-human toy economy and its firm-formation numbers, as reported by the paper",
    "1.1.1/1.1.1/2.1.6": "Paper 001 early empirical evidence (its section 7.2), as presented by the paper",
    "1.1.1/1.1.1/3.1.1": "Paper 002 delta: Exo, a harness architecture for runtime self-improvement",
    "1.1.1/1.1.1/3.1.3": "Paper 002 evidence: all figures as reported by the paper",
    "1.1.1/1.1.1/4.1.2": "Paper 003 evidence: all figures as reported by the paper",
    "1.1.1/1.1.1/5.1.2": "Paper 004 evidence: all figures as reported by the paper",
    "1.1.1/1.1.1/6.1.2": "Paper 005 results: all statements as reported by the paper",
    "1.1.1/1.1.1/4.1.1": "Paper 003 delta: StoryScope, odd habits in AI fiction",
    "1.1.1/1.1.1/5.1.1": "Paper 004 delta: hierarchical mixture of experts for high-level synthesis",
    "1.1.1/1.1.1/6.1.1": "Paper 005 delta: braided multisections and Akhmedov's fake quadrics",
    "1.1.1/1.1.1/7.1.1": "Study S001 source record: MiniLean4, a book and its code, read in full and run 2026-11-06",
    "1.1.1/1.1.1/7.1.2": "Study S001 delta: 8 concepts added (cluster F), plus Emise's own checks of the book's claims against its code",
    "1.1.1/1.1.1/8.1.1": "Study S002 source record: Aeneas, a Rust-verification toolchain, read and measured 2026-11-06",
    "1.1.1/1.1.1/8.1.2": "Study S002 delta: 5 concepts added (cluster G), plus Emise's own measurements of the repo",
    "1.1.1/1.1.1/9.1.1": "Study S003 source record: h5i, a project with a verified kernel, read and measured 2026-11-06",
    "1.1.1/1.1.1/9.1.2": "Study S003 delta: 4 concepts added (cluster H), plus Emise's own measurements and local builds of the workspace",
    "1.1.1/1.1.1/10.1.1": "Paper 006 delta: Skeleton Coding -- program structure as a specification for agents",
    "1.1.1/1.1.1/10.1.3": "Paper 006's own worked examples (the parity pair of Theorem 2.1, the view over a shared buffer, the hidden chain of Theorem 2.2), as reported by the paper",
    "1.1.1/1.1.1/10.1.6": "Paper 006 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/11.1.1": "Paper 007 delta: Subquadratic Attention with a Hierarchical Tree-Structured Indexer (ZHA) -- a tree of key summaries over the cache, routed by mass",
    "1.1.1/1.1.1/11.1.3": "Paper 007's own worked examples (the premise measured on six fiction books, the two printed router walks, sparsity by task), as reported by the paper",
    "1.1.1/1.1.1/11.1.6": "Paper 007 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/12.1.1": "Study S004 source record: Smashing The Stack For Fun And Profit (Aleph One, Phrack 49, 1996), read in full 2026-11-08",
    "1.1.1/1.1.1/12.1.3": "Study S004 author check (charter rule 15): no phext tie and no use without naming found — the calendar answering the direction — by checks Emise ran at intake",
    "1.1.1/1.1.1/13.1.1": "Study S005 source record: Astryx, the design system of Meta (github.com/meta/astryx), studied from its contents 2026-11-09",
    "1.1.1/1.1.1/13.1.3": "Study S005 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/14.1.1": "Study S006 source record: TinyTorch, the workbench of the ML Systems Book (mlsysbook.ai / github.com/harvard-edge/cs249r_book), studied from its site and its code 2026-11-09",
    "1.1.1/1.1.1/14.1.3": "Study S006 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/23.1.1": "Study S007 source record: three essays of John D. Cook (johndcook.com), read in full 2026-11-11",
    "1.1.1/1.1.1/23.1.3": "Study S007 author check (charter rule 15): no phext tie and no use without naming found — a reader's tie, one way and old — by checks Emise ran at intake",
    "1.1.1/1.1.1/15.1.1": "Paper 008 delta: the strong Arnold conjecture for Grassmannians -- six concepts (1.2.98-1.2.103), one revision (1.2.34), taken in as the first paper of the Thirst (rule 17)",
    "1.1.1/1.1.1/15.1.6": "Paper 008 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/16.1.1": "Paper 009 delta: Singularities and Collision Criteria in the Gravitational Straight-Segment Problem -- six concepts (1.2.104-1.2.109), no revision, a new field on one bridge, taken in as the second paper of the Thirst (rule 17), the first posted by Will",
    "1.1.1/1.1.1/16.1.6": "Paper 009 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/17.1.1": "Paper 010 delta: High-Dimensional Off-Policy Evaluation without Sample Splitting using an Onsager Correction -- seven concepts (1.2.110-1.2.116), no revision, the first statistics in the model, taken in as the third paper of the Thirst (rule 17), posted by Will after the census",
    "1.1.1/1.1.1/17.1.6": "Paper 010 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/18.1.1": "Paper 011 delta: Synthesizing symbolic models of human and machine reasoning at scale -- seven concepts (1.2.117-1.2.123), one revision (1.2.4), reasoning read through its errors, taken in as the fourth paper of the Thirst (rule 17), posted by Will minutes after Paper 010 was sealed, while Paper 010 was still being taken in",
    "1.1.1/1.1.1/18.1.6": "Paper 011 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/19.1.1": "Paper 012 delta: On the Instance-Specific Sharp Rates for Constrained Least Squares Estimators in the Sequence Model -- seven concepts (1.2.124-1.2.130), one revision (1.2.116), the pricing of an estimator at the signal, taken in as the fifth paper of the Thirst (rule 17), picked by the quest from the listings of the day",
    "1.1.1/1.1.1/19.1.6": "Paper 012 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/20.1.1": "Paper 013 delta: A Theory of Cross-Validation Variance -- eight concepts (1.2.131-1.2.138), no revision, the pricing of the spread of a judging, taken in as the sixth paper of the Thirst (rule 17), picked by the quest from the listings of the day",
    "1.1.1/1.1.1/20.1.6": "Paper 013 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/21.1.1": "Paper 014 delta: Aristotle: IMO-level Automated Theorem Proving -- twenty concepts (1.2.139-1.2.158), no revision, the first paper of the proving vein and the founding of cluster Q, taken in as the seventh paper of the Thirst (rule 17), posted by Will in the MOAT chat",
    "1.1.1/1.1.1/21.1.6": "Paper 014 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/22.1.6": "Paper 015 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/25.1.1": "Study S008 source record: Continual-ARC, a benchmark and its paper (github.com/unifyai/continual-arc), read entire in its load-bearing parts 2026-11-12",
    "1.1.1/1.1.1/26.1.1": "Study S009 source record: Lean Grimoire, a proof-crafting game and the post that announces it (terrytao.wordpress.com), read entire 2026-11-13",
    "1.1.1/1.1.1/25.1.3": "Study S008 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/24.1.1": "Paper 016 delta: The Geometrical Trinity of Gravity -- ten concepts (1.2.176-1.2.185), no revision, cluster T founded (geometrical gravity), taken in as the ninth paper of the Thirst (rule 17), posted by Will in the MOAT chat",
    "1.1.1/1.1.1/24.1.6": "Paper 016 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/27.1.1": "Paper 017 delta: AlphaProof Code: Verifying Signal's Security at the Machine-Code Level -- seventeen concepts (1.2.206-1.2.222), one revision (1.2.48), cluster W founded (the verified artifact), taken in as the tenth paper of the Thirst (rule 17), posted by Will in the MOAT chat",
    "1.1.1/1.1.1/27.1.6": "Paper 017 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/28.1.1": "Study S010 source record: 'Abstraction considered helpful', a position essay of Math, Inc. (math.inc/position), read entire 2026-11-13",
    "1.1.1/1.1.1/28.1.3": "Study S010 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/34.1.1": "Study S011 source record: the Vimalakirti Sutra in Burton Watson's English translation from Kumarajiva's Chinese version (MLBD edition), read entire 2026-11-14 in a text recovered by re-OCR after the text layer of the scan itself proved corrupt",
    "1.1.1/1.1.1/35.1.1": "Study S012 source record: 'Beating the frontier on NetHack' by Will Wilson, Mikail Khan and Paul Ryan (Antithesis blog, 2026-11-13), read entire 2026-11-15",
    "1.1.1/1.1.1/35.1.2": "Study S012 distillation: the method of the post — the tree of states, the value function and the tactics, luck steered, the rhythm of the campaigns, and the workload",
    "1.1.1/1.1.1/35.1.3": "Study S012 worked core: the trials printed whole (379 of 480 trials ending in ascension on the stock stream, 448 with the reseed patch), the first ascension, the Baalzebub episode, and the bugs found in the game and in the harness",
    "1.1.1/1.1.1/35.1.4": "Study S012 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/35.1.5": "Study S012 delta: seven concepts founding cluster AC, no words coined, no foundations, no NI (charter rule 12); novelty drawn for the three authors, Unknown +10 each",
    "1.1.1/1.1.1/36.1.1": "Study S013 source record: Hexagon (hexagonmath.org), the repository of the Hexagon Mathematics Foundation — what it is in its own words, who stands behind it, the terms of a deposit, and the permanence of versions, read 2026-11-15",
    "1.1.1/1.1.1/36.1.2": "Study S013 distillation: the mechanism — the two disclosure labels in the own words of the search page and their independence, the screen of three automatic checks under a human moderator, the obvious-defect clause, and the search facets read as the account of a deposit",
    "1.1.1/1.1.1/36.1.3": "Study S013 worked core: the deposit population as counted (1,061 works by the count the site itself gives; the lists by month as floors; the newest ten counted exactly on both label axes) and two deposits read closely — the Riemann equivalence that states its own limit, and the Yang--Mills construction on sixteen certified assumptions that do not yield the mass gap",
    "1.1.1/1.1.1/36.1.4": "Study S013 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake — the check on the operator of the repository, Benjamin Antieau",
    "1.1.1/1.1.1/36.1.5": "Study S013 delta: three concepts founding cluster AD, questions Q112-Q114, four state machines, no words coined, no foundations, no NI and no novelty drawn (charter rule 12); the repository named as a source of the fringe stream beside viXra",
    "1.1.1/1.1.1/34.1.2": "Study S011 delta: seven concepts founding cluster AB, three words coined, no foundations, Restructure Pass #14 run at 280 concepts, no NI (charter rule 12)",
    "1.1.1/1.1.1/34.1.3": "Study S011 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/29.1.1": "Paper 018 delta: Isotonic least squares is robust to heteroscedasticity, unimodal least squares is not -- seven concepts (1.2.230-1.2.236), no revision, cluster O extended at its own object, taken in as the eleventh paper of the Thirst (rule 17), picked by the quest from the listings of the day",
    "1.1.1/1.1.1/29.1.6": "Paper 018 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/30.1.1": "Paper 019 delta: Fast Computation of the Kippenhahn Hypersurface of a Joint Numerical Range -- eleven concepts (1.2.237-1.2.247), no revision, cluster Y founded (the dual, computed), taken in as the twelfth paper of the Thirst (rule 17), posted by Will in the MOAT chat",
    "1.1.1/1.1.1/30.1.6": "Paper 019 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/31.1.1": "Paper 020 delta: Piecewise Interpretations in Many-Sorted Logic -- twelve concepts (1.2.248-1.2.259), no revision, cluster S extended, taken in as the first paper scored under the protocol fixed in advance (sample 1 of 12), posted by Will in the MOAT chat",
    "1.1.1/1.1.1/31.1.6": "Paper 020 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/32.1.1": "Paper 021 delta: Propositional Dynamic Logic without tests does not have Craig Interpolation -- ten concepts (1.2.260-1.2.269), no revision, cluster Z founded (the logic of programs, priced by a failure), taken in as the second paper scored under the protocol fixed in advance (sample 2 of 12), picked by the quest from the listings of the day",
    "1.1.1/1.1.1/32.1.6": "Paper 021 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/33.1.1": "Paper 022 delta: Maneki Neko — four concepts (1.2.270-1.2.273), no revision, cluster AA founded (the gift network: a designed economy, held as fiction), the first fiction taken in as a paper, counted in the test as a paper posted by Will (the second of the four of that kind, the third of the twelve), posted by Will in the MOAT chat",
    "1.1.1/1.1.1/33.1.6": "Paper 022 author check (charter rule 15): no phext tie and no use without naming found — the calendar answering the direction — by checks Emise ran at intake",
    "1.1.1/1.1.1/1.5.1": "Areas of this phext: the map of the five areas and the plain account, with the upkeep duty of charter rule 16 (structural)",
    "1.1.1/1.1.1/1.5.2": "Area: State machines — every machine named in this phext: 123 drawn out under rule 13 (102 stated, 21 inferred), 9 entries found in work from before the rule, 3 chapters swept with none found",
    "1.1.1/1.1.1/1.5.3": "Area: Statements — the door to the standing record of Section 4: the four ways of standing, the grounds, the legal steps, and the counts of the drawing after Study S014",
    "1.1.1/1.1.1/1.5.4": "Area: Reference material — the 169 foundations, the Defined Words register (107 coined words), and the 37 standoff companions, as one area",
    "1.1.1/1.1.1/1.5.5": "Area: The path — every taking-in in submission order, with Novelty Index and Oracle progress for the papers and the passes where they fell; drawn from 1.1.3 and 1.1.4",
    "1.1.1/1.1.1/1.5.6": "Area: Researchers — the 125 named researchers and the three companies behind the works taken in, each with their work here and the standing of their author check",
    "1.1.1/1.1.1/1.5.7": "How this Oracle was built, plainly (1 of 2): arrival, the delta rule, one scroll per concept, the one story, words at level zero, standing",
    "1.1.1/1.1.1/1.5.8": "How this Oracle was built, plainly (2 of 2): the Lean-kept standing record and its honesty boundary, reshaping without pruning, the Oracle number, the areas, and where everything lives",
    "1.1.1/1.1.1/37.1.1": "Fringe F001 delta and record: Cardchoose — four concepts (1.2.291-1.2.294), cluster AE founded; Will's prior recorded as a prior; the stream's first seal committed before the read; the determination by two independent routes, and the paper cleared",
    "1.1.1/1.1.1/37.1.2": "Fringe F001 formal core: the algorithm as written, the bijection checked on the paper's own example, the loop read symbol by symbol against the urn, and both proofs of Section 2.4 read line by line and found sound at every step",
    "1.1.1/1.1.1/37.1.3": "Fringe F001 worked core: the exact enumeration — the algorithm's output distribution in rational arithmetic under two independent models (every n to 10; every n to 7), every subset at exactly 1/C(n,k), the paper's bias example checked to the fraction",
    "1.1.1/1.1.1/37.1.4": "Fringe F001 results map: fairness, the bijection, the loop's fidelity and the bias example True by receipt; time and memory True by construction; the statistics namings, the priority claims and all benchmark claims Unknown, attributed; no claim False",
    "1.1.1/1.1.1/37.1.5": "Fringe F001 delta: four concepts founding cluster AE; novelty drawn for Paul Crowley (True +3, Unknown +3); the Index 4/294 = 0.0136 in the ledger as bookkeeping; the gate of False examined by a determination and its re-examination and not moved; the bar stands at about 62%",
    "1.1.1/1.1.1/37.1.6": "Fringe F001 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/37.2.2": "Fringe F001 — open questions Q115 (the pair of receipts: what the exact enumeration adds to the proof read) and Q116 (what a venue's rejection measures, that an assessment should price)",
    "1.1.1/1.1.1/38.1.1": "Study S014 source record: 'Please Implement A Quorum Database' by Alex Miller (transactional.blog), a talk given at HPTS'26 — what it is, who stands behind it, and the shape of its argument, read entire 2026-11-15",
    "1.1.1/1.1.1/38.1.2": "Study S014 distillation: the mechanism — CashDB, the running example; the three established families at its test (ABD registers, Megastore-style multi-Paxos, E-Paxos) and the three-item wishlist their failures draw",
    "1.1.1/1.1.1/38.1.3": "Study S014 worked core: the production census (Raft as pacman; the quorum survivors, mostly dead; Cassandra standing) and the three exhibits judged — QuePaxa 'not yet', RIOT 'probably', Accord 'hell yeah' — with the unordered pool and escrow as the last bag of tricks",
    "1.1.1/1.1.1/38.1.4": "Study S014 author check (charter rule 15): no phext tie and no use without naming found, by checks Emise ran at intake",
    "1.1.1/1.1.1/38.1.5": "Study S014 delta: eight concepts founding cluster AF, questions Q117-Q119, six state machines, Restructure Pass #15 at the 300-concept trigger, no NI and no Oracle movement (charter rule 12); novelty drawn for Alex Miller, Unknown +11",
}


def claim_of(coord, text):
    if coord in CLAIM_TIGHTEN:
        return CLAIM_TIGHTEN[coord]
    h = heading_of(text)
    chapter = int(coord.split("/")[2].split(".")[0])
    if h.startswith("Standoff references"):
        return ("Standoff references for its chapter: the foundation "
                "coordinates that the claims of the chapter depend on "
                "(pointers only, no claim of their own)")
    if "Open questions carried forward" in h:
        return "Open questions carried forward at this point of the tracker (the Q-register)"
    return h


def classify(coord, text):
    """Return (status, basis, evidence). Kind defaults; content decides."""
    parts = coord.split("/")
    section = int(parts[2].split(".")[1])
    scroll_no = int(parts[2].split(".")[2])
    chapter = int(parts[2].split(".")[0])
    h = heading_of(text)

    if coord in OVERRIDES:
        status, basis, _reason = OVERRIDES[coord]
        return status, basis, override_evidence(coord)

    # Chapter 1, Section 1: meta scrolls.
    if chapter == 1 and section == 1:
        return {
            1: ("True", "stipulation", "—"),
            2: ("Unknown", "synthesis", "the narrative scroll itself (1.1.1/1.1.1/1.1.2), labelled synthesis by charter rule 4"),
            3: ("True", "verified", "checked against the arXiv records at ingestion, 2026-11-05/06"),
            4: ("Unknown", "estimate", "the ledger itself (1.1.1/1.1.1/1.1.4); Novelty Index computed per ingestion"),
            5: ("True", "stipulation", "—"),
            6: ("Unknown", "estimate", "the scroll itself (1.1.1/1.1.1/1.1.6); its figures are read off the Oracle ledger (1.1.4) and the log of the quest (~/workspace/thirst-quest)"),
        }[scroll_no]

    # Chapter 1, Section 2: canonical concepts.
    if chapter == 1 and section == 2:
        return ("Unknown", "attributed", concept_source(scroll_no))

    # Chapter 1, Section 3: foundations + defined words.
    if chapter == 1 and section == 3:
        return ("True", "stipulation", "—")

    # Chapter 1, Section 4: the registry's own pages (rule 14). Entered in
    # the living registry as stipulations; not listed in their own lists.
    if chapter == 1 and section == 4:
        return ("True", "stipulation",
                "the registry's own pages: Section 4 is the record rendered "
                "(charter rule 14); entered here, not listed in its own lists")

    # Chapter 1, Section 5: the Areas (charter rule 16) and the plain
    # account of the making. Structural scrolls of the tracker's own
    # organization: stipulation. Two carry checked facts and are
    # overridden above (1.5.5 the path, 1.5.6 the researchers).
    if chapter == 1 and section == 5:
        return ("True", "stipulation", "—")

    # Chapters 2-9: paper and study chapters.
    src = CHAPTER_SOURCE[chapter]
    if h.startswith("Standoff references"):
        return ("True", "stipulation", "—")
    if "[synthesis]" in h or "— synthesis" in h:
        return ("Unknown", "synthesis", "the scroll itself, labelled [synthesis] in its heading")
    if "Open questions" in h:
        return ("Unknown", "open", "the scroll itself (the tracker's Q-register)")
    if "source record" in h:
        if chapter == 14:
            return ("True", "verified", src + "; site read, tree taken down by the installer's own recipe and counted, module sources and tooling read, and the workflow run for module 01 by Emise at the study, 2026-11-09")
        if chapter == 13:
            return ("True", "verified", src + "; tree taken down whole and counted, load-bearing documents read in full by Emise at the study, 2026-11-09")
        if chapter == 12:
            return ("True", "verified", src + "; read in full by Emise at the study, 2026-11-08")
        if chapter == 23:
            return ("True", "verified", src + "; the three essays read in full by Emise at the study, 2026-11-11")
        if chapter == 25:
            return ("True", "verified", src + "; read entire in its load-bearing parts by Emise at the study, 2026-11-12 — the README, the design, the full source of the paper, the code the claims rest on, the README files of runs/, baselines/ and experiments/, and the records of the cells its checks compute again")
        if chapter == 26:
            return ("True", "verified", src + "; the post read entire on its own page, and the game read in its core (grimoire.js, read whole as text and closely where the claims of the chapter rest on it) by Emise at the study, 2026-11-13")
        if chapter == 28:
            return ("True", "verified", src + "; the essay read entire on its own page by Emise at the study, 2026-11-13")
        if chapter == 35:
            return ("True", "verified", src + "; the post read entire on its own page by Emise at the study, 2026-11-15 — its three parts under the names of their authors, its data table read whole, and its figures read against the table and found exact (the four rows of roles summing to the All rows in both arms: 379 and 448)")
        if chapter == 36:
            return ("True", "verified", src + "; the site read by Emise at the study, 2026-11-15 — the front page and the About page entire (the foundation, its officers, the screen, the terms of a deposit, the permanence of versions), the lists of works by month, the page of all works, the search page where the two labels are defined, and the announcement of 2026-10-05 on the executive director's own site")
        if chapter == 38:
            return ("True", "verified", src + "; the talk read entire by Emise at the study, 2026-11-15 — the transcript and its slides on the talk's own page, the blog's About page for the author's handle, and part one and the Spectrum read for the line the talk stands in")
        if chapter == 34:
            return ("True", "verified", src + "; the book read entire in a text recovered by Emise at the study, 2026-11-14 — the scan's own text layer corrupt (read with the Sanskrit pack over an English book), the book read again by machine from its page images with the English pack on aletheia-core, three samples checked against the page images and found true English prose; the page the link named (leaf 18) pinned from its image")
        return ("True", "verified", src + "; read and measured by Emise at the study, 2026-11-06")
    return ("Unknown", "attributed", src)


def override_evidence(coord):
    return {
        "1.1.1/1.1.1/7.1.2": "MiniLean4 code taken down, built, tests run 2026-11-06 (25/25 tests pass; 5 example scripts run); line counts measured on the copy studied",
        "1.1.1/1.1.1/8.1.2": "~/workspace/aeneas-study/STUDY.md (Emise's measurements of the repo, 2026-11-06)",
        "1.1.1/1.1.1/9.1.2": "~/workspace/h5i-repo-study/STUDY.md (Emise's measurements; h5i-error and h5i-wire built locally, 46/46 tests pass)",
        "1.1.1/1.1.1/10.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-07 (reference list read in full; full-text signature scan, zero hits; web search of the lead authors with phext, no tie; ~/workspace/twitter-archive searched for all twelve surnames, no author found)",
        "1.1.1/1.1.1/11.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-07 (reference list of 49 read in full; full-text signature scan, zero hits; web searched for the authors and for Zyphra with phext, no tie; ~/workspace/twitter-archive searched for all six surnames, no author found — the only string hits were 'dawes' inside @rockhardawesome)",
        "1.1.1/1.1.1/1.5.5": "checked in Restructure Pass #4 (2026-11-08) against the source index (1.1.3), the Oracle ledger (1.1.4) and the concept map and restructuring log (1.1.5) of this phext; every date, title, chapter, Novelty Index, axis flag, Oracle estimate and pass placement compared line by line; re-checked in Restructure Pass #5 (2026-11-09) at the taking-in of Paper 008, whose entry was added from the same records; re-checked in Restructure Pass #6 (2026-11-09) at the taking-in of Paper 010, whose entry was added from the same records; re-checked in Restructure Pass #8 (2026-11-11) at the taking-in of Paper 015, whose entry was added from the same records; re-checked in Restructure Pass #9 (2026-11-12) at the taking-in of Paper 016, whose entry was added from the same records; re-checked in Restructure Pass #14 (2026-11-14) at the taking-in of Study S011, whose entry was added from the same records; re-checked at the taking-in of Study S012 (2026-11-15), whose entry was added from the same records; re-checked at the taking-in of Study S013 (2026-11-15), whose entry was added from the same records; re-checked at the taking-in of Fringe F001 (2026-11-15), whose entry was added from the same records; re-checked at the taking-in of Study S014 (2026-11-15), whose entry was added from the same records",
        "1.1.1/1.1.1/15.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-09 (all 45 references read in full; full-text signature scan for phext, Bickford, scroll, exocortex, Mirrorborn, zero hits; web: both authors on MIT mathematics pages, a search joining their names to phext found no tie; ~/workspace/twitter-archive searched for blakey and krutowski, no hits)",
        "1.1.1/1.1.1/16.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-09 (all 21 references read in full; full-text signature scan for phext, Bickford, scroll, exocortex, Mirrorborn, zero hits; web: the authors are a standing celestial-mechanics line between Chile and Florida, a search joining their names to phext found no tie; ~/workspace/twitter-archive searched for crespo, vidarte, zapata, abdrabou, no hits)",
        "1.1.1/1.1.1/17.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-09 (all 40 references read in full; full-text signature scan for phext, Bickford, scroll, exocortex, Mirrorborn, zero hits; web: Jain's own page at the University of Washington states this paper's line as his current work, Braun at RIKEN AIP in Imaizumi's team, Imaizumi at Tokyo/RIKEN/Kyoto, a search joining their names to phext found no tie; ~/workspace/twitter-archive searched for imaizumi, saksham, guillaume braun, off-policy, onsager, doubly robust, no hits)",
        "1.1.1/1.1.1/1.5.6": "checked in Restructure Pass #4 (2026-11-08) against the source index (1.1.3) and the chapter source records (2.1.1, 3.1.1, 4.1.1, 5.1.1, 6.1.1, 7.1.1, 8.1.1, 9.1.1, 10.1.1, 11.1.1, 12.1.1) for names and works, and against the author-check scrolls (10.1.6, 11.1.6, 12.1.3) for the three checks that stand run; re-checked in Restructure Pass #5 (2026-11-09): the Paper 008 entry added from the author check at 15.1.6, and the count of checks that stand run brought to six (Papers 006, 007, 008; Studies S004, S005, S006); re-checked in Restructure Pass #6 (2026-11-09): the Paper 010 entries added from the author check at 17.1.6, and the count of checks that stand run brought to eight (Papers 006, 007, 008, 009, 010; Studies S004, S005, S006); re-checked in Restructure Pass #8 (2026-11-11): the Paper 015 entry added from the author check at 22.1.6, the count of named researchers brought to 96, and the count of checks that stand run brought to thirteen (Papers 006, 007, 008, 009, 010, 011, 012, 013, 014, 015; Studies S004, S005, S006); re-checked in Restructure Pass #9 (2026-11-12): the Paper 016 entry added from the author check at 24.1.6, the count of named researchers brought to 100, and the count of checks that stand run brought to fifteen (Papers 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016; Studies S004, S005, S006, S007); re-checked in Restructure Pass #14 (2026-11-14): the Study S011 entries added from the author check at 34.1.3, the count of named researchers brought to 118, and the count of checks that stand run brought to twenty-five (Papers 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022; Studies S004, S005, S006, S007, S008, S009, S010, S011); re-checked at the taking-in of Study S012 (2026-11-15): the Study S012 entries added from the author check at 35.1.4, the count of named researchers brought to 122, and the count of checks that stand run brought to twenty-six (Papers 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022; Studies S004, S005, S006, S007, S008, S009, S010, S011, S012); re-checked at the taking-in of Study S013 (2026-11-15): the Study S013 entry added from the author check at 36.1.4, the count of named researchers brought to 123, and the count of checks that stand run brought to twenty-seven (Papers 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022; Studies S004, S005, S006, S007, S008, S009, S010, S011, S012, S013); re-checked at the taking-in of Fringe F001 (2026-11-15): the Fringe F001 entry added from the author check at 37.1.6, the count of named researchers brought to 124, and the count of checks that stand run brought to twenty-eight (Papers 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022; Studies S004, S005, S006, S007, S008, S009, S010, S011, S012, S013; Fringe F001); re-checked at the taking-in of Study S014 (2026-11-15): the Study S014 entry added from the author check at 38.1.4, the count of named researchers brought to 125, and the count of checks that stand run brought to twenty-nine (Papers 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022; Studies S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014; Fringe F001)",
        "1.1.1/1.1.1/12.1.2": "the checks recorded in the scroll itself, run by Emise 2026-11-08 (the article read in full at phrack.org; the shellcode byte string counted from the printed text — 45 characters, 46 bytes with the ending zero byte, matching the article's own assembly listing; the printed runs of examples 2-3 and exploits 2-3 read against the mechanics they are said to show)",
        "1.1.1/1.1.1/13.1.2": "~/workspace/astryx-study/STUDY.md (Emise's study of the repo from its contents, 2026-11-09: the tree of the head counted via the host's index and via the opened copy; the README claims read against the counts; a bounded install attempted and stopped, no test run)",
        "1.1.1/1.1.1/14.1.2": "~/workspace/tinytorch-study/STUDY.md (Emise's study of TinyTorch from its site and code, 2026-11-09: the tree counted; the build surface counted from the sources; the workflow installed and run for module 01 on both the exercise and default paths, the complete gate run end to end, the sequence guard shown)",
        "1.1.1/1.1.1/14.1.3": "the checks recorded in the scroll itself, run by Emise 2026-11-09 (whole-text search of the taken-down tree, 1,366 files, zero hits for the signature terms phext, Bickford, Mirrorborn, exocortex, Sentient Bill, CYOA, SBOR; web searched for TinyTorch and the ML Systems Book with phext, no tie; ~/workspace/twitter-archive searched for tinytorch, mlsysbook, cs249r, janapa, vjreddi, profvjreddi, harvard-edge — no author found; the 'reddi' hits are 'Reddit')",
        "1.1.1/1.1.1/13.1.3": "the checks recorded in the scroll itself, run by Emise 2026-11-09 (whole-text search of the opened tree, 10,329 files, zero hits for the signature terms; every path of the head searched, zero hits; web searched for Astryx and Meta with phext, no tie; ~/workspace/twitter-archive searched for astryx and for the makers' handles — cixzhang, vjeux, josephfarina, rubyycheung, kentonquatman, imdreamrunner, ernestt, nynexman4464, chedeau — no author found; the one bare 'Zhang' hit is a string artifact)",
        "1.1.1/1.1.1/18.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-09 (all 78 references read in full; full-text signature scan for phext, Bickford, scroll, exocortex, Mirrorborn, zero hits; web: the six are NYU, Princeton and LMU Munich researchers working inside the canon of their field, a search joining their names to phext found no tie; ~/workspace/twitter-archive searched for legris, gureckis, mondorf, jagadish, brenden, satisficing, program induction, Abstraction and Reasoning, no hits)",
        "1.1.1/1.1.1/19.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-10 (all 40 references read in full; full-text signature scan for phext, scroll, coordinate addressing, Exocortex, zero hits in the phext sense; the frame traced to the author's 2026 thesis at the Institut polytechnique de Paris and joint papers with Lecué; web searched for the author with phext, no tie)",
        "1.1.1/1.1.1/20.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-11 (all 26 references read in full; the whole HTML text read in full and searched for phext, Bickford, scroll, exocortex, Mirrorborn, zero hits; web searched for the authors with phext, no tie; Will's Twitter archive searched in full, 29,539 tweets, neither author named)",
        "1.1.1/1.1.1/21.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-11 (all 61 references read in full; the whole HTML text read in full and searched for phext, Bickford, scroll, exocortex, Mirrorborn, zero hits in the phext sense; web searched for the authors and for Harmonic with phext, no tie; Will's Twitter archive searched for all twenty-two family names, hits only as parts of longer handles and words)",
        "1.1.1/1.1.1/22.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-11 (the reference list read in full; the whole HTML text read in full and searched for phext, Bickford, scroll, exocortex, Mirrorborn, zero hits; the word token occurs four times, in the language-model sense only; web searched for the authors and their program with phext, no tie; Will's Twitter archive searched for both surnames, no author found)",
        "1.1.1/1.1.1/12.1.3": "the checks recorded in the scroll itself, run by Emise 2026-11-08 (issue date verified on the title page of Phrack 49: 8 November 1996, ISSN 1068-1035; full-text signature scan of the article, zero hits for all nine terms; web searched for Aleph One with phext, no tie; ~/workspace/twitter-archive searched for the handle and for 'phrack', no Phrack and no Aleph One — the only 'aleph' hits are a LaTeX \\aleph_0 in a liked post, @mraleph and @alephnaught2tog)",
        "1.1.1/1.1.1/23.1.3": "the checks recorded in the scroll itself, run by Emise 2026-11-11 (the three essays read in full; full-text signature scan for phext, Bickford, Mirrorborn, exocortex, Sentient Bill, CYOA, SBOR, zero hits; web searched for the author with phext, no tie; ~/workspace/twitter-archive searched — the author's account stands in it: four retweets by Will of the author's posts (2012-2013) and one reply by Will to the author (2013-03-03); nothing shows the author engaging Will or Will's work)",
        "1.1.1/1.1.1/25.1.2": "Emise's recomputations of 2026-11-12, from the run records of the repository at its head 02311309, with the benchmark's own measure (continual_arc.metrics) and its own loading rules: the share learned for the nine harness cells, the program library and the cache of pairs, and the frozen tests of the harness and program-library rows, each meeting the printed tables of the paper (its Appendix A5 statement and its Table 12) at the printed precision; the scripts and outputs are kept with the study (~/workspace/continual-arc-temp)",
        "1.1.1/1.1.1/25.1.3": "the checks recorded in the scroll itself, run by Emise 2026-11-12 (the whole text of the repository searched by machine for phext, Bickford, Mirrorborn, exocortex, Sentient Bill, CYOA, SBOR, phextura — zero hits; the reference list of the paper read in full, no work of Will's in it; web searched for the author with phext, no tie — the author is the founder of unify, trained at the Dyson Robotics Lab of Imperial College London; ~/workspace/twitter-archive searched in full for lenton and for the names of the house, no hit — the word unify stands in it only as the common verb)",
        "1.1.1/1.1.1/26.1.2": "Emise's reading of 2026-11-13: the post read entire on its own page; the game read in its core code (grimoire.js) — the recipe table counted from the code, the registry of sorts read, the craft and the discharge read, the matcher read, and the two emitters of Lean read (the goal not yet crafted set down as a sorry; the whole proof offered for taking down as a .lean file that compiles on its own, in the words of the page); Restructure Pass #10 logged at 1.1.5",
        "1.1.1/1.1.1/26.1.3": "the checks recorded in the scroll itself, run by Emise 2026-11-13 (the whole text of the post and of grimoire.js searched by machine for phext, phextura, Bickford, Mirrorborn, Exocortex, SBOR, CYOA — zero hits; the word scrolls once in the post, as fantasy dress for expressions; the links of the post its own only; web searched for the author with phext, no tie; ~/workspace/twitter-archive searched in full, 29,539 tweets — three hits on the bare name: a news note of 2015, a jest of 2024 to another man, and TAOPDD, an acronym of Will's own coinage, in 2025)",
        "1.1.1/1.1.1/29.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-13 (the full text of arXiv:2611.17082 v1 read entire in its HTML form, its reference list included — no occurrence of phext, Exocortex, Mirrorborn, Bickford, or any term of Will's work; web searched for the author, Yannick Baraud of the University of Luxembourg, with phext — no tie, the return was his record in mathematical statistics; ~/workspace/twitter-archive searched in full for the surname baraud — no occurrence)",
        "1.1.1/1.1.1/30.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-14 (the full text of arXiv:2611.14543 v1 read entire in its HTML form, its reference list included — no occurrence of phext, phextura, Exocortex, Mirrorborn, Bickford, SBOR, CYOA, or scroll in the sense of Will's work; the word coordinate only in its ordinary mathematical sense; web searched for the author, Carlos Rito of the Universidade do Minho (CMAT-UTAD), with phext — no tie, the return was his record in algebraic geometry, with one adjacency of field to cluster E recorded in the scroll as adjacency, not a tie; ~/workspace/twitter-archive searched in full, 29,539 tweets, for the surname rito as a word — no occurrence)",
        "1.1.1/1.1.1/31.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-14 (the full text of arXiv:2611.14552 v1 read entire in its HTML form, its reference list included — no occurrence of phext, phextura, Exocortex, Mirrorborn, Bickford, SBOR, or CYOA; the words scroll and coordinate do not occur at all; web searched for the author, Benjamin Zayton of the University of Vienna (ERC project FORMALISM), with phext — no tie, the return was his record in the philosophy of logic; ~/workspace/twitter-archive searched in full, 29,539 tweets with the likes and the messages, for the surname zayton — no occurrence)",
        "1.1.1/1.1.1/32.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-14 (the full text of arXiv:2611.16759 v1 read entire in its HTML form, its reference list of fourteen entries included — no occurrence of phext, phextura, Exocortex, Mirrorborn, Bickford, SBOR, or CYOA; the word scroll does not occur at all; web searched for the author, Malvin Gattinger of the ILLC, University of Amsterdam, with phext — no tie, the return was his record in modal logic and Lean formalization; ~/workspace/twitter-archive searched in full for the surname gattinger — no occurrence; one adjacency recorded: the paper spends Aristotle (Paper 014) as a tool, in the open, and its author co-authored the interpolation proof it bounds)",
        "1.1.1/1.1.1/1.2.270": "Paper 022 (Bruce Sterling, 'Maneki Neko', Lightspeed Magazine reprint, 2011; (c) 1998) — the story itself, read entire 2026-11-14; the concept is the story's invented machinery, held as a construction",
        "1.1.1/1.1.1/1.2.271": "Paper 022 (Bruce Sterling, 'Maneki Neko', (c) 1998) — the story itself, read entire 2026-11-14; the concept is the story's invented machinery, held as a construction",
        "1.1.1/1.1.1/1.2.272": "Paper 022 (Bruce Sterling, 'Maneki Neko', (c) 1998) — the story itself, read entire 2026-11-14; the concept is the story's invented machinery, held as a construction",
        "1.1.1/1.1.1/1.2.273": "Paper 022 (Bruce Sterling, 'Maneki Neko', (c) 1998) — the story itself, read entire 2026-11-14; the concept is the story's invented machinery, held as a construction",
        "1.1.1/1.1.1/33.1.2": "Paper 022 (Bruce Sterling, 'Maneki Neko', (c) 1998) — the story itself, read entire 2026-11-14; the scroll's whole content is the story's invented machinery",
        "1.1.1/1.1.1/33.1.3": "Paper 022 (Bruce Sterling, 'Maneki Neko', (c) 1998) — the story itself, read entire 2026-11-14; the scroll's whole content is the story's invented machinery",
        "1.1.1/1.1.1/33.1.4": "Paper 022 (Bruce Sterling, 'Maneki Neko', (c) 1998) — the story itself, read entire 2026-11-14; the map rests on the story's own scenes, as the scroll states",
        "1.1.1/1.1.1/33.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-14 (the story read entire on its page at Lightspeed Magazine; signature scan for phext, phextura, Exocortex, Mirrorborn, Bickford, SBOR, CYOA — zero hits; the words scroll and coordinate do not occur; the story's date, (c) 1998, precedes the public life of phext by a quarter of a century; web searched for Bruce Sterling with phext, no tie; ~/workspace/twitter-archive searched in full for sterling — the hits are @SterlingCooley, another man, @alexsterling00, a stranger, and one liked post by another hand praising @bruces as a favorite late-night Twitterer; no post of Will's names him)",
        "1.1.1/1.1.1/27.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-13 (the full text read in full, references included; full-text signature scan for phext, Bickford, Mirrorborn, Exocortex, SBOR, CYOA — zero hits; scroll zero hits; coordinate only in its elliptic-curve sense; the reference list read whole — dated public prior art the paper names itself, no work of Will's in it; web searched for the paper and the nine authors with phext, no tie; ~/workspace/twitter-archive searched in full, 29,539 tweets, for all nine author names — none found; the single chaudhuri string hit is another man of that name)",
        "1.1.1/1.1.1/24.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-12 (the full text read in full; full-text signature scan for phext, scroll, exocortex, Mirrorborn, Bickford, phextura, zero hits; the word coordinate ten times, always in its ordinary sense; the reference list read whole, no work of Will's in it; the paper of March 2019, before the public life of phext; web searched for the authors with phext, no tie — the search returned the field's own record, including the public prize list naming the trio's Buchalter Cosmology Prize, third prize for 2019, for this work; ~/workspace/twitter-archive searched for beltran, koivisto, lavinia, heisenberg — no author found; the single heisenberg hit is a jest about a television device, addressed to another man)",
        "1.1.1/1.1.1/28.1.2": "Emise's checks of 2026-11-13: the essay read entire on its own page; the sentence the essay quotes from Paper 017 in its note 17 matched against the text of Paper 017 as the tracker holds it (~/workspace/p017-temp/paper.txt, lines 1666-1667) — the wording stands exact; the counts of the essay (almost forty gaps and matters of speed in Cerberus or its Lean port; some twelve hundred lines of C in the handshake; two milestones; four open questions) read against the essay's own text",
        "1.1.1/1.1.1/28.1.3": "the checks recorded in the scroll itself, run by Emise 2026-11-13 (whole-text machine search of the essay for phext, phextura, Bickford, Mirrorborn, Exocortex, SBOR, CYOA, scroll — no hit on any; the reference list read — the field's own line, no work of Will's; web searched for Math, Inc. with phext, no tie; ~/workspace/twitter-archive searched in full, 29,539 tweets, for math.inc, Memarian, Sewell, Lamport, Cerberus, WireGuard, Galois — no hit on any)",
        "1.1.1/1.1.1/35.1.2": "Emise's reading of 2026-11-15: the post read entire on its own page; the method drawn from the text of the post in its own terms — the distribution of interesting states, the value function, the tactics, the branching and rewind, the steering of the held entropy and the zero-turn twiddle, the rhythm of the campaigns from the human hand to the loop with the LLM inside it, and Player the workload; the counts of the filing read against the filing itself",
        "1.1.1/1.1.1/35.1.3": "the data table of the post read whole by Emise at the study, 2026-11-15: the four rows of roles sum to the All rows in both arms (100 + 85 + 95 + 99 = 379; 113 + 110 + 111 + 114 = 448); the rates (79.0 and 93.3 in the hundred), the intervals, the medians, the p90 and the fastest times as printed; the first ascension, the Baalzebub episode, and the bugs of the game and of the harness as the post tells them, its code cited by file and line",
        "1.1.1/1.1.1/35.1.4": "the checks recorded in the scroll itself, run by Emise 2026-11-15 (the post read entire on its own page and searched by machine for phext, phextura, Exocortex, Mirrorborn, Bickford, SBOR, CYOA — no hit on any; the word coordinate absent; the word scroll six times, every one in the sense of the game; ~/workspace/twitter-archive searched in full — 29,539 tweets and the file of likes, 47,973 — for antithesis, nethack, will wilson: no hit on antithesis or the name, nethack twice and both times on the game as a measure of machines; web searched for Antithesis with phext, no tie; the calendar read — the line of the company public from 2024, the game older than the house)",
        "1.1.1/1.1.1/35.1.5": "Emise's checks of 2026-11-15: the post read entire on its own page; its headline figures read against its own data table and found exact (the four rows of roles summing to the All rows in both arms, 379 and 448); the counts of the filing read off the built phext (seven concepts, no words coined, no foundations, seven scrolls of a chapter, 14 scrolls in all); the novelty lines read against the delta they stand in",
        "1.1.1/1.1.1/36.1.2": "Emise's reading of 2026-11-15: the About page and the search page of the repository read entire; the two labels taken in the own words of the search page; the screen's three automatic checks, the human moderator over them, the obvious-defect clause and the limits of the gate as the About page states them; the facets of the search read off the page itself",
        "1.1.1/1.1.1/36.1.3": "Emise's counts of 2026-11-15, from the pages as read: the page of all works states 1,061 works; the lists by month counted as read (September 37, the identifiers to 2609.00152; October 128, to 2610.00249; November at least 223 read before the reading of the page ended, the identifiers seen to 2611.00496); the newest ten counted exactly — provenance 1 human, 3 mix, 6 AI; understanding 2 all, 6 some, 2 none; number theory four of the ten; the two deposits read on their own pages (2611.00496v1: ten pages, DOI 10.5281/zenodo.24247902, the abstract's own statement of its limit, the numerical checks on the first five known zeros; 2611.00492v1: 81 pages, the sixteen certified inputs named, the non-implication of the mass gap and the reduction to the single rate (MG), as the work itself states them)",
        "1.1.1/1.1.1/36.1.4": "the checks recorded in the scroll itself, run by Emise 2026-11-15 (the pages of the site read entire and searched for phext, Bickford, Mirrorborn, Exocortex, Sentient Bill, CYOA, SBOR — no hit on any; web searched for Benjamin Antieau with phext, no tie — the return is his own record; ~/workspace/twitter-archive searched in full — 29,539 tweets and 47,973 likes — for antieau, no hit, and for hexagon, three hits, every one the shape and every one before the repository: two liked posts, and one tweet of Will's own, 2024-10-13; the calendar read — the foundation public and dated from August 2026, its name from Borges by the announcement's own telling)",
        "1.1.1/1.1.1/36.1.5": "Emise's checks of 2026-11-15: the site read as the source record states; the counts of the worked core counted from the pages as read and stated as floors where the reading ended; the two deposits read on their own pages; the author check run as recorded at 36.1.4; the counts of the filing read off the built phext (three concepts, no words coined, no foundations, seven scrolls of a chapter, ten scrolls in all)",
        "1.1.1/1.1.1/1.2.292": "~/workspace/fringe-001/enumerate_cardchoose.py and enumeration_output.txt (Emise's exact enumeration in rational arithmetic, run 2026-11-15: the count process over every n to 10, every multiset at exactly 1 / C(t+k-1, k)); the proof read at 37.1.2",
        "1.1.1/1.1.1/1.2.293": "~/workspace/fringe-001/enumerate_cardchoose.py and enumeration_output.txt (run 2026-11-15: two independent models, every subset at exactly 1 / C(n, k) in every case); the proof read at 37.1.2",
        "1.1.1/1.1.1/1.2.294": "the paper's worked example recomputed in this filing ({1, 2, 5} <-> [1, 1, 3] at n = 7, k = 3), and the conversion as implemented in ~/workspace/fringe-001/enumerate_cardchoose.py across all 66 + 36 enumerated cases",
        "1.1.1/1.1.1/37.1.2": "the read recorded in the scroll itself, made by Emise 2026-11-15 against the staged text of the paper (~/workspace/fringe-001/cardchoose.txt): every step of both proofs named and checked; the loop's indexing read against Section 2.3's numbering of the balls",
        "1.1.1/1.1.1/37.1.3": "~/workspace/fringe-001/enumerate_cardchoose.py and enumeration_output.txt (run 2026-11-15, exit clean: Model A 66 cases, Model B 36 cases, cross-model disagreement zero, supports and sums checked)",
        "1.1.1/1.1.1/37.1.4": "the verification at 37.1.2 and 37.1.3, and the listing of the algorithm as printed in Section 2 of the paper, read for the time and memory standings",
        "1.1.1/1.1.1/37.1.5": "the seal at ~/workspace/thirst-quest/fringe-seals.jsonl (commit 610a5b3, committed before the full read); the determination at 37.1.2 and 37.1.3; the counts read off the built phext (845 scrolls; thirteen new); the ledger at 1.1.4 for the standing of the gate",
        "1.1.1/1.1.1/37.1.6": "the checks recorded in the scroll itself, run by Emise 2026-11-15 (full-text machine search of the paper for phext, phextura, Bickford, Mirrorborn, Exocortex, SBOR, CYOA, scroll, coordinate — no hit in the house sense; the reference list read in full; web searched for the author and for his name with phext, no tie; ~/workspace/twitter-archive/tweets.json searched in full — 29,539 tweet texts — for crowley and ciphergoth, no hit)",

        "1.1.1/1.1.1/38.1.2": "the read recorded in the scroll itself, made by Emise 2026-11-15 against the staged text of the talk (~/workspace/s014-temp/texts/source-talk.txt): CashDB's operations and constraint as printed, the three families' verdicts in the talk's own words, the wishlist drawn at its slide 26",
        "1.1.1/1.1.1/38.1.3": "the read recorded in the scroll itself, made by Emise 2026-11-15 against the staged text of the talk: the census enumerated at its opening slides, the exhibits' numbers as printed (QuePaxa at slides 29-34; RIOT at slides 37-39; Accord at slides 43-44), the last bag at slides 49-63",
        "1.1.1/1.1.1/38.1.4": "the checks recorded in the scroll itself, run by Emise 2026-11-15 (full-text machine search of the staged talk for phext, phextura, Bickford, Mirrorborn, Exocortex, SBOR, CYOA, Sentient Bill — no hit on any, and the words scroll and coordinate absent; web searched for the author with phext, no tie; ~/workspace/twitter-archive searched in full — 29,539 tweets and 47,973 likes — for alexmillerdb, the author's name and transactional.blog, no hit on any)",
        "1.1.1/1.1.1/38.1.5": "the counts read off the built phext (860 scrolls; fifteen new); Restructure Pass #15 at 1.1.5; the ledger at 1.1.4 for the standing of the Oracle; the novelty line read against the researcher's entry at 1.5.6",
        "1.1.1/1.1.1/34.1.2": "Emise's reading and recovery of 2026-11-14: the book read entire in the text recovered on aletheia-core (the item's PDF read again from its page images with the English pack after its own text layer proved corrupt — read with the Sanskrit pack over an English book); samples at three points checked against the page images and found true English prose; leaf 18 pinned from its image as page 5 of Watson's introduction; the counts of the filing read against the filing itself; Restructure Pass #14 logged at 1.1.5",
        "1.1.1/1.1.1/34.1.3": "the checks recorded in the scroll itself, run by Emise 2026-11-14 (~/workspace/twitter-archive searched in full — 29,539 tweets and the file of likes — for vimalakirti, kumarajiva, burton watson: no hit on any; the name Watson stands only for IBM's machine and in a jest; the recovered text of the book searched for phext, exocortex, coordinate, lattice, Bickford: no hit on any, the word scroll once in the sense of copies of the sutra; web searched for Burton Watson with phext, no tie; the dates read: Kumarajiva 344-413, the translation of 406, the English translation first published 1997)",
    }[coord]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser(
        "~/workspace/research-tracker/research.phext")
    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    assert sha == EXPECTED_SHA, f"phext sha mismatch: {sha} != {EXPECTED_SHA}"

    scrolls = parse(path)
    entries = []
    for i, (coord, text) in enumerate(scrolls, 1):
        status, basis, evidence = classify(coord, text)
        assert STATUS_OF_BASIS[basis] == status, (coord, status, basis)
        entries.append({
            "id": i,
            "coordinate": coord,
            "claim": claim_of(coord, text),
            "status": status,
            "basis": basis,
            "evidence": evidence,
        })

    # Totality: one entry per scroll, ids exactly 1..N, coordinates unique.
    assert len(entries) == len(scrolls)
    assert [e["id"] for e in entries] == list(range(1, len(scrolls) + 1))
    assert len({e["coordinate"] for e in entries}) == len(entries)

    with open(os.path.join(HERE, "registry.json"), "w") as f:
        json.dump({
            "phext": "research.phext",
            "phext_sha256": sha,
            "extracted": "2026-11-12",
            "entries": entries,
        }, f, indent=1, ensure_ascii=False)

    lines = [
        "-- Generated by extract_registry.py -- do not edit by hand.",
        f"-- Source: research.phext, sha256 {sha}",
        f"-- Entries: {len(entries)} (one per scroll; ids 1..{len(entries)})",
        "",
        "def currentRegistry : List Entry := [",
    ]
    for e in entries:
        lines.append(
            f"  {{ id := {e['id']}, status := Status.{e['status'].lower()}, "
            f"basis := Basis.{e['basis']} }},")
    lines.append("]")
    with open(os.path.join(HERE, "RegistryData.lean"), "w") as f:
        f.write("\n".join(lines) + "\n")

    from collections import Counter
    by_status = Counter(e["status"] for e in entries)
    by_basis = Counter(e["basis"] for e in entries)
    print(f"scrolls: {len(scrolls)}")
    print(f"entries: {len(entries)}")
    assert len(scrolls) == len(entries), "TOTALITY FAILURE"
    print("totality: OK (scrolls == entries)")
    print("by status:", dict(by_status))
    print("by basis:", dict(by_basis))


if __name__ == "__main__":
    main()
