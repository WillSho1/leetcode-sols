# 0006-caching-strategies.md
Reference: https://github.com/donnemartin/system-design-primer

## Goal
Explain different caching strategies and their trade-offs.

## Questions
1. Compare Cache-Aside, Write-Through, and Write-Behind (Write-Back) patterns. Which one provides the highest write performance, and why?
2. What is the difference between an Eviction Policy and an Expiration (TTL)? Name 3 common eviction policies.
3. Explain the problem of "Cache Stampede" (Thundering Herd). How would you mitigate it at scale?
4. When would you use a Distributed Cache (like Redis) over a Local In-memory Cache (like Guava)?
