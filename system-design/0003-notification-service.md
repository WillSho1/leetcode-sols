# High-Level Design: Notification Service

## Requirements
- Support multiple channels (Email, SMS, Push).
- Guarantee delivery (at-least-once) using retry logic.
- Handle massive scale (billions of notifications/day) via distributed workers.
- Rate-limiting (prevent spamming the same user within set windows).

## Components to Design
1. **API Gateway / Load Balancer**: Entry point for internal services to trigger notifications.
2. **Rate Limiting Engine**: Redis-based check to verify if a user has exceeded their notification quota.
3. **Notification Service (Core Logic)**: Validates requests, fetches user preferences, and routes to the correct channel.
4. **Message Queues (Kafka/RabbitMQ)**: Decouples the request from the sending. Each channel (Email/SMS) has its own topic to prevent one slow provider from blocking others.
5. **Worker Nodes**: Consumer processes that pull from the queue and interact with third-party APIs.
6. **Third-Party Integrations**: SendGrid (Email), Twilio (SMS), Firebase/APNS (Push).
7. **Database (Cassandra/Postgres)**: Stores user notification settings and a log of notification statuses.

## Review & Correct (Answers)
- **How do we handle duplicate notifications?** 
  Implement **Idempotency Keys**. Each notification request is assigned a unique UUID. Workers check a distributed cache (Redis) before sending to ensure that specific UUID hasn't already been processed.
- **How do we prioritize urgent notifications (e.g., OTP) vs non-urgent (e.g., promotional)?**
  Use **Weighted Queues** or separate Kafka Topics. OTPs go into a `high-priority` queue with a larger pool of dedicated workers, while marketing blasts go into a `low-priority` bulk queue.
- **What is the fallback mechanism if a third-party provider is down?**
  Implement the **"Circuit Breaker" pattern**. If SendGrid fails several times, the system automatically flips to a secondary provider (like AWS SES) for a set cooldown period before retrying the primary.

## Reference Material for Review
- [System Design Primer: Notification Service](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/notification_service/README.md)
- [Grokking System Design: Designing a Notification System](https://www.educative.io/blog/complete-guide-to-system-design#notification-system)
