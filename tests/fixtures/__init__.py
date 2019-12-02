# -*- coding: utf-8 -*-
from fixtures import nodepool
from fixtures import sql

secrets = {
    "service_account_file": "tests/fixtures/fake_creds.json"
}

configuration_legacy = {
    "gce_project_id": "chaosiqdemos",
    "gce_cluster_name": "demos-cluster",
    "gce_zone": "us-west1-a"
}

configuration = {
    "gcp_project_id": "chaosiqdemos",
    "gcp_zone": "us-west1-a",
    "gcp_region": "us-west1",
    "gcp_gke_cluster_name": "demos-cluster",
}
