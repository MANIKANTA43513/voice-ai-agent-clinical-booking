Real-Time Multilingual Voice AI Agent

Clinical Appointment Booking System

A real-time voice AI agent designed for a digital healthcare platform that allows patients to manage clinical appointments using natural voice conversations.

The system processes spoken input, detects the language, interprets user intent through an AI agent, and responds with appointment scheduling actions.

This project demonstrates low-latency voice pipelines, agentic reasoning, tool orchestration, and contextual memory design.

---

Key Features

Voice Conversation Agent

The system accepts voice input from the user, converts it into text, interprets intent using an AI agent, and performs scheduling actions.

Supported actions include:

- Appointment booking
- Appointment rescheduling
- Appointment cancellation
- Conflict detection and alternative slot suggestions

---

Multilingual Support

The agent is designed to support conversations in:

- English
- Hindi
- Tamil

The system detects the spoken language and processes the conversation accordingly.

Example inputs:

English

Book appointment with cardiologist tomorrow

Hindi

मुझे कल डॉक्टर से मिलना है

Tamil

நாளை மருத்துவரை பார்க்க வேண்டும்

---

System Architecture

The system follows a real-time voice processing pipeline designed for modularity and low latency.

User Voice
↓
WebSocket Streaming
↓
Speech-to-Text (Whisper)
↓
Language Detection
↓
AI Agent
↓
Tool Orchestration
↓
Appointment Scheduler
↓
Memory Layer
↓
Text Response
↓
Text-to-Speech
↓
Audio Response

Architecture Diagram:

docs/architecture.png

---

Memory Design

The system maintains context at two levels.

Session Memory

Stores temporary conversation state such as:

- current user intent
- pending confirmations
- conversation context

Example:

User: Book appointment
Agent: Which doctor?
User: Cardiologist

Session memory tracks the pending intent.

---

Persistent Memory

Stores long-term patient information:

- language preference
- previous appointments
- preferred doctors

This enables continuity across multiple interactions.

---

Appointment Scheduling Logic

The system prevents invalid bookings through validation rules.

Checks include:

- doctor availability
- double booking prevention
- past time selection validation

Example:

If a requested slot is unavailable, the system suggests alternatives.

Example response:

The requested slot is unavailable.
Available slots are 2 PM and 4 PM.

---

Real-Time API Access

Backend server exposes APIs through FastAPI.

After running the server, API documentation is available at:

http://127.0.0.1:8000/docs

This interactive documentation allows testing endpoints directly.

Example endpoint:

POST /process

---

Latency Breakdown

The system is designed to meet the target latency requirement.

Stage| Estimated Latency
Speech-to-Text| ~150 ms
Agent reasoning| ~200 ms
Response generation| ~80 ms

Estimated total latency:

~430 ms

Target requirement:

< 450 ms

---

Setup Instructions

1 Clone Repository

git clone <repository_url>

2 Install Dependencies

pip install -r requirements.txt

3 Start Backend Server

uvicorn backend.main:app --reload

Open API docs:

http://127.0.0.1:8000/docs

---

4 Run Voice Agent

python voice_input.py

Example command:

Speak into microphone:

Schedule meeting tomorrow at 7 PM

Example response:

AI Agent received: schedule meeting tomorrow at 7 PM

---

Project Structure

voice-ai-agent
│
├ agent
│   ├ agent.py
│   └ tools.py
│
├ backend
│   ├ main.py
│   ├ websocket_server.py
│   └ conversation.py
│
├ services
│
├ memory
│
├ scheduler
│
├ docs
│   ├ architecture.md
│   └ architecture.png
│
├ voice_input.py
├ test_client.py
├ requirements.txt
└ README.md

---

Trade-offs

Some design decisions were made to simplify the implementation:

- Local speech processing instead of cloud streaming
- Lightweight memory layer instead of Redis-backed distributed memory
- Simplified scheduling logic for demonstration purposes

These decisions keep the architecture modular and easy to extend.

---

Known Limitations

- Full multilingual conversational optimization is limited
- Redis-based memory system not implemented
- Persistent database integration simplified
- Outbound campaign automation not fully implemented

---

Future Improvements

Possible improvements include:

- Redis-backed memory with TTL
- Advanced multilingual conversation handling
- Real-time streaming speech recognition
- Cloud deployment and horizontal scalability
- Background job queues for appointment reminders
- Interrupt handling (barge-in) during agent responses

---

Demo

The system can be demonstrated by running the voice client locally.

Voice input is processed and interpreted by the AI agent to perform scheduling tasks.

Example interaction:

User Voice

Schedule meeting tomorrow at 7 PM

Agent Response

Meeting scheduled for tomorrow at 7 PM

---

Author

Manikanta Kandula
MCA Student
AI / Backend Development
