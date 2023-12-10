import asyncio
import os
from hypercorn.asyncio import serve
from hypercorn.config import Config
from langchain.globals import set_debug, set_verbose
from dotenv import load_dotenv

load_dotenv()

def main():
    from api.server import app
    debug_mode = (os.getenv('DEBUG_MODE', 'False') == 'True')

    # Create a new event loop
    loop = asyncio.new_event_loop()

    # Configure Hypercorn settings
    cfg = Config()
    port = os.getenv('APP_PORT', '8080')
    cfg.bind = f"0.0.0.0:{port}"

    # Enable debug mode if DEBUG_MODE environment variable is set to 'True'
    if debug_mode:
        cfg.loglevel = "DEBUG"
        set_debug(True)
        set_verbose(True)
        print("Hypercorn & LangChain running in debug mode")

    # Create and start the server coroutine
    server_coro = serve(app, cfg, shutdown_trigger=lambda: asyncio.Future())
    loop.create_task(server_coro)

    # Start the event loop
    loop.run_forever()


if __name__ == '__main__':
    main()
