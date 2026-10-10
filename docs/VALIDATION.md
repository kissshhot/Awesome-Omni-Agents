# Validation

Completed for the initial local catalog on **2026-10-10**, with the same research cutoff.

## Inventory and Structural Results

| Check | Result |
| --- | --- |
| Inventory | PASS: 36 unique works across 6 categories; 19 method/framework papers, 11 benchmark papers, 5 technical reports, 1 official system release. |
| Languages | PASS: 35 parallel English/Chinese paper/report summaries; system-only description and repository guidance in English. Numeric parity also checked. |
| Source metadata | PASS: all 35 arXiv records match the retrieved canonical title, complete ordered author metadata, first date, reviewed version/date, and HTML digest. |
| Verification depth | 29 M entries with named method/evaluation passages, 6 A entries restricted to abstracts/metadata, and 1 S official-source entry. |
| Dates | PASS: first dates and reviewed revisions are on or before the cutoff; revisions do not precede first submissions. First submissions span 2023-03-08 through 2026-09-25, with 11 entries first submitted in 2026. |
| Duplicate handling | PASS: unique identifiers, normalized titles and labels; companion agents/benchmarks are not double counted; both OmniAgent works remain distinct. |
| Generated documents | PASS: README and SOURCE_AUDIT match data/catalog.json exactly. |
| Markdown | PASS: four Markdown files; consistent table widths, six-column entry rows, relative file links, and all local anchors. |
| Git whitespace | PASS: staged diff checked with git diff --cached --check before committing. |
| Repository isolation | Independent Git repository on main. The initial local validation used no remote; publication was subsequently authorized. The reference repository was read only. |

The commands below completed successfully:

```sh
python3 scripts/render_catalog.py --check
python3 scripts/validate_catalog.py
git diff --cached --check
```

## External Links

All **100 unique external URLs** in the Markdown were checked. The automated GET run returned **95 reachable**, **4 connection failures**, and **1 HTTP 403** after up to two attempts per URL. The four arXiv pages and the official release were also successfully read through the web retrieval tool. Thus every linked page had a readable-source access path during this review, but the automated checker is intentionally **not reported as 100/100 HTTP success**.

The original machine-readable responses and redirects remain in [LINK_CHECK.json](LINK_CHECK.json). The follow-up access results are separately recorded in [WEB_CHECK.json](WEB_CHECK.json); web-reader success does not invent an HTTP status or erase an automated failure.

| URL | Automated result | Follow-up |
| --- | --- | --- |
| [Agent-Omni v2 method](https://arxiv.org/html/2511.02834v2) | Connection closed without a response | Primary content readable through the web reader. |
| [Full-Duplex-Bench-v3 v1 method](https://arxiv.org/html/2604.04847v1) | Connection closed without a response | Primary content readable through the web reader. |
| [Qwen3.8-Omni v1 method](https://arxiv.org/html/2609.25611v1) | Connection closed without a response | Primary content readable through the web reader. |
| [Omni-IO Skills v1 method](https://arxiv.org/html/2609.31847v1) | Connection closed without a response | Primary content readable through the web reader. |
| [gpt-realtime official release](https://openai.com/index/introducing-gpt-realtime/) | HTTP 403 for the script | Dated release and tool/image sections readable through the web reader. |

These are access limitations, not confirmed broken links. No replacement URLs were guessed. This check covers catalog links, not all links inside the cited papers, linked assets, downloadable weights, or repository dependencies. Redirect targets and check timestamps are in the automated report. External fragments are not remotely tested; the catalog uses versioned document URLs and names the inspected sections in the audit.

## Manual Review and Limits

Paper identity, source-provided authors, first-submission dates, reviewed revisions, and abstract-level contributions were checked from original records. Author rosters are transcribed from source metadata; individual identities and affiliations were not independently disambiguated. Selected method and evaluation passages were read for the M entries listed in [SOURCE_AUDIT.md](SOURCE_AUDIT.md). The source-page byte hashes match the research copies used for inspection. The research copies are outside the Git repository; full copyrighted papers are not redistributed.

English and Chinese summaries were read side by side for matching mechanisms, modality/action boundaries, and limitations. Two potentially misleading translations were corrected: Agent S is a computer-use agent system, not an operating system; VisualWebArena tasks depend on visual information and are not merely element-localization tasks. Markdown rows were inspected as source and validated structurally; no claim of cross-client visual rendering tests is made.

The catalog does not claim complete literature coverage, peer-review verification, experimental reproduction, code/weight/data auditing, runtime testing, commercial API availability, or validation of every claim in each source. Supporting models and interaction components are explicitly labeled. No numeric leaderboard comparisons are included. There are no unresolved content or repository blockers; reproducible scripted HTTP access remains limited for the five URLs above.

## Publication Preparation

The tracked files and reachable Git history were checked for credentials, private keys, local filesystem paths, internal hostnames, and non-public contact details. No such content is intended for publication. The unpublished root commit was re-authored using the verified GitHub account's public noreply address so that the local workstation's default work email is not published. This repository contains research summaries and verification records only; research cache files are outside its Git history.

## Reproduce the Checks

```sh
python3 scripts/render_catalog.py --check
python3 scripts/validate_catalog.py
python3 scripts/check_links.py --output docs/LINK_CHECK.json
git diff --check
```

The remote checker exits nonzero when any URL is unresolved. Its report is a point-in-time access record, and re-running it overwrites only the requested report file. Preserve relevant follow-up evidence and update this report when the inventory or observed access results change.
