# -*- coding: utf-8 -*-
import warnings
from typing import Any, Dict

from chaoslib.types import Configuration, Secrets
from logzero import logger

import chaosgcp
from chaosgcp.gke.nodepool.actions import \
    create_new_nodepool as gke_create_new_nodepool, \
    delete_nodepool as gke_delete_nodepool, \
    swap_nodepool as gke_swap_nodepool


__all__ = ["create_new_nodepool", "delete_nodepool", "swap_nodepool"]


DeprecatedChaosGCEMessage = \
    "This module `{m}` has been moved to `chaosgcp.gke.nodepool.actions`. "\
    .format(m=__name__)

DeprecatedFunctionMessage = \
    "The function `{}.{}` is deprecated and will be removed in a "\
    "future release. Please use `{}.{}` instead."

warnings.warn(DeprecatedChaosGCEMessage, DeprecationWarning)
logger.warn(DeprecatedChaosGCEMessage)


def create_new_nodepool(body: Dict[str, Any], wait_until_complete: bool = True,
                        configuration: Configuration = None,
                        secrets: Secrets = None) -> Dict[str, Any]:
    """
    DEPRECATED
        This function is now replaced by:
        chaosgcp.gke.nodepool.actions.create_new_nodepool

        It will be removed in a future release,
        please fix your experiment and switch to using the new API.
    """
    msg = DeprecatedFunctionMessage.format(
        __name__, create_new_nodepool.__name__,
        chaosgcp.gke.nodepool.actions.__name__,
        gke_create_new_nodepool.__name__
    )
    warnings.warn(msg, DeprecationWarning)
    logger.warning(msg)

    return gke_create_new_nodepool(
        body,
        wait_until_complete=wait_until_complete,
        configuration=configuration,
        secrets=secrets
    )


def delete_nodepool(node_pool_id: str, wait_until_complete: bool = True,
                    configuration: Configuration = None,
                    secrets: Secrets = None) -> Dict[str, Any]:
    """
    DEPRECATED
        This function is now replaced by:
        chaosgcp.gke.nodepool.actions.delete_nodepool

        It will be removed in a future release,
        please fix your experiment and switch to using the new API.
    """
    msg = DeprecatedFunctionMessage.format(
        __name__, delete_nodepool.__name__,
        chaosgcp.gke.nodepool.actions.__name__,
        gke_delete_nodepool.__name__
    )
    warnings.warn(msg, DeprecationWarning)
    logger.warning(msg)

    return gke_delete_nodepool(
        node_pool_id,
        wait_until_complete=wait_until_complete,
        configuration=configuration,
        secrets=secrets
    )


def swap_nodepool(old_node_pool_id: str, new_nodepool_body: Dict[str, Any],
                  wait_until_complete: bool = True,
                  delete_old_node_pool: bool = False, drain_timeout: int = 120,
                  configuration: Configuration = None,
                  secrets: Secrets = None) -> Dict[str, Any]:
    """
    DEPRECATED
        This function is now replaced by:
        chaosgcp.gke.nodepool.actions.swap_nodepool

        It will be removed in a future release,
        please fix your experiment and switch to using the new API.
    """
    msg = DeprecatedFunctionMessage.format(
        __name__, swap_nodepool.__name__,
        chaosgcp.gke.nodepool.actions.__name__,
        gke_swap_nodepool.__name__
    )
    warnings.warn(msg, DeprecationWarning)
    logger.warning(msg)

    return gke_swap_nodepool(
        old_node_pool_id,
        new_nodepool_body,
        wait_until_complete=wait_until_complete,
        delete_old_node_pool=delete_old_node_pool,
        drain_timeout=drain_timeout,
        configuration=configuration,
        secrets=secrets
    )
