Previous work
Up to this point, the work was experimental: we tested different frameworks, models and designs. From what we learned, we have formulated a proper architecture. The next step is to implement it for the Phase 1 presentation. Through this trial-and-error phase, we also refined our idea, objectives and designs.

Context
Main aim: Build a voice assistant that lets people with partial or full immobility control their computers and work more productively. The goal is not just to complete tasks, but to complete them efficiently.

Project Objectives
To develop a modular agent package that enables desktop navigation, system control and file management through the operating system's native APIs and UI tree.

To implement an audio package that converts spoken commands into text using a lightweight, CPU-only speech recognition model.

To design a context manager that serves as the user's second brain, storing personal information, work information and documents alongside screen state and interaction history, so that short, relative and personal commands are interpreted correctly.

To integrate productivity plugins through the Model Context Protocol (MCP), enabling browser navigation and connections to Antigravity, Claude, PowerPoint, Word and Canva.

Methodology
Phase 1: Requirement Analysis and Model Selection
Define the use case and constraints, then select the speech recognition and tool-calling models that fit them.

Phase 2: System and Module Design
Design the audio, agent, context manager and plugin modules and the interfaces between them.

Phase 3: Experimentation and Redesign
Test design choices on small prototypes, such as router thresholds and context resolution order, and refine the initial design.

Phase 4: MVP Architecture Implementation
Build the end-to-end prototype, starting with Windows.

Phase 5: Testing and Evaluation
Evaluate the architecture on a benchmark of about 300 commands for command success (with and without the context manager), latency, memory usage and user experience.

Phase 6: Real-Time Audio Testing
Test the complete system with live spoken commands to measure speech recognition accuracy, end-to-end response time and usability, including soft and fatigued speech.

Methodology
Phase 3 correction mvp on Linux

