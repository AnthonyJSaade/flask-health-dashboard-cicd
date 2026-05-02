from flask import Flask, jsonify, render_template_string

from diagnostics import build_health_response, build_report_response, load_config

app = Flask(__name__)
config = load_config()

DASHBOARD_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ report.application }}</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 32px;
        background: #f4f7fb;
        color: #1f2937;
      }
      .card {
        max-width: 780px;
        margin: 0 auto;
        background: #ffffff;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
      }
      h1 {
        margin-top: 0;
      }
      .status {
        display: inline-block;
        padding: 8px 12px;
        border-radius: 999px;
        background: #dcfce7;
        color: #166534;
        font-weight: 700;
        text-transform: uppercase;
      }
      dl {
        display: grid;
        grid-template-columns: 180px 1fr;
        gap: 12px;
      }
      dt {
        font-weight: 700;
      }
      a {
        color: #2563eb;
      }
    </style>
  </head>
  <body>
    <div class="card">
      <h1>{{ report.application }}</h1>
      <p class="status">{{ report.status }}</p>
      <dl>
        <dt>Environment</dt>
        <dd>{{ report.environment }}</dd>
        <dt>Hostname</dt>
        <dd>{{ report.hostname }}</dd>
        <dt>Python Version</dt>
        <dd>{{ report.python_version }}</dd>
        <dt>Platform</dt>
        <dd>{{ report.platform }}</dd>
        <dt>Uptime (seconds)</dt>
        <dd>{{ report.uptime_seconds }}</dd>
        <dt>Timestamp</dt>
        <dd>{{ report.timestamp }}</dd>
        <dt>Health API</dt>
        <dd><a href="/api/health">/api/health</a></dd>
        <dt>Report API</dt>
        <dd><a href="/api/report">/api/report</a></dd>
      </dl>
    </div>
  </body>
</html>
"""


@app.get("/")
def dashboard():
    report = build_report_response(config)
    return render_template_string(DASHBOARD_TEMPLATE, report=report)


@app.get("/api/health")
def api_health():
    return jsonify(build_health_response(config))


@app.get("/api/report")
def api_report():
    return jsonify(build_report_response(config))


if __name__ == "__main__":
    app.run(host=config["host"], port=int(config["port"]))
