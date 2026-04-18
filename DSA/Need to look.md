# TCS Prime — Project & PR Deep Dive (v2, code-accurate)
**Companion to the main cram pack. Focus: your actual projects + pgmpy math.**

> **This is version 2, updated after you shared the actual PR code, file tree, and PR discussions. All PR descriptions now match what the code really does. The inaccurate "before my work" framing from v1 has been removed — the correct story is the three-act one: you built the first registry in #2347, refactored your own design in #2515 after maintainer discussion, and extended the pattern to models in #2571.**

---

## Part 0 — Study strategy verdict

### STOP reading GeeksforGeeks DSA tutorials straight through.

Reading algorithm theory without coding it = **wasted hours**. You will not remember 80% of it by Monday morning, and you can't explain what you haven't written. Finishing the sorting chapter doesn't help if you can't write quicksort's partition function on paper when asked.

### The correct 3-source hybrid

| Source | Purpose |
|---|---|
| **Roadmap PDF** | Breadth checklist — OOP, OS, CN, DBMS topics TCS asks |
| **Main cram pack** | Depth on resume-critical topics (Prob/Stats, LoRA, Pandas, advanced SQL) |
| **This doc** | Your PRs + pgmpy math + Bitcoin project rehearsal |
| **GeeksforGeeks** | DROP. Only if stuck on a specific problem. |
| **Coding practice** | 1 problem solved per pattern on paper > 10 read tutorials |

### Six DSA problems on paper (2-3 hrs)

1. Two-pointer — "Two sum on sorted array"
2. Sliding window — "Longest substring without repeating chars"
3. Hash map — "Subarray sum equals K"
4. Binary search — "Search in rotated sorted array"
5. BFS/DFS — "Number of islands"
6. DP — "Coin change"

### Updated schedule

**Today remaining:**
- 2 hrs — this doc (PR walkthroughs + pgmpy math). Read + explain out loud.
- 2 hrs — Prob/Stats + LoRA sections from main cram pack
- 1.5 hrs — 3 DSA problems on paper
- Sleep by 11.

**Tomorrow:**
- 2 hrs — Roadmap topics (OOP 4 pillars, OS basics, CN OSI + TCP, DBMS normalization + ACID)
- 1.5 hrs — 3 more DSA problems
- 1.5 hrs — Mock drill + STAR rehearsal
- 1 hr — Advanced SQL
- No studying after 8pm Sunday.

---

# Part 1 — Your pgmpy PRs, taught from the actual code

## 1.0 — Essential pgmpy context

pgmpy is a Python library for **causal and probabilistic reasoning with graphical models.** It implements:

- **Bayesian Networks** (DAG + CPDs encoding a joint distribution)
- **Markov Networks**, **Dynamic Bayesian Networks**, **Structural Equation Models**
- **Causal discovery** (PC, FCI)
- **Parameter learning** (MLE, Bayesian, EM)
- **Inference** (Variable Elimination, Belief Propagation, sampling)
- **Simulation**

It ships with example models (`asia`, `alarm`, `sachs`, `cancer`, `earthquake`, `arth150`, `ecoli70`) and example datasets for benchmarking causal discovery. These live in companion HuggingFace repos: `pgmpy/example_models` and `pgmpy/example_datasets`.

**What is `skbase`?** A meta-framework extracted from `sktime`. Provides:
- `BaseObject` — base class with parameter management, tag system, sklearn compatibility
- `skbase.lookup.all_objects` — reflection-based function that walks a package's modules and returns classes inheriting from a given base, with optional tag filtering

pgmpy adopted skbase to align with the broader scientific Python ecosystem.

---

## 1.1 — The honest three-act story (your main narrative)

Your three PRs form a clean evolution. **Tell it in this order. Do not say "before my work" for anything — you built the whole system.**

**Act 1 — PR #2347 (Sept–Dec 2025):** You built the **first** unified dataset loading system for pgmpy. It used a custom `DATASET_REGISTRY` plus a `register_dataset_class` function that contributors called to register a dataset.

**Act 2 — PR #2515 (Dec 2025–Jan 2026):** After design discussions in issues **#2506 and #2512**, you **refactored your own earlier registry** into skbase-based auto-discovery. `_BaseDataset` now inherits from `skbase.base.BaseObject`; `skbase.lookup.all_objects` discovers classes via introspection; tags became a class-level `_tags` dict.

**Act 3 — PR #2571:** You **extended the same pattern to example models**, seeded three example model classes (one per format: DAG via dagitty, continuous via JSON→LinearGaussianBN, discrete via BIF.gz), and other contributors have since added more models on top of your infrastructure.

This three-act framing is powerful because it shows:
- **Shipping** (Act 1)
- **Iterating on your own design without ego** (Act 2)
- **Building scaffolding that unblocks others** (Act 3)

---

## 1.2 — PR #2347: "Dataset loader" (your first pgmpy PR)

**Branch:** `Theavinash02:get_example_dataset`
**Merged:** Dec 15, 2025 by @ankurankan (43 commits, +791/-4 lines)
**Scope:** 12 files across `pgmpy/datasets/`, `extension_templates/`, tests, CI

### What it was

The **first implementation** of a unified dataset API for pgmpy. Before this PR, there was no standardized way to list or load example datasets programmatically. You built:

