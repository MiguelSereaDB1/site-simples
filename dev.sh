#!/usr/bin/env bash
set -e

trap 'kill 0' SIGINT EXIT

(cd backend && uv run fastapi dev app/main.py) &
(cd frontend && npm run dev) &

wait
