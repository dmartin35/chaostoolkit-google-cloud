# -*- coding: utf-8 -*-
import warnings

from logzero import logger


DeprecatedChaosGCEMessage = \
    "The `chaosgce` package is deprecated and will be removed in a future "\
    "release. Please use the `chaosgcp` package from now on. "


warnings.warn(DeprecatedChaosGCEMessage, DeprecationWarning)
logger.warn(DeprecatedChaosGCEMessage)
