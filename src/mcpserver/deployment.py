from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(x: int, y: int) -> int:
    """
    Adds two integers and returns the result.

    Args:
        x (int): The first integer to add.
        y (int): The second integer to add.

    Returns:
        int: The sum of x and y.

    Example:
        >>> add(2, 3)
        5
    """
    result = x + y
    return result