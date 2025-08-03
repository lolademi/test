from fasthtml.common import *
import os

app = FastHTML()

counter = 0

@app.get("/")
def home():
    return Titled("HTMX Counter Example",
        Div(
            H1("HTMX Counter", cls="text-2xl font-bold mb-4"),
            Div(
                P(f"Current count: {counter}", id="counter", cls="text-xl mb-4"),
                Button("Increment",
                    hx_post="/increment",
                    hx_target="#counter",
                    cls="bg-blue-500 text-white px-4 py-2 rounded mr-2"),
                Button("Decrement",
                    hx_post="/decrement",
                    hx_target="#counter",
                    cls="bg-red-500 text-white px-4 py-2 rounded"),
                cls="p-4 bg-gray-100 rounded"
            ),
            cls="container mx-auto p-4"
        ),
        Script(src="https://cdn.tailwindcss.com")
    )

@app.post("/increment")
def increment():
    global counter
    counter += 1
    return P(f"Current count: {counter}", id="counter", cls="text-xl mb-4")

@app.post("/decrement")
def decrement():
    global counter
    counter -= 1
    return P(f"Current count: {counter}", id="counter", cls="text-xl mb-4")

if __name__ == "__main__":
    serve(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
