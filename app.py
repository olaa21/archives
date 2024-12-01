from flask import Flask, render_template, jsonify
import json
import logging

# Initialize Flask app and specify 'pages' as the template folder
app = Flask(__name__, template_folder='pages')

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)  # DEBUG level logs everything
logger = logging.getLogger(__name__)

# Load content from the JSON file
def load_content():
    try:
        with open('data/content.json', 'r') as file:
            logger.debug("Loading content from JSON file.")
            return json.load(file)
    except FileNotFoundError as e:
        logger.error(f"JSON file not found: {e}")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON file: {e}")
        return {}

@app.route("/")
def index():
    # Load content and get the page-specific content for the homepage
    content = load_content()
    if not content:
        logger.warning("Content is empty or failed to load.")
    return render_template("index.html", content=content)

@app.route("/<page>")
def show_page(page):
    # Load content for the requested page
    content = load_content()
    logger.debug(f"Requested page: {page}")
    
    # Check if the requested page exists in the content
    page_content = content.get(page, {})
    
    # If no content is found for the page, return a 404
    if not page_content:
        logger.warning(f"Page not found in content: {page}")
        return "Page not found", 404
    
    # Render the appropriate template with the content
    try:
        return render_template(f"{page}.html", content=page_content)
    except FileNotFoundError:
        logger.warning(f"Page template not found: {page}")
        return "Page template not found", 404

if __name__ == "__main__":
    # Enable Flask Debug Toolbar
    try:
        from flask_debugtoolbar import DebugToolbarExtension
        app.debug = True  # Ensure debug mode is enabled
        app.config['SECRET_KEY'] = 'randomsecretkey'  # Required for the toolbar
        toolbar = DebugToolbarExtension(app)
        logger.info("Flask-DebugToolbar is enabled.")
    except ImportError:
        logger.warning("Flask-DebugToolbar is not installed. Skipping...")

    # Run the app with debug mode enabled
    logger.info("Starting Flask app in debug mode...")
    app.run(debug=True)
