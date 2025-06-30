from flask import Flask, Response

# Create Flask application instance
app = Flask(__name__)

# Configuration constants to match Node.js implementation
HOST = '127.0.0.1'
PORT = 3000

# Catch-all route handler for all HTTP methods and all paths
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
def handle_all_requests(path=''):
    """
    Universal request handler that returns identical response for all HTTP methods.
    Replicates the behavior of the original Node.js server.js implementation.
    
    Args:
        path: Optional path parameter (ignored, maintains compatibility)
        
    Returns:
        Flask Response object with static content matching Node.js implementation
    """
    return Response(
        'Hello, World!\n',
        status=200,
        content_type='text/plain'
    )

if __name__ == '__main__':
    # Display startup message matching Node.js format exactly
    print(f'Server running at http://{HOST}:{PORT}/')
    
    # Start Flask development server with configuration matching Node.js behavior
    app.run(
        host=HOST,
        port=PORT,
        debug=False,        # Disable debug mode for production-like behavior
        use_reloader=False  # Disable reloader to prevent development mode features
    )