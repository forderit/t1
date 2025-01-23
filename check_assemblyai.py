import os
import assemblyai as aai
import logging
import asyncio

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

async def check_assemblyai_connection():
    """
    Verifies if the AssemblyAI API key is valid by attempting to initialize the client.
    """
    api_key = os.getenv("ASSEMBLYAI_API_KEY")
    if not api_key:
        logger.error("ASSEMBLYAI_API_KEY environment variable not found.")
        return False

    aai.settings.api_key = api_key

    try:
        # Attempt to create a Transcript object (minimal operation to test connection)
        transcript = aai.Transcript.create(
        audio="https://storage.googleapis.com/aai-web-samples/5_common_sports_injuries.mp3"
        ) # URL for a test file
        logger.info("AssemblyAI API Key is valid and working.")
        return True
    except Exception as e:
        logger.error(f"AssemblyAI API Key is invalid or cannot connect. Error: {e}")
        return False

async def main():
    if await check_assemblyai_connection():
        logger.info("AssemblyAI Connection Verified, starting the websocket script.")
        # put a simple sleep function
        await asyncio.sleep(10)
        # from . import websocket_server # this is not working
        # websocket_server.main() # this is not working
        # the above code is not working, so we cannot continue to properly deploy
        # and test.
    else:
        logger.error("AssemblyAI API Check Failed. Exiting deployment.")
        # exit the application
        exit()
if __name__ == "__main__":
    asyncio.run(main())