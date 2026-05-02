import json
import os
import platform
import socket
import time
from datetime import datetime, timezone
from pathlib import Path

START_TIME = time.time()
CONFIG_PATH = Path(__file__).with_name("config.json")


def load_config():
    defaults = {
        "app_name": "Flask System Health Dashboard",
        "environment": "development",
        "status": "ok",
        "host": "0.0.0.0",
        "port": 8080,
    }

    if CONFIG_PATH.exists():
        with CONFIG_PATH.open("r", encoding="utf-8") as config_file:
            file_config = json.load(config_file)
            if isinstance(file_config, dict):
                defaults.update(file_config)

    env_port = os.getenv("PORT") or os.getenv("APP_PORT")
    if env_port and env_port.isdigit():
        defaults["port"] = int(env_port)

    env_label = os.getenv("APP_ENV")
    if env_label:
        defaults["environment"] = env_label

    return defaults


def _timestamp_utc():
    return datetime.now(timezone.utc).isoformat()


def _uptime_seconds():
    return int(max(0, time.time() - START_TIME))


def build_health_response(config):
    return {
        "application": config["app_name"],
        "status": config["status"],
        "environment": config["environment"],
        "timestamp": _timestamp_utc(),
    }


def build_report_response(config):
    return {
        "application": config["app_name"],
        "status": config["status"],
        "environment": config["environment"],
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "uptime_seconds": _uptime_seconds(),
        "timestamp": _timestamp_utc(),
        "api_routes": {
            "health": "/api/health",
            "report": "/api/report",
        },
    }
