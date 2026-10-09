from flask import Flask, Response
from prometheus-client import Counter, generate_latest, CONTENT_TYPE_LATEST
myapp = Flask(__name__)

RESPONSE_COUNT = Counter(
    "student_portal_request_total",
    "Total number of request to student portal",
    ["endpoint"]
)

@myapp.route("/home")
def home_page():
    RESPONSE_COUNT.labels(endpoint = "/home").inc()
    return"""
    <h1>Home Page</h1>
    """

@myapp.route("/about")
def about_us():
    RESPONSE_COUNT.labels(endpoint = "/about").inc()
    return"""
    <h1>Home Page</h1>
    """
@myapp.route("/contact")
def contact_page():
    RESPONSE_COUNT.labels(endpoints = "/contact").inc()
    return"""
    <h1>Contact Page</h1>
    """
@myapp.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    myapp.run("0.0.0.0.",port = 5000)
