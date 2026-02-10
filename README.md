# pattern-hunter

# What is Candlestick Pattern

https://groww.in/blog/candlestick-patterns


# High Level Architecutre
```
                ┌──────────────┐
                │   Telegram   │
                │   (Commands) │
                └──────┬───────┘
                       │
               ┌───────▼────────┐
               │   OpenClaw     │
               │ (Orchestrator) │
               └───────┬────────┘
                       │
        ┌──────────────▼──────────────┐
        │       PatternHunter Core    │
        │   (Python Backend Engine)   │
        └──────────────┬──────────────┘
                       │
      ┌────────────────▼────────────────┐
      │      Market Data Layer          │
      │      (yfinance / UpStox API)    │
      └────────────────┬────────────────┘
                       │
        ┌──────────────▼──────────────┐
        │ Pattern Detection Engine    │
        └──────────────┬──────────────┘
                       │
        ┌──────────────▼──────────────┐
        │ Chart / Visualization Layer │
        └──────────────┬──────────────┘
                       │
        ┌──────────────▼──────────────┐
        │  AI Interpretation (Ollama) │
        └──────────────┬──────────────┘
                       │
                ┌──────▼───────┐
                │  Telegram    │
                │  (Alerts)    │
                └──────────────┘
```

# Data Flow (End-to-End)
```
User adds stock (Telegram)
        ↓
OpenClaw updates watchlist
        ↓
Scheduler triggers scan
        ↓
Market data fetched
        ↓
Patterns detected
        ↓
Chart generated (if signal)
        ↓
Ollama summarizes signal
        ↓
Telegram alert sent
User adds stock (Telegram)
        ↓
OpenClaw updates watchlist
        ↓
Scheduler triggers scan
        ↓
Market data fetched
        ↓
Patterns detected
        ↓
Chart generated (if signal)
        ↓
Ollama summarizes signal
        ↓
Telegram alert sent
User adds stock (Telegram)
        ↓
OpenClaw updates watchlist
        ↓
Scheduler triggers scan
        ↓
Market data fetched
        ↓
Patterns detected
        ↓
Chart generated (if signal)
        ↓
Ollama summarizes signal
        ↓
Telegram alert sent
```


# Folder Structure
```
pattern-hunter/
│
├── patternhunter/
│   ├── __init__.py
│   ├── config.py
│   ├── scanner.py
│   ├── patterns.py
│   ├── charts.py        # later
│   │
│   └── data/
│       ├── __init__.py
│       ├── base.py
│       └── yfinance_provider.py
│
├── requirements.txt
└── README.md
```
