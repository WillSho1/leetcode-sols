# System Design Concept: Consistent Hashing

*Scenario: You are using `hash(key) % N` to distribute data across N servers.*

### 1. The Membership Problem
If you have 3 servers (N=3) and you add a 4th (N=4), what happens to the result of `hash(key) % N` for all your existing data? 

The simple modulo would change for every single piece of data.

### 2. The Re-sharding Nightmare
When the server count changes, do you have to move your data? How much of it?
Yes, if you add or remove a server, since the key would change for most of the data, there would have to be a big migration.

### 3. What is "Consistent Hashing" in one sentence? 
(Hint: It minimizes the number of keys that need to be remapped when N changes.)
Consistent hashing is a method of hashing that avoids the re-sharding nightmare of mapping with a simple modulo by placing the servers and user ids in a circle, and assigning the users to the first server they hit going clockwise. When one server goes down, or one is added, only the users belonging to the server must move.