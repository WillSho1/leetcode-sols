# System Design: API Design (REST vs gRPC)
Category: System Design/API Design

## Core Concepts: REST
- **Protocol:** HTTP/1.1 (usually).
- **Payload:** JSON or XML.
- **Communication:** Request/Response, Stateless.
- **Pros:** Human-readable, browser support, ubiquitous.
- **Cons:** Text-heavy (larger payloads), no streaming (usually).

## Core Concepts: gRPC
- **Protocol:** HTTP/2.
- **Payload:** Protocol Buffers (Binary).
- **Communication:** Unary, Server Streaming, Client Streaming, Bi-directional Streaming.
- **Pros:** Highly efficient, strongly typed (via .proto), built-in streaming.
- **Cons:** Not browser-native, requires tools to debug/read.

## When to use which?
- **REST:** Public-facing APIs, web clients, simplicity.
- **gRPC:** Internal microservices, high-performance needs, polyglot environments.
