# Arch Drill: API Gateway Design & Protocols

## Problem Statement
Design an API Gateway for a high-traffic microservices architecture (e.g., Netflix or Uber style). 
It must handle authentication, rate limiting, and request routing.

## Requirements & Constraints
- Support both REST/JSON and gRPC for internal/external communication.
- Low latency (< 10ms overhead).
- Highly available and scalable.

## High-Level Design (HLD)
[Describe the placement of the Gateway, Load Balancers, and Service Discovery]

## Technical Deep Dive: REST vs. gRPC
- **Scenario A:** Public-facing mobile apps. Which protocol and why?
- **Scenario B:** Internal service-to-service communication. Which protocol and why?

## Caching Strategy
Where would you implement caching in this gateway? What are the invalidation trade-offs?

## Review & Correct (Fundamentals)
- [ ] What is the difference between Layer 4 and Layer 7 load balancing?
- [ ] How does TLS termination impact Gateway performance?
