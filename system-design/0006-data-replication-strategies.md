# [System Architecture] 0006-data-replication-strategies.md
- **Focus:** Data Persistence (Tier 2/3)
- **Source:** ByteByteGo / General
- **Link:** https://bytebytego.com/courses/system-design-interview/data-replication

## Focus: Multi-Leader and Leaderless Replication
Compare the trade-offs of single-leader, multi-leader, and leaderless (Quorum-based) replication systems.

### Key Concepts
- Consistency vs Availability (CAP Theorem)
- Read-your-writes consistency
- Write conflicts and resolution strategies (LWW, CRDTs)
- Quorum (N, W, R) configuration
