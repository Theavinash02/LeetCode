# TCS Prime Interview — Full Script

> For rehearsal. Read out loud at least once tonight and once tomorrow morning. Time yourself on the self-intro.

---

## 1. Self-Introduction (~90 seconds)

> **Cue to deliver:** *"Tell me about yourself."*

Good morning/afternoon. My name is Avinash. I am currently working as a Software Analyst Trainee at Fern Software, where I have been for over a year and a half. My work is primarily centered around a fintech core banking product called Abacus and AbacusWeb, which covers modules like lending, savings, payroll, reconciliation, onboarding, and settlement.

On a day-to-day basis, I spend most of my time handling client tickets — triaging issues on Freshdesk, replicating them in our test environments, and performing root cause analysis. I also support User Acceptance Testing and Go-Lives for new clients, write specifications for enhancements, handle client calls, and conduct internal case discussions with my team. I work extensively with SQL Server to investigate issues and generate client-specific reports.

Alongside my job, I contribute to an open-source Python library called pgmpy, which is used in causal inference and probabilistic machine learning research. I started contributing in September 2025 to stay close to development work and to improve my coding skills beyond my support role. Over the past seven months, I have landed three pull requests that refactored the library's dataset and example-model discovery system. I was ranked among the top thirteen contributors to their version 1.1.0 release.

In terms of learning, I have also worked on a self-driven project on large language model fine-tuning using LoRA and Supervised Fine-Tuning, which gave me hands-on familiarity with the modern machine learning stack. Before joining Fern, I completed my Bachelor of Technology in Information Technology from Anna University in 2024, with a CGPA of 8.19.

I am looking for a role that offers broader technical exposure and a stronger development orientation than my current position, which is why I am very interested in this opportunity at TCS.

---

## 2. Fern Software — Deep Dive

> **Cue:** *"Tell me about your work at Fern."* / *"What do you do day-to-day?"*

At Fern Software, I work as a Software Analyst Trainee on a fintech core banking product called Abacus and its web version AbacusWeb. The product is used by microfinance institutions and banks, covering modules like lending, savings, payroll, reconciliation, onboarding and KYC, and settlement.

My day-to-day work is primarily client-facing. I spend most of my time handling client tickets on Freshdesk — I triage incoming issues, replicate them in our test environments, categorize them by module and severity, and perform root cause analysis. When a fix is required at the data level, I write SQL scripts to correct the data in production. When it is a code-level issue, I document the findings and coordinate with the development and QA teams.

Beyond tickets, I support new client Go-Lives and User Acceptance Testing. I have been part of two Go-Lives for microfinance implementations, where I assisted in system validation and post-deployment issue resolution. I also write test cases and specifications when we identify new bugs or when the client requests enhancements. A significant part of my week involves client calls and internal team discussions where we walk through ongoing cases.

I use SQL Server extensively — both for investigating issues using SQL Profiler and for generating MIS and client-specific reports via stored procedures. I often export data from SQL to Excel for analysis or to prepare specifications for new features.

### Key wins — have these ready

**Win 1 — Director-level appreciation:**

> There was a live payment and settlement issue at one of our clients that was blocking their operations. I was involved in the investigation, identifying the root cause, and coordinating the fix. After the issue was resolved, I received direct appreciation from our director for the effort, which was a significant recognition given the urgency and client impact.

**Win 2 — Shipped specifications:**

> Over my time at Fern, I have written and delivered more than ten specifications that have gone into production. These cover both enhancements to existing reports and new features in modules like loans and savings. Seeing specifications I authored being deployed and used by clients has been a meaningful part of my role.

### Likely follow-up questions

**"What kind of SQL do you write?"**
> Mostly T-SQL on SQL Server. Complex joins across multiple tables, stored procedures for client reports, data fix scripts for production, and queries using SQL Profiler to debug performance issues.

