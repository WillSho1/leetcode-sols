# High-Level Design: Notification Service

## Requirements
- Support multiple channels (Email, SMS, Push).
- Guarantee delivery (at-least-once).
- Handle massive scale (billions of notifications/day).
- Rate-limiting (prevent spamming the same user).

## Components to Design
1. **API Gateway / Load Balancer**
2. **Rate Limiting Engine**
3. **Notification Service (Core Logic)**
4. **Message Queues (Kafka/RabbitMQ)**
5. **Worker Nodes (Processing and sending)**
6. **Third-Party Integrations (SendGrid, Twilio, APNS/FCM)**
7. **Database (User preferences, status logs)**

## Review & Correct
- [ ] How do we handle duplicate notifications?
- [ ] How do we prioritize urgent notifications (e.g., OTP) vs non-urgent (e.g., promotional)?
- [ ] What is the fallback mechanism if a third-party provider is down?
