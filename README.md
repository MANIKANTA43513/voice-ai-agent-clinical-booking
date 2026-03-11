Real-Time Multilingual Voice AI Agent

Clinical Appointment Booking System

A Real-Time Multilingual Voice AI Agent capable of handling clinical appointment management through natural voice conversations.
The system processes speech input, understands user intent using an AI agent, executes appointment-related operations, and responds back in voice.

This project demonstrates real-time AI system architecture, agent reasoning, scheduling logic, and multilingual interaction capabilities.

---

Project Overview

The AI agent enables patients to interact with a healthcare system using voice to:

- Book appointments
- Reschedule appointments
- Cancel appointments
- Check doctor availability

The system processes voice input → reasoning → scheduling → voice response in a low-latency pipeline.

Supported languages:

- English
- Hindi
- Tamil

---

Key Features

Real-Time Voice Interaction

Users can communicate with the AI agent using voice commands.

Multilingual Support

The agent automatically detects and responds in:

- English
- Hindi
- Tamil

AI Agent Reasoning

The LLM-based agent interprets user requests and decides which system tool to execute.

Appointment Lifecycle Management

The system handles the complete appointment workflow:

- Booking
- Rescheduling
- Cancellation
- Conflict resolution

Contextual Memory

The agent maintains session-level context to track conversation state.

Conflict Handling

If a requested slot is unavailable, the system suggests alternative times.

---

System Architecture

The system follows a real-time voice processing pipeline.

"Architecture Diagram" (docs/architecture.png.jpeg)

Pipeline flow:

User Voice
↓
WebSocket Streaming
↓
Speech-to-Text
↓
Language Detection
↓
LLM Agent
↓
Tool Orchestration
↓
Appointment Scheduler
↓
Memory System
↓
Text Response
↓
Text-to-Speech
↓
Audio Response

---

Project Structure

voice-ai-agent-clinical-booking
│
├ agent
│   ├ agent.py
│   └ tools.py
│
├ backend
│   ├ main.py
│   ├ conversation.py
│   └ websocket_server.py
│
├ services
│   ├ speech_to_text.py
│   ├ text_to_speech.py
│   ├ language_detection.py
│   └ latency_logger.py
│
├ memory
│   └ session_memory.py
│
├ scheduler
│   └ appointment_engine.py
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

AI Components

Speech-to-Text

Converts spoken audio into text.

Technology used:

- Whisper STT

---

Language Detection

Detects user language automatically.

Languages supported:

- English
- Hindi
- Tamil

---

AI Agent (LLM)

The AI agent:

- Understands user intent
- Determines the required tool
- Executes scheduling actions

Example request:

Book appointment tomorrow at 5 pm

Agent output:

Intent: Book Appointment
Date: Tomorrow
Time: 5 PM

---

Tool Orchestration

The agent interacts with backend tools:

- Check availability
- Book appointment
- Cancel appointment
- Reschedule appointment

---

Appointment Scheduler

Handles scheduling rules:

- Prevents double booking
- Validates doctor availability
- Rejects past time slots
- Suggests alternatives

---

Memory Design

The system maintains session-level context memory.

Example conversation:

User: Book appointment
Agent: Which doctor?
User: Cardiologist

The memory stores:

intent: booking
doctor: cardiologist
date: pending

This ensures multi-turn conversations remain coherent.

Future improvements include:

- Redis-based memory
- Persistent patient history

---

Latency Design

The system is optimized for low latency.

Approximate pipeline latency:

Stage| Latency
Speech Recognition| ~150 ms
Agent Reasoning| ~200 ms
Response Generation| ~80 ms

Total Estimated Latency:

~430 ms

Target requirement:

< 450 ms

---

Running the Project

1 Install Dependencies

pip install -r requirements.txt

---

2 Run Backend Server

uvicorn backend.main:app --reload

API documentation will be available at:
Live API Deployment:
https://voice-ai-agent-clinical-booking.onrender.com

API Documentation:
https://voice-ai-agent-clinical-booking.onrender.com/docs



3 Test Voice Interaction

Run:

python voice_input.py

Speak commands such as:

Schedule meeting tomorrow at 5 pm
Cancel my appointment
Reschedule appointment to Friday

---

Testing Scenarios

Scenario| Expected Result
Book appointment| Appointment confirmed
Cancel appointment| Booking removed
Reschedule| Slot updated
Language switch| Agent adapts language
Conflict booking| Alternative slot suggested

---

Trade-offs

- Local STT model increases CPU usage but removes API dependency
- Session memory simplifies implementation but limits long-term personalization
- In-memory scheduler used for simplicity instead of full database

---

Known Limitations

- Persistent patient history not implemented
- Redis memory not integrated yet
- Outbound campaign calling not implemented
- Deployment not configured

---

Future Improvements

Planned enhancements include:

- Redis-backed memory with TTL
- Cloud deployment
- Horizontal scalability
- Background job queue for reminder campaigns
- Real-time WebRTC voice streaming
- Interrupt / barge-in voice handling

---

Demo

A working demo includes:

- Real-time voice interaction
- Speech-to-text conversion
- Agent reasoning
- Appointment scheduling

---

Repository

GitHub Repository:

https://github.com/MANIKANTA43513/voice-ai-agent-clinical-booking

---

Author

Manikanta
AI / Backend Developer

---

License

This project is intended for educational and engineering evaluation purposes.
