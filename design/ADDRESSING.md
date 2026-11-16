# Paper Addressing for tluf.org — a profile of phextura Layer 2

*Written 2026-11-15. Task: tasks.phext 42.9.6/12.6.15/5.8.10, on Will's direction of the same day: "add a feature to tluf.org that allows users to submit new paper resources — create a paper addressing scheme to unify them all." This document is the addressing design of record for tluf.org submissions and for every Assay build stage that mints an address (see the addendum in `REQUIREMENTS.md` and the note in `BUILD-PLAN.md`).*

## 1. This is a profile, not a new scheme

The unified paper address is phextura's **Layer 2** address (the `px2:` scheme specified in `~/workspace/phextura-design/LAYER2.md`, v0.1 draft, 2026-11-11), profiled for one job: naming a submitted or filed paper, whatever repository or web page it lives at. Everything LAYER2.md states and this document does not restate stands as written — the model (a work, an edition, a copy are three different things), the object table, the resolution algorithm and its failure vocabulary, the rule that there is no registry in the resolution path. This profile does exactly three things:

1. It extends the work-reference registry with the sources the house actually files from (§3).
2. It fixes canonicalization: how a locator a submitter pastes — a URL, a bare ID, a prefixed ID — becomes the one canonical address for that work (§4–§6).
3. It states what a submission mints, and what it never mints (§4.3).

Where this profile's needs exceed LAYER2 as designed, the excess is recorded in §9 as a stated gap. The grammar is not silently forked anywhere in this document.

## 2. The grammar, as adopted

Adopted unchanged from LAYER2.md §3, including its normative parse order:

```ebnf
address     = scheme work-ref [ pin ] [ "#" object-ref ] ;
scheme      = "px2:" ;
work-ref    = typed-id | declared-name | checksum-form ;
typed-id    = ("arxiv" | "doi") ":" id-text ;        (* id-text runs to pin, "#", or end;
                                                        a DOI's "/" is safe — see parse order *)
declared-name = "corpus" ":" slug ;
checksum-form = "sum" ":" "xxh3-128" ":" 32HEXDIG ;
pin         = "@" "e" ":" 16*HEXDIG ;                (* prefix of the edition checksum *)
object-ref  = kind ":" key ;
kind        = "theorem" | "lemma" | "proposition" | "corollary"
            | "definition" | "assumption" | "remark" | "proof"
            | "equation" | "equationgroup" | "figure" | "table"
            | "algorithm" | "section" | "bibentry" | "claim"
            | "paper" | "author" | "concept" | ext-kind ;
key         = slug ;
slug        = ALPHA *( ALPHA | DIGIT | "-" ) ;       (* lowercase ASCII *)
```

Parse order (LAYER2.md §3, normative): (1) require and strip the `px2:` prefix; (2) split at the **first** `#` — the tail, if present, is the object-ref; (3) in the head, if it begins `sum:` it is a checksum form and is complete; otherwise split the pin at the **last** `@e:`; the remainder is the work-ref. An address with no `#` denotes the work itself.

**The profile's single grammar extension** is inside `typed-id`: the token registry is extended from LAYER2's two tokens to the six of §3 —

```ebnf
typed-id    = ("arxiv" | "doi" | "hexagon" | "vixra" | "url" | "tluf") ":" id-text ;
```

`corpus:` declared names and the `sum:` checksum form are carried over unchanged. No other production is altered, added, or removed.

## 3. The work-reference registry

| Token | System | id-text form | Notes |
|---|---|---|---|
| `arxiv:` | arXiv | modern `YYMM.NNNNN`, or old-style `archive/NNNNNNN` (e.g. `math.AG/0309136`) | §4.4 |
| `doi:` | DOI / Crossref | `10.<registrant>/<suffix>`, lowercased | §4.5 |
| `hexagon:` | Hexagon (hexagonmath.org) | `YYMM.NNNNN` as deposited (e.g. `2611.00496`) | §4.6 |
| `vixra:` | viXra | `YYMM.NNNN` as deposited | §4.6 |
| `url:` | the bare web | the canonicalized URL, scheme included | §6 |
| `tluf:` | tluf.org itself | 16 lowercase hex digits, house-minted | §5 |
| `corpus:` | a phextura file's declared name | slug, as in LAYER2 | unchanged |
| `sum:` | no system — the content | `xxh3-128:<32 hex>` of an edition, as in LAYER2 | unchanged; also §6.3 |

A work has **one** canonical address. When several forms could name it (a paper with both a DOI and an arXiv ID), the address of record is the one for the source the house filed it from; the other forms are recorded in the filing as the same work's alternate locators, not as second addresses. Precedence when a *locator* is ambiguous between forms is a canonicalization matter (§4.2), not a second address.

