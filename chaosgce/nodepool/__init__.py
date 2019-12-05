# -*- coding: utf-8 -*-
import warnings

from logzero import logger


DeprecatedChaosGCEMessage = \
    "This package `{m}` has been moved to `chaosgcp.gke.nodepool`. "\
    .format(m=__name__)


warnings.warn(DeprecatedChaosGCEMessage, DeprecationWarning)
logger.warn(DeprecatedChaosGCEMessage)
