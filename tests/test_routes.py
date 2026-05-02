import unittest

from app import app


class RouteTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_dashboard_route_returns_html(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Flask System Health Dashboard", response.data)
        self.assertIn(b"/api/health", response.data)

    def test_health_route_returns_expected_json(self):
        response = self.client.get("/api/health")
        payload = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["application"], "Flask System Health Dashboard")
        self.assertIn("timestamp", payload)

    def test_report_route_returns_system_data(self):
        response = self.client.get("/api/report")
        payload = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(payload["status"], "ok")
        self.assertIn("hostname", payload)
        self.assertIn("python_version", payload)
        self.assertIn("uptime_seconds", payload)
        self.assertIn("api_routes", payload)


if __name__ == "__main__":
    unittest.main()
