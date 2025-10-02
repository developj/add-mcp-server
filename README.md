/**
 * Demo configuration for adding the MCP server using uvx.
 *
 * To use this configuration, copy and add the following block inside your `mcpServer` object in `clude config.json` or any client config of choice:
 *
 * ```json
 * "Demo": {
 *   "command": "uvx",
 *   "args": [
 *     "--from",
 *     "git+https://github.com/developj/add-mcp-server.git",
 *     "mcp-server"
 *   ]
 * }
 * ```
 *
 * - `command`: The command to execute (`uvx`).
 * - `args`: Arguments for the command:
 *   - `--from`: Specifies the source repository.
 *   - The GitHub repository URL for the MCP server.
 *   - The name of the server to add (`mcp-server`).
 *
 * Ensure this block is placed within the `mcpServer` object of your `clude config.json`.
 */