**"Have you handled critical production issues?"**
> Yes. The one that stands out is the payment-settlement issue I mentioned, but I regularly handle production-impacting tickets where I need to investigate quickly, identify the cause, and either apply a data fix or coordinate a code fix with the development team.

**"How do you approach a new client ticket?"**
> My process is — read the ticket carefully to understand the symptoms, try to replicate in a test environment, narrow down whether it is a data issue, configuration issue, or a code defect, check the audit trail and logs in SQL Server, and then either apply a fix or document the findings for the development team. I always update the client through Freshdesk on progress.

---

## 3. pgmpy — Open Source Contribution

> **Cue:** *"Tell me about your open-source contribution."* / *"What is pgmpy?"*

pgmpy is a Python library for causal inference and probabilistic reasoning using graphical models. It is used in research and industry for working with Bayesian networks, causal discovery, and related probabilistic modeling techniques. The library is actively maintained and has a significant user base in the causal-inference research community.

### Why I started contributing

> My role at Fern is primarily client-facing — tickets, root cause analysis, and SQL — which is solid production experience, but I wanted to stay close to development work on the side. I searched for open-source projects with beginner-friendly issues tagged, and pgmpy was a good fit. I started with small contributions in September 2025 and gradually took on more substantial work. Over the past seven months, I have landed three pull requests and was ranked among the top thirteen contributors to their version 1.1.0 release.

### What I contributed — the three PRs

My main contribution was a refactoring of how pgmpy discovers and loads datasets and example models.

**The problem:** Before my work, pgmpy used a manual registry — essentially a hand-maintained dictionary mapping dataset names to classes. Every time someone added a new dataset, they had to update this registry in multiple places, which was error-prone and did not scale well.

**My solution:** I refactored the dataset base class to inherit from skbase, which is a lightweight library that provides automatic class discovery and a tag-based metadata system. This eliminated the manual registry entirely. Adding a new dataset now only requires creating a new class in the datasets folder with a few tags declared — the discovery, loading, and filtering all happen automatically.

**The three pull requests:**

1. **PR 2347** — My initial contribution on the dataset discovery and loading mechanism.
2. **PR 2515** — The full refactor using skbase, including the `_BaseDataset` class, the tag system, the public API functions `load_dataset` and `list_datasets`, and updating the test suite.
3. **PR 2571** — Extending the same registry pattern to example models — pre-built Bayesian networks like Alarm, Asia, and others.

### Technical specifics I own

- I designed `_BaseDataset` to inherit from `skbase.base.BaseObject`, which provides the tag management machinery.
- I defined the `_tags` schema with metadata like `name`, `n_variables`, `n_samples`, `has_ground_truth`, `has_expert_knowledge`, and flags for data type.
- I implemented `load_dataframe` as a tag-guarded pipeline — it fetches the data from Hugging Face Hub, parses the CSV, and applies optional post-processing like missing-value replacement, categorical conversion, and ordinal conversion, based on what the subclass declares.
- I wrote `_parse_expert_knowledge`, a state-machine parser for a text format used by the causal-discovery community to encode domain knowledge like forbidden edges, required edges, and temporal ordering.
- I implemented the public API — `load_dataset` and `list_datasets` — using skbase's `all_objects` for auto-discovery and tag-based filtering.

### Scope honesty — what I did not write

> I want to be clear about scope. There are mixin classes in the same file — `_CovarianceMixin` and `_TubingenBenchmarkMixin` for datasets, and the file-format mixins for example models like `DiscreteMixin`, `BIFMixin`, `ContinuousMixin`, and `DAGMixin` — that were contributed by other maintainers. My work was on the framework that those mixins plug into. My design allowed additional formats and dataset types to be added as mixins without changing the base class or the public API, which is exactly how those contributions came in.

### Likely follow-up questions

**"What is skbase?"**
> skbase is a lightweight library that provides base-class infrastructure for scientific Python projects. It is used by sktime and other libraries. It gives me tag management through the `_tags` class attribute, class discovery through `all_objects`, and tag-based filtering. By inheriting from `skbase.base.BaseObject`, I got all of this functionality without writing it from scratch.