- `_BaseDataset` — abstract base class with a contract every dataset implements
- `DATASET_REGISTRY` — dict mapping dataset names to their classes
- `register_dataset_class(cls)` — the function contributors called to register a dataset
- `load_dataset(name)` — public API that looks up the class in `DATASET_REGISTRY`
- Initial dataset classes (`_abalone.py`, `_adult.py`, `_airfoil.py`, `_algeria.py`, `_sachs.py`) — files underscore-prefixed
- `extension_templates/_dataset.py` — a template for future contributors
- pytest tests validating the loading workflow
- CI updates (`lint.yml` Python 3.11 → 3.12, `pyproject.toml` adding an `[all]` extras group)

### How contributors used it

1. Create `_mydataset.py` in `pgmpy/datasets/`
2. Subclass `_BaseDataset`, set metadata
3. Call `register_dataset_class(MyDataset)` — the manual step
4. `load_dataset("mydataset")` looks up the name and returns the dataset

### Why this is a real contribution

- Introduced an API pattern that didn't exist before (inspired by sklearn's `load_iris`)
- Set up HuggingFace Hub as dataset backend (`repo_id = "pgmpy/example_datasets"`)
- Seeded 5 concrete dataset implementations
- Shipped CI and extension templates for future contributors

### Math content: **zero.**
Pure software engineering — class design, file I/O, registry pattern, module organization.

### Likely follow-up: "Why 43 commits?"
Normal for a new subsystem PR — reviewer feedback, integration, CI, test iteration, style fixes. Open source iterates publicly.

---

## 1.3 — PR #2515: skbase refactor (your strongest engineering story)

**Branch:** `Theavinash02:Refactor-BaseDataset-to-scikit-base-BaseObject`
**Merged:** Jan 16, 2026 by @ankurankan (5 of your commits + 4 maintainer follow-ups, +794/-462 lines)
**Closes:** issues #2506 and #2512
**Reviewers:** @fkiraly (skbase maintainer) approved; @ankurankan merged

### What it was

You **refactored your own earlier `DATASET_REGISTRY`** from PR #2347 into skbase-based auto-discovery. This is the PR that shows real engineering judgment — accepting a better abstraction over your own prior design after maintainer discussion.

### The before/after (be precise)

