import asyncio
import os
from langchain.globals import set_debug, set_verbose
from dotenv import load_dotenv
import uvicorn

load_dotenv()

def main():
    debug_mode = (os.getenv('DEBUG_MODE', 'False') == 'True')

    # Create a new event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Enable debug mode if DEBUG_MODE environment variable is set to 'True'
    if debug_mode:
        set_debug(True)
        set_verbose(True)
        print("Uvicorn & LangChain running in debug mode")

    # Uvicorn settings
    port = int(os.getenv('APP_PORT', '8080'))
    uvicorn_config = {
        "app": "api.server:app",  # Assuming 'app' is in the 'api.server' module
        "host": "0.0.0.0",
        "port": port,
        "loop": "asyncio",
        "reload": debug_mode,
        "log_level": "debug" if debug_mode else "info"
    }

    # Start the Uvicorn server
    uvicorn.run(**uvicorn_config)

if __name__ == '__main__':
    main()
