# JINO AI

[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/afnan006/JINO.AI/issues)

A privacy-focused, context-aware conversational AI with dynamic personality and temporal intelligence capabilities. Jino AI maintains comprehensive conversational context while ensuring rigorous user data privacy protection.

[Live Demo](https://jino-ai.netlify.app/) Work In Progress | [Report Bug](https://github.com/afnan006/JINO.AI/issues) | [Request Feature](https://github.com/afnan006/JINO.AI/issues)

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Technical Implementation](#technical-implementation)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Deployment](#deployment)
- [Development Roadmap](#development-roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

Jino AI is an advanced conversational agent designed to deliver natural, contextually relevant interactions while adhering to stringent privacy standards. The project implements a sophisticated multi-model architecture leveraging OpenRouter to distribute specialized conversational tasks across purpose-optimized AI models:

- **DeepSeek R1**: Performs structured data extraction from conversational inputs
- **Mixtral 8x7B**: Handles context summarization and memory management
- **Yi 34B**: Generates contextually appropriate, personality-consistent responses

A custom fine-tuned model is currently under development to further enhance Jino's conversational intelligence and distinctive personality traits, with a addition of alarms and remainders using NLP from user message
"I have a meeting at 10am tommorow" Remainder set to 10am with a custom message.

## Key Features

- 🔒 **Privacy-First Architecture**: End-to-end design that prioritizes user data protection with localized context management
- 🧠 **Advanced Context Retention**: Maintains comprehensive conversation history for contextually coherent dialogue
- ⏰ **Temporal Intelligence**: Sophisticated awareness of time-related contexts and conversation timeframes
- 🎭 **Consistent Personality**: Delivers engaging, coherent character expression throughout user interactions
- 🔄 **Multi-Model Orchestration**: Intelligently leverages specialized AI models for distinct conversational functions
- 📊 **Developer Insights Panel**: Real-time visualization of internal processing for development and debugging
- 🌐 **Modern Web Interface**: Responsive, accessible design built with React and Tailwind CSS

## System Architecture

Jino AI employs a three-tier architecture that separates concerns between data extraction, context management, and response generation:

1. **Data Extraction Layer**: Processes incoming messages to identify entities, intents, and sentiment
2. **Context Management Layer**: Maintains conversation history with intelligent summarization
3. **Response Generation Layer**: Creates contextually appropriate, personality-consistent replies

This modular design allows for independent scaling and optimization of each component while maintaining coherent system behavior.

## Technical Implementation

### Backend

- Flask-based RESTful API handling all core AI processing functions
- Multi-model integration via OpenRouter API for specialized conversational tasks
- Advanced memory management system for efficient context retention and retrieval
- Sophisticated judgment logic for evaluating user intent, sentiment, and conversation flow
- Temporal awareness module for time-sensitive contextual responses

### Frontend

- Modern React application built with Vite for optimal development experience
- Responsive UI implementation using Tailwind CSS utility framework
- Component-based architecture for maintainability and reusability
- Firebase integration with Google SignIn authentication and data persistence capabilities
- Real-time message streaming for natural conversation flow with local device timestamps

## Project Structure

```
├── Backend/jino-backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── context.py
│   │   │   ├── extract.py
│   │   │   └── reply.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── judgement.py
│   │       ├── memory.py
│   │       ├── openrouter_client.py
│   │       ├── time.py
│   │       └── uuid_gen.py
│   ├── memory_store/
│   ├── config.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── run.py
│   └── wsgi.py
└── Frontend/jino-ui/
    ├── src/
    │   ├── App.jsx
    │   ├── firebase.js
    │   ├── index.css
    │   ├── main.jsx
    │   └── components/
    │       ├── ChatWindow.jsx
    │       ├── DevPanel.jsx
    │       ├── Home.jsx
    │       ├── Loader.jsx
    │       ├── LoginModal.jsx
    │       ├── MessageBubble.jsx
    │       └── Navbar.jsx
    ├── package.json
    ├── vite.config.js
    ├── tailwind.config.js
    ├── postcss.config.js
    └── eslint.config.js
```

## Installation & Setup

### Prerequisites

- Python 3.9+
- Node.js 16+
- OpenRouter API key
- Git

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/afnan006/JINO.AI.git
   cd JINO.AI/Backend/jino-backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with necessary environment variables:
   ```
   OPENROUTER_API_KEY=your_openrouter_api_key
   FLASK_ENV=development
   ```

5. Start the Flask server:
   ```bash
   python run.py
   ```

The backend will be available at http://localhost:5000.

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd JINO.AI/Frontend/jino-ui
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file with necessary environment variables:
   ```
   VITE_API_URL=http://localhost:5000
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at http://localhost:5173.

## Deployment

- **Backend**: Currently deployed on [Render](https://render.com)
- **Frontend**: Currently deployed on [Netlify](https://netlify.com)

Comprehensive deployment documentation is available in the [deployment guide](./docs/deployment.md).

## Development Roadmap

- [ ] Complete custom model fine-tuning for enhanced conversational abilities
- [ ] Add conversation export/import functionality for data portability
- [ ] Enhance personality traits with customization options
- [ ] Optimize response latency and system reliability
- [ ] Develop companion mobile application
- [ ] Implement advanced analytics for conversation insights
- [ ] Add multilingual support capabilities

## Contributing

Jino AI is an open-source project, and contributions are enthusiastically welcomed. Whether you're fixing bugs, improving documentation, or proposing new features, your input is valuable.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please refer to the [contribution guidelines](./CONTRIBUTING.md) for detailed information.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact

**Afnan Ahmed** - [afnan006cs@gmail.com](mailto:afnan006cs@gmail.com)

Project Link: [https://github.com/afnan006/JINO.AI](https://github.com/afnan006/JINO.AI)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

Built with Curiosity by Afnan Ahmed, Aspiring AI Backend Developer.