**"What is a tag?"**
> A tag is a piece of class-level metadata. Each dataset class declares a `_tags` dictionary with keys like `name`, `is_discrete`, `has_ground_truth`. Tags serve three purposes — they identify the class, they are used as filters for listing datasets, and they act as runtime switches inside the loading pipeline. For example, if `has_missing_data` is True, the loader applies missing-value replacement; otherwise, it skips that step.

**"How does auto-discovery work?"**
> When a user calls `load_dataset` or `list_datasets`, the function calls `skbase.lookup.all_objects`, which walks the `pgmpy.datasets` package, imports every module, and collects every class that inherits from `_BaseDataset`. For filtering, I pass `filter_tags` to `all_objects` so the filtering happens during discovery rather than in a Python post-processing step.

**"Why was the refactor needed?"**
> The old manual registry had two problems. First, every new dataset required updating the registry manually, which was easy to forget. Second, there was no standardized metadata — users could not filter datasets by type. After the refactor, adding a dataset is a matter of creating a class with a tag declaration — zero changes to the loading code or the registry. It is configuration rather than imperative code.

**"What would you change if you were revisiting this today?"**
> In the newer `load_model` function I pushed name-matching into `all_objects` via `filter_tags={"name": name}`, which is cleaner than the explicit for-loop I originally wrote in `load_dataset`. If I were refactoring `load_dataset` today, I would adopt the same pattern for consistency.

---

## 4. LLM Fine-Tuning Project

> **Cue:** *"Tell me about your ML project."* / *"What have you done with LLMs?"*

### Upfront honesty — deliver this early

> This was a self-driven learning project from July 2025. I built it to get hands-on with the modern large language model fine-tuning stack — LoRA, quantization, Supervised Fine-Tuning, and the Hugging Face ecosystem. I understand the flow and the concepts well. Since September I have been focused on pgmpy and real open-source contribution work, so I have not iterated further on this project. If you ask me for specific hyperparameter values, I may need to recall, but I can walk you through what I built and what I learned.

### The project

> I fine-tuned Microsoft's Phi-3-mini, a 3.8 billion parameter instruction-tuned language model, to generate structured outputs for math word problems. Given a natural-language problem, the model learned to output a Schema label and a Sub-Category label. The training data was the Schema-Based Instruction Dataset from Hugging Face.

### The stack — what I used

- **Phi-3-mini-4k-instruct** — the base model, 3.8 billion parameters, loaded from Hugging Face.
- **LoRA** — Low-Rank Adaptation, for parameter-efficient fine-tuning.
- **4-bit quantization** via bitsandbytes, to fit the model into a free Google Colab T4 GPU.
- **Unsloth** — a library that speeds up fine-tuning by patching Hugging Face internals.
- **TRL library's SFTTrainer** for Supervised Fine-Tuning.
- **Hugging Face datasets** library for loading and splitting the data.

### The pipeline — six steps

1. Install the libraries.
2. Load Phi-3-mini with 4-bit quantization using Unsloth's `FastLanguageModel.from_pretrained`.
3. Apply LoRA adapters on attention and feed-forward layers — `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj` — with rank 16.
4. Load the dataset, split 90/10 train/eval, and format each row using an Alpaca-style prompt template with `### Problem:` and `### Response:` markers.
5. Train using SFTTrainer with batch size 2, gradient accumulation of 8, learning rate 3e-4, for 50 steps.
6. Test with a held-out prompt, generate, decode, and evaluate.

### What I learned

> My goal was hands-on familiarity with the modern fine-tuning stack rather than a production model. I trained for only 50 steps as a learning exercise. The model classified most problems correctly but sometimes generated messy tails because the step count was too low and the end-of-sequence token handling was not fully trained. Real use would require more data, more training steps, and cleaner stop-token handling in the prompt template.

