# Database Indexing Strategies: B-Trees vs. LSM-Trees
# Link: https://github.com/donnemartin/system-design-primer#database-indexing

## Context
A key performance bottleneck in distributed systems is physical disk I/O. Proper indexing strategies balance write throughput against read latency.

## Questions (Response Required)
1. How does a B-Tree differ from an LSM-Tree in terms of "Write Amplification"?
2. In what specific use-case would you prefer an LSM-Tree (e.g., used by Cassandra/LevelDB) over a B-Tree (e.g., used by Postgres/MySQL)?
3. Explain the role of "Bloom Filters" in LSM-Tree read performance.
4. Describe the "Merge-Sort" process during LSM-Tree compaction.
