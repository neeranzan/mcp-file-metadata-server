# main.py
from server import mcp

import tools.csv_tools
import tools.parquet_tools

# Entry point to run the server
if __name__ == "__main__":
    # https://gofastmcp.com/deployment/running-server
    #mcp.run() This is STDIO transport
    # Start an HTTP server on port 8000
    mcp.run(transport="http", host="127.0.0.1", port=8000)