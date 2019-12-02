# -*- coding: utf-8 -*-
from typing import Any, Dict

from chaoslib.types import Configuration, Secrets

from chaosgcp import get_context, get_service

__all__ = ["list_instances", "describe_instance"]


def list_instances(configuration: Configuration = None,
                   secrets: Secrets = None) -> Dict[str, Any]:

    """
    Lists Cloud SQL instances in a given project in the alphabetical order of
    the instance name.

    See: https://cloud.google.com/sql/docs/postgres/admin-api/v1beta4/instances/list
    """
    ctx = get_context(configuration=configuration, secrets=secrets)
    service = get_service('sqladmin', version='v1beta4',
                          configuration=configuration, secrets=secrets)

    instances = []

    request = service.instances().list(project=ctx.project_id)
    while request is not None:
        response = request.execute()
        instances.extend(response["items"])
        request = service.instances().list_next(
            previous_request=request, previous_response=response)

    return {"instances": instances}


def describe_instance(instance_id: str,
                      configuration: Configuration = None,
                      secrets: Secrets = None) -> Dict[str, Any]:
    """
    Displays configuration and metadata about a Cloud SQL instance.

    Information such as instance name, IP address, region, the CA certificate
    and configuration settings will be displayed.

    See: https://cloud.google.com/sql/docs/postgres/admin-api/v1beta4/instances/get

    :param instance_id: Cloud SQL instance ID.
    """
    ctx = get_context(configuration=configuration, secrets=secrets)
    service = get_service('sqladmin', version='v1beta4',
                          configuration=configuration, secrets=secrets)

    request = service.instances().get(project=ctx.project_id,
                                      instance=instance_id)
    response = request.execute()
    return response