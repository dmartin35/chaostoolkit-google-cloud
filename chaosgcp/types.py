# -*- coding: utf-8 -*-
from collections import namedtuple

__all__ = ["GCPContext"]


GCPContext = namedtuple('GCPContext', [
    'project_id',
    'cluster_name',
    'zone',
    'region'
])