**Before (your own PR #2347):** Contributors called `register_dataset_class(MyDataset)`. Forgetting the call was a silent failure. Adding a dataset touched multiple files.

**After (PR #2515):**
- `_BaseDataset(BaseObject)` — inherits from `skbase.base.BaseObject`
- Each dataset class declares metadata via a `_tags` class attribute
- `list_datasets(**filter_tags)` — implemented via `skbase.lookup.all_objects`; walks `pgmpy.datasets`, imports modules, finds subclasses, filters by tag
- `load_dataset(name)` — uses `all_objects` to find the class by its `name` tag
- Dataset files **renamed from `_abalone.py` to `abalone.py`** — skbase's scanner ignores underscore-prefixed (private) modules
- Extension template moved to new location
- Tests updated for the new workflow

### The actual `_tags` dict from your code

```python
_tags = {
    "name": None,
    "n_variables": None,
    "n_samples": None,
    "has_ground_truth": False,
    "has_expert_knowledge": False,
    "has_missing_data": False,
    "has_index_col": False,
    "is_simulated": False,
    "is_interventional": False,
    "is_discrete": False,
    "is_continuous": False,
    "is_mixed": False,
    "is_ordinal": False,
}
```

Every concrete dataset overrides these. `AbaloneContinuous` sets `is_continuous=True`; `Adult` sets `is_mixed=True` with ordinal variables for education and income; `sachs_discrete` sets `is_discrete=True, has_ground_truth=True`.

### The actual `list_datasets` from your code

```python
def list_datasets(**filter_tags) -> list[str]:
    valid_tags = set(_BaseDataset._tags.keys())
    if invalid_tags := set(filter_tags.keys()) - valid_tags:
        raise ValueError(
            f"Unrecognized filter argument(s): {sorted(invalid_tags)}."
        )

    all_datasets = all_objects(
        object_types=_BaseDataset,
        package_name="pgmpy.datasets",
        return_names=False,
        filter_tags=filter_tags,
    )
    return sorted(
        cls.get_class_tag("name") for cls in all_datasets
        if cls.get_class_tag("name") is not None
    )
```

Design highlights worth name-dropping:
- Validates filter tags against the known set (prevents silent bugs from typos)
- Delegates discovery entirely to skbase
- Returns sorted names for reproducibility

### The mixins you wrote

Three mixin classes for different dataset formats:

- **`_CovarianceMixin`** — for datasets distributed as covariance matrices (goldberg, spartina, lead, cities). Reads the matrix file and samples from a multivariate Gaussian. **This is the only place your code does real math** (see Section 1.6).
- **`_TubingenBenchmarkMixin`** — for the Tübingen cause-effect benchmark (108 pairs). Each pair is separate files; `load_dataframe(pair_id)` and `load_ground_truth(pair_id)` accept IDs 1–108.

### The expert knowledge parser you wrote

Nontrivial. `_parse_expert_knowledge` handles a domain-specific text format with three section types:

- `addtemporal` — temporal order of variables
- `forbiddirect` — edges forbidden in the causal DAG
- `requiredirect` (also accepts `requireddirect`) — edges that must be present

You wrote a state-machine parser that tracks the current section, strips line numbers from temporal lines, handles empty temporal entries (just a digit), and returns an `ExpertKnowledge` object. This is real parser engineering, not just `open()` and `split()`.

### Why this refactor was architecturally superior

- **Convention over configuration**: inherit from `_BaseDataset`, set `_tags`, done. No registry call.
- **Impossible to forget registration**: adding a subclass auto-registers via introspection.
- **Filterable**: `list_datasets(is_discrete=True, has_ground_truth=True)` → `['sachs_discrete']`.
- **Ecosystem alignment**: pgmpy now follows the same pattern as sktime, skpro, skchange.

### The fkiraly review — your behavioral-interview gold

The PR conversation is worth rehearsing as a **STAR story for "tell me about a time a reviewer pushed back"**:

> "In PR #2515, my reviewer @fkiraly — who is actually one of the skbase maintainers — initially thought I had removed the registry lookup entirely without replacement. He wrote: 'one thing that gets removed, not replaced, is the registry lookup — is this intentional, or an oversight?'
>
> I replied that I had removed the custom `DatasetRegistry` class because we were replacing the manual registry mechanism with `skbase.lookup.all_objects` for dynamic discovery. I pointed him to the new `list_datasets` function in `_base.py` that wraps `all_objects` with tag filtering, and explained that `load_dataset` now uses `all_objects` internally to find the correct class by its `name` tag.
>
> He came back with 'Ah, I overlooked `list_datasets`. Great!' and approved the PR. Then @ankurankan merged it and added four follow-up commits of his own — categorical and ordinal variable support and a filtering option on `list_datasets`.
>
> What I took from that: in open source, reviewers sometimes miss parts of a large PR. The right response is to clarify with specific references — file paths, function names — rather than get defensive. And the fact that the maintainer then built on top of my code rather than rewriting it meant the architecture was sound."

This is a gold answer for any "tell me about disagreement" / "how do you handle feedback" question.

### Likely follow-up questions

**Q: What does `all_objects` actually do?**
Walks the package's module hierarchy using Python's import machinery, inspects each module for classes, returns those inheriting from the target base class, filters by tag if specified.

**Q: Why not `__subclasses__()`?**
`__subclasses__()` only finds classes that have been imported at least once. Passive discovery fails unless you import everything eagerly. `all_objects` walks the package namespace and imports modules explicitly, so discovery is deterministic and complete.

**Q: Why rename files from `_abalone.py` to `abalone.py`?**
skbase's module scanner, following Python convention, treats leading-underscore modules as private and skips them. Underscore-prefixed files wouldn't be scanned, so their dataset classes wouldn't be discovered.

**Q: Your earlier design in #2347 worked — why replace it?**
It worked, but manual registration doesn't scale. Every new dataset required editing multiple files, and forgetting a registration was a silent failure. Inheritance-based auto-discovery removes that class of bug entirely. Plus aligning with skbase gave pgmpy consistency with the rest of the scientific Python ecosystem.

**Q: What did you break?**
Public API stayed compatible — `list_datasets()` and `load_dataset()` signatures are the same. Internally, the registry disappeared and tag access migrated from `cls.tags[key]` to `cls.get_class_tag(key)`. pytest caught breakages early.

**Q: What are `_tags`?**
Class-level dictionary of metadata describing what the dataset is. Used by `all_objects` for filtering and can be used by tests for parametrization.

---

## 1.4 — PR #2571: Example models registry (same pattern, new target)

**Closes:** issue #2551
**Scope:** `pgmpy/example_models/` — `_base.py`, `__init__.py`, three seed model classes

### What it was

You applied the PR #2515 skbase discovery pattern to **example models**. Example models are predefined Bayesian networks (structure + often CPDs) — `alarm`, `asia`, `arth150`, etc. Different from datasets, which are tabular data.

### What you actually built

- `_BaseExampleModel(BaseObject)` — base class with tags: `name`, `n_nodes`, `n_edges`, `is_parameterized`, `is_discrete`, `is_continuous`, `is_hybrid`
- Four mixin classes for different file formats:
  - **`DiscreteMixin`** — gzipped BIF via `BIFReader(gzip.decompress(...))` → `DiscreteBayesianNetwork`
  - **`BIFMixin`** — plain BIF via `BIFReader` → `DiscreteBayesianNetwork`
  - **`ContinuousMixin`** — JSON via `LinearGaussianBayesianNetwork.load(file_obj)`
  - **`DAGMixin`** — dagitty string via `DAG.from_dagitty(...)` (structure only, no CPDs)
- `load_model(name)` and `list_models(**filter_tags)` — mirror the dataset API
- **Three seed model classes** as examples:
  - `Acid_1996` DAG via `DAGMixin`
  - `arth150` continuous BN via `ContinuousMixin`
  - `alarm` discrete BN via `DiscreteMixin`

### What you did NOT do (be honest)

- Did not write the test file for example models — other contributors added that
- Did not add the full catalog of models — you seeded three, others extended
- Did not write `BIFReader`, `DAG.from_dagitty`, or `LinearGaussianBayesianNetwork.load` — those existed. You delegated to them from the mixins.

### "I built the scaffolding, others extended it" — an underrated angle

From your own words:

> "For the example models PR, I built the registry infrastructure and three seed models showing the pattern — one for each format: discrete BIF, continuous JSON, and DAG dagitty. Other contributors then used my base class to add many more models. That's actually one of the outcomes I'm proudest of — my work unblocked a broader contribution pipeline."

**Say exactly that.** Unblocking others is bigger impact than a single feature — and it's a maturity signal.

### Math content: **zero.**
Class design + delegation to existing parsers.

---

## 1.5 — The "Top 13 contributor" framing (discussion #3270)

Your resume mentions top-13 in pgmpy v1.1.0. That release had many contributions — new algorithms, bug fixes, docs, infrastructure. Yours were **infrastructure-level** — dataset and example-model registries — which is often undercredited but genuinely valuable.

If asked "what's your most significant contribution?", lead with **PR #2515**. Shows iteration, maintainer collaboration, and engineering judgment.

---

## 1.6 — The one piece of real math in your code

I audited every file you shared. There is exactly one place your code does something mathematical beyond file I/O and metadata:

From `_CovarianceMixin` in `datasets/_base.py`:

```python
@classmethod
def load_dataframe(cls) -> pd.DataFrame:
    cov_matrix = cls._load_covariance_matrix()
    mean = [0] * cls.get_class_tag("n_variables")
    data = pd.DataFrame(
        np.random.multivariate_normal(
            mean, cov_matrix.values,
            size=cls.get_class_tag("n_samples")
        ),
        columns=cov_matrix.columns,
    )
    return data
```

### What this is doing mathematically

Some datasets (goldberg, spartina, lead, cities) are distributed as **only the covariance matrix**, not raw data — because they come from published causal inference papers. To produce usable samples, you draw from a **multivariate Gaussian**:

**X ~ N(0, Σ)**

where Σ is the covariance matrix and 0 is the zero mean vector.

### What you had to understand to write this correctly

1. A **covariance matrix** is symmetric positive semi-definite; entry Σᵢⱼ = Cov(Xᵢ, Xⱼ)
2. The file stores **only the upper triangular** (space-saving convention); you reconstruct the full symmetric matrix by mirroring:
   ```python
   mat[i, :i+1] = vals
   mat[:i+1, i] = vals
   ```
3. Sampling from `N(0, Σ)` gives synthetic data with the specified dependence structure — crucial for benchmarking causal discovery, which operates on the covariance structure
4. Zero mean is fine because causal discovery algorithms are typically scale/mean invariant — they work on correlations, not absolute values

### How to talk about this in interview

> "There's one place in my code that touches real probability — for datasets distributed as covariance matrices rather than raw data, I wrote a `_CovarianceMixin` that samples from a zero-mean multivariate Gaussian with the given covariance structure. The sampling itself uses `np.random.multivariate_normal`, but I had to understand the file format — which stores only the upper triangular — and reconstruct the full symmetric matrix. I also had to understand why zero mean is acceptable, which is because causal discovery algorithms are typically scale and mean invariant. Beyond that single spot, my code is infrastructure."

Better than claiming zero math — shows you engage with math when required.

---

# Part 2 — pgmpy math essentials (user-level understanding)

**Framing:** you didn't implement these — but you need to understand them at a **user level** to explain what pgmpy does and why your infrastructure matters. Treat this as "I understand the domain my work operates in," not "I implemented these."

## 2.1 Bayesian Networks — definition

A Bayesian Network is `(G, P)` where G is a DAG over random variables and P is a set of CPDs — one per node — giving `P(Xᵢ | Parents(Xᵢ))`.

Joint distribution factorizes:
```
P(X₁, ..., Xₙ) = ∏ᵢ P(Xᵢ | Parents(Xᵢ))
```

**Why it matters:** naively, joint over n binary vars needs 2ⁿ − 1 parameters. With BN structure, it's the sum of local CPD sizes — exponentially smaller for sparse graphs.

### The Asia network (ships with pgmpy)

Nodes: `asia, tub, smoke, lung, bronc, either, xray, dysp`

Joint factorizes as:
```
P(asia) · P(smoke) · P(tub|asia) · P(lung|smoke) · P(bronc|smoke) ·
P(either|tub,lung) · P(xray|either) · P(dysp|either,bronc)
```

8 local CPDs instead of one 256-cell joint.

## 2.2 CPDs

Discrete CPDs use `TabularCPD`:

```python
cpd_cancer = TabularCPD(
    variable="Cancer", variable_card=2,
    values=[[0.03, 0.05, 0.001, 0.02],
            [0.97, 0.95, 0.999, 0.98]],
    evidence=["Smoker", "Pollution"],
    evidence_card=[2, 2],
)
```

Each column = one combination of parent states; columns sum to 1.

## 2.3 D-separation

**Chain: A → B → C** — A and C dependent; given B, independent (B blocks).

**Fork: A ← B → C** — A and C dependent (common cause); given B, independent.

**Collider: A → B ← C** — A and C independent unconditionally; given B (or any descendant), they become dependent. **"Explaining away."**

Classic example: Rain and Sprinkler both cause Wet Grass. Marginally independent. Observing Wet Grass + Sprinkler → belief in Rain decreases.

## 2.4 Inference algorithms pgmpy ships

- **Variable Elimination (VE)** — exact, depends on elimination order (finding optimal order is NP-hard; pgmpy uses heuristics)
- **Belief Propagation** — exact for tree-structured graphs
- **Sampling** — approximate: forward, likelihood weighting, Gibbs/MCMC

Exact inference in general BNs is NP-hard → approximate methods for dense networks.

## 2.5 Parameter learning

- **MLE**: `P̂(X=x | Parents=u) = count / count`. Overfits on small data (zero counts break inference)
- **Bayesian with Dirichlet prior**: adds pseudo-counts, regularizes
- **BDeu**: uniform pseudo-counts scaled by `equivalent_sample_size`
- **EM** for latent variables

## 2.6 Structure learning

- **Score-based**: BIC, K2, BDeu + search (hill-climbing, tabu)
- **Constraint-based**: PC algorithm uses CI tests (χ² for discrete, Pearson for continuous)
- **Hybrid**: MMHC

## 2.7 Interview Q&A on pgmpy math

**Q: What is a Bayesian Network?**
A DAG over random variables where each node has a CPD giving its distribution conditional on its parents. The DAG encodes conditional independencies, letting the joint factorize into local CPDs — reducing parameter count from exponential to sum of local tables.

**Q: Why Bayesian estimator over MLE?**
MLE assigns zero probability to unseen events, breaking inference. Dirichlet prior with pseudo-counts regularizes — unseen states get small but non-zero probability. `equivalent_sample_size` controls prior strength.

**Q: Structure learning vs causal discovery?**
Structure learning recovers a DAG consistent with the data's CI structure — but multiple DAGs share the same CI (Markov equivalence class). Causal discovery tries to identify the specific causal DAG, which needs additional assumptions (faithfulness, no hidden confounders).

**Q: Did you implement any of these?**
No — my work is infrastructure. Dataset and model registries. The algorithms are implemented by other contributors. I understand them at the level needed to build tools for them.

---

# Part 3 — Bitcoin Ransomware Detection (from your actual notebook)

> **This section is rewritten from your actual `bitcoin_ransomware.ipynb`. Earlier versions of this doc claimed `class_weight='balanced'` and "stratified split" — your code shows neither of those. Corrected here.**

## 3.1 — What your code actually shows

```python
X = df[['year', 'day', 'length', 'weight', 'count', 'looped', 'neighbors', 'income']]
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier()   # all defaults — 100 estimators, no class_weight
clf.fit(X_train, y_train)
```

Plain vanilla — no class_weight, no stratification, no hyperparameter tuning, no SMOTE.

## 3.2 — The data facts (honest)

- **2,916,697 addresses** total
- **29 unique labels** — 28 ransomware families + `white` (benign). Your resume says "29 ransomware families" — slightly off (actual: 28). If pressed, say "around 29 labels in the dataset, the majority being benign." Don't get into counting debates.
- **Severe class imbalance**: 2,875,284 out of 2,916,697 are `white` → **98.6% benign**
- Some families have fewer than 10 samples in the full dataset (montrealComradeCircle: 1, montrealSam: 1, montrealXLocker: 1)

## 3.3 — Features: code has 8, resume lists 6

**In your code:** `year, day, length, weight, count, looped, neighbors, income` (8 features)

**On your resume:** `length, weight, count, looped, neighbors, income` (6 features)

**Strategy:** Lead with the 6 on your resume. If asked to name all features, say: *"The 6 transaction-graph features listed on my resume, plus `year` and `day` as temporal context — 8 total."*

## 3.4 — Features explained (all 8)

| Feature | Type | What it captures |
|---|---|---|
| `length` | int | Length of the transaction chain |
| `weight` | float | BTC flow (fraction from a single source) |
| `count` | int | Number of transactions at the address |
| `looped` | binary (0/1) | Whether coins were sent back to source |
| `neighbors` | int | Distinct addresses transacted with |
| `income` | float | Total BTC received |
| `year` | int | Year of transaction (temporal) |
| `day` | int | Day of year 1–365 (temporal) |

## 3.5 — Model (what you actually used)

- `RandomForestClassifier()` with **all scikit-learn defaults** (100 estimators, gini criterion, no class_weight, no max_depth limit)
- `train_test_split(test_size=0.2, random_state=42)` — **not stratified**
- Training ran to completion; model saved with `joblib.dump` as `model.pkl`

## 3.6 — What "addressing class imbalance" actually means in your work

**Your code did NOT:**
- Use `class_weight='balanced'`
- Apply SMOTE or other oversampling
- Use stratified sampling
- Tune any hyperparameters

**Your code DID:**
- Call `df['label'].value_counts()` — saw the 2.87M vs ~40K split clearly
- Use `classification_report` on test predictions — got per-class precision/recall/F1
- Observe that macro F1 = 0.13 while weighted F1 = 0.99 — exposed the imbalance
- Identify which families the model learned (5) vs didn't (23)

**The honest framing:**

> "I addressed class imbalance by using per-class metrics — precision, recall, F1 via `classification_report` — instead of relying on accuracy, which would have been misleading. This revealed that the model learned the majority benign class and a handful of the larger ransomware families, but struggled on rare families with few samples. The observation was the extent of the handling in the scope of this final year project."

This is **honest and defensible.** Awareness is the first step. Don't overclaim by saying you used SMOTE or class weights — you didn't.

## 3.7 — The 60-second pitch (resume-scoped, code-honest)

> "This was my B.Tech final year project at Anna University, done between January and May 2024. I built a machine learning model to classify Bitcoin addresses as benign or linked to ransomware, using the UCI BitcoinHeist dataset — about 2.9 million addresses.
>
> I trained a Random Forest classifier using scikit-learn. The features were transaction-graph derived — length, weight, count, looped, neighbors, income — with year and day as temporal context. I used an 80/20 train/test split with a fixed random state.
>
> The main ML challenge was class imbalance — over 98% of addresses are benign. I addressed this by using per-class precision, recall, and F1 metrics instead of relying on accuracy, which would have been misleading. That let me analyze prediction behavior across ransomware categories and see which families the model learned well versus which remained hard because of low sample counts.
>
> I chose Random Forest because it handles non-linear feature interactions, gives feature importance out of the box, and doesn't require heavy hyperparameter tuning — a good fit for a 2.9 million row tabular dataset."

## 3.8 — Interview Q&A (honest-code version)

**Q: Walk me through it.**
Use the 60-second pitch.

**Q: Why Random Forest?**
Non-linear interactions, robust to outliers, gives feature importance for interpretability, less tuning than gradient boosting, variance reduction via ensemble averaging.

**Q: How did you handle class imbalance?**
Use the honest framing from 3.6:
> "I addressed it by using per-class metrics — precision, recall, F1 — instead of accuracy, so I could see the model's behavior per family. Looking at macro F1 versus weighted F1 exposed that the model was learning the majority class and a few big families but not the rare ones. In this project I didn't apply SMOTE or class weights — the observation was the scope."

**Q: Did you use `class_weight='balanced'`?**
Honest:
> "No, I used default RandomForestClassifier parameters. I didn't apply weighted training in this project — something I'd try in a follow-up along with SMOTE."

**Q: Did you stratify your split?**
Honest:
> "No — I used a plain 80/20 split with a fixed random state. With 2.9 million rows the class ratios come out roughly preserved, but stratified sampling would have been a cleaner choice."

**Q: What features did you use?**
> "Six transaction-graph features — length, weight, count, looped, neighbors, income — plus year and day as temporal context, so eight total."

**Q: What was your accuracy?**
> "About 99%. But that's a misleading headline on this dataset — over 98% of addresses are benign, so a majority-class predictor would score similarly. The more informative metric is per-class behavior, which showed the model learned the large classes well and struggled on the rare families."

**Q: How would you improve it?**
Three standard directions:
1. Try gradient boosting (XGBoost / LightGBM) — often handles imbalance better
2. Apply SMOTE or similar oversampling for rare families
3. Use stratified sampling and class weights
Keep it short — this was an FYP, it's done.

**Q: Why not a neural network or graph neural network?**
Overkill for 8 tabular features, loses interpretability. A GNN on the raw transaction graph could capture more structure than summary features, but that's a different project scope.

**Q: What were the biggest limitations?**
> "The model is effectively a binary classifier in practice — benign versus one of the larger ransomware families. Families with fewer than a few hundred samples weren't learned at all. That's an artifact of the dataset distribution and wasn't something a standard Random Forest was going to solve on its own."

---

# Part 4 — LoRA / Phi-3 fine-tuning project (code-accurate, rehearsed)

> **This section is rewritten from the actual notebook you shared. Corrects earlier cram-pack assumptions about alpha and dropout. Also incorporates the two real issues you observed and your resume's "analyzed output inconsistencies" framing.**

## 4.1 — Your exact stack and config

- **Environment:** Google Colab, Tesla T4 GPU (14.7 GB VRAM), free tier
- **Base model:** `unsloth/Phi-3-mini-4k-instruct` — Microsoft's 3.8B parameter decoder-only model (32 layers, hidden 3072, FFN 8192, RMSNorm, SiLU, rotary embeddings). Unsloth patches it as `MistralForCausalLM` because Phi-3-mini uses Mistral-style blocks.
- **Loaded in 4-bit** via `FastLanguageModel.from_pretrained`, `max_seq_length = 2048`
- **Dataset:** `pdx97/Schema_Based_Instruction_Dataset` — 360 math word problems labeled with Schema (Additive, Multiplicative, …) and Sub-Category (Total, Ratios/Proportions, …). Split 90/10 → **324 train / 36 eval**.
- **Prompt template:** Alpaca-style with `### Problem:` and `### Response:` sections

## 4.2 — Your LoRA config (memorize this exactly)

```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj"],
    lora_alpha = 16,          # scaling factor α/r = 1.0
    lora_dropout = 0,
    bias = "none",
    use_gradient_checkpointing = True,
    random_state = 42,
)
```

**Trainable parameters:** **29,884,416 of 3,850,963,968 = 0.78%.** This is your headline number.

## 4.3 — Your training setup

```python
per_device_train_batch_size = 2
gradient_accumulation_steps = 8      # effective batch = 16
max_steps = 50                        # ~3 epochs over 324 examples
learning_rate = 3e-4
warmup_steps = 5
optim = "adamw_8bit"                  # 8-bit AdamW for memory
eval_steps = 10
```

Training completed in ~220 seconds via `trl.SFTTrainer`.

## 4.4 — The two issues you observed (OWN THESE)

Your resume says you *"evaluated model performance on unseen inputs and analyzed output inconsistencies for further refinement."* Here's what that actually means:

**Issue 1 — Training loss collapsed to ~2.44e-08.**
A loss at 10⁻⁸ means the model is predicting target tokens with probability ~1.0. Red flag for **overfitting** — the output space is tiny (only a handful of Schema/Sub-Category combinations), so at LR 3e-4 with no dropout, the model memorized it in ~50 steps.

**Issue 2 — Generation on a test prompt was empty.**
After fine-tuning, the model produced nothing after `### Response:`. Likely causes: (a) overfitting collapsed generation behavior, (b) the template's trailing whitespace with no explicit EOS token trained the model to emit EOS immediately.

**You flagged both in the notebook.** That's the mature read — not a failure, a diagnosis.

## 4.5 — The 60-second pitch (memorize this)

> "This was a learning project to understand LoRA fine-tuning end-to-end. I fine-tuned Phi-3-mini — Microsoft's 3.8 billion parameter model — using Unsloth with 4-bit quantization to fit it on a Colab T4 with 14 GB of VRAM. The task was structured output generation: mapping math word problems to a Schema label like Additive or Multiplicative, and a Sub-Category label like Total or Ratios.
>
> I configured LoRA at rank 16 with alpha 16, targeting both attention projections — q, k, v, o — and the feedforward projections — gate, up, down. That trained only 0.78% of the parameters, about 30 million out of 3.85 billion. I used the trl library's SFTTrainer for the supervised fine-tuning with an Alpaca-style prompt template, effective batch size 16 via gradient accumulation, and AdamW-8bit to save optimizer memory.
>
> When I evaluated on unseen inputs, I observed output inconsistencies — specifically, the training loss collapsed to near-zero, which signaled overfitting on the small output space, and generation on a test prompt came out empty. I flagged both as needing refinement. The fixes I'd apply next are a lower learning rate, adding lora_dropout for regularization, early stopping on eval loss, and cleaner EOS handling in the template."

## 4.6 — The 30-second version (if they cut you off)

> "I fine-tuned Phi-3-mini using LoRA via Unsloth with 4-bit quantization, on a structured output task — mapping math problems to Schema and Sub-Category labels. Rank 16 adapter on attention and FFN layers, about 0.78% of parameters trained. I used SFT via trl's SFTTrainer. On evaluation I observed output inconsistencies — training loss collapsed indicating overfitting, and generation came out empty on test prompts — which I flagged for further refinement."

## 4.7 — Resume line → what you say

| Resume line | What you say |
|---|---|
| *"Fine-tuned an instruction-based LLM (Phi-3-mini) using LoRA and SFT"* | "Phi-3-mini is Microsoft's 3.8B decoder-only model. I used the Unsloth-optimized version. SFT means supervised fine-tuning — training on (input, expected-output) pairs with cross-entropy, as opposed to reward-based methods like RLHF or DPO." |
| *"Trained the model to map natural language inputs to Schema and Sub-category labels"* | "Dataset was `pdx97/Schema_Based_Instruction_Dataset` — 360 math word problems labeled with Schema (Additive/Multiplicative) and Sub-Category (Total/Ratios). 90/10 train/eval split." |
| *"Designed custom prompt templates"* | "Alpaca-style template with an instruction preamble, `### Problem:` for input, and `### Response:` containing `Schema:` and `Sub-Category:` fields. Trains the model to produce output in that exact structure." |
| *"Applied parameter-efficient fine-tuning using Unsloth with 4-bit quantization"* | "Unsloth accelerates LoRA via custom Triton kernels — roughly 2× faster than vanilla transformers+peft. 4-bit quantization shrinks the frozen base ~4× vs fp16 — required to fit Phi-3 on a T4's 14 GB." |
| *"Configured LoRA adapters on attention and feedforward layers"* | "Rank 16, alpha 16 — scaling factor 1.0. q/k/v/o for attention, gate/up/down for FFN. Attention controls what the model attends to; FFN stores most of the task-specific knowledge. Covering both gives the adapter the most expressive capacity per parameter." |
| *"Evaluated model performance on unseen inputs and analyzed output inconsistencies for further refinement"* | "I tested on held-out prompts and observed two issues. First, training loss dropped to around 10⁻⁸, which indicates severe overfitting — the output space was small, with only a few unique label combinations, so the model memorized it. Second, generation on a test prompt produced empty output, which I diagnosed as a combination of overfitting and the template lacking explicit EOS token handling. I flagged both for further refinement." |

## 4.8 — Interview Q&A

**Q: Why alpha = 16 and not 32?**
I matched alpha to rank, so the scaling factor α/r is 1.0 — a common default where the adapter contributes at natural magnitude without dampening or amplification. Higher alpha would amplify the adapter's effect.

**Q: Why target both attention and FFN?**
Attention projections learn what to attend to; FFN layers store most of the model's knowledge. Adapting only attention limits how much task-specific information the adapter can encode. Covering q, k, v, o, gate, up, down gives the most expressive capacity per parameter.

**Q: Why 4-bit quantization?**
To fit on a T4's 14 GB. Phi-3-mini in fp16 is ~7.6 GB for weights alone, plus activations, gradients, and optimizer state. 4-bit shrinks the frozen base model ~4× — leaving room for LoRA training.

**Q: Your training loss was 10⁻⁸ — is that good?**
No, it's a red flag. It indicates overfitting — the model memorized the small output space. Realistic SFT runs show loss decreasing to somewhere around 0.1–1.0 and stabilizing, not collapsing to zero.

**Q: Your test output was empty — what's wrong?**
I flagged that as needing debugging. Hypothesis: aggressive overfitting collapsed generation behavior, and the template had trailing blank lines with no explicit EOS — so the model may have learned to predict EOS immediately after `### Response:`.

**Q: So did the model actually work?**
It didn't generalize well. This was a learning project — I set up the pipeline end-to-end, but output quality wasn't production-ready. I took away concrete understanding of what overfitting looks like in a fine-tuning context and how template design affects generation.

**Q: What would you do differently next time?**
Four fixes: (1) lower learning rate from 3e-4 to 1e-4, (2) add `lora_dropout = 0.05` for regularization, (3) use eval_loss-based early stopping instead of fixed max_steps, (4) clean up the template with explicit EOS token handling.

**Q: What is `gradient_accumulation_steps` doing?**
Accumulates gradients over multiple forward passes before the optimizer step. I used batch 2 × grad_accum 8 → effective batch 16 — necessary because the T4 can't fit batch 16 directly. Trades wall-clock time for fitting in limited VRAM.

**Q: Why `adamw_8bit`?**
Standard AdamW stores momentum and variance in fp32 — 8 bytes per param. On 30M trainable params that's ~240 MB just for optimizer state. `adamw_8bit` from bitsandbytes quantizes to 8-bit, saving ~75% of that with negligible quality impact.

**Q: SFT vs RLHF vs DPO?**
SFT trains on (prompt, response) pairs with cross-entropy — imitation learning. RLHF trains a reward model on preference pairs, then optimizes the LM with PPO. DPO skips the reward model — directly optimizes the LM on preference pairs with a clever loss. Typical pipeline: pretrain → SFT → DPO/RLHF.

**Q: Why scale attention by √d_k?**
Without scaling, dot products grow with dimension, pushing softmax into saturated regions with tiny gradients. Dividing by √d_k keeps variance roughly unit, so gradients flow.

## 4.9 — Strategic framing note

Your resume phrase *"analyzed output inconsistencies for further refinement"* is well-written — it's honest and professional. **Don't walk it back in the interview.** Observing problems, analyzing them, and identifying refinement needs is what real ML engineering looks like. An interviewer who has run fine-tuning jobs will respect the honesty; one who hasn't won't push. Either way you win.

---

# Part 5 — Rapid-reference "tell me about your PRs" answer (60-second version)

Memorize this. Correct, honest, three-act:

> "I have three pgmpy contributions that form a clean evolution. My first PR, #2347, introduced a unified dataset loading API — pgmpy didn't have a standardized way to list or load example datasets. I built `_BaseDataset`, a `DATASET_REGISTRY`, and a `register_dataset_class` function, seeded with five concrete datasets.
>
> After design discussions in issues #2506 and #2512, we decided the manual registry wouldn't scale well. PR #2515 was the refactor: I replaced my own earlier registry with skbase-based auto-discovery. `_BaseDataset` now inherits from `skbase.base.BaseObject`, tags became class attributes, and `skbase.lookup.all_objects` handles discovery via introspection. The skbase maintainer fkiraly reviewed and approved.
>
> PR #2571 extended the same pattern to example models — I built the registry infrastructure and three seed model classes, one per format, and other contributors have since added more models on top. My work is infrastructure-level — I didn't implement inference or learning algorithms. Those are by other contributors. What I built is the scaffolding that makes the library easier to use and extend."

Practice until natural. Aim 60–75 seconds. Key line: **"I replaced my own earlier registry"** — shows iteration and non-attachment.

---

# Final checklist

- [ ] I can explain what a Bayesian Network is in 2 sentences
- [ ] I can draw chain/fork/collider and explain d-separation
- [ ] I can explain why MLE can fail and why Dirichlet prior helps
- [ ] I can name 4 example BNs that ship with pgmpy (alarm, asia, sachs, arth150)
- [ ] I can tell the three-act PR story in under 90 seconds without saying "before my work"
- [ ] I can name skbase's key components: BaseObject, all_objects, tags
- [ ] I can explain why files were renamed from `_abalone.py` to `abalone.py`
- [ ] I have the fkiraly review story ready for "tell me about disagreement"
- [ ] I can explain the one piece of math (multivariate Gaussian from covariance)
- [ ] I can walk through Bitcoin in 60 seconds (resume-scoped)
- [ ] I know my code used **default RandomForestClassifier()** — no class_weight, no tuning
- [ ] I know my split was **plain 80/20, NOT stratified**
- [ ] I know my code used **8 features** (6 on resume + year + day)
- [ ] I have the honest "addressed imbalance via per-class metrics" answer (not SMOTE or class_weight)
- [ ] I will NOT volunteer the Flask app, live demo, or v2 roadmap — FYP is done
- [ ] If asked "how would you improve it?", short generic answer: XGBoost, SMOTE, stratified sampling
- [ ] I know my LoRA config exactly: **r=16, alpha=16, dropout=0, 7 target modules**
- [ ] I know my trainable percentage: **0.78%** (~30M of 3.85B)
- [ ] I know my dataset: **pdx97 Schema_Based_Instruction_Dataset, 324/36 split**
- [ ] I know the two output inconsistencies: **loss collapse to 10⁻⁸ + empty generation**
- [ ] I have 4 specific fixes ready: **lower LR, add dropout, early stopping, EOS in template**

---

# Key phrases to drop naturally

Spread across the interview — don't cluster:

- "Convention over configuration"
- "Inheritance-based auto-discovery"
- "Tag-based filtering"
- "Module introspection"
- "Reflection via `skbase.lookup.all_objects`"
- "Unblocked downstream contributors"
- "I didn't get attached to my first design"
- "Infrastructure-level contribution"
- "The math is implemented by other contributors; my work serves their algorithms"
- "Scale invariant" (for the covariance-to-sample mixin)

---

You are in a stronger position than most 36-hour preps allow. The code proves the story. Own it.
