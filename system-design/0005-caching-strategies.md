# Caching Strategies (System Architecture Tier 1)

## Overview
Caching is the practice of storing frequently accessed data in a fast, temporary storage layer (the cache) to reduce expensive data-fetching operations from the primary storage (e.g., a database).

## Core Strategies

1. **Cache-Aside (Lazy Loading)**:
   - The application first checks the cache.
   - If data is not there (cache miss), it fetches from the database and updates the cache.
   - **Pros**: Only requested data is cached.
   - **Cons**: Cache miss penalty for the first request.

2. **Read-Through**:
   - The cache sits in the middle between the app and the DB.
   - The app asks the cache for data; the cache fetches from the DB if it's missing.
   - **Pros**: Simplifies application code.
   - **Cons**: Still has initial fetch penalty.

3. **Write-Through**:
   - Data is written to the cache and the DB simultaneously.
   - **Pros**: Database and cache are always in sync.
   - **Cons**: Higher write latency for every update.

4. **Write-Around**:
   - Data is written directly to the database, skipping the cache.
   - **Pros**: Prevents the cache from being filled with low-priority, rarely-accessed data.
   - **Cons**: Reading recently written data results in a cache miss.

5. **Write-Back (Write-Behind)**:
   - Application writes to the cache only; data is written to the DB asynchronously.
   - **Pros**: Extremely fast writes.
   - **Cons**: Data loss risk if the cache crashes before it syncs to the DB.

## Cache Eviction Policies
- **LRU (Least Recently Used)**: Discards the least recently accessed items first.
- **LFU (Least Frequently Used)**: Discards items used least often.
- **FIFO (First In, First Out)**: Discards items in the order they were added.

## Common Interview Scenarios
- **Cold Start**: Pre-populating the cache to avoid performance hits.
- **Cache Stampede**: Multiple threads hitting the DB at once for a missing key.
- **Hot Key**: A single key getting overwhelmed by traffic.
