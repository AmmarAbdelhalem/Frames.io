import reflex as rx
from .Backend.main import fapp
# Create the Reflex app
app = rx.App()

# Add your frontend pages to Reflex
def index():
    return rx.text("Welcome to my Reflex app!")

app.add_page(index)

async def gethello():
    return {"hello": "heelo"}

# Mount the FastAPI app onto Reflex
app.api = fapp
app.api.add_api_route("/api/hello/", gethello)