# TCS Prime — Pre-Interview Cheat Sheet

> Glance 10 minutes before. Do NOT re-read the full script this close to the interview.

---

## Self-Intro (~90s) — Structure

1. **Name + current role.** "Good morning, my name is Avinash. I am a Software Analyst Trainee at Fern Software, over a year and a half."
2. **What Fern does.** Fintech core banking product — Abacus and AbacusWeb. Lending, savings, payroll, reconciliation, onboarding, settlement.
3. **What I do there.** Client tickets and root cause analysis on Freshdesk. SQL Server daily. UAT and Go-Live support. Specifications for enhancements. Client calls.
4. **pgmpy.** Open-source contributor since Sep 2025. Three PRs. Top 13 contributor in v1.1.0. Dataset and example-model registry refactor using skbase.
5. **LLM project.** Self-driven learning project in July 2025. LoRA fine-tuning of Phi-3-mini with Hugging Face stack.
6. **Education.** B.Tech IT, Anna University, 2024, CGPA 8.19.
7. **Why TCS.** Looking for broader scale and stronger development focus.

---

## Four Power Phrases (use throughout)

1. **"I want to be honest..."** — signals maturity. Use before any scope limitation.
2. **"My contribution was primarily on the framework..."** — for pgmpy mixins you didn't write.
3. **"That was a learning project — I understand the concepts, but may need to recall specific details."** — for the LLM project.
4. **"My specific contribution was at the team coordination level — my teammates led the implementation."** — for the Bitcoin final year project.

---

## Fern — Keywords to Drop

- Software Analyst Trainee, 1.5 years
- Abacus / AbacusWeb — fintech core banking
- Microfinance institutions, banks
- Lending, Savings, Payroll, Reconciliation, KYC/Onboarding, Settlement
- Freshdesk — client ticket triage, RCA (root cause analysis)
- SQL Server, SQL Profiler, T-SQL, stored procedures
- MIS reports, data fix scripts
- UAT, Go-Live support (2 Go-Lives done)
- Black-box, functional, regression, performance, stress, database testing

**Two wins to mention:**
- **Director-level appreciation** for a live payment/settlement issue
- **10+ specifications** shipped to production (reports + loans/savings features)

---

## pgmpy — Keywords to Drop

- **Causal inference, Bayesian networks, probabilistic graphical models**
- **skbase** — lightweight base-class library (used by sktime). Provides tags + auto-discovery
- **3 PRs:** #2347, #2515, #2571 — dataset registry + example models
- **Top 13 contributor** in v1.1.0 release
- **7 months** of contribution, alongside full-time job
- `_BaseDataset`, `_tags`, `all_objects`, `load_dataset`, `list_datasets`
- `load_dataframe` as a tag-guarded pipeline
- `_parse_expert_knowledge` — state-machine parser

**What I did:** Base class framework, tag schema, discovery logic, public API, tests.
**What others did:** Covariance mixin, Tubingen mixin, the four file-format mixins (BIF, gzipped BIF, JSON, DAGitty).

**One-liner if asked "Why pgmpy?":**
> "My Fern role is client-facing. I wanted to stay close to development through open source. pgmpy had beginner-friendly issues tagged, and it turned into substantial work over seven months."

---

## LLM Project — Keywords + Safe Answers

### Must-drop keywords
- **Phi-3-mini** (3.8B params, Microsoft, instruction-tuned)
- **LoRA** — Low-Rank Adaptation (r=16)
- **4-bit quantization** via bitsandbytes
- **Supervised Fine-Tuning (SFT)** via TRL's SFTTrainer
- **Alpaca prompt format** — `### Problem:` / `### Response:`
- **Unsloth** — speeds up fine-tuning
- **Hugging Face** — transformers, datasets, PEFT
- **Schema-Based Instruction Dataset**
- **Tesla T4 on Colab**, 50 steps training

### Upfront honesty line
> "This was a learning project from July 2025. I understand the concepts well, but may need to pause to recall specific hyperparameters since I haven't touched it since pgmpy work started in September."

### LoRA (confident)
> "Low-Rank Adaptation. Freeze base weights, add small trainable matrices B and A at each target layer. y = Wx + BAx. r=16 in my case. Trained ~millions of params instead of 3.8 billion."

