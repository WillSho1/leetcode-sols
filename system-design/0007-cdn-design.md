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

### Answers
1. If they are trying to access the same resource, I would halt the requests after the first cache miss, until the resource has been cached.

Request Collapsing (Request Joining). The Edge node should identify that 1,000 requests are asking for the same missing file. It puts 999 on "wait" and sends only one request to the origin. Once it returns, it broadcasts the result to all 1,000 users.
2. I do not know what this means.

Pull (Query-on-demand). A news site has thousands of articles. "Pushing" every update to every edge node is wasteful (expensive bandwidth). In a Pull model, the content is only cached when a user actually asks for it. Use a short TTL (Time to Live) to ensure news stays fresh.
3. I do not know.

GeoDNS: The DNS server looks at your IP, looks up your location in a database, and gives you an IP of a server near you. (Decision at DNS level).
Anycast: Multiple servers across the world share the exact same IP. The internet's routing protocol (BGP) automatically sends your packet to the "closest" server based on network hops. (Decision at Routing level). Anycast is faster and more resilient.