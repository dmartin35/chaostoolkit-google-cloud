# -*- coding: utf-8 -*-
import warnings

from logzero import logger
from chaoslib.types import Discovery


DeprecatedChaosGCEMessage = \
    "The `chaosgce` package is deprecated and will be removed in a future "\
    "release. Please use the `chaosgcp` package from now on. "


warnings.warn(DeprecatedChaosGCEMessage, DeprecationWarning)
logger.warn(DeprecatedChaosGCEMessage)


def discover(discover_system: bool = True) -> Discovery:
    """
    No activity shall be discovered as this package is deprecated
    """
    return {}
