# Topic: Data Replication Strategies
# https://bytebytego.com/courses/system-design-interview/data-replication

### Questions

1. **Leader-Based Replication:** Explain the difference between Synchronous and Asynchronous replication. What is the tradeoff regarding durability vs. latency?

2. **Multi-Leader Replication:** In what scenarios (e.g., multi-datacenter) is this beneficial, and what is the primary complexity it introduces for write operations?

3. **Leaderless Replication (Quorums):** If you have $N$ replicas, what are the values for $W$ (write) and $R$ (read) to ensure a "strict quorum" where at least one node has the latest data?

4. **Conflict Resolution:** When two nodes receive different writes for the same key (Write-Write conflict), what are two common strategies to resolve this?
