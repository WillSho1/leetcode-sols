# 0009 - REST vs gRPC Design Tradeoffs

[Resource: API Design for System Design Interviews](https://www.hellointerview.com/learn/system-design/core-concepts/api-design)

## Context
You are tasked with designing the communication protocol for a new microservices architecture. One service is a public-facing mobile gateway, and the other is a high-throughput internal analytics engine.

## Questions

1. **Why/How:** Why would you choose gRPC over REST for the internal analytics engine? Mention specific benefits regarding serialization and network performance.
2. **Standardization:** How does gRPC handle the "Interface Definition" differently than a standard RESTful API (e.g., OpenAPI/Swagger)?
3. **Tradeoffs:** In what scenario would REST be a superior choice for the mobile gateway compared to gRPC? (Consider browser support and payload human-readability).
4. **Performance:** Explain the role of HTTP/2 in gRPC and how it differs from the standard request-response cycle of HTTP/1.1 used by most REST APIs.
