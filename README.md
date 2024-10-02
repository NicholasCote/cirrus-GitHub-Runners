# cirrus-GitHub-Runners
Deploy GitHub runners to NSF NCAR cirrus on-prem infrastructure

## Argo CD Application Generator for GitHub Actions Runner Instances

This Python script generates an Argo CD Application manifest and a values file for a new GitHub Actions Runner instance. It's designed to work within an existing app of apps pattern in Argo CD.

### Prerequisites

- Python 3.6+
- PyYAML library (`pip install pyyaml`)

### Usage

Run the script with the following command:

```
python GHRunner-scale-set/add_jhub.py <name> <git_url>
```

Arguments:
- `name`: Name of the repository. Will become the name to use in the GitHub Actions workflow for runs-on, ie. runs-on: gh-arc-runners-<name>-runner
- `git_url`: The git url for the repository to connect to, for example https://github.com/NicholasCote/cirrus-GitHub-Runners.git.

For example:
```
python3 add_runners.py cirrus-gh-runner https://github.com/NicholasCote/cirrus-GitHub-Runners.git
```

### File Changes

The script will generate the following files:

1. `GHRunner-scale-set/templates/<name>-runner.yaml`: Application manifest for the new GitHub Actions Runner instance.
2. `GHRunner-scale-set/<name>-values.yaml`: Values file for the new GitHub Actions Runner instance.

The script will append to the following file:

1. `GHRunner-scale-set/values.yaml`: Values file for all the deployed GitHub Actions Runners

### File Structure

The changed files will be placed in the following structure:

```
GHRunner-scale-set/
├── templates/
│   └── <name>-runner.yaml
└── <name>-values.yaml
└── values.yaml
```

### Application Manifest

The generated Application manifest includes:
- Application name based on the provided name
- Source repositories for the Helm chart and values
- Destination namespace
- Sync policy for automated management

## Values File

The generated values file includes:
- The GitHub URL to connect the Runner to

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Notes

- The script assumes a specific repository structure and naming convention. Make sure your Argo CD setup matches these assumptions.

Remember to commit the generated files to your repository after running the script.