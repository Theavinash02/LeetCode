# TCS Prime Interview Cram Pack — Avinash P
**Interview: Monday, 20 April 2026 | Chennai**

---

## How to use this pack

This is dense. Don't passively read. For each section:

1. Read the **Concepts** block once.
2. Cover the screen and **explain it out loud** as if I'm interviewing you.
3. Type out the **Code you must be able to write** on a blank editor — no copy-paste.
4. Read the **Interview Q&A** and rehearse answers in your own words.
5. Check the **Your Resume Angle** to know how to pivot back to your projects.

If you can't explain something out loud, you don't know it yet.

---

## 36-Hour Study Schedule

### Saturday (Today) — ~8 hours of focused study
| Time | Block | What |
|------|-------|------|
| Now — 2hr | **Probability & Statistics** | Highest risk. You claim pgmpy contributor. |
| +1hr break | Walk, food | |
| 2hr | **NumPy + Pandas** | Tie to Bitcoin project. |
| 1hr | **DSA Patterns — Part 1** | 2 problems: two-pointer + hash map. |
| Dinner | | |
| 2hr | **Transformers + Hugging Face** | Connect to LoRA/Phi-3 project. |
| 30min | Resume rehearsal | Read your own resume out loud. |
| **Sleep by 11pm.** | | |

### Sunday — ~8 hours of focused study
| Time | Block | What |
|------|-------|------|
| Morning 2hr | **SQL/RDBMS Deep Dive** | Execution plans, isolation, indexes. |
| 1hr | **DSA Patterns — Part 2** | Binary search + BFS/DFS. |
| 1hr | **Linear Algebra** | Fast pass. |
| Lunch | | |
| 2hr | **pgmpy + your PRs** | Re-read PRs 2347, 2515, 2571. Explain out loud. |
| 1hr | **Mock rapid-fire drill** | Ask Claude to grill you. |
| 1hr | STAR stories | skbase refactor, Fern bug, Go-Live, LoRA. |
| Evening | Logistics | Print 3 resumes. Plan commute. Iron clothes. |
| **Sleep by 10:30pm. No studying after dinner Sunday.** | | |

### Monday — Interview day
- Wake 2.5 hrs before interview. Light breakfast.
- Re-read this pack's **Interview Q&A sections only** (30 min).
- Leave 90 min early for Chennai traffic.
- Carry: 3 resumes, pen, ID, water.

---

# 1. NUMPY

## Concepts

NumPy provides the **`ndarray`** — an n-dimensional array stored as a contiguous block of memory with a single fixed dtype. This is why it's fast: no Python object overhead, operations run in compiled C, and CPU-level SIMD can vectorize them.

**Four things you must own:**

**Shape & dtype.** Every array has `.shape` (tuple of dimensions) and `.dtype` (e.g., `float64`, `int32`). Mismatched dtypes cause silent upcasts (`int + float → float`).

**Axis.** For a 2D array, `axis=0` moves down rows (collapses vertically across rows), `axis=1` moves across columns. Remember: **axis is the one being eliminated** by the operation. `arr.sum(axis=0)` on a `(3,4)` array gives a `(4,)` result.

**Broadcasting.** When shapes don't match, NumPy aligns them from the right and stretches dimensions of size 1. Rule: two dimensions are compatible if equal OR one of them is 1. Example: `(3,4) + (4,)` works — the `(4,)` is broadcast across each row. `(3,4) + (3,)` does NOT work — align from right, 4 ≠ 3.

**Views vs copies.** Basic slicing returns a **view** (shares memory). Fancy indexing (boolean or integer arrays) returns a **copy**. Modifying a view modifies the original. When in doubt, `.copy()`.

## Code you must be able to write

```python
import numpy as np

# Creation
a = np.array([[1, 2, 3], [4, 5, 6]])      # shape (2, 3)
z = np.zeros((3, 4))                       # 3x4 zeros
o = np.ones((2, 2))
r = np.arange(0, 10, 2)                    # [0, 2, 4, 6, 8]
lin = np.linspace(0, 1, 5)                 # 5 points between 0 and 1
rand = np.random.randn(3, 3)               # standard normal

# Shape manipulation
a.reshape(3, 2)
a.T                                         # transpose
a.flatten()                                 # to 1D

# Math — all vectorized
a + 10
a * 2
np.exp(a)
np.log(a + 1)

# Aggregations with axis
a.sum()              # scalar: sum of all
a.sum(axis=0)        # shape (3,): column sums
a.sum(axis=1)        # shape (2,): row sums
a.mean(axis=1)

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
A @ B                                       # matrix multiplication
np.dot(A, B)                                # same thing
np.linalg.inv(A)                            # inverse
np.linalg.eig(A)                            # eigenvalues, eigenvectors

# Boolean indexing
arr = np.array([1, 2, 3, 4, 5])
arr[arr > 2]                                # [3, 4, 5]

# Broadcasting example
matrix = np.ones((3, 4))
row_vec = np.array([1, 2, 3, 4])
matrix + row_vec                            # row_vec broadcast across 3 rows
```

## Interview Q&A

**Q: Why is NumPy faster than Python lists?**
Contiguous memory layout with fixed dtype means no per-element object overhead. Operations run in compiled C with SIMD vectorization, so a million-element addition is one C loop, not a million Python interpreter steps.

**Q: Explain broadcasting.**
A mechanism to apply element-wise ops on arrays of different shapes without making copies. NumPy aligns shapes from the right; dimensions are compatible if they're equal or one is 1. The size-1 dimension is stretched conceptually. Example: adding a bias vector of shape `(4,)` to a batch of shape `(32, 4)` works — the vector is applied to every row.

**Q: What's the difference between `arr.sum()` and `arr.sum(axis=0)`?**
`arr.sum()` returns a scalar — sum of all elements. `arr.sum(axis=0)` collapses along axis 0 (rows), returning an array where each element is the sum of a column.

**Q: View vs copy?**
Basic slicing like `arr[1:3]` returns a view that shares memory with the original — modifying it changes the original. Fancy indexing (boolean masks, integer arrays) returns a new copy. Use `.copy()` when you need independence.

