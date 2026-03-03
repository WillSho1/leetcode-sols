# System Design Concept: Load Balancing (Level 1)

*Answer these based on your current understanding or quick research. No corporate fluff—just the engineering "why".*

### 1. What is a Load Balancer (LB)?
I have no clue, but judging by the questions, I would assume that a load balancer is used to distribute traffic among different servers.

### 2. Why do we need an LB? (What happens to a single server when 10,000 people hit it at once?)
We need a load balancer because a single server cannot manage 10,000 requests at once, and they must be distributed among all available servers.

### 3. If you have 3 servers (A, B, C), what is the "fair" way to distribute traffic between them? (Hint: Think "Round-robin")
I would distribute more traffic towards a server that is facing less load?

### 4. What is a "Single Point of Failure" (SPOF)? How can an LB both solve and create a SPOF?
I am not sure. I need to review load balancing.
