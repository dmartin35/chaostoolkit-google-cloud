# Changelog

## [Unreleased][]

[Unreleased]: https://github.com/chaostoolkit-incubator/chaostoolkit-google-cloud/compare/0.2.2...HEAD

### Added

-   New extension structure: 
    `chaosgcp` package with GCP products as first level subpackage.
    This new structure intends to follow GCP products navigation, as seen
    on the GCP console to keep some consistency for the user.
-   New `chaosgcp.gke` package for Google Kubernetes Engine probes & actions.

### Changed

-   The `chaosgce` package is now deprecated. It will be removed in a future
    release. The `chaosgce.nodepool.actions` module has been moved to
    `chaosgcp.gke.nodepool.actions`. Please update your experiments to use the
    new package.

## [0.2.2][] - 2018-05-14

[0.2.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-google-cloud/compare/0.2.1...0.2.2

### Added

-   Read version from source file without importing

## [0.2.1][] - 2018-04-24

[0.2.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-google-cloud/compare/0.2.0...0.2.1

### Changed

-   Fixed setup.py to read version from package

## [0.2.0][] - 2018-04-23

[0.2.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-google-cloud/compare/0.1.0...0.2.0

### Added

-   Added discovery support for `chaos discover`

### Changed

-   Access token is refreshed when expired
-   No more of decorators to inject services and project context because it
    broke the experiment validation (since those arguments weren't explicitly
    passed on by the user). Good thing is API is leaner and less magical


## [0.1.0][] - 2018-04-13

[0.1.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-google-cloud/tree/0.1.0

### Added

-   Initial release
