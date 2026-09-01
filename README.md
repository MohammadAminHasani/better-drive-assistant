![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-v1.0-green)

# Better Drive Assistant

A modular, Python-based driving assistant that plans routes, estimates journey costs, and analyzes trips to help users make informed decisions before and during a drive.

## Overview

Planning a drive usually means juggling several disconnected tools: one for directions, another for estimating fuel cost, and a mental checklist for judging whether a trip is going to be easy or exhausting. Better Drive Assistant brings these concerns together into a single, coherent workflow.

Rather than treating routing as the end goal, the project treats it as one input to a broader picture of a journey — combining location resolution, route generation, cost estimation, and trip analysis so a user can understand not just *how* to get somewhere, but what the trip will actually cost and demand of them.

The project is built with a service-oriented architecture from the ground up, so it can grow from a command-line tool into additional interfaces without a rewrite.

## Key Features

These are the stable, implemented capabilities the project is built around. They are intentionally described at a conceptual level so this section stays accurate as the implementation evolves.

- **Route planning** — Resolves user-provided locations and generates driving routes between them, including multi-stop journeys, with distance, duration, and step-by-step navigation instructions.
- **Location resolution** — Converts addresses into geographic coordinates, validates matches, and handles ambiguous or unknown locations gracefully instead of failing outright.
- **Fuel cost estimation** — Calculates estimated fuel usage and cost for a journey based on distance, vehicle efficiency, and fuel price.
- **Trip analysis** — Classifies journeys (e.g. by length) and evaluates driving difficulty based on distance and duration, surfacing practical recommendations rather than raw numbers alone.
- **Resilient by design** — Defensive handling of network failures, timeouts, invalid API responses, and bad user input, so the application degrades gracefully instead of crashing.
- **Structured logging** — Application activity (searches, routing requests, failures, successes) is logged to support debugging and iterative improvement.
- **Secure configuration** — API keys and other sensitive values are kept out of source control and managed through environment-based configuration.

## How It Works

At a high level, a journey moves through four stages:

1. **Location resolution** — Raw address input is turned into validated geographic coordinates.
2. **Route generation** — Coordinates are passed to a routing provider, which returns distance, duration, and navigation steps for the full multi-stop journey.
3. **Cost calculation** — Route distance is combined with vehicle and fuel data to estimate fuel usage and cost.
4. **Trip analysis** — The resulting route and cost data are evaluated to classify the trip and generate recommendations.

Each stage is handled by an isolated service, coordinated by a central entry point. This separation means any stage — the routing provider, the cost model, the analysis logic — can be modified or replaced without affecting the others.

## Project Structure

```
Better-Drive-Assistant/
├── main.py                  # Application entry point / orchestration
├── core/
│   └── trip_analyzer.py     # Trip classification, difficulty analysis, recommendations
├── services/
│   ├── geo_coding.py        # Address resolution and validation
│   ├── routing.py           # Route generation, distance and duration calculation
│   └── cost_engine.py       # Fuel usage and cost estimation
├── utils/
│   └── logger.py            # Application-wide logging
├── config.py                 # Configuration loading
└── requirements.txt
```

The structure separates *services* (external-facing integrations), *core logic* (domain analysis independent of any provider), and *utilities* (cross-cutting concerns like logging and configuration). New capabilities are expected to slot into this structure as additional services or core modules rather than requiring architectural changes.

## Technologies Used

- **Python 3** — core language
- **Requests** — HTTP communication with external APIs
- **OpenStreetMap Nominatim API** — geocoding and location search
- **GraphHopper Routing API** — route generation and navigation data
- **python-dotenv** — environment-based configuration
- **Python `logging` module** — structured application logging

## External Services

This project uses:

- OpenStreetMap Nominatim for geocoding
- GraphHopper for routing services

Their respective terms and licenses apply.

## Installation and Setup

```bash
# Clone the repository
git clone https://github.com/MohammadAminHasani/Better-Drive-Assistant.git
cd Better-Drive-Assistant

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# then edit .env with your API keys (e.g. GraphHopper)
```

The application reads configuration from environment variables at startup, so no source changes are required to supply API credentials or adjust runtime settings.

## Usage Example

```bash
python main.py
```

The CLI guides the user through entering departure, stop, and destination locations, then returns a full trip summary:

```
ROUTE OVERVIEW

Category:         Long Trip
Driving Level:     Demanding
Distance:          450 km
Estimated Time:    5 hours 20 minutes
Fuel Used:         33.75 L
Fuel Cost:         60.75
```

## Roadmap

The long-term direction for the project, at a conceptual rather than promissory level:

- **Personalization** — vehicle-specific profiles and user preferences that refine cost and recommendation accuracy.
- **Journey history** — persistent trip records and driving insights over time.
- **Broader interfaces** — a web-based experience alongside the CLI, built on the existing service architecture.
- **Context-aware recommendations** — incorporating factors such as traffic and weather into trip analysis.
- **Mobile access** — extending the assistant beyond desktop/CLI environments.

This roadmap describes direction, not commitments — specific features will be designed and scoped as the project evolves.

## Contributing

This project is developed as a personal engineering effort, but suggestions, issue reports, and pull requests are welcome. If you'd like to contribute, please open an issue first to discuss the change you have in mind.

## License

MIT License

## Author

MohammadAmin