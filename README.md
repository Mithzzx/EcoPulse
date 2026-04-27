# EcoPulse

Decentralized edge-AI architecture for autonomous household energy management using reinforcement learning.

## Overview

EcoPulse is a smart home energy optimization project designed to reduce electricity cost and avoid unnecessary consumption without relying on cloud control loops. The system combines:

- Edge inference and decision-making on a local gateway
- Non-Intrusive Load Monitoring (NILM) for appliance-level disaggregation from aggregate power
- Proximal Policy Optimization (PPO) for adaptive appliance orchestration
- Occupancy and environmental sensing for context-aware control

The project currently includes a browser-based simulation and a formal technical proposal describing the full architecture and projected performance.

## Problem Statement

Urban households often experience avoidable energy waste due to fixed schedules, always-on devices, and manual control behavior. Conventional cloud-managed automation can also introduce latency and privacy risks.

EcoPulse addresses this by keeping sensing, inference, and control on the local network and optimizing decisions continuously through a perception-reasoning-actuation loop.

## Objectives

- Minimize household electricity expenditure while preserving user comfort
- Reduce carbon emissions associated with unnecessary load
- Enable low-latency and privacy-preserving control at the edge
- Provide a practical path from simulation to real deployment

## System Architecture

EcoPulse is organized into four logical layers:

1. Sensing and telemetry
    - Aggregate power monitoring (for example, PZEM-004T)
    - Context sensors such as PIR, DHT22, and ambient light sensors
2. Edge intelligence
    - NILM pipeline for appliance-level signal separation
    - LSTM-based temporal consumption modeling
    - PPO policy for control decisions
3. Communication and control
    - Local MQTT message bus
    - ESP32 endpoints for relay-level appliance actuation
4. Feedback and supervision
    - Simulation dashboard
    - Logging of reward, overrides, and projected outcomes

## Optimization Formulation

The control objective balances energy savings and comfort penalties:

R = w1 * E_saved - w2 * C_penalty

Where:

- E_saved is energy reduction relative to baseline usage
- C_penalty captures discomfort or override events
- w1 and w2 are tunable trade-off weights

## Projected Performance (Proposal Baseline)

The proposal reports the following projected monthly outcomes for a representative urban household scenario:

| Metric | Baseline | EcoPulse | Reduction |
| --- | ---: | ---: | ---: |
| Energy consumption | 450 kWh | 308 kWh | 31.5% |
| Monthly bill | INR 3825 | INR 2610 | INR 1215 |
| Carbon footprint | 369 kg CO2 | 252 kg CO2 | 117 kg CO2 |

Estimated annual bill reduction from this scenario is approximately INR 14580.

## Simulation

An interactive simulation is available at:

- simulation/ecopulse_simulation.html

The simulator includes:

- Real-time power and cost tracking
- Baseline versus optimized consumption comparison
- Appliance-level AI/manual control switching
- Occupancy-aware behavior
- NILM-style disaggregation visualization
- RL event log and projected monthly outcomes

## Getting Started

### Prerequisites

- macOS, Linux, or Windows
- A modern web browser

### Run the Simulation

From the repository root:

```bash
open simulation/ecopulse_simulation.html
```

Alternative cross-platform approach:

1. Open simulation/ecopulse_simulation.html directly in your browser.
2. Interact with controls for simulation speed, pause/resume, and manual overrides.

## Repository Structure

Current top-level structure:

```text
EcoPulse/
├── README.md
├── LICENSE
├── backend/
├── docs/
│   ├── proposal.md
│   └── PCL(2).pdf
├── experiments/
├── hardware/
├── models/
└── simulation/
     └── ecopulse_simulation.html
```

## Technology Stack

- Frontend simulation: HTML, CSS, JavaScript, Chart.js
- Learning methods: PPO (policy optimization), NILM pipeline with sequence modeling
- Edge deployment target: Raspberry Pi class gateway with ESP32 endpoints
- Messaging: MQTT (proposed integration path)

## Documentation

- Technical proposal: docs/proposal.md
- Reference paper artifact: docs/PCL(2).pdf

## Development Status

Current stage:

- Completed: architecture proposal and simulation prototype
- In progress: model packaging and hardware integration planning
- Planned: end-to-end edge deployment and field evaluation

## Roadmap

- Integrate trained NILM and PPO checkpoints into a deployable edge runtime
- Add real device telemetry ingestion through MQTT topics
- Implement robust safety constraints and fallback policies
- Evaluate performance on real household traces
- Extend to solar-aware and multi-home optimization workflows

## Authors

- Mithun Rajan
- Sabaris S
- Vikrant S

## License

This project is distributed under the MIT License. See LICENSE for details.