### Likely follow-up questions — safe answers

**"What is LoRA?"** — (you rated 3, confident)
> Low-Rank Adaptation. Instead of updating all the weights of a pretrained model, you freeze them and inject small trainable matrices alongside each target layer. Mathematically, if a linear layer computes `y = W·x`, LoRA replaces it with `y = W·x + B·A·x`, where W is frozen and A and B are small matrices whose product has rank r. By picking a small rank — I used 16 — I trained only a few million parameters instead of 3.8 billion, with minimal quality loss. That is what made fine-tuning feasible on a free Colab GPU.

**"What is 4-bit quantization?"** — (rated 2)
> Normally model weights are stored as 16-bit or 32-bit floating-point numbers. 4-bit quantization compresses each weight to 4 bits, cutting memory usage roughly four times. You lose some numerical precision, but for inference and LoRA training the loss is small. Without quantization, Phi-3-mini would have needed more VRAM than my Colab T4 had available. Quantization is what made the whole project fit in memory.

**"What is Supervised Fine-Tuning?"** — (rated 2)
> SFT trains the model to imitate specific input-output pairs. You give it a prompt and a target response, and it learns to produce the target. It is the standard first step in fine-tuning, as opposed to RLHF — Reinforcement Learning from Human Feedback — which uses preference signals instead of explicit targets. In my project, the input was a problem statement and the target was a Schema and Sub-Category pair.

**"Why Phi-3-mini specifically?"** — (rated 1, safe answer)
> To be honest, the main reason was practical. It is a modern instruction-tuned model from Microsoft that is small enough to fit on a free Colab GPU with quantization, but capable enough to follow structured prompts. I wanted to learn fine-tuning, and Phi-3-mini was a sensible model for that purpose given my hardware constraints.

**"What is the Alpaca prompt format?"** — (rated 3, confident)
> It is a convention popularized by Stanford's Alpaca project for instruction-tuning prompts. The format uses section markers like `### Problem:` and `### Response:` with newlines between them. The model learns to treat these markers as structural signals — when it sees `### Response:` during inference, it knows it should produce the expected output pattern. I used this format for both training and inference, with the response section left empty at inference so the model fills it in.

**"What is gradient accumulation?"** — (rated 1, safe answer)
> Memory constraints only allowed me to fit a physical batch size of two examples on my GPU. Small batches produce noisy gradients. Gradient accumulation solves this — instead of updating weights after every batch, the gradients accumulate over multiple forward passes, and then one weight update is applied. In my setup, I accumulated over eight steps, giving an effective batch size of sixteen without the memory cost.

**"Why was the output not clean at the end?"** — (rated 1, honest answer)
> Two reasons. First, I trained for only 50 optimizer steps, which is very low — the model did not fully learn when to emit the end-of-sequence token. Second, my prompt template did not include an explicit stop marker in the training data, so the model did not have a clean signal for where to stop. A proper fix would be more training steps, more data, and including an explicit end-of-sequence token in the training format. I noted this as a known limitation at the end of the notebook.

**"Can you name all the libraries you used?"** — (rated 1, best-effort answer)
> The main ones were Hugging Face transformers for the model infrastructure, TRL for SFTTrainer, PEFT for LoRA configuration, bitsandbytes for 4-bit quantization and the 8-bit AdamW optimizer, Unsloth for the fine-tuning speedup, and Hugging Face datasets for data loading. PyTorch was the underlying tensor library.

### If they dig deeper than you can recall

> I'd need to revisit the notebook to answer that precisely. Conceptually, what's happening is... *[pivot to concept]*.

This is a completely acceptable response for a learning project from nine months ago.

---

## 5. Bitcoin Ransomware Detection — Final Year Project

> **Cue:** *"Tell me about your final year project."*

### Critical framing — deliver this upfront