**Q: How do you check if two arrays are equal?**
`np.array_equal(a, b)` for exact equality. `np.allclose(a, b)` for floating-point comparison with tolerance — always use this for floats.

## Your resume angle
"I used NumPy in the Bitcoin ransomware project for vectorized feature computation over transaction graph features — length, weight, count, neighbors, looped, income — across millions of Bitcoin addresses. Without vectorization, feature engineering would have been orders of magnitude slower."

---

# 2. PANDAS

## Concepts

Pandas gives you two labeled data structures: **`Series`** (1D) and **`DataFrame`** (2D — think SQL table in Python). The killer feature is the **index**: rows have labels, not just positions. Operations auto-align by index, so `df1 + df2` matches rows by label, not position.

**Core ops to master:**

**Selection.** `df['col']` returns a Series. `df[['col1', 'col2']]` returns a DataFrame. `.loc[]` is label-based (`df.loc[2024, 'revenue']`). `.iloc[]` is position-based (`df.iloc[0, 1]`). Confusing these is the #1 Pandas bug.

**groupby.** Split-apply-combine. `df.groupby('category')['revenue'].sum()` splits rows by category, applies sum to revenue within each group, combines results. You can chain multiple aggs with `.agg({'col1': 'mean', 'col2': 'sum'})`.

**merge.** SQL-style joins. `pd.merge(df1, df2, on='id', how='left')`. Options: `inner`, `outer`, `left`, `right`. If key names differ, use `left_on`/`right_on`.

**Missing data.** Represented as `NaN`. Handle with `df.isna()`, `df.fillna(value)`, `df.dropna()`. Don't impute blindly — think about what the missing value represents.

**Apply vs vectorized.** `df['col'].apply(func)` runs a Python function per element — slow. Prefer vectorized ops (`df['col'] * 2`, `df['col'].str.lower()`, `np.where(...)`). `apply` is a last resort.

## Code you must be able to write

```python
import pandas as pd
import numpy as np

# Creation
df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'category': ['A', 'B', 'A', 'B'],
    'revenue': [100, 200, 150, 250],
    'date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'])
})

# Reading
# df = pd.read_csv('file.csv')
# df = pd.read_sql('SELECT * FROM table', connection)   # connect to SQL Server
# df = pd.read_excel('file.xlsx')

# Inspection
df.head()
df.info()
df.describe()
df.dtypes
df.shape

# Selection
df['revenue']                              # Series
df[['id', 'revenue']]                      # DataFrame
df.loc[0, 'revenue']                       # label-based
df.iloc[0, 2]                              # position-based
df[df['revenue'] > 150]                    # filter

# Adding/modifying columns
df['revenue_inr'] = df['revenue'] * 83
df['tier'] = np.where(df['revenue'] > 150, 'high', 'low')

# groupby — the workhorse
df.groupby('category')['revenue'].sum()
df.groupby('category').agg({'revenue': ['sum', 'mean', 'count']})
df.groupby('category').agg(total=('revenue', 'sum'), avg=('revenue', 'mean'))

# Merge
df2 = pd.DataFrame({'category': ['A', 'B'], 'manager': ['Alice', 'Bob']})
merged = pd.merge(df, df2, on='category', how='left')

# Missing data
df['revenue'].isna().sum()
df['revenue'].fillna(0)
df.dropna(subset=['revenue'])

# Sort
df.sort_values('revenue', ascending=False)

# Pivot
df.pivot_table(index='category', values='revenue', aggfunc='sum')

# Value counts (like GROUP BY COUNT)
df['category'].value_counts()

# String operations (vectorized)
df['category'].str.lower()
df['category'].str.contains('A')

# Date operations
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
```

## Interview Q&A

**Q: Difference between `.loc` and `.iloc`?**
`.loc` uses labels (index values, column names). `.iloc` uses integer positions. `df.loc['2024-01-01']` selects by date label; `df.iloc[0]` selects the first row regardless of its label.

**Q: How would you join SQL Server data into Pandas?**
Use `pd.read_sql(query, connection)` with a pyodbc or SQLAlchemy connection. For large tables, read in chunks with `chunksize` to avoid memory issues. I'd push filtering and aggregation into SQL when possible — don't pull a million rows to compute a sum.

**Q: How do you handle missing values?**
Depends on why they're missing. If random and rare, drop rows. If a meaningful absence (e.g., "no loan default"), fill with a sentinel or category. For numerical features I'd typically impute with median (robust to outliers); for categorical, with mode or a "Missing" category. Never impute blindly with mean without thinking.

**Q: `groupby` returns what?**
A lazy `GroupBy` object — no computation yet. You must chain an aggregation (`.sum()`, `.mean()`, `.agg()`) or transformation (`.transform()`) to get a DataFrame back.

**Q: `apply` vs vectorized operations?**
`apply(func)` runs a Python function per row or element, which is slow — Python's for loop under the hood. Vectorized operations (`df['col'] * 2`, `df['col'].str.contains('x')`, `np.where(...)`) run in compiled code. I use `apply` only when there's no vectorized alternative.

**Q: How do you optimize Pandas for large data?**
Use appropriate dtypes (`int8` instead of `int64` if values fit), read in chunks, filter early, use `categorical` dtype for low-cardinality strings, consider DuckDB or Polars for datasets that don't fit in memory.

## Your resume angle
"In the Bitcoin project I used Pandas heavily for preprocessing — loading the BitcoinHeist dataset, handling class imbalance, feature engineering from transaction graph data, and preparing train/test splits. For Fern, Pandas would be the natural tool to pull MIS data from SQL Server and do ad-hoc analysis that's too complex for stored procedures alone."

---

# 3. SQL / RDBMS — DEEP DIVE

You use SQL at Fern daily. The panel will push past basics — **prepare for advanced topics.**

## Concepts

