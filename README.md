# Awesome Omni Agents

A curated research catalog on **multimodal agents that perceive, reason, act, and interact** across text, images, audio, and video. It connects early tool orchestration to active audio-video perception, computer use, real-time interaction, and evaluation.

**36 entries** · **Cutoff and source review: 2026-10-10** · **English and Chinese paper summaries**

19 method/framework papers · 11 benchmark papers · 5 technical reports · 1 official system release. These are primary contribution types, not peer-review certifications.

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

- [Multimodal Tool Orchestration](#tool-orchestration)
- [Active Audio-Video Perception and Memory](#active-perception)
- [GUI and Computer-Use Agents](#computer-use)
- [Real-Time Interaction and Voice Systems](#realtime)
- [Agent and Interaction Evaluation](#evaluation)
- [Supporting Omni Foundation Models](#foundations)
- [Reading routes](#reading-routes)
- [Contributing](#contributing)

## Category Overview

| Category | Entries | Central question |
| --- | --- | --- |
| [Multimodal Tool Orchestration](#tool-orchestration) | 8 | Systems that plan and execute calls to specialist models, tools, or media workflows. Modality breadth can come from composition rather than one native model. |
| [Active Audio-Video Perception and Memory](#active-perception) | 6 | Agents that decide what evidence to inspect or retrieve. Their actions change the information available to the reasoner; they do not necessarily manipulate an external application. |
| [GUI and Computer-Use Agents](#computer-use) | 4 | Visual action grounding and closed-loop task execution on websites, desktops, and phones. These are relevant action-side foundations, not claims of full audio-video coverage. |
| [Real-Time Interaction and Voice Systems](#realtime) | 4 | Full-duplex perception and response, interruption handling, and speech-to-tool integration. Interaction components are explicitly separated from tool-capable systems. |
| [Agent and Interaction Evaluation](#evaluation) | 11 | Execution environments, tool-use tasks, and selected interaction/perception diagnostics. Evaluation targets and their limits are stated per entry. |
| [Supporting Omni Foundation Models](#foundations) | 3 | A deliberately small set of direct enabling models. Broad modality support or fluent speech alone does not establish autonomous planning or tool execution. |

<a id="tool-orchestration"></a>

## Multimodal Tool Orchestration

Systems that plan and execute calls to specialist models, tools, or media workflows. Modality breadth can come from composition rather than one native model.

| Entry and role | First submitted / released | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **Visual ChatGPT**<br>Paper · Tool agent<br>T/I | 2023-03-08 | Connects ChatGPT to visual foundation models through prompts that describe model capabilities, inputs, and outputs. Supports multi-step image understanding, generation, editing, and user corrections; its modality scope is primarily image and text. | 通过描述模型能力、输入和输出的提示，将 ChatGPT 连接到视觉基础模型。支持多步骤图像理解、生成、编辑及用户纠正；其模态范围主要为图像和文本。 | [arXiv 2303.04671](https://arxiv.org/abs/2303.04671) | [A · v1](docs/SOURCE_AUDIT.md#paper-2303-04671) |
| **ViperGPT**<br>Paper · Tool agent<br>T/I/V | 2023-03-14 | Generates and executes Python programs that compose vision-language modules through an API for visual reasoning. Provides an executable program-based precursor to multimodal agents; it does not establish a general conversational or full-duplex agent. | 生成并执行 Python 程序，通过 API 组合视觉语言模块开展视觉推理。它是基于可执行程序的多模态智能体前驱工作，并未证明通用对话或全双工智能体能力。 | [arXiv 2303.08128](https://arxiv.org/abs/2303.08128) | [A · v1](docs/SOURCE_AUDIT.md#paper-2303-08128) |
| **MM-REACT**<br>Paper · Tool agent<br>T/I/V | 2023-03-20 | Interleaves ChatGPT reasoning with calls to vision experts, returning their observations as text with file references and spatial information. Further calls depend on the accumulated observations; audio is discussed as an extension rather than demonstrated native omni coverage. | 交替进行 ChatGPT 推理与视觉专家调用，将观测转为带文件引用和空间信息的文本。后续调用依据累积观测决定；音频被作为扩展方向讨论，而非已展示的原生全模态覆盖。 | [arXiv 2303.11381](https://arxiv.org/abs/2303.11381) | [M · v1](docs/SOURCE_AUDIT.md#paper-2303-11381) |
| **HuggingGPT**<br>Paper · Tool agent<br>T/I/A/V | 2023-03-30 | Uses an LLM to decompose requests, select specialist models, execute subtasks with resource dependencies, and summarize results. A foundational example of multimodal capability composition through a language-based controller. | 利用 LLM 分解请求、选择专用模型、按资源依赖执行子任务并总结结果。它展示了通过语言控制器组合多模态能力的奠基性系统思路。 | [arXiv 2303.17580](https://arxiv.org/abs/2303.17580) | [M · v4](docs/SOURCE_AUDIT.md#paper-2303-17580) |
| **AudioGPT**<br>Paper · Tool agent<br>T/A/V | 2023-04-25 | Combines ChatGPT with specialist audio models and ASR/TTS interfaces for multi-round speech, music, sound, and talking-head tasks. This is model orchestration with spoken interfaces, not evidence of native full-duplex audio-video reasoning. | 将 ChatGPT 与音频专用模型及 ASR/TTS 接口结合，处理多轮语音、音乐、声音和说话人视频任务。这是带语音接口的模型编排系统，并非原生全双工音视频推理的证据。 | [arXiv 2304.12995](https://arxiv.org/abs/2304.12995) | [A · v1](docs/SOURCE_AUDIT.md#paper-2304-12995) |
| **Agent-Omni**<br>Paper · Tool agent<br>T/I/A/V | 2025-11-04 | A master agent decomposes a request into modality-specific questions, invokes specialist models, and iteratively integrates their answers without retraining. The demonstrated action space is model coordination for understanding, not general GUI or physical control. | 主智能体将请求分解为针对不同模态的问题，调用专用模型，并在不重新训练的情况下迭代整合答案。其展示的行动空间是面向理解的模型协作，而非通用 GUI 或物理控制。 | [arXiv 2511.02834](https://arxiv.org/abs/2511.02834) | [M · v2](docs/SOURCE_AUDIT.md#paper-2511-02834) |
| **Qwen3.8-Omni**<br>Technical report · Agentic model and harness<br>T/I/A/V | 2026-09-22 | Reports native multimodal co-training and tool-driven audio-video workflows, including on-demand evidence gathering and media production. Qwen-MM-Plugins and Qwen-Live-Harness supply system support for tools and real-time orchestration; this entry concerns the documented agent workflows, not modality support alone. | 报告原生多模态联合训练及工具驱动的音视频工作流，包括按需获取证据和媒体制作。Qwen-MM-Plugins 与 Qwen-Live-Harness 为工具及实时编排提供系统支持；本条目关注已描述的智能体工作流，而不只是模态支持。 | [arXiv 2609.25611](https://arxiv.org/abs/2609.25611) | [M · v1](docs/SOURCE_AUDIT.md#paper-2609-25611) |
| **Omni-IO Skills**<br>Paper · Agent harness<br>T/I/A/V | 2026-09-25 | Adds hierarchical skills, a common execution interface, dependency-aware graphs, and a persistent asset registry to existing agents. It composes replaceable multimodal backends and reuses outputs across turns; omni capability belongs to the combined harness and host agent, not a newly trained model. | 为现有智能体增加分层技能、统一执行接口、感知依赖关系的执行图和持久化资产注册表。它组合可替换的多模态后端，并跨轮次复用输出；全模态能力来自支架与宿主智能体的组合，而非新训练的模型。 | [arXiv 2609.31847](https://arxiv.org/abs/2609.31847) | [M · v1](docs/SOURCE_AUDIT.md#paper-2609-31847) |

<a id="active-perception"></a>

## Active Audio-Video Perception and Memory

Agents that decide what evidence to inspect or retrieve. Their actions change the information available to the reasoner; they do not necessarily manipulate an external application.

| Entry and role | First submitted / released | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **VideoAgent (Wang et al.)**<br>Paper · Perception agent<br>T/I/V | 2024-03-15 | Uses an LLM to decide whether to answer or retrieve more video frames, with vision-language captioning and segment-level retrieval as tools. The iterative observation loop targets long-video question answering and does not demonstrate native audio reasoning or external task execution. | 由 LLM 决定作答还是继续检索视频帧，并使用视觉语言描述与片段级检索工具。其迭代观测循环面向长视频问答，未展示原生音频推理或外部任务执行。 | [arXiv 2403.10517](https://arxiv.org/abs/2403.10517) | [M · v1](docs/SOURCE_AUDIT.md#paper-2403-10517) |
| **M3-Agent**<br>Paper · Perception agent<br>T/I/A/V | 2025-08-13 | Builds entity-centric episodic and semantic memory from visual and auditory streams, then reasons through repeated memory-search actions. Uses reinforcement learning and introduces M3-Bench; its control loop is evaluated mainly through memory-grounded video question answering. | 从视觉与听觉流构建以实体为中心的情景记忆和语义记忆，再通过反复搜索记忆进行推理。采用强化学习并引入 M3-Bench；其控制循环主要通过基于记忆的视频问答评估。 | [arXiv 2508.09736](https://arxiv.org/abs/2508.09736) | [M · v4](docs/SOURCE_AUDIT.md#paper-2508-09736) |
| **OmniAgent (Tao et al.)**<br>Paper · Perception agent<br>T/I/A/V | 2025-12-29 | Dynamically chooses visual, audio, and event-localization tools in a coarse-to-fine perception loop. Audio cues help locate relevant events before more detailed inspection; this training-free framework is distinct from the later native OmniAgent by Xing et al. | 在由粗到细的感知循环中动态选择视觉、音频和事件定位工具。音频线索帮助先定位相关事件，再开展更细致的检查；这一无需训练的框架不同于后来 Xing 等人的原生 OmniAgent。 | [arXiv 2512.23646](https://arxiv.org/abs/2512.23646) | [M · v2](docs/SOURCE_AUDIT.md#paper-2512-23646) |
| **OmniRAG-Agent**<br>Paper · Perception agent<br>T/I/A/V | 2026-02-03 | Retrieves relevant frames and audio segments from external banks through multi-turn tool calls for budgeted long audio-video question answering. GRPO uses format and answer rewards to improve the policy; retrieval quality and iterative evidence gathering remain part of the system. | 通过多轮工具调用，从外部库检索相关帧和音频片段，在预算约束下完成长音视频问答。GRPO 利用格式与答案奖励改进策略；检索质量和迭代证据获取仍是系统的重要组成部分。 | [arXiv 2602.03707](https://arxiv.org/abs/2602.03707) | [M · v4](docs/SOURCE_AUDIT.md#paper-2602-03707) |
| **OmniAgent (Xing et al.)**<br>Paper · Perception agent<br>T/I/A/V | 2026-06-17 | Treats audio-video exploration as an Observation-Thought-Action process with on-demand media access and persistent textual memory. Agentic supervised fine-tuning and TAURA reinforcement learning train native active perception; the actions gather evidence rather than control a desktop. | 将音视频探索建模为观测—思考—行动过程，按需访问媒体并保留文本记忆。通过智能体监督微调和 TAURA 强化学习训练原生主动感知；其行动用于获取证据，而非控制桌面。 | [arXiv 2606.19341](https://arxiv.org/abs/2606.19341) | [M · v2](docs/SOURCE_AUDIT.md#paper-2606-19341) |
| **Light-Omni**<br>Paper · Perception agent<br>T/I/A/V | 2026-07-06 | Combines a bounded global memory summary with a learned latent state that drives retrieval and response decisions. Targets lower-overhead, memory-based video understanding by reducing iterative explicit reasoning; the reported actions are information access and answering. | 将有界的全局记忆摘要与学习得到的潜在状态结合，由后者驱动检索和响应决策。通过减少显式迭代推理，降低基于记忆的视频理解开销；报告中的行动是信息访问与作答。 | [arXiv 2607.05511](https://arxiv.org/abs/2607.05511) | [M · v1](docs/SOURCE_AUDIT.md#paper-2607-05511) |

<a id="computer-use"></a>

## GUI and Computer-Use Agents

Visual action grounding and closed-loop task execution on websites, desktops, and phones. These are relevant action-side foundations, not claims of full audio-video coverage.

| Entry and role | First submitted / released | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **SeeAct**<br>Paper · GUI agent<br>T/I | 2024-01-03 | Separates screenshot-based action generation from grounding the proposed action to a web element. Studies visual and HTML-based grounding, exposing the gap between describing the right action and executing it; manually grounded results are not autonomous-agent results. | 将基于截图的行动生成与将行动定位到网页元素的过程分开。研究视觉和 HTML 辅助定位，揭示描述正确行动与实际执行之间的差距；人工定位结果不等于自主智能体结果。 | [arXiv 2401.01614](https://arxiv.org/abs/2401.01614) | [M · v2](docs/SOURCE_AUDIT.md#paper-2401-01614) |
| **Agent S**<br>Paper · GUI agent<br>T/I | 2024-10-10 | Combines experience-augmented hierarchical planning with an agent-computer interface for multi-step GUI tasks. Retrieves external knowledge and prior task experience to support planning and execution; this is a visual computer-use system rather than a full omni model. | 将经验增强的分层规划与智能体计算机接口结合，完成多步骤 GUI 任务。检索外部知识及既往任务经验以支持规划和执行；它是基于视觉的计算机操作智能体系统，而非完整的全模态模型。 | [arXiv 2410.08164](https://arxiv.org/abs/2410.08164) | [M · v1](docs/SOURCE_AUDIT.md#paper-2410-08164) |
| **UI-TARS**<br>Paper · GUI agent<br>T/I | 2025-01-21 | Maps screenshots and interaction history to a unified cross-platform action space, with explicit reasoning before actions. Trains on GUI perception, action traces, and reflective online interaction data to improve closed-loop execution. | 将截图和交互历史映射到跨平台统一行动空间，并在行动前进行显式推理。利用 GUI 感知数据、行动轨迹和带反思的在线交互数据训练，以改进闭环执行。 | [arXiv 2501.12326](https://arxiv.org/abs/2501.12326) | [M · v1](docs/SOURCE_AUDIT.md#paper-2501-12326) |
| **Agent S2**<br>Paper · GUI agent<br>T/I | 2025-04-01 | Routes GUI grounding to specialist models while a hierarchical planner revises the remaining plan after completed subgoals. Separates general reasoning from precise interface localization for desktop and mobile task execution. | 将 GUI 定位交给专用模型，并由分层规划器在子目标完成后修订剩余计划。分离通用推理与精确界面定位，以执行桌面和移动端任务。 | [arXiv 2504.00906](https://arxiv.org/abs/2504.00906) | [M · v1](docs/SOURCE_AUDIT.md#paper-2504-00906) |

<a id="realtime"></a>

## Real-Time Interaction and Voice Systems

Full-duplex perception and response, interruption handling, and speech-to-tool integration. Interaction components are explicitly separated from tool-capable systems.

| Entry and role | First submitted / released | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **Moshi**<br>Paper · Interaction component<br>T/A | 2024-09-17 | Models user and assistant speech in parallel streams, with time-aligned text assisting speech generation. Establishes a full-duplex dialogue architecture for overlap and interruptions; the reviewed contribution does not establish external tool execution. | 以并行流建模用户和助手语音，并用时间对齐的文本辅助语音生成。建立可处理重叠说话与打断的全双工对话架构；所核验贡献并未证明外部工具执行能力。 | [arXiv 2410.00037](https://arxiv.org/abs/2410.00037) | [M · v2](docs/SOURCE_AUDIT.md#paper-2410-00037) |
| **OmniFlatten**<br>Paper · Interaction component<br>T/A | 2024-10-23 | Flattens interleaved speech and text streams into a single sequence and progressively trains modality alignment, half-duplex dialogue, and full-duplex dialogue. Targets natural turn dynamics and low-latency conversation, not a demonstrated tool-using agent. | 将交错的语音和文本流展平为单一序列，逐步训练模态对齐、半双工对话和全双工对话。目标是自然的轮次动态和低延迟交流，并非已展示的工具使用智能体。 | [arXiv 2410.17799](https://arxiv.org/abs/2410.17799) | [M · v2](docs/SOURCE_AUDIT.md#paper-2410-17799) |
| **gpt-realtime and Realtime API**<br>System · Tool-capable API<br>T/I/A | 2025-08-28 | Officially documented speech-to-speech system with asynchronous function calling, remote MCP support, and image input. Images are added as conversation items rather than a native live-video stream; applications provide the execution environment. | — | [Official release](https://openai.com/index/introducing-gpt-realtime/) | [S · release](docs/SOURCE_AUDIT.md#system-gpt-realtime) |
| **MiniCPM-o 4.5**<br>Technical report · Interaction component<br>T/I/A/V | 2026-04-30 | Aligns visual input, audio input, and text/speech output on a shared timeline through Omni-Flow, enabling continuous perception and proactive response. Time-aligned interleaving addresses speech lag; these interaction capabilities do not by themselves demonstrate tool use. | 通过 Omni-Flow 将视觉输入、音频输入及文本/语音输出对齐到共同时间轴，实现持续感知和主动响应。时间对齐交错机制处理语音滞后；这些交互能力本身并不证明工具使用能力。 | [arXiv 2604.27393](https://arxiv.org/abs/2604.27393) | [M · v1](docs/SOURCE_AUDIT.md#paper-2604-27393) |

<a id="evaluation"></a>

## Agent and Interaction Evaluation

Execution environments, tool-use tasks, and selected interaction/perception diagnostics. Evaluation targets and their limits are stated per entry.

| Entry and role | First submitted / released | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **GAIA**<br>Benchmark · Agent evaluation<br>T/I | 2023-11-21 | Proposes real-world questions requiring combinations of reasoning, multimodal handling, browsing, and tools. A foundational assistant benchmark whose answer-based evaluation differs from checking a changed computer state; not every question requires all modalities. | 提出需要组合推理、多模态处理、浏览和工具使用的现实问题。它是通用助手评测的奠基性基准，其基于答案的评估不同于检查计算机状态变化；并非每道题都需要所有模态。 | [arXiv 2311.12983](https://arxiv.org/abs/2311.12983) | [A · v1](docs/SOURCE_AUDIT.md#paper-2311-12983) |
| **VisualWebArena**<br>Benchmark · Execution evaluation<br>T/I | 2024-01-24 | Provides visually grounded tasks in reproducible web environments, requiring agents to interpret images and act on websites. Extends functional evaluation with visual criteria; screenshot or element grounding alone is insufficient to establish task success. | 在可复现的网页环境中提供依赖视觉信息的任务，要求智能体理解图像并操作网站。在功能性评估中加入视觉判据；仅正确理解截图或定位元素不足以证明任务成功。 | [arXiv 2401.13649](https://arxiv.org/abs/2401.13649) | [M · v2](docs/SOURCE_AUDIT.md#paper-2401-13649) |
| **OSWorld**<br>Benchmark · Execution evaluation<br>T/I | 2024-04-11 | Evaluates open-ended tasks in real computer environments using screenshots, optional accessibility information, and mouse/keyboard actions. Task-specific setup and execution-based checks assess application and file outcomes across multi-application workflows. | 利用截图、可选的无障碍信息及鼠标键盘动作，在真实计算机环境中评估开放式任务。通过任务专用初始化与执行结果检查，评估跨应用工作流中的应用及文件结果。 | [arXiv 2404.07972](https://arxiv.org/abs/2404.07972) | [M · v2](docs/SOURCE_AUDIT.md#paper-2404-07972) |
| **AndroidWorld**<br>Benchmark · Execution evaluation<br>T/I | 2024-05-23 | Runs parameterized tasks on functional Android apps with controlled initialization and state-based rewards. Screenshots and UI trees support perception, while gestures, typing, and limited function APIs support actions; task variation is part of the evaluation. | 在可运行的 Android 应用上执行参数化任务，控制初始化并依据系统状态给出奖励。截图与 UI 树支持感知，手势、输入和有限函数 API 支持行动；任务变化也是评估的一部分。 | [arXiv 2405.14573](https://arxiv.org/abs/2405.14573) | [M · v5](docs/SOURCE_AUDIT.md#paper-2405-14573) |
| **VideoWebArena**<br>Benchmark · Execution evaluation<br>T/I/A/V | 2024-10-24 | Tests whether agents can use video tutorials to retain skills or retrieve facts needed for web tasks. Separates intermediate video-question answers from final environment-state success, exposing the difference between video understanding and acting on it. | 测试智能体能否从视频教程中保留技能，或检索完成网页任务所需的事实。将中间视频问答与最终环境状态成功分开评估，揭示理解视频与据此行动之间的区别。 | [arXiv 2410.19100](https://arxiv.org/abs/2410.19100) | [M · v3](docs/SOURCE_AUDIT.md#paper-2410-19100) |
| **OmniMMI / M4**<br>Benchmark · Interaction evaluation<br>T/I/A/V | 2025-03-29 | Evaluates streaming-video understanding and proactive reasoning, and introduces multiplexed input/output modeling with M4. Includes action-planning and response-timing tasks, but does not constitute a general external-tool execution benchmark. | 评估流式视频理解与主动推理，并通过 M4 引入输入输出复用建模。包含行动规划和响应时机任务，但不构成通用外部工具执行基准。 | [arXiv 2503.22952](https://arxiv.org/abs/2503.22952) | [M · v1](docs/SOURCE_AUDIT.md#paper-2503-22952) |
| **OmniGAIA / OmniAtlas**<br>Benchmark · Agent evaluation<br>T/I/A/V | 2026-02-26 | Constructs cross-modal, multi-hop tasks through event graphs, requiring tool-integrated reasoning over image, audio, and video evidence. Also introduces OmniAtlas, trained with guided trajectory exploration and fine-grained preference correction; its tools include search, browsing, code, and active media access. | 通过事件图构造跨模态多跳任务，要求围绕图像、音频和视频证据开展工具集成推理。同时提出 OmniAtlas，以引导式轨迹探索和细粒度偏好纠正训练；其工具包括搜索、浏览、代码及主动媒体访问。 | [arXiv 2602.22897](https://arxiv.org/abs/2602.22897) | [M · v3](docs/SOURCE_AUDIT.md#paper-2602-22897) |
| **LVOmniBench**<br>Benchmark · Perception diagnostic<br>T/A/V | 2026-03-19 | Tests long audio-video comprehension, including temporal localization, memory, and fine-grained cross-modal evidence. Included as a diagnostic for perception agents; question-answer accuracy alone does not establish tool-use or environment-control ability. | 测试长音视频理解，包括时间定位、记忆和细粒度跨模态证据处理。作为感知智能体的诊断基准收录；问答准确率本身不能证明工具使用或环境控制能力。 | [arXiv 2603.19217](https://arxiv.org/abs/2603.19217) | [A · v1](docs/SOURCE_AUDIT.md#paper-2603-19217) |
| **Full-Duplex-Bench-v3**<br>Benchmark · Voice tool evaluation<br>T/A | 2026-04-06 | Pairs natural human speech disfluencies with chained tool-use scenarios, evaluating tool selection, arguments, completion, latency, and turn taking. Uses deterministic local mock APIs, so measured latency excludes real network/service delays and does not certify production performance. | 将自然人类语音中的不流畅现象与链式工具使用情景配对，评估工具选择、参数、完成情况、延迟及轮次控制。使用确定性的本地模拟 API，因此测得延迟不含真实网络/服务延迟，也不能认证生产性能。 | [arXiv 2604.04847](https://arxiv.org/abs/2604.04847) | [M · v1](docs/SOURCE_AUDIT.md#paper-2604-04847) |
| **Omni-DuplexEval**<br>Benchmark · Interaction evaluation<br>T/A/V | 2026-05-17 | Evaluates continuous real-time descriptions and proactive reminders with timestamp-aware assessment of content and response timing. Uses an LLM judge for interaction quality; it measures duplex behavior rather than general-purpose tool execution. | 通过感知时间戳的评估，检查连续实时描述和主动提醒中的内容与响应时机。使用 LLM 评判交互质量；衡量的是双工行为，而非通用工具执行。 | [arXiv 2605.17360](https://arxiv.org/abs/2605.17360) | [M · v2](docs/SOURCE_AUDIT.md#paper-2605-17360) |
| **OmniAssistBench**<br>Benchmark · Interaction evaluation<br>T/I/A/V | 2026-08-21 | Builds goal-oriented, multi-turn assistant tasks from segmented videos, including visual references, context retention, and event-dependent responses. Evaluation simulates online interaction offline along predefined routes; it does not test freely branching user-agent interaction. | 从分段视频构建面向目标的多轮助手任务，涵盖视觉指代、上下文保持及事件触发响应。评估沿预设路径离线模拟在线交互，并不测试可自由分支的用户—智能体交互。 | [arXiv 2608.21360](https://arxiv.org/abs/2608.21360) | [M · v1](docs/SOURCE_AUDIT.md#paper-2608-21360) |

<a id="foundations"></a>

## Supporting Omni Foundation Models

A deliberately small set of direct enabling models. Broad modality support or fluent speech alone does not establish autonomous planning or tool execution.

| Entry and role | First submitted / released | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **GPT-4o System Card**<br>Technical report · Supporting model<br>T/I/A/V | 2024-10-25 | Documents an end-to-end omni model and its capability, limitation, and safety evaluations, especially speech-to-speech interaction. Included as a foundation for multimodal assistants; the system card alone is not evidence of an autonomous action loop or of every described modality being publicly exposed. | 记录端到端全模态模型的能力、局限和安全评估，尤其关注语音到语音交互。作为多模态助手的基础收录；系统卡本身不能证明自主行动循环，也不能证明所有描述的模态均已公开开放。 | [arXiv 2410.21276](https://arxiv.org/abs/2410.21276) | [A · v1](docs/SOURCE_AUDIT.md#paper-2410-21276) |
| **Qwen2.5-Omni**<br>Technical report · Supporting model<br>T/I/A/V | 2025-03-26 | Uses Thinker-Talker modeling, time-aligned multimodal position encoding, and streaming speech generation to connect text, images, audio, and video. Directly supports later perception agents such as M3-Agent; the base report is not evidence of a general tool-use loop. | 通过 Thinker-Talker 建模、时间对齐多模态位置编码及流式语音生成，连接文本、图像、音频和视频。直接支撑 M3-Agent 等后续感知智能体；基础模型报告并非通用工具使用循环的证据。 | [arXiv 2503.20215](https://arxiv.org/abs/2503.20215) | [M · v1](docs/SOURCE_AUDIT.md#paper-2503-20215) |
| **Qwen3-Omni**<br>Technical report · Supporting model<br>T/I/A/V | 2025-09-22 | Extends Thinker-Talker with mixture-of-experts components, multi-codebook speech generation, and a causal waveform decoder. Decoupled text and speech pathways allow external tool-related intervention, but the architecture alone does not establish an autonomous agent. | 以混合专家组件、多码本语音生成和因果波形解码器扩展 Thinker-Talker。解耦的文本与语音路径允许外部工具相关干预，但架构本身并不能证明自主智能体能力。 | [arXiv 2509.17765](https://arxiv.org/abs/2509.17765) | [M · v1](docs/SOURCE_AUDIT.md#paper-2509-17765) |

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
