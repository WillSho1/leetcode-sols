# Database Indexing Strategies: B-Trees vs. LSM-Trees
# Link: https://github.com/donnemartin/system-design-primer#database-indexing

## Context
A key performance bottleneck in distributed systems is physical disk I/O. Proper indexing strategies balance write throughput against read latency.

## Questions (Response Required)
1. How does a B-Tree differ from an LSM-Tree in terms of "Write Amplification"?
LSM-Tree is a data structure that is write optimized, where writes are appended to a log then compacted to a memtable. B-Tree dbs are optimized for reading and quick look ups.
2. In what specific use-case would you prefer an LSM-Tree (e.g., used by Cassandra/LevelDB) over a B-Tree (e.g., used by Postgres/MySQL)?
If you have write heavy operations and need to ingest a lot of data versus search though it.
3. Explain the role of "Bloom Filters" in LSM-Tree read performance.
The Bloom Filters are associated with the SSTables and stored in RAM. They act as a cache and if a key is not found in a Bloom filter, the program avoids reading the respective SSTable.
4. Describe the "Merge-Sort" process during LSM-Tree compaction.
When the buffer fills, it compacts down into the levels of the LSM tree. The entries in the buffer are sorted on the key, and the buffer is flushed to disk. On disk, when a level fills, the same process happens and the level is merged down.

I am not an expert on any of this, I had to look up most answers.