**Indexes.** A separate data structure (usually a B-tree) that makes lookups on indexed columns O(log n) instead of O(n) table scan.
- **Clustered index**: determines the physical order of rows in the table. One per table. Usually the primary key.
- **Non-clustered index**: a separate structure pointing to rows. Can have many per table.
- **Downside**: indexes speed up reads but slow down inserts/updates/deletes because the index must be maintained.
- **Covering index**: includes all columns needed by a query, so SQL Server doesn't do a key lookup back to the table.

**Execution plans.** SQL Server optimizer converts your query into an execution plan — a tree of physical operators. Read the plan right-to-left, bottom-up. Key things to spot:
- **Table scan / index scan**: reads every row. Bad on large tables unless you need most of them.
- **Index seek**: uses the index to jump to specific rows. Good.
- **Key lookup**: the index had some columns but had to jump back to the table for others. If frequent, create a covering index.
- **Hash match vs merge join vs nested loop**: different join algorithms — optimizer chooses based on data size and sort state.

**Stored procedures vs functions vs views.**
- **Stored procedure**: compiled SQL that can take params, return multiple result sets, modify data, have side effects. Execution plan cached.
- **Function**: returns a single value (scalar) or table (TVF). Should be deterministic and side-effect-free. Used inside queries.
- **View**: a saved SELECT statement, treated like a virtual table. No parameters. Indexed views can materialize data.

**Transaction isolation levels** (critical in fintech):
| Level | Dirty read | Non-repeatable read | Phantom read |
|-------|-----------|--------------------|--------------|
| READ UNCOMMITTED | Yes | Yes | Yes |
| READ COMMITTED (default) | No | Yes | Yes |
| REPEATABLE READ | No | No | Yes |
| SERIALIZABLE | No | No | No |
| SNAPSHOT | No | No | No (uses row versioning) |

