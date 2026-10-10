#!/usr/bin/env python3
"""Render the catalog and evidence tables from the reviewed local inventory."""
import argparse
import json
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def cell(value):
    return value.replace('|', r'\|').replace('\n', ' ')

def anchor(entry):
    return ('paper-' + entry['id'].replace('.', '-')) if entry['kind'] != 'System' else 'system-' + entry['id']

def authors(entry):
    names = entry['authors']
    def natural(name):
        parts = name.split(', ', 1)
        return ' '.join(parts[::-1]) if len(parts) == 2 else name
    return '; '.join(natural(n) for n in names[:3]) + (f'; et al. ({len(names)} credited authors/entities)' if len(names) > 3 else '')

def render(data):
    entries = data['entries']
    counts = Counter(e['kind'] for e in entries)
    reviewed = Counter(e['checked'] for e in entries)
    readme = f'''# Awesome Omni Agents

A curated research catalog on **multimodal agents that perceive, reason, act, and interact** across text, images, audio, and video. It connects early tool orchestration to active audio-video perception, computer use, real-time interaction, and evaluation.

**{len(entries)} entries** · **Cutoff and source review: {data['cutoff']}** · **English and Chinese paper summaries**

{counts['Paper']} method/framework papers · {counts['Benchmark']} benchmark papers · {counts['Technical report']} technical reports · {counts['System']} official system release. These are primary contribution types, not peer-review certifications.

[Table of contents](#table-of-contents) · [Scope and terminology](#scope-and-terminology) · [Source audit](docs/SOURCE_AUDIT.md) · [Contributing](CONTRIBUTING.md) · [Validation](docs/VALIDATION.md)

## Scope and Terminology

For this catalog, an **agent** selects and executes actions conditioned on its goal and observations. Actions may invoke tools/models, retrieve additional evidence, or change a GUI environment. A **perception agent** actively chooses what to inspect; that narrower action space is distinct from sending messages, editing files, or controlling a desktop. A generated plan without execution is insufficient evidence of an action-capable agent.

**Omni** is an operational research scope, not a standardized certification. The core interest is joint visual, auditory, video, and textual information in a perception-reasoning-action loop. Selected image-text and speech-text work is retained when it establishes a useful action or interaction mechanism. Inclusion does not mean that every entry supports every modality, every output type, or unrestricted general intelligence.

**Interaction components** choose when/how to speak or perceive while responding; they are not automatically tool-using agents. **Supporting models** supply directly relevant multimodal capabilities, but are not counted as demonstrated agents. A model plus a harness may provide capabilities that the base model alone does not. Foundation models are deliberately limited to a small enabling set, rather than a general MLLM collection.

The scope excludes text-only agent catalogs, standalone image/audio/video generation with no relevant agent or interaction mechanism, generic perception leaderboards, and comprehensive robotics/navigation/VLA coverage. Specialized embodied control deserves a separate catalog. Commercial products with “Omni” in the name are not included merely by name. Papers first submitted or revisions released after the cutoff are excluded. This is a selective reading list, not an exhaustive systematic review or a current leaderboard.

## Reading the Entries

- **Entry and role** distinguishes papers, benchmarks, technical reports, and an official system release, then states the operational role. Modalities describe the relevant interface discussed here: **T** text, **I** images (including screenshots), **A** audio/speech, **V** video. They are not an input/output support matrix or a claim that every task uses them all.
- **First submitted / released** is the first arXiv submission date for papers/reports, or the dated official announcement for the system. It is not inferred from an arXiv ID, a conference date, or a product launch date.
- **A** means the primary abstract, title, author roster, and submission history were read. **M** adds selected method/evaluation passages named in the audit. **S** means named sections of an official system source were read. Downloading full text alone does not earn M; no mark means full-paper verification, code audit, or experimental reproduction.
- English and Chinese descriptions are parallel for all papers, benchmarks, and technical reports. The system-only description and all repository guidance are in English. The em dash in that system's Chinese cell is intentional.
- Each primary work appears once. Companion models/benchmarks stay in the same row: e.g., OmniGAIA/OmniAtlas, OmniMMI/M4, and M3-Agent/M3-Bench. The two unrelated OmniAgent works are distinguished by authors.
- Entries are chronological within each category. Source links are canonical records; the audit pins reviewed versions, dates, authors, and evidence. Later revisions are not silently certified.

## Table of Contents

'''
    readme += '\n'.join(f"- [{c['title']}](#{c['id']})" for c in data['categories'])
    readme += '''
- [Reading routes](#reading-routes)
- [Contributing](#contributing)

## Category Overview

| Category | Entries | Central question |
| --- | --- | --- |
'''
    for c in data['categories']:
        readme += f"| [{c['title']}](#{c['id']}) | {sum(e['category']==c['id'] for e in entries)} | {c['description']} |\n"
    for c in data['categories']:
        readme += f"\n<a id=\"{c['id']}\"></a>\n\n## {c['title']}\n\n{c['description']}\n\n"
        readme += '| Entry and role | First submitted / released | English | 中文 | Source | Checked |\n| --- | --- | --- | --- | --- | --- |\n'
        for e in entries:
            if e['category'] != c['id']:
                continue
            label = f"**{e['label']}**<br>{e['kind']} · {e['role']}<br>{'/'.join(e['modalities'])}"
            source_label = f"arXiv {e['id']}" if e['kind'] != 'System' else 'Official release'
            readme += '| ' + ' | '.join(cell(x) for x in [label,e['first_date'],e['summary_en'],e['summary_zh'] or '—',f"[{source_label}]({e['source_url']})",f"[{e['checked']} · {e['version']}](docs/SOURCE_AUDIT.md#{anchor(e)})"]) + ' |\n'
    readme += '''
## Reading Routes

| Goal | Suggested sequence | What to distinguish |
| --- | --- | --- |
| Understand executable multimodal reasoning | MM-REACT → HuggingGPT → Agent-Omni → Omni-IO Skills | Calling specialist models versus training a native omni model; planning versus executing. |
| Study active audio-video agents | VideoAgent → M3-Agent → OmniAgent (Tao et al.) → OmniRAG-Agent → OmniAgent (Xing et al.) → Light-Omni | Evidence retrieval, persistent memory, native perception, and learned action policies. |
| Build an audio-video assistant with tools | Qwen2.5-Omni / Qwen3-Omni → OmniGAIA / OmniAtlas → Qwen3.8-Omni | Base-model interfaces versus tool-enabled training and runtime orchestration. |
| Connect visual perception to computer actions | SeeAct → Agent S / UI-TARS → Agent S2 → VisualWebArena / OSWorld / AndroidWorld | Grounding accuracy, autonomous execution, and final environment-state success. |
| Evaluate real-time interaction | Moshi / OmniFlatten → MiniCPM-o 4.5 → OmniMMI / Omni-DuplexEval / OmniAssistBench → Full-Duplex-Bench-v3 | Duplex speech, response timing, offline interaction simulation, and actual tool-call correctness. |
| Connect video understanding to downstream work | VideoWebArena → OmniGAIA → Qwen3.8-Omni | Answering about media versus completing tasks based on media. |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Prioritize scope clarity and primary-source evidence over counts. The editable inventory is [data/catalog.json](data/catalog.json); [render_catalog.py](scripts/render_catalog.py) generates this README and the audit.

```sh
python3 scripts/render_catalog.py --check
python3 scripts/validate_catalog.py
git diff --check
```

The layout and A/M evidence distinction are inspired by the local Awesome-OPD reference at commit `5d575fc`. This catalog has its own taxonomy and inventory. No remote repository, publication, or hosted service is required.
'''
    audit = f'''# Source Audit

Review and eligibility cutoff: **{data['cutoff']}**. Format reference: local Awesome-OPD commit **5d575fc** (read-only). No topic inventory or OPD classifications were copied.

## Review Method and Limits

The inventory contains **{len(entries)} primary works**: {counts['Paper']} method/framework papers, {counts['Benchmark']} benchmark papers, {counts['Technical report']} technical reports, and {counts['System']} official system release. Verification depth: **{reviewed['A']} A**, **{reviewed['M']} M**, **{reviewed['S']} S**.

Every paper/report record was retrieved directly from arXiv and inspected for title, author metadata, first submission, revision history, and abstract. For M rows, selected passages of the versioned arXiv HTML were additionally read to verify the mechanism, action space, or evaluation protocol; the exact inspected sections are named below. This is targeted source inspection, not a claim that every page, equation, experiment, or appendix was checked. Search results, author sites, and project repositories were discovery aids; search snippets were not treated as full-text verification. Abstract-only entries remain A even when a detailed summary is possible from the abstract.

Full ordered author rosters and retrieval SHA-256 digests are retained in [the inventory](../data/catalog.json). The digest identifies the HTML bytes retrieved during research, not a signature of scientific validity or a guarantee that an unversioned page will never change. Long author lists are abbreviated in this table. GPT-4o's author metadata contains a standalone colon separator, which was omitted from the normalized roster; the corporate credit was retained. Full copyrighted papers are not redistributed in the repository.

A means abstract/metadata/history only; M adds the named passages; S means the named official documentation sections. A canonical source and a version-specific record are both linked. All reviewed revision dates are on or before the cutoff. Publication type describes the main contribution: a benchmark paper can include a method, and a technical report can describe a system. No conference acceptance or peer-review status is inferred from an arXiv posting.

Experiments, code, model weights, benchmark datasets, annotations, human evaluations, judge reliability, deployment behavior, API availability, prices, security, and licenses were not independently tested or audited. No result numbers or current “best” claims are used in the summaries. External-link reachability is reported separately in [VALIDATION.md](VALIDATION.md); HTTP access is not scientific validation.

## Search and Selection

The search covered foundational multimodal tool composition, video evidence selection and memory, visual computer-use agents, full-duplex speech and audio-video interaction, agent environments, and directly enabling omni models. Searches combined exact paper titles with terms such as `omni agent multimodal audio video tool use`, `native active perception`, `voice tool benchmark`, and `multimodal agent October 2026`. Broad keyword searches sometimes returned unrelated products or generic sites; those were discarded. Citation and project trails were resolved back to primary records before inclusion. The search was bounded by the review date, but it does not prove that every work released before that date was found.

The selected first-submission dates range from 2023-03-08 to 2026-09-25. Older general agent ideas are background rather than a separate text-only inventory. Recent coverage includes active native perception, memory-efficient video agents, multimodal harnesses, and interaction benchmarks. The classification is specific to omni agents and remains independent of the reference catalog.

## Boundary Decisions and Corrections

| Issue | Decision |
| --- | --- |
| Two OmniAgent works | Use Tao et al. for 2512.23646 and Xing et al. for 2606.19341; do not merge by alias. Agent-Omni is a third, separate work. |
| OmniAgent title evolution | 2512.23646 v2 uses “Active Perception Agent for Omnimodal Audio-Video Understanding”; the earlier title includes an OmniAgent prefix and audio-guided wording. The current record title is preserved in the audit. |
| VisualWebArena title | The metadata title and v2 HTML heading differ slightly (“Visual” versus “Visually Grounded”). Retain the record title and explicitly note the body-heading variant. |
| Date semantics | Moshi was first submitted on 2024-09-17 despite its 2410 identifier. GPT-4o's 2024-10-25 date is its arXiv submission, not the original product/system-card release. Qwen3.8-Omni uses the report's 2026-09-22 submission rather than the earlier model announcement. |
| Model versus agent | GPT-4o, Qwen2.5-Omni, and Qwen3-Omni are supporting models. Moshi, OmniFlatten, and MiniCPM-o 4.5 are interaction components. They are not promoted to external-action agents based solely on multimodal or duplex outputs. |
| Narrow action spaces | VideoAgent, M3-Agent, both OmniAgents, OmniRAG-Agent, and Light-Omni gather/retain evidence. Agent-Omni coordinates model calls. These actions do not establish arbitrary computer control. |
| Evaluation distinctions | VisualWebArena, OSWorld, AndroidWorld, and VideoWebArena check execution outcomes. GAIA and OmniGAIA assess assistant answers with tool access. OmniMMI, Omni-DuplexEval, and OmniAssistBench diagnose interaction; LVOmniBench diagnoses perception. |
| Simulator boundaries | OmniAssistBench simulates interaction offline on predefined routes. Full-Duplex-Bench-v3 uses local mock APIs, so it does not measure real service latency. SeeAct's manually grounded setting must not be represented as autonomous execution. |
| One work, one row | OmniAtlas remains in OmniGAIA; M4 remains in OmniMMI; M3-Bench remains in M3-Agent. Different revisions do not create new entries. |
| Deliberate exclusions | General MLLM surveys, pure content-generation catalogs, text-only agents, and exhaustive robotics/VLA coverage are outside this inventory. An initially retrieved MM-LLMs survey (2401.13601) was discarded as a mismatched candidate, not mislabeled as VisualWebArena. |

## Per-Entry Evidence

All records were inspected on the review date above. Author names preserve source ordering; complete rosters are in the inventory.

| Source | Canonical title and credited authors | First submitted / released | Reviewed revision | Evidence |
| --- | --- | --- | --- | --- |
'''
    for e in entries:
        source = f'<a id="{anchor(e)}"></a>[{e["id"]}]({e["source_url"]})'
        title = f"{e['title']}<br>{authors(e)}"
        version = f"[{e['version']}]({e['reviewed_record_url']}) · {e['revision_date']}"
        evidence = f"{e['checked']} — "
        if e['method_url']:
            evidence += f"Abstract/history + [{e['method_sections']}]({e['method_url']}). "
        elif e['kind'] == 'System':
            evidence += f"Official source: {e['method_sections']}. "
        evidence += e['evidence_note']
        audit += '| ' + ' | '.join(cell(x) for x in [source,title,e['first_date'],version,evidence]) + ' |\n'
    return {'README.md':readme,'docs/SOURCE_AUDIT.md':audit}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    data=json.loads((ROOT/'data/catalog.json').read_text())
    stale=[]
    for name,text in render(data).items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text()!=text:stale.append(name)
        else:path.write_text(text,encoding='utf-8')
    if stale:
        print('FAIL: stale generated files: '+', '.join(stale));return 1
    print('PASS: generated files match inventory' if args.check else 'Rendered README.md and docs/SOURCE_AUDIT.md')
    return 0
if __name__=='__main__':raise SystemExit(main())
