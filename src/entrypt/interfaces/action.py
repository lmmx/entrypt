from pydantic import BaseModel

from .debug import DebugConfig
from .display import DisplayConfig

__all__ = ("FilterConfig", "ActionConfig")


class FilterConfig(BaseModel):
    filter_arg1: bool = False


class IOConfig(BaseModel):
    io_arg1: bool = False


class ActionConfig(DebugConfig, DisplayConfig, FilterConfig, IOConfig):
    """
    Configure input filtering and output display.

      :param io_arg1: The first IO configuration entry.
      :param filter_arg1: The first filtering configuration entry.
      :param quiet: Whether to suppress console output.
      :param debug: Whether to run debug diagnostics.
    """
