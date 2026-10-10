# Contributing

Prefer a precise, well-sourced addition or correction over increasing the entry count. This repository is a research directory, not a leaderboard or a claim that all listed systems are fully autonomous.

## Scope and Classification

Apply the [scope criteria](README.md#scope-and-terminology). State what the system observes, what it decides, and which actions actually execute. Distinguish evidence retrieval, specialist-model calls, GUI actions, dialogue timing, and passive multimodal generation. Mark base models as Supporting model and speech/streaming components as Interaction component unless the reviewed source establishes a relevant action loop.

Use one primary category and one row per work. A paper containing both a benchmark and an agent keeps both in one row. Disambiguate shared aliases by authors, and deduplicate by canonical identifier rather than display name. Revisions of the same paper are not new entries. The six categories can be revised when the topic definition changes; explain any migration rather than preserving an unsuitable taxonomy mechanically.

Do not silently broaden this into an all-MLLM, all-agent, or robotics catalog. A narrower modality pair is acceptable when its action or interaction mechanism clearly explains its relevance. Describe the boundary in both languages.

## Sources and Verification

1. Open the original paper record or a dated official source. Verify canonical title, ordered author roster, first submission or release date, and reviewed version. Do not derive dates from identifiers or search-engine snippets.
2. Confirm the reviewed revision is on or before the declared cutoff. An updated current page is not automatically evidence of what a historical version said.
3. Use A for primary abstract, metadata, and submission-history inspection. Use M only after reading the relevant method or evaluation passages; name them and use a versioned source. Use S for an official system source with named sections. Do not describe downloading a paper as reviewing it.
4. Explain mechanism, contribution, and scope without unverified superlatives. For any result number, identify model, task/benchmark version, metric, setting, and exact table/section. Otherwise omit the number.
5. Distinguish mock APIs, offline interaction simulation, answer scoring, GUI grounding, and end-state success. A human-oracle setting must not become an autonomous result. A product announcement does not certify present availability or measured behavior.
6. Keep inaccessible or insufficiently verified candidates out of the counted inventory; record the blocker separately. A transient connection error or rate limit is not proof that a paper or URL is invalid.

## Editable Inventory and Entry Format

Edit [data/catalog.json](data/catalog.json), then run the renderer. README and the source audit are generated to prevent date, count, and translation drift. Keep all headings, metadata, navigation, guidance, and evidence notes in English. Provide matching English/Chinese summaries for Paper, Benchmark, and Technical report entries; System descriptions remain English with an empty `summary_zh` field.

Each entry contains a stable identifier, display label, category, primary type, operational role, relevant modalities, canonical title, full author roster, first date/date basis, reviewed version/date, source URL, verification depth, evidence notes, and parallel summaries. M entries additionally require a versioned method URL and exact inspected sections. Source byte digests are provenance of retrieval, not scientific endorsement; record a new digest only when a source was actually fetched.

The rendered table follows the reference catalog's six-column form:

```markdown
| Entry and role | First submitted / released | English | Chinese summary | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **Short label**<br>Paper · Tool agent<br>T/I/A/V | YYYY-MM-DD | Mechanism and boundary. | Matching Chinese translation. | Primary source | Status and reviewed version, linked to the audit |
```

Use concise, original paraphrases, usually two sentences. Do not copy full abstracts. Both languages must express the same mechanism, limitations, and any numbers. Escape literal table pipes as `\|`; the renderer handles this. Do not alter a canonical title simply to match a familiar alias. If the record and paper body disagree, document both explicitly.

## Local Checks

No package installation or application build is required; the scripts use Python 3's standard library.

```sh
python3 scripts/render_catalog.py
python3 scripts/render_catalog.py --check
python3 scripts/validate_catalog.py
git diff --check
```

Run remote checks separately when network access is available:

```sh
python3 scripts/check_links.py --output docs/LINK_CHECK.json
```

The offline validator checks unique identifiers and titles, category/type/role constraints, dates and cutoff, evidence URLs and versions, generated-file consistency, table shapes, summary-language presence, numeric parity, local file links, and anchors. It cannot prove scientific truth or semantic translation equivalence. Read the two summaries side by side, inspect changed primary sources, and review the Markdown tables. Document the scope and limitations of those manual checks in [VALIDATION.md](docs/VALIDATION.md).

The remote checker uses GET requests and records redirects, response status, errors, attempts, and check time. It does not audit code, weights, datasets, or all links inside the papers. Record any browser-only verification separately and preserve the automated result rather than turning an access failure into a fabricated HTTP success.

## Local Repository Workflow

Use an isolated local branch or commit as appropriate. Publishing repository content requires the repository owner's authorization. Do not publish unrelated files, force-push shared history, or deploy services as part of a catalog update. There is no assumed paper/code/data license granted by inclusion here; follow the linked source's own terms.