### Quantization (medium)
> "Compresses weights from 16-bit to 4-bit. Cuts memory ~4x. That's what made the 3.8B model fit on a free Colab T4."

### SFT (medium)
> "Supervised Fine-Tuning — train on input-output pairs. Model learns to imitate target responses. First step in fine-tuning, before RLHF."

### Alpaca format (confident)
> "Stanford convention. Uses `### Problem:` and `### Response:` section markers. Model learns the structure during training; at inference, response is left empty and model fills it in."

### Gradient accumulation (weak — safe answer)
> "Memory limited me to batch size 2. Small batches are noisy. Accumulate gradients over 8 forward passes, update once — effective batch size 16, no extra memory."

### Output was not clean (weak — honest answer)
> "Only 50 training steps — model didn't fully learn to emit end-of-sequence. Template didn't have an explicit stop marker either. I noted this as a known limitation in the notebook."

### Libraries (weak — best-effort)
> "Main ones: transformers for the model, TRL for SFTTrainer, PEFT for LoRA, bitsandbytes for 4-bit quantization and 8-bit AdamW, Unsloth for speedup, datasets for data loading. PyTorch underneath."

### If stuck on detail
> "I'd need to revisit the notebook for that specific value. Conceptually, what's happening is..." → pivot to concept.

---

## Bitcoin Ransomware — Short Script

### Opening (deliver this upfront)
> "That was my UG final-year project in 2024 — a team project. Detecting Bitcoin ransomware addresses using Random Forest on the UCI BitcoinHeist dataset. I want to be honest: my contribution was at the team discussion and coordination level — my teammates handled the modeling work. It was my first exposure to ML concepts. Since graduating and especially since starting the pgmpy contribution, my technical focus has been production work and open-source."

### If pushed on specifics
> "My specific coding contribution was limited. That's actually why I've focused so heavily on pgmpy since — I wanted hands-on work that is genuinely mine."

### Do NOT volunteer technical detail. Keep answers short. Redirect to pgmpy/Fern.

---

## Why TCS? — The Answer

> "My role at Fern has been valuable — fintech domain, SQL, client experience. But it's primarily support, not development. I've been using my personal time on pgmpy to stay close to coding, and I'd like that to be my day-to-day role. TCS Prime offers broader scale, technical depth, and more experienced engineers to learn from. That's the fit."

---

## Strengths & Weaknesses — Short

**Strengths:** Honest about what I know. Self-driven (pgmpy on personal time). Good with clients (director-level appreciation).

**Weakness:** Current role is support-heavy, so large-scale system design and formal enterprise practices are limited exposure. Addressing through open source; would accelerate in a Prime role.

---

## 5-Year Plan — Short

> "Strong backend/full-stack developer with solid domain expertise. Open to fintech or other domains. Combining production engineering with ongoing learning and open-source contribution."

---

## Questions to Ask Them (pick 2)

1. "What does onboarding look like for someone joining Prime?"
2. "What kinds of projects is the team currently working on?"
3. "What qualities do you see in the top performers on this team?"

**Avoid** in round 1: salary, leave, WFH.

---

## DSA — Honest Strategy

If asked to code live:

> "I'd like to be upfront — I haven't been doing daily LeetCode, so I may be rusty on advanced data structures. I'm comfortable with arrays, strings, dictionaries, and standard logic. I'll think out loud as I work through it."

**Warm-ups done mentally:** reverse string, palindrome, max in list, count chars, find dupes, FizzBuzz.

**Process matters as much as the answer. Talk out loud.**

---

## 30-Second Pre-Interview Reminders

- **Pause before answering.** 1-second pause = confidence.
- **Speak slowly.** Slightly slower than your natural pace.
- **Eye contact with camera** (if video).
- **"I want to be honest..."** is your power phrase.
- **When you don't know:** "I'm not fully sure, but my best understanding is..."
- **Don't bluff.** Ever.
- **Water nearby.** Sip if you need a pause.
- **One breath** before starting each answer.

---

## Closing Line

> "Thank you for the conversation. I'm genuinely excited about this opportunity, and I appreciate the chance to discuss my work."

---

**You've prepared well. Trust the work. Good luck.**