> That was my undergraduate final-year project from 2024 — a team project with my classmates. The project was on detecting Bitcoin ransomware addresses using machine learning on the UCI BitcoinHeist dataset. I want to be honest — my contribution was primarily at the team discussion and coordination level. My teammates handled most of the technical modeling work. It was my first exposure to machine learning concepts like supervised classification, Random Forest, and class imbalance. Since graduating and joining Fern, and more recently starting the pgmpy contribution, my focus has shifted to production work and open-source contribution rather than this particular project.

### What the project was (high-level)

> The dataset was UCI BitcoinHeist, which has about 2.9 million Bitcoin transactions labeled by ransomware family — 28 known ransomware families plus a `white` class for legitimate transactions. The team used graph-derived features like transaction length, weight, income, and neighbor count to train a Random Forest classifier. The overall accuracy was around 99%, though we understood class imbalance was a challenge — the legitimate transactions dominated the data, and rare ransomware families had very few examples.

### If they ask "what did you specifically do?"

> To be honest, my specific coding contribution was limited. I was involved in team discussions, reviewing the approach, and helping with coordination. My teammates led the implementation and modeling. That is actually one of the reasons I have focused so heavily on pgmpy since — I wanted hands-on technical work that is genuinely mine rather than shared team credit. I am comfortable being clear about what I did and did not do.

### If they ask about ML concepts from the project

You can still answer conceptually because you reviewed the material:

**"What is a Random Forest?"**
> An ensemble of decision trees. Each tree trains on a random subsample of the data using a random subset of features at each split. At prediction time, all trees vote and the majority class wins. The randomness makes the trees diverse, which reduces overfitting compared to a single deep decision tree.

**"What is class imbalance?"**
> When some classes have far more examples than others. In the BitcoinHeist dataset, legitimate transactions were about 98.5% of the data, while individual ransomware families had very few examples. The effect is that a model can achieve high accuracy by always predicting the majority class and still completely fail on the minority classes. That is why accuracy alone is a misleading metric here.

### Do not volunteer technical depth

Keep answers short on this project. Redirect naturally toward pgmpy and Fern if they probe technical details. Your strongest move is to be *honest and brief* rather than *detailed and defensive*.

---

## 6. Why TCS? / Why leave Fern?

> **Cue:** *"Why TCS?"* or *"Why do you want to leave your current company?"*

### The answer

> My time at Fern Software has been valuable. I have learned the fintech domain, worked directly with clients, handled production issues, and developed strong SQL and problem-solving skills. However, my role is primarily support and analysis rather than development, and I have been looking for a role that offers two things.

> First, a stronger development focus — I have spent my personal time contributing to pgmpy precisely because I want to do more hands-on coding work, and I would like that to be part of my day-to-day role rather than something I do on the side.

> Second, broader scale and exposure. TCS works on a much larger range of technologies, clients, and project types than my current company. I want to grow my technical breadth and work alongside more experienced engineers.

> TCS Prime is a natural fit because it combines technical depth with the scale of a top-tier consulting and technology organization. I believe my production experience, SQL skills, and open-source contribution work prepare me well for the role, and I am excited about the growth opportunity.

### Why this answer is strong

- It is honest about why you are leaving (support role, want development).
- It does not bad-mouth Fern (you credit what you learned).
- It positions pgmpy as evidence of your development interest.
- It closes on a forward-looking note (growth, fit).

---

## 7. Common HR / Behavioral Questions

### "What are your strengths?"

> Three things. First, I am honest about what I know and do not know — which makes me reliable for root cause analysis and escalation. Second, I am self-driven — my pgmpy contribution happened entirely on my own time because I wanted to grow my technical skills. Third, I am good with clients — I have handled difficult tickets and live issues while maintaining professional communication, and I have received director-level appreciation for my work on a production incident.

### "What are your weaknesses?"

