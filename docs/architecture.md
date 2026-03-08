# System Architecture

This project implements a real-time multilingual voice AI agent capable of managing clinical appointments through natural voice conversations.

The architecture follows a real-time voice processing pipeline designed for low latency.

## Architecture Diagram

![Voice AI Agent Architecture](architecture.png)

## Processing Pipeline

User Voice  
↓  
WebSocket Streaming  
↓  
Speech-to-Text (Whisper)  
↓  
Language Detection  
↓  
LLM Agent  
↓  
Tool Orchestration  
↓  
Appointment Scheduler  
↓  
Memory Layer (Session + Persistent)  
↓  
Text Response  
↓  
Text-to-Speech  
↓  
Audio Response