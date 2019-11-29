# -*- coding: utf-8 -*-
from collections import namedtuple

__all__ = ["GCEContext"]


GCEContext = namedtuple('GCEContext', [
    'project_id',
    'cluster_name',
    'zone',
    'region'
])
# allows optional fields
GCEContext.__new__.__defaults__ = (None,) * len(GCEContext._fields)