## 4. Canonicalization

### 4.1 Locators

A **locator** is what a submitter pastes: a repository URL, a bare ID, a prefixed ID (`arXiv:…`, `doi:…`), a web URL, or an existing `px2:` address. Canonicalization is a pure function from locator to canonical address, or to a stated failure. It is implemented twice — in the submit page's JavaScript (so the submitter sees the address as they type) and in the receiving service (whose derivation is authoritative). Where an implementation and this section disagree, this section governs and the implementation is wrong.

General steps, in order:

1. Trim surrounding whitespace. An empty locator is `MALFORMED` (LAYER2's failure word, reused at intake).
2. A locator already beginning `px2:` is parsed per §2 and re-emitted in canonical form (its work-ref is canonicalized by the same per-scheme rules). A `px2:` locator that does not parse is `MALFORMED`.
3. Repository URLs and scheme prefixes are recognized and reduced to their scheme's ID (§4.4–§4.6, §6.1). A locator naming a repository the registry knows is never filed under `url:`.
4. Sentence punctuation clinging to a pasted locator — one trailing `.` or `,` — is stripped before scheme handling (for DOIs, see G-3 in §9).

### 4.2 Bare IDs: the ambiguity rule

A bare modern numeric ID (`YYMM.NNNNN`) fits the arXiv, Hexagon, and viXra grammars at once, and no digit pattern separates them. **The profile does not guess.** A bare numeric ID with no source context fails canonicalization as `AMBIGUOUS-SOURCE` (the intake analogue of LAYER2's `AMBIGUOUS-NAME`), and the submitter is asked to name the source — by pasting the repository URL or prefixing the ID (`arxiv:…`, `hexagon:…`, `vixra:…`). Two bare forms *do* have unique grammars and are accepted: a bare DOI (it begins `10.`) and a bare old-style arXiv ID (letters, a `/`, seven digits).

### 4.3 Version handling — what a submission mints

This is the rule the whole registry turns on, so it is stated once, for all repository schemes:

- A repository **version suffix** (arXiv `v2`, Hexagon `v1`, viXra `v3`) is information about the repository's copy. It is **not** an L2 edition pin: the pin is the prefix of a *phextura file's* manifest checksum (LAYER2 §1.3), and a submitted preprint is not yet a phextura file — there is nothing to pin to.
- The canonical work address therefore **drops the version suffix**. `2611.14552` and `2611.14552v1` are the same work and collapse to the one address `px2:arxiv:2611.14552`. The verbatim locator, version included, is preserved in the submission record, so nothing the submitter said is lost — it lives in the record, not in the address.
- A submission mints the **bare work address**: no pin, no object selector. Pins are minted later, by citers, against phextura editions the house's work produces; object selectors (`#kind:key`) name objects inside an L2-enabled phextura file, and a submitted preprint has no object table until such a file exists. A bare address and a pinned address name different things — the work, versus one exact edition of one file about the work — and intake only ever creates the first.

### 4.4 `arxiv:`

Recognized locators: an `arxiv:` prefix in any case; a URL on `arxiv.org`, `www.arxiv.org`, or `export.arxiv.org` under `/abs/` or `/pdf/`; a bare old-style ID. Reduction: strip the prefix or the scheme/host/path scaffolding, a trailing `.pdf`, the version suffix (§4.3), and clinging punctuation (§4.1 step 4). Modern IDs are digits and a dot, kept exactly. Old-style IDs keep their case — subject classes are case-bearing (`math.AG/0309136` is not `math.ag/0309136`).

### 4.5 `doi:`

Recognized locators: a `doi:` prefix in any case; a URL on `doi.org` or `dx.doi.org` whose path is the DOI (percent-decoded once); a bare `10.` form. Canonical form: the whole DOI **lowercased** (DOIs are case-insensitive; lowercase is the canonical spelling), resolver scaffolding removed. One trailing `.` or `,` is stripped per §4.1 step 4 — see G-3 for the priced risk.

### 4.6 `hexagon:` and `vixra:`

Recognized locators: a `hexagon:` / `vixra:` prefix in any case; a URL on `hexagonmath.org` whose final path segment is the deposit ID; a URL on `vixra.org` under `/abs/<id>`. Reduction strips the scaffolding and the version suffix (§4.3). The ID is kept digit-for-digit as deposited. (Neither repository publishes an ID grammar this profile can cite — the recognizers are fitted to the observed forms; see G-5.)

## 5. `tluf:` — works whose home is tluf itself

A `tluf:` address names a work deposited natively at tluf.org — born here, with no external repository to borrow durability from (the case REQUIREMENTS.md's Stage 1 calls the native intake form). The minting rule:

- **Form:** `tluf:` followed by the first **16 lowercase hex digits of the xxh3-128 of the work's canonical bytes** — the same hash, at the same prefix length, that LAYER2 uses for edition pins (§3) and checksum forms (§1.3). For a phext or phextura deposit, the canonical bytes are LAYER2 §1.3's normalized corpus; for any other format, the exact deposited bytes (see G-6).
- **Minted by the house, at deposit, never derived from a pasted locator.** A submitter cannot compute one into the form; the submit page never displays a `tluf:` derivation. A pasted `tluf.org` URL is a `url:` locator unless the house's records already bind it to a native work.
- **Properties:** unguessable (a native ID leaks nothing about the intake's size or order — submissions are private by default, and an address must not enumerate them); content-bound (two deposits of identical bytes are the same work and mint the same address, which is what the duplicate discipline wants); counter-free (no central sequence every minting must consult).

The alternative, priced in one line: sequential minting (`tluf:000123`) is friendlier to say aloud and was rejected — it enumerates the intake, leaking the existence and count of private submissions, and it makes every mint consult a central counter.

## 6. `url:` — bare-web resources

A `url:` address names a work by where it lives on the web, for the many filed resources that have no repository ID — a magazine story, an author's PDF on their own site, a blog post. Its id-text is the canonicalized URL, **scheme included**: `px2:url:https://ciphergoth.org/sansreplace/cardchoose.pdf`.

### 6.1 Recognition

Any `http`/`https` locator not claimed by a repository rule in §4 is a `url:` locator. A locator with no scheme but a host-like shape (`ciphergoth.org/sansreplace/cardchoose.pdf`) is read as an `https` URL. A locator that is neither a recognized ID nor URL-shaped is `MALFORMED`.

### 6.2 Canonicalization steps

Applied in order to the parsed URL:

1. Scheme and host lowercased. Userinfo stripped (credentials never belong in an address). A leading `www.` label stripped from the host. A default port (80 for http, 443 for https) stripped; any other port kept.
2. Percent-encodings of unreserved characters (`A–Z a–z 0–9 - . _ ~`) decoded to the literal character; all remaining percent-encodings kept, with uppercase hex digits.
3. Dot-segments (`.` / `..`) removed from the path, per RFC 3986 §5.2.4. Path case is preserved — paths are case-sensitive.
4. The fragment is dropped, always: a fragment names a place inside a resource, never a different work.
5. Query: tracking parameters are dropped — `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`, `fbclid`, `gclid`, `mc_cid`, `mc_eid`. Remaining parameters are kept (they may identify the resource) and sorted by name, then value. An emptied query drops its `?`.
6. One trailing `/` is stripped from a non-root path; a root path (`/`) is dropped entirely.
7. If the result contains the literal substring `@e:` (which the §2 parse order would read as an edition pin), its `@` is percent-encoded to `%40`. This is the only point where the profile alters a URL's own characters for the grammar's sake — see G-1.

What is **not** collapsed: `http` versus `https` on the same host are two addresses until the house's records join them (see G-4). The address names the locator as canonicalized; sameness of the underlying work across schemes is decided by content, at intake, not by syntax.

### 6.3 When `sum:` must disambiguate

A `url:` address names a location, and locations change what they serve. The rule:

- A `url:` submission mints `px2:url:<canonical URL>`, and the house's intake records the content hash of what the URL served (the S-6 duplicate machinery in REQUIREMENTS.md already computes it).
- If the house's records ever hold **two distinct content hashes for one canonical URL**, the address alone no longer distinguishes the works. The first work keeps the `url:` address; each later, distinct work at that URL is minted as a checksum-form address, `px2:sum:xxh3-128:<the work's content hash>`, and the collision is recorded in both filings. Citations to the displaced work use its `sum:` form, which is exactly as durable as the content it names (LAYER2 §1.3).
- The same rule covers a `url:` that turns out to serve a work the house already holds under a repository scheme: the filing links them, the repository address is the address of record (§3), and the `url:` form remains as the submitted locator in the record.

## 7. Worked examples

From the house's real corpus. Each row: the locator as submitted (or as it would be pasted), then the canonical address a submission mints.

| # | Submitted locator | Canonical address | Note |
|---|---|---|---|
| 1 | `https://arxiv.org/abs/2611.14552v1` | `px2:arxiv:2611.14552` | Paper 020 (Zayton). The `v1` drops per §4.3; the verbatim locator stands in the record. `arXiv:2611.14552` and bare-prefixed forms collapse to the same address. |
| 2 | `https://www.lightspeedmagazine.com/fiction/maneki-neko/` | `px2:url:https://lightspeedmagazine.com/fiction/maneki-neko` | Paper 022 (Sterling, "Maneki Neko"), posted as this bare link. `www.` and the trailing slash drop per §6.2. No repository ID exists for it — `url:` is its scheme. |
| 3 | `hexagon:2611.00496v1` | `px2:hexagon:2611.00496` | S013's shortlist #1, the Riemann Hypothesis equivalence deposit. Version drops per §4.3. |
| 4 | `https://www.ciphergoth.org/sansreplace/cardchoose.pdf` | `px2:url:https://ciphergoth.org/sansreplace/cardchoose.pdf` | Fringe F001 (Crowley, "Cardchoose"). An author's own site: no repository ID, so `url:` — and §6.3's hash rule is what protects this address if the PDF is ever replaced in place. |
| 5 | `https://vixra.org/abs/2509.0147` | `px2:vixra:2509.0147` | A form example (no such filing is claimed): any viXra deposit URL reduces this way. |
| 6 | `https://doi.org/10.1214/09-SS054` | `px2:doi:10.1214/09-ss054` | The demo corpus's bibliography entry for Arlot–Celisse 2010 (LAYER2 §7). Lowercasing is the canonicalization, per §4.5. |

## 8. What the address is not

A `px2:` address names **the work** — the paper, story, or deposit as a continuing thing in the world. It does not name the house's filing of it. The tracker's chapters, its concept coordinates, and every L1 scroll position inside research.phext are addresses of the *filing*, internal to that file, and they keep their own scheme untouched: Paper 020 is Chapter 31 of the tracker *and* `px2:arxiv:2611.14552`, and neither address can be derived from or substituted for the other. Two filings of one work — the same paper taken in by the tracker and later assessed by Assay — share the one work address, and each filing points at it; that sharing is the unification Will asked for. And per LAYER2 §1.2 and §9.3, the address denotes and nothing more: a resolved address certifies that a held copy is the work named, and asserts nothing about the work's truth, its authorship, or its merit. Those are the assessment's claims to make, in the assessment's own file, citing this address.

## 9. Gaps — where LAYER2 as designed does not cover a need

Recorded, not papered over. Each gap is LAYER2's to close or refuse; this profile works around none of them silently — the workaround, where one exists, is stated with the gap.

- **G-1 — No quoting rule for work-ref id-text.** A URL can contain `#`, `@e:`, `?`, `&` as data. LAYER2's parse order survives URLs only because §6.2 canonicalizes the dangerous characters away (fragment dropped, `@e:` percent-encoded). A URL that *needs* its fragment, or carries `@e:` followed by 16 hex digits as content, is unrepresentable. L2 needs an escaping or length-delimiting rule for id-text.
- **G-2 — Repository versions have no home.** LAYER2's only edition notion is the phextura manifest checksum. arXiv v1 versus v2 is real edition information; §4.3 drops it from the address into the submission record because the grammar has nowhere else to put it. A repository-version component is L2's to add or refuse.
- **G-3 — DOI trailing punctuation is not syntactically decidable.** A DOI suffix may legitimately end in `.`, and a pasted DOI may carry a sentence's period. No purely syntactic rule separates them; §4.5's strip-one rule can mangle a genuine DOI. Only a fetch (discovery, LAYER2 §4.4) can tell — syntax alone cannot.
- **G-4 — No same-work assertion between work-references.** An `http`/`https` pair, or a `url:` and an `arxiv:` naming one work, are two addresses until the house's content-hash duplicate detection links the filings. The scheme cannot itself say "same work"; catalogs (LAYER2 §4.4) can carry the assertion as data, but the address cannot.
- **G-5 — Scheme recognizers rest on unpublished ID grammars.** Neither Hexagon nor viXra publishes an ID grammar this profile can cite; §4.6's recognizers are fitted to observed deposits. An out-of-shape ID falls through to `url:` — a safe landing, but a silent one unless intake logs the fall.
- **G-6 — `tluf:` minting needs canonical bytes for non-phext formats, which L2 does not define.** LAYER2 §1.3's checksum is defined over a normalized phext corpus. For a PDF deposit, §5 hashes the exact bytes — so two PDFs differing only in metadata mint two addresses for arguably one work. The profile accepts this (the bytes are the deposit) rather than inventing a PDF canonicalization, and records it as a gap.

## 10. Authority

This document governs the submit page's live derivation and the receiving service's derivation alike. The implementations are tested against §7's worked examples; where an implementation and this document disagree, the implementation is fixed, not the document — unless Will rules otherwise, in which case the ruling is recorded here as a dated amendment, as with the requirements it serves.

*End of specification.*