> My current role is primarily support, so my exposure to large-scale system design and to formal software engineering practices like code review at an enterprise level is limited. I have been addressing this through open-source contribution in pgmpy, where I go through formal PR review with maintainers — but I know I have a lot more to learn, and a role like TCS Prime would accelerate that.

### "Where do you see yourself in 5 years?"

> I see myself as a strong backend or full-stack developer with solid domain expertise — ideally continuing in fintech given my current experience, but open to other domains. I would like to combine production engineering with ongoing learning, possibly moving toward ML-adjacent work given my interest in that area. Continuing to contribute to open source is also part of the plan.

### "Why should we hire you?"

> I bring three things. First, real production experience — I have been in a client-facing fintech role for over a year and a half, so I understand how production systems behave and how to debug them. Second, self-driven learning — my open-source work in pgmpy shows I invest in my own growth. Third, honest communication — I know what I know and what I do not know, and I will ask the right questions instead of bluffing, which makes me reliable in a team setting.

### "What do you know about TCS?"

> TCS is one of the largest IT services and consulting companies in the world, headquartered in India and part of the Tata Group. TCS Prime is a premium hiring track focused on high-caliber technical talent. The company works across domains including financial services, retail, healthcare, and telecommunications, and it has a strong engineering and research presence. I am particularly drawn by the scale and the variety of technology work available.

### "Are you willing to relocate?"

> Yes. I am open to relocating to wherever the role requires.

### "Any questions for us?"

Always have 2-3 questions ready. Good ones:
1. *"What does the onboarding and learning curve look like for someone joining Prime at this level?"*
2. *"What kinds of projects is the team I would be joining currently working on?"*
3. *"What qualities do you see in the strongest performers in this team?"*

Avoid salary/leave/work-from-home questions in a first technical round.

---

## 8. DSA / Coding Questions — Honest Strategy

If they ask you to code live, here is your script:

> I would like to be upfront — I have not been doing daily LeetCode, so I may be rusty on advanced data structures. I am comfortable with basic arrays, strings, dictionaries, and standard logic. I will think out loud as I solve it so you can see my approach, and I would appreciate guidance if I get stuck.

This is a mature, honest answer that most TCS interviewers will respect. It is infinitely better than bluffing and freezing.

### Quick warm-ups to practice tonight (10 minutes max)

Go through these mentally only — do not spend an hour on them:

- **Reverse a string** — `s[::-1]` in Python.
- **Check if a string is a palindrome** — compare with its reverse.
- **Find the maximum in a list** — `max(lst)` or iterate with a running max.
- **Count occurrences of each character** — dictionary where key is char, value is count.
- **Find duplicates in a list** — use a set to track seen items.
- **FizzBuzz** — print "Fizz" for multiples of 3, "Buzz" for 5, "FizzBuzz" for 15.

If they give you something harder, talk through your approach even if you do not reach a complete solution. Process matters as much as the answer.

---

## 9. Delivery Reminders

**Pace.** Speak slowly. A calm, slightly slow delivery sounds more confident than a fast one. When asked a question, pause for one second before answering. It feels like a long time to you but sounds natural to the interviewer.

**Honesty signals.** When you do not know something, say so. "I'm not fully sure, but my best understanding is..." is better than bluffing. Interviewers can tell.

**Anchor answers in examples.** Instead of "I know SQL well," say "I write T-SQL daily for MIS reports and data fixes at Fern."

**Smile on video.** Even a slight smile and eye contact with the camera makes a huge difference.

**Closing.** If they ask if you have anything else to add, a safe close is: *"Thank you for the conversation. I am genuinely excited about this opportunity, and I appreciate the chance to discuss my work."*

---

## Your timeline from now

- **Now** — one read-through out loud. Time the self-intro. Should be ~90 seconds.
- **Morning** — one more read-through. Quick glance at the cheat sheet.
- **Just before interview** — 10 minutes with cheat sheet only. Water. Deep breath.
- **During interview** — pause, breathe, speak slowly, be honest.

You are prepared. Trust the work you have done.
