# Arch Drill: API Gateway Design & Protocols

## Problem Statement
Design an API Gateway for a high-traffic microservices architecture (e.g., Netflix or Uber style). 
It must handle authentication, rate limiting, and request routing.

## Requirements & Constraints
- Support both REST/JSON and gRPC for internal/external communication.
- Low latency (< 10ms overhead).
- Highly available and scalable.

## High-Level Design (HLD)
The API Gateway sits behind a **Layer 4 Load Balancer** (like AWS NLB) and acts as the entry point for all client requests. It integrates with a **Service Registry** (like Consul or Kubernetes CoreDNS) to dynamically discover where to route traffic. For authentication, it validates **JWT tokens** at the edge before passing the request to the target microservice, reducing load on internal services.

## Technical Deep Dive: REST vs. gRPC
- **Scenario A:** Public-facing mobile apps. **REST/JSON** is the standard because of its universal support across web browsers and mobile platforms. It is human-readable and handles varying network conditions well.
- **Scenario B:** Internal service-to-service communication. **gRPC** (over HTTP/2) is preferred because it uses **Protocol Buffers** (binary serialization) which is significantly faster and uses less bandwidth than JSON. It also supports bidirectional streaming and is strongly typed.

## Caching Strategy
Caching should be implemented at the **Edge/Gateway layer** for idempotent `GET` requests (e.g., product catalogs, public profiles). 
- **Trade-off:** Invalidation is the biggest challenge. Using a **TTL (Time to Live)** is simple but can lead to stale data. **Event-based invalidation** (via a message bus like Kafka) is more precise but adds complexity.

## Review & Correct (Fundamentals)
- [x] **What is the difference between Layer 4 and Layer 7 load balancing?** Layer 4 (Transport) routes based on IP and Port (TCP/UDP), making it extremely fast. Layer 7 (Application) routes based on the content of the request (HTTP headers, URL paths, cookies), which allows for much smarter routing but has more overhead.
- [x] **How does TLS termination impact Gateway performance?** Decrypting HTTPS traffic (TLS Termination) is CPU-intensive. By terminating TLS at the Gateway or a dedicated Load Balancer, internal traffic can remain "plain text" (HTTP) over a secure VPC, which drastically reduces the processing load on individual microservices.
