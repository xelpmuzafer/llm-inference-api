# LLM Inference API

A production-ready REST API for serving Large Language Models with FastAPI, designed for low-latency inference and easy deployment.

## Features

- **FastAPI** — async, high-performance API server
- **Structured outputs** — JSON schema support for tool use and parsing
- **Health checks** — readiness and liveness endpoints for Kubernetes
- **Configurable** — model name, max tokens, and temperature via environment

## Requirements

- Python 3.10+
- (Optional) CUDA for GPU acceleration

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Set environment variables:

- `MODEL_NAME` — model identifier (default: `meta-llama/Llama-3.2-3B`)
- `MAX_TOKENS` — max generation length (default: `1024`)
- `TEMPERATURE` — sampling temperature (default: `0.7`)

## Usage

Run the server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Endpoints

- `GET /health` — liveness probe
- `GET /ready` — readiness (model loaded)
- `POST /v1/chat/completions` — OpenAI-compatible chat completions
- `POST /v1/completions` — text completion

## License

MIT
