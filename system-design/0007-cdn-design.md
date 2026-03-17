# 0007-cdn-design.md
## Content Delivery Network (CDN) Design

### High-Level Design (AI Skeleton)
1. **User Request:** User requests `image.jpg`.
2. **DNS Routing:** Request is routed to the nearest Edge Node via Anycast.
3. **Cache Hit:** Edge Node returns the cached image.
4. **Cache Miss:** Edge Node requests from Origin, caches, and returns.

### Review & Correct
1. **Flaw 1:** How would you handle "Thundering Herd" if a new video goes viral and 1M users miss the cache at once?
2. **Flaw 2:** What invalidation strategy (Push vs Pull) is best for a news site? Why?
3. **Fundamental:** Explain the difference between Anycast and GeoDNS.

---
Reference: https://github.com/donnemartin/system-design-primer#content-delivery-network