**ACID.** Atomicity (all or nothing), Consistency (valid state to valid state), Isolation (concurrent txns don't interfere), Durability (committed data survives crashes).

**Normalization.**
- **1NF**: atomic values, no repeating groups.
- **2NF**: 1NF + no partial dependency on composite key.
- **3NF**: 2NF + no transitive dependencies (non-key doesn't depend on non-key).
- **BCNF**: stricter 3NF.
- Normalize for integrity, denormalize for read performance.

**Deadlocks.** Two transactions each hold a lock the other wants. SQL Server detects and kills the cheaper one (deadlock victim). Prevent by: accessing resources in the same order, shorter transactions, lower isolation where safe.

**CTE vs temp table vs table variable.**
- **CTE** (`WITH x AS (...)`): query scoped, no statistics, good for readability and recursion.
- **Temp table** (`#temp`): session scoped, has statistics, indexable, good for large intermediate results.
- **Table variable** (`@t`): batch scoped, no statistics (optimizer guesses 1 row), good for small datasets only.

## Code you must be able to write

```sql
-- Window functions
SELECT 
    account_id,
    transaction_date,
    amount,
    SUM(amount) OVER (PARTITION BY account_id ORDER BY transaction_date) AS running_total,
    ROW_NUMBER() OVER (PARTITION BY account_id ORDER BY transaction_date DESC) AS recency_rank,
    LAG(amount, 1) OVER (PARTITION BY account_id ORDER BY transaction_date) AS prev_amount
FROM transactions;

-- CTE with recursion (org hierarchy)
WITH emp_hierarchy AS (
    SELECT employee_id, manager_id, name, 1 AS level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.manager_id, e.name, h.level + 1
    FROM employees e
    JOIN emp_hierarchy h ON e.manager_id = h.employee_id
)
SELECT * FROM emp_hierarchy;

-- Find duplicate rows
SELECT account_id, COUNT(*) 
FROM transactions 
GROUP BY account_id 
HAVING COUNT(*) > 1;

-- Second highest salary
SELECT MAX(salary) FROM employees 
WHERE salary < (SELECT MAX(salary) FROM employees);
-- OR with window function
SELECT DISTINCT salary FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) x WHERE rnk = 2;

-- Stored procedure with error handling
CREATE PROCEDURE sp_TransferFunds
    @FromAccount INT, @ToAccount INT, @Amount DECIMAL(18,2)
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRY
        BEGIN TRANSACTION;
        UPDATE Accounts SET Balance = Balance - @Amount WHERE AccountID = @FromAccount;
        UPDATE Accounts SET Balance = Balance + @Amount WHERE AccountID = @ToAccount;
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH
END;

-- JOIN types quick reference
-- INNER JOIN: only matching rows
-- LEFT JOIN: all left rows + matches (null if no match)
-- RIGHT JOIN: all right rows + matches
-- FULL OUTER JOIN: all rows from both, nulls where no match
-- CROSS JOIN: Cartesian product

-- Index creation
CREATE NONCLUSTERED INDEX IX_Transactions_AccountDate 
    ON Transactions (AccountID, TransactionDate) 
    INCLUDE (Amount);   -- covering index
```

## Interview Q&A

**Q: When would you use a clustered vs non-clustered index?**
One clustered per table — use it on the column you most often range-scan or sort by (often the PK). Non-clustered for other frequent lookup columns. On a transactions table, clustered on `(AccountID, Date)` if queries usually filter by account and date range.

**Q: You have a slow query. Walk me through diagnosis.**
First check the execution plan. Look for table scans on large tables, key lookups, and expensive hash joins on unsorted data. Check statistics — stale stats lead to bad plans. Check for missing indexes the optimizer suggests. If the plan looks fine but it's still slow, look at wait stats — is it I/O bound, CPU bound, or blocked by another transaction? SQL Profiler or Extended Events can capture the actual execution.

**Q: Dirty read vs non-repeatable read vs phantom read?**
**Dirty read**: reading uncommitted data from another transaction. **Non-repeatable read**: same row read twice in your transaction returns different values because another committed an UPDATE in between. **Phantom read**: same range query returns different row counts because another transaction INSERTed into that range.

**Q: How do you prevent deadlocks?**
Access resources in a consistent order across transactions (e.g., always lock Account A before Account B by ID order). Keep transactions short. Use the lowest isolation level that's safe. For read-heavy workloads, SNAPSHOT isolation avoids many lock conflicts by using row versioning.

**Q: CTE vs temp table?**
CTE is a query-scoped named subquery — good for readability and recursion, but the optimizer may re-evaluate it if referenced multiple times. Temp table (`#t`) is materialized with statistics, so for large intermediate results that you join to multiple times, a temp table is faster.

**Q: When would you denormalize?**
When read performance on heavy aggregations outweighs the cost of maintaining redundant data. Typical case: reporting/analytics tables where joins across 6 normalized tables are too expensive. Also when you need a consistent snapshot (e.g., invoice with customer address at time of invoice, not current address).

**Q: What's a covering index?**
An index that contains all columns a query needs — either as key columns or as INCLUDEd columns. The query is answered from the index alone, no key lookup back to the table. Huge performance win for frequent queries.

## Your resume angle
"At Fern I use SQL Profiler and execution plans routinely. One common pattern I've seen is stored procedures that got slow after a customer's data grew — often it's a key lookup that wasn't a problem at 10k rows but hurts at 5M. I fix these by adding covering indexes or restructuring the query. For production defects, SQL Profiler traces help me reproduce and isolate the offending statement."

---

# 4. TRANSFORMERS & HUGGING FACE

This is high-risk because your resume explicitly mentions Phi-3-mini, LoRA, SFT, Unsloth. Be ready for deep technical questions.

## Concepts

### The Transformer architecture

Introduced in *Attention Is All You Need* (Vaswani et al., 2017). Replaces RNNs for sequence modeling.

**The self-attention mechanism:**
For each input token, we compute three projections:
- **Query (Q)**: what am I looking for?
- **Key (K)**: what do I offer?
- **Value (V)**: what's my content?

Attention scores = `softmax(QKᵀ / √d_k) · V`

- `QKᵀ` gives a score for every pair of tokens.
- Divide by `√d_k` (dimension of keys) to stabilize gradients — without scaling, large dot products push softmax into tiny-gradient regions.
- Softmax turns scores into a probability distribution.
- Multiply by V to get a weighted sum.

**Multi-head attention**: run the above H times in parallel with different learned projections, concatenate, and project back. Each head can learn different relationships.

**Full transformer block:**
1. Multi-head self-attention
2. Residual connection + LayerNorm
3. Position-wise feedforward (2 linear layers with activation — typically GELU or SwiGLU)
4. Residual connection + LayerNorm

Stack N of these blocks.

**Positional encoding.** Attention is order-agnostic (it sees a set, not a sequence). So we add positional info — either fixed sinusoidal encodings (original paper) or learned (BERT, GPT) or rotary (RoPE, used in LLaMA, Phi-3).

### Three flavors of transformers

| Type | Example | Training | Use case |
|------|---------|----------|----------|
| Encoder-only | BERT, RoBERTa | Masked language modeling | Classification, NER, embedding |
| Decoder-only | GPT, Phi-3, LLaMA | Next-token (causal) | Generation, chat |
| Encoder-Decoder | T5, BART | Span corruption | Translation, summarization |

**You fine-tuned Phi-3-mini, which is decoder-only.**

### Fine-tuning hierarchy

- **Full fine-tuning**: update all parameters. Quality: best. Cost: massive — Phi-3-mini has 3.8B params, needs 30+ GB VRAM.
- **LoRA (Low-Rank Adaptation)**: freeze original weights, add small trainable matrices. For a weight matrix W of shape (d, d), we write the update as `ΔW = B·A` where `A` is `(r, d)` and `B` is `(d, r)` with `r << d`. You train A and B only. For `d=4096, r=16`, you train 131k params instead of 16M per matrix.
- **QLoRA**: LoRA on top of a 4-bit quantized base model. Fits 7B models on a single consumer GPU.
- **SFT (Supervised Fine-Tuning)**: training paradigm where you fine-tune on (instruction, response) pairs. LoRA is the parameter method; SFT is the training objective.
- **RLHF/DPO**: align model to preferences (ranked responses). Different problem from SFT.

### Unsloth

A library that accelerates LoRA/QLoRA fine-tuning by 2-5x through custom Triton kernels and optimized backward passes. 4-bit quantization shrinks memory ~4x vs fp16, enabling you to fine-tune large models on a single GPU.

### Hugging Face ecosystem

- **`transformers`**: model + tokenizer classes. `AutoModel`, `AutoTokenizer`, `AutoModelForCausalLM`, `AutoModelForSequenceClassification`.
- **`datasets`**: streaming-friendly dataset library with a standard format.
- **`tokenizers`**: fast Rust-based tokenizers.
- **`peft`**: LoRA, prefix tuning, prompt tuning, etc.
- **`accelerate`**: handles multi-GPU, mixed precision, gradient accumulation.
- **`trl`**: SFTTrainer, DPOTrainer, PPO for RLHF.

## Code you must be able to write / explain

```python
# Basic inference
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

inputs = tokenizer("What is Bayes' theorem?", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100, do_sample=True, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

# LoRA fine-tuning pattern (what you did)
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer

lora_config = LoraConfig(
    r=16,                              # rank — controls capacity of adapter
    lora_alpha=32,                     # scaling factor
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", 
                    "gate_proj", "up_proj", "down_proj"],  # attention + FFN
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()   # e.g., "0.5% of total"

# SFT with formatted instruction-response pairs
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    tokenizer=tokenizer,
    dataset_text_field="text",
    max_seq_length=2048,
    args=training_args,
)
trainer.train()
```

## Interview Q&A

**Q: Explain self-attention.**
For each token, we project it into query, key, and value vectors. The query is compared against every key via dot product to produce attention weights — how much this token should attend to each other token. Those weights (after softmax) are used to compute a weighted sum of value vectors. The output is a new representation of each token that incorporates information from relevant other tokens. The full formula is `softmax(QKᵀ/√d_k)V`.

**Q: Why scale by √d_k?**
As dimension grows, dot products grow in magnitude, pushing softmax into saturated regions with tiny gradients. Dividing by √d_k keeps variance roughly unit, so gradients flow.

**Q: Why multi-head attention?**
A single attention head averages relationships; different heads can specialize — one might track syntactic structure, another coreference, another positional. Multi-head gives the model parallel channels for different relationship types at the same computational cost as larger single-head attention.

**Q: Encoder-only vs decoder-only vs encoder-decoder?**
Encoder-only (BERT) sees the full context bidirectionally — good for classification and embedding. Decoder-only (GPT, Phi-3) is autoregressive, generating one token at a time with causal masking — good for generation. Encoder-decoder (T5) has separate encoder and decoder with cross-attention — natural for seq2seq tasks like translation.

**Q: Why use LoRA instead of full fine-tuning?**
Full fine-tuning updates billions of parameters, requires massive memory (optimizer states are 2x model size), and risks catastrophic forgetting. LoRA freezes the base model and trains small low-rank matrices A and B where the update is `ΔW = BA` with rank r << d. You train ~0.1-1% of parameters, get most of the quality, and can swap adapters per task.

**Q: What rank did you use and why?**
I used rank 16, which is a common default — high enough to adapt behavior for structured output tasks without overfitting on a small dataset, low enough to keep the adapter tiny. Higher rank (32, 64) helps for more complex adaptation; lower rank (4, 8) for simpler tasks.

**Q: Why target both attention and feedforward layers with LoRA?**
Attention layers learn what to attend to; FFN layers do most of the knowledge storage in transformers. Adapting only attention limits how much the model can learn new associations. Full coverage (q, k, v, o, gate, up, down) gives the adapter the most expressive capacity per parameter.

**Q: What does 4-bit quantization do?**
Compresses each weight from 16 or 32 bits to 4 bits using a quantization scheme (NF4 in QLoRA). Cuts memory ~4x vs fp16 with minimal quality loss for inference. Training happens in higher precision on the LoRA adapters while the quantized base weights stay frozen.

**Q: SFT vs RLHF vs DPO?**
SFT trains on labeled (prompt, response) pairs with standard cross-entropy — teaches the model to imitate. RLHF trains a reward model on human preference pairs, then optimizes the LM with PPO to maximize reward. DPO skips the reward model — directly optimizes the LM on preference pairs with a clever loss derivation. Typical pipeline: pretrain → SFT → DPO/RLHF.

**Q: What's a tokenizer doing?**
Converting text into integer token IDs the model can consume. Modern tokenizers use subword algorithms — BPE (GPT), WordPiece (BERT), or SentencePiece (LLaMA, Phi-3) — which balance vocabulary size with out-of-vocabulary robustness. The same text can tokenize differently across models.

## Your resume angle
"In my LLM fine-tuning project I used LoRA on Phi-3-mini with Unsloth for 4-bit quantized training. I configured rank-16 adapters on both attention projections and FFN layers to give the model enough capacity to learn schema-to-sub-category mappings. The SFT objective on my structured instruction dataset aligned outputs to the target format. I evaluated on held-out inputs and did error analysis on inconsistencies — common failures were schema hallucinations on under-represented categories, which I'd address in a follow-up with more balanced data or higher-rank adapters."

---

# 5. DSA — PATTERNS & TEMPLATES

You don't have time to grind 100 LeetCode problems. You need **pattern recognition** and **template code** for the 6 patterns below. Practice one problem per pattern.

## Complexity recap

| Operation | Array | Hash Map | Sorted Array | Heap | Balanced BST |
|-----------|-------|----------|--------------|------|--------------|
| Access by index | O(1) | — | O(1) | — | — |
| Search | O(n) | O(1) avg | O(log n) | — | O(log n) |
| Insert | O(n) | O(1) avg | O(n) | O(log n) | O(log n) |
| Delete | O(n) | O(1) avg | O(n) | O(log n) | O(log n) |
| Min/Max | O(n) | O(n) | O(1) | O(1) | O(log n) |

## Pattern 1: Two pointers

Use when array is sorted or when finding pairs.

```python
# Two sum on sorted array
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

## Pattern 2: Sliding window

Use for substrings/subarrays with a constraint.

```python
# Longest substring without repeating characters
def longest_unique_substring(s):
    seen = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

## Pattern 3: Hash map counting

Use for frequency problems, anagrams, subarray sums.

```python
# Subarray sum equals k
def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    seen = {0: 1}        # prefix_sum -> count
    for n in nums:
        prefix_sum += n
        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count
```

## Pattern 4: Binary search

On sorted array, or "search on the answer" for optimization problems.

```python
# Classic binary search
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# Search in rotated sorted array
def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:              # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                   # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

## Pattern 5: BFS/DFS on tree or graph

```python
from collections import deque

# BFS on graph
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# DFS recursive
def dfs(node, visited, graph):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited, graph)

# Tree level order
def level_order(root):
    if not root: return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

# Number of islands (BFS on grid)
def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    queue.append((nx, ny))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                bfs(r, c)
    return count
```

## Pattern 6: Dynamic programming (one template)

```python
# Coin change — min coins to make amount
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Fibonacci with memoization
def fib(n, memo={}):
    if n in memo: return memo[n]
    if n < 2: return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

## Interview rules for coding

1. **Read the problem twice.** Clarify constraints — array size, value ranges, edge cases (empty input, single element, duplicates).
2. **State the brute force first.** Always. Give its time complexity.
3. **Optimize.** State the approach and new complexity before coding.
4. **Write clean code.** Meaningful variable names. Comments for non-obvious steps.
5. **Test with a small example** out loud after writing.
6. **State final complexity.** Time and space.
7. **Talk while you code.** Silence reads as uncertainty.

---

# 6. PROBABILITY & STATISTICS

High-yield given pgmpy. Own Bayes' theorem and conditional independence in your sleep.

## Concepts

### Probability basics

- **Probability**: `P(event)` in [0, 1].
- **Conditional probability**: `P(A|B) = P(A ∩ B) / P(B)` — probability of A given B has happened.
- **Independence**: `P(A ∩ B) = P(A) · P(B)`, equivalently `P(A|B) = P(A)`.
- **Conditional independence**: `P(A ∩ B | C) = P(A|C) · P(B|C)`. A and B are independent *given* C — even if they're dependent marginally. **This is the core factorization assumption in Bayesian networks.**

### Bayes' theorem (own this cold)

**`P(A|B) = P(B|A) · P(A) / P(B)`**

In words: **posterior = (likelihood × prior) / evidence.**

Canonical medical example: Disease prevalence 0.1%. Test is 99% accurate (true positive rate and true negative rate). You test positive. What's the probability you have the disease?

```
P(D|+) = P(+|D) · P(D) / P(+)
       = 0.99 · 0.001 / [0.99·0.001 + 0.01·0.999]
       = 0.00099 / 0.01098
       ≈ 0.090  → only 9%!
```

The counterintuitive answer is because the prior is so low. Essential intuition.

### Chain rule of probability

`P(A, B, C) = P(A) · P(B|A) · P(C|A, B)`

Bayesian networks exploit conditional independence to simplify this — if C is independent of A given B, then `P(C|A,B) = P(C|B)`, and the joint factorizes much more compactly.

### Expectation & variance

- **Expectation**: `E[X] = Σ x · P(x)` (discrete), `∫ x · f(x) dx` (continuous).
- **Variance**: `Var(X) = E[(X - E[X])²] = E[X²] - E[X]²`.
- **Std dev**: `σ = √Var(X)`.
- **Covariance**: `Cov(X,Y) = E[(X - E[X])(Y - E[Y])]`.
- **Correlation**: `ρ = Cov(X,Y) / (σ_X · σ_Y)` — in [-1, 1].

### Key distributions

- **Bernoulli(p)**: single trial, P(1)=p, P(0)=1-p. Mean p, variance p(1-p).
- **Binomial(n, p)**: sum of n Bernoullis. Mean np, variance np(1-p).
- **Normal(μ, σ²)**: bell curve. ~68% within 1σ, ~95% within 2σ, ~99.7% within 3σ.
- **Poisson(λ)**: count of rare events. Mean = variance = λ.
- **Uniform(a, b)**: all values equally likely.

### Central Limit Theorem

Sum (or mean) of n i.i.d. random variables with finite variance approaches a Normal distribution as n grows, regardless of the original distribution's shape. **This is why Normal appears everywhere.**

### Law of Large Numbers

Sample mean converges to population mean as sample size grows.

### Hypothesis testing

- **Null hypothesis H₀**: the default assumption (e.g., "no effect").
- **Alternative H₁**: what you'd accept if evidence is strong.
- **p-value**: probability of seeing data this extreme assuming H₀ is true.
- **Reject H₀** if p < α (typically 0.05).
- **Type I error**: rejecting a true H₀ (false positive). Probability = α.
- **Type II error**: failing to reject a false H₀ (false negative). Probability = β.
- **Power**: `1 - β`.

### Statistics basics

- **Mean** is sensitive to outliers; **median** is robust.
- **Correlation ≠ causation** — a hidden confounder can create correlation without causal relationship. **Causal discovery algorithms like SortnRegress try to recover causal structure from observational data using additional assumptions like varsortability.**

## Interview Q&A

**Q: Explain Bayes' theorem with an example.**
[Use the medical test example above. Calculate it out loud.] The key insight is that even a very accurate test can produce a low posterior when the prior (base rate) is low, because false positives on the large negative population outnumber true positives.

**Q: What's conditional independence? Why does it matter for Bayesian networks?**
Two variables A and B are conditionally independent given C if `P(A,B|C) = P(A|C)·P(B|C)`. They might be correlated marginally — say sprinkler usage and wet grass are correlated — but become independent once you condition on rain. Bayesian networks encode these conditional independencies as missing edges in a DAG, which dramatically reduces the number of parameters needed to represent the joint distribution.

**Q: What's the difference between correlation and causation?**
Correlation is a statistical association — X and Y vary together. Causation means X directly influences Y. Correlation can arise from causation, reverse causation, confounders, or coincidence. Standard statistics from observational data can't distinguish these without additional assumptions. *[Mention your pgmpy SortnRegress work — "causal discovery algorithms use assumptions like varsortability or interventions to recover causal structure from observational data."]*

**Q: What does the Central Limit Theorem say and why does it matter?**
Sums or means of many independent identically-distributed random variables converge to a Normal distribution, regardless of the original distribution's shape (as long as variance is finite). It's why Normal assumptions work for sample means, why confidence intervals are constructed the way they are, and why many natural phenomena look Gaussian — they're sums of many small effects.

**Q: What's a p-value?**
The probability of observing data at least as extreme as what you saw, assuming the null hypothesis is true. Small p-value means the data is unlikely under H₀, so you reject it. It is NOT the probability that H₀ is true.

**Q: Type I vs Type II error?**
Type I: reject a true null (false alarm). Type II: fail to reject a false null (miss). In fraud detection, Type I means flagging a legitimate transaction (annoying customers); Type II means missing actual fraud (financial loss). The business sets the tradeoff.

**Q: What's MLE vs Bayesian estimation?**
Maximum Likelihood Estimation picks the parameter θ that maximizes `P(data|θ)` — point estimate, no prior. Bayesian estimation treats θ as a random variable, computes posterior `P(θ|data) ∝ P(data|θ)·P(θ)` — full distribution, incorporates prior beliefs. MLE can overfit on small data; Bayesian (with reasonable prior) regularizes.

## Your resume angle
"Probability and Bayesian reasoning are central to my pgmpy contributions. The library is built on probabilistic graphical models, which represent joint distributions via conditional independencies encoded in a DAG. My work on SortnRegress and the dataset registry required understanding of how causal discovery algorithms use observational statistics to recover structure — which is fundamentally a probabilistic inference problem."

---

# 7. LINEAR ALGEBRA

Fast pass. Focus on what actually appears in ML.

## Concepts

**Vector**: ordered list of numbers. Represents a point or direction in n-dimensional space.

**Matrix**: 2D grid of numbers. Represents a linear transformation.

**Dot product**: `a · b = Σ aᵢbᵢ = |a||b|cos(θ)`. Measures alignment. Zero iff orthogonal. The basis of cosine similarity used in embeddings.

**Matrix multiplication**: `(m×n) × (n×p) = (m×p)`. Inner dimensions must match. **Not commutative** — generally `AB ≠ BA`. Think of each column of the result as A applied to a column of B.

**Transpose** `Aᵀ`: flip rows and columns. `(AB)ᵀ = BᵀAᵀ`.

**Identity matrix I**: diagonal of ones. `AI = IA = A`.

**Inverse A⁻¹**: `AA⁻¹ = I`. Only exists if A is square and has non-zero determinant (full rank).

**Determinant**: scalar summary of a square matrix. `det(A) = 0` means A is singular (not invertible) and collapses space along some direction. Geometrically, |det| is the volume scaling factor.

**Rank**: number of linearly independent columns (equivalently rows). Full rank = all columns independent = invertible (if square).

**Eigenvalues and eigenvectors**: for square A, an eigenvector v satisfies `Av = λv` for scalar λ. v is a direction that A merely scales (doesn't rotate). Eigenvalues tell you the scaling factor.

- Used in **PCA**: the eigenvectors of the covariance matrix are the principal components; eigenvalues are the variance explained along each direction.
- Used in **spectral methods**, **Markov chains** (stationary distribution), **PageRank**.

**Norms**:
- **L1 norm**: `Σ|xᵢ|` — sum of absolute values. Sparse solutions.
- **L2 norm**: `√Σxᵢ²` — Euclidean length. Standard regularizer.

**Orthogonality**: vectors a and b are orthogonal if `a · b = 0`. Orthogonal matrices (QᵀQ = I) preserve lengths and angles — used in decompositions.

**Singular Value Decomposition (SVD)**: any matrix A = UΣVᵀ where U, V are orthogonal and Σ is diagonal with non-negative entries (singular values). Foundation of dimensionality reduction and recommender systems.

## Code you should recognize

```python
import numpy as np

A = np.array([[2, 1], [1, 3]])
b = np.array([5, 8])

# Matrix multiplication
np.dot(A, A)         # or A @ A

# Solve Ax = b
x = np.linalg.solve(A, b)    # prefer this over A⁻¹b

# Inverse (rarely needed directly)
np.linalg.inv(A)

# Eigenvalues/vectors
eigvals, eigvecs = np.linalg.eig(A)

# Determinant and rank
np.linalg.det(A)
np.linalg.matrix_rank(A)

# Norms
np.linalg.norm(b)            # L2 by default
np.linalg.norm(b, ord=1)     # L1

# SVD
U, S, Vt = np.linalg.svd(A)
```

## Interview Q&A

**Q: Why does linear regression use `β = (XᵀX)⁻¹Xᵀy`?**
Derived by minimizing squared error `||y - Xβ||²`. Taking derivative with respect to β and setting to zero gives the normal equations `XᵀXβ = Xᵀy`. Solve for β. In practice we don't invert `XᵀX` explicitly — we use numerically stable methods like QR decomposition.

**Q: What are eigenvectors intuitively?**
Directions that a linear transformation doesn't rotate — only stretches or shrinks. The eigenvalue is the scaling factor. For a shear transformation, the shear direction is an eigenvector with eigenvalue 1.

**Q: Where do eigenvectors appear in ML?**
PCA: covariance matrix eigenvectors are the principal components, and eigenvalues tell you variance captured. Spectral clustering. Google's PageRank — the stationary distribution of the web graph is the dominant eigenvector of the transition matrix.

**Q: L1 vs L2 regularization?**
L1 (Lasso) adds `λΣ|βᵢ|` — encourages sparse solutions (many coefficients exactly zero) because the penalty is non-differentiable at zero, which acts like feature selection. L2 (Ridge) adds `λΣβᵢ²` — shrinks coefficients smoothly toward zero but rarely exactly zero. Elastic Net combines both.

---

# 8. SUPERVISED LEARNING (bonus — quick reference)

## Concepts

**Definition**: learning a function f: X → Y from labeled (x, y) pairs. Classification (discrete y) or regression (continuous y).

**The workflow**:
1. Split data — train/validation/test (or k-fold cross-validation).
2. Preprocess — scale numerical features, encode categorical, handle missing.
3. Train model on train set.
4. Tune hyperparameters on validation set (or via CV).
5. Report final performance on held-out test set — **once only**.

**Bias-variance tradeoff**:
- **High bias** (underfitting): model too simple, misses signal. Low train and test accuracy.
- **High variance** (overfitting): model memorizes train, fails to generalize. High train accuracy, low test accuracy.
- Fix overfitting: more data, regularization, simpler model, early stopping, dropout (NNs), cross-validation.

**Class imbalance** (you handled this in the Bitcoin project):
- Accuracy is meaningless — a model that predicts "not ransomware" always gets 99% on imbalanced data.
- Use precision, recall, F1, ROC-AUC instead.
- Techniques: SMOTE (synthetic oversampling), class weights in the loss, stratified sampling.

**Key algorithms** (one-line intuition each):

| Algorithm | Intuition | Strength |
|-----------|-----------|----------|
| Linear regression | Fit a line minimizing squared error | Interpretable, fast |
| Logistic regression | Linear → sigmoid → probability | Baseline classifier, calibrated |
| Decision tree | Greedy splits minimizing impurity | Non-linear, interpretable |
| Random Forest | Ensemble of trees (bagging) | Your Bitcoin project. Robust, low-tuning |
| Gradient Boosting | Sequential trees correcting errors | Best tabular performance (XGBoost, LightGBM) |
| SVM | Max-margin hyperplane | High-dim, kernel trick |
| k-NN | Majority vote of k nearest | No training, simple baseline |
| Neural Networks | Stacked non-linear transformations | Flexible, needs data |

**Metrics**:
- **Classification**: accuracy (balanced data only), precision = TP/(TP+FP), recall = TP/(TP+FN), F1 = harmonic mean, ROC-AUC, confusion matrix.
- **Regression**: MSE, RMSE, MAE, R².
- **When precision vs recall matters**: spam filter — precision (don't flag real mail). Medical screening — recall (don't miss sick patients). Business context decides.

## Interview Q&A

**Q: Walk me through your Bitcoin ransomware detection project.**
Dataset: UCI BitcoinHeist, ~3M Bitcoin addresses labeled across 29 ransomware families plus benign. Features were transaction-graph derived — length, weight, count, looped, neighbors, income. Heavy class imbalance (vast majority benign), so I used stratified sampling and class weights, and evaluated with precision/recall/F1 per class, not accuracy. I chose Random Forest because it handles non-linear feature interactions, gives feature importance out of the box, is robust to class imbalance with weights, and requires less tuning than gradient boosting. I did train/test split with stratification, trained the classifier, and analyzed per-family prediction behavior — some families were harder than others, likely due to sample size differences.

**Q: Why Random Forest over a single decision tree?**
A single tree overfits — it can achieve 100% train accuracy by growing deep. RF trains many trees on bootstrapped samples with random feature subsets, then averages. The decorrelation between trees reduces variance dramatically without much increase in bias — classic bagging benefit.

**Q: How do you handle class imbalance?**
First, don't use accuracy as the metric — it's misleading. Use precision, recall, F1, or ROC-AUC. Algorithmically: class weights in the loss function, stratified sampling to preserve ratios, oversampling minority class (SMOTE), or undersampling majority. Choice depends on data size and business cost of each error type.

**Q: What's cross-validation?**
Split training data into k folds. For each fold, train on the other k-1 and validate on this one. Average the metrics. Gives a more robust estimate of generalization than a single train/val split, at k× compute cost. Essential when data is small.

**Q: Precision vs recall — give a real example.**
In my ransomware project, recall matters more — missing a ransomware address (false negative) is worse than flagging a benign one for review. So I'd optimize for high recall, accepting some precision loss. For a spam filter, it's opposite — flagging a real email as spam is worse than letting one spam through, so precision matters more.

## Your resume angle
Already covered above — lead with the Bitcoin project, tie class imbalance handling to the metric choice, explain the RF rationale clearly.

---

# MOCK RAPID-FIRE QUESTION BANK

Go through these the night before. If you can't answer in 30 seconds, flag it for re-study.

1. Why is NumPy faster than Python lists? → Contiguous memory, fixed dtype, C-level vectorized operations.
2. What's broadcasting? → Automatic shape alignment for element-wise ops; dimensions compatible if equal or 1.
3. `.loc` vs `.iloc`? → Label-based vs position-based indexing.
4. How does `groupby` work? → Split rows by key, apply function within each group, combine results.
5. Clustered vs non-clustered index? → Physical row order vs separate pointer structure.
6. What's a key lookup in an execution plan? → Index had partial columns; query had to fetch rest from table. Fix with covering index.
7. READ COMMITTED vs SNAPSHOT? → First uses locks; second uses row versioning (no read-write blocking).
8. Stored procedure vs function? → SP has side effects, caches plan; function returns value, side-effect-free.
9. Explain self-attention in one paragraph. → Tokens project into Q/K/V; attention weights are softmax(QKᵀ/√dk); output is weighted sum of V.
10. Why scale by √d_k? → Keep dot-product variance stable; avoid softmax saturation.
11. BERT vs GPT? → Bidirectional encoder vs causal decoder.
12. Why LoRA? → Freeze base, train low-rank ΔW = BA, ~1% params, no catastrophic forgetting.
13. What's 4-bit quantization? → Compress weights to 4 bits; ~4× memory saving with minimal quality loss.
14. SFT vs RLHF? → Imitation learning on pairs vs reward-optimized with human preferences.
15. Bayes' theorem? → `P(A|B) = P(B|A)·P(A)/P(B)`. Posterior proportional to likelihood times prior.
16. Conditional independence? → `P(A,B|C) = P(A|C)·P(B|C)`. Core assumption in Bayesian networks.
17. Correlation vs causation? → Association vs direct influence. Confounders can create correlation without causation.
18. CLT? → Sum/mean of many i.i.d. RVs tends to Normal, regardless of original distribution.
19. What's a p-value? → Probability of data this extreme assuming H₀; small → reject H₀.
20. Type I vs Type II error? → Reject true null vs fail to reject false null.
21. What's an eigenvalue? → Scaling factor for a direction (eigenvector) that the matrix doesn't rotate.
22. L1 vs L2 regularization? → Sparse (feature selection) vs smooth shrinkage.
23. Overfitting — symptoms and fixes? → High train accuracy, low test; fix with regularization, more data, simpler model, CV.
24. Random Forest vs single tree? → Ensemble reduces variance via bagging and feature randomness.
25. Precision vs recall? → TP/(TP+FP) vs TP/(TP+FN). Trade off based on cost of false positives vs false negatives.
26. Why not use accuracy on imbalanced data? → A trivial majority-class predictor can score high without learning anything.
27. k-fold cross-validation? → Partition data into k folds, train on k-1, validate on 1, rotate, average.
28. What's a deadlock, how do you resolve? → Two txns each holding a lock the other needs. SQL Server kills cheaper one. Prevent with consistent lock ordering.
29. What's ACID? → Atomicity, Consistency, Isolation, Durability.
30. Why normalize a database? → Integrity, reduce redundancy. Denormalize for read performance.

---

# FINAL RULES FOR MONDAY

1. **Never bluff.** If you don't know, say so cleanly, then reason from first principles.
2. **Brute force first, then optimize.** For DSA.
3. **Talk while you code.** Silent coding reads as uncertainty.
4. **Route every project question back to your resume.** pgmpy and LoRA are your differentiators.
5. **Ask clarifying questions.** For coding problems especially — constraints, edge cases, input format.
6. **Own your weaknesses gracefully.** "I haven't used X, but based on Y principles I'd expect it to work like Z."
7. **Smile and slow down.** Rushed answers sound uncertain. Take a breath before answering.

You got this. The resume is already strong. Now just don't freeze, don't bluff, and route hard questions back to what you've actually built.
