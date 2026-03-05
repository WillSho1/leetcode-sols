# System Design Concept: Consistent Hashing

*Scenario: You are using `hash(key) % N` to distribute data across N servers.*

### 1. The Membership Problem
If you have 3 servers (N=3) and you add a 4th (N=4), what happens to the result of `hash(key) % N` for all your existing data? 

### 2. The Re-sharding Nightmare
When the server count changes, do you have to move your data? How much of it?

### 3. What is "Consistent Hashing" in one sentence? 
(Hint: It minimizes the number of keys that need to be remapped when N changes.)
