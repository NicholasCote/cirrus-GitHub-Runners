# Automated GitHub Actions Runner Deployments

## Description
This PR updates the Argo CD Application manifests for multiple GitHub Actions Runner scale set instances, tailored to our specific deployment structure. <br>
The main changes are:

1. Update `values.yaml` with new GitHub Actions Runner name
2. Add a custom values file for the new GitHub Actions Runner 
3. Add an Argo CD Application manifest for the new GitHub Actions Runner

## Benefits
- Simplifies management of multiple GitHub Actions Runner instances
- Reduces duplication in configuration files
- Makes it easier to add new GitHub Actions Runner instances
- Maintains consistency with our current deployment structure

## Implementation
To use this new approach:
1. Run the script to generate Application manifests, a custom values.yaml file, and update the complete values.yaml
2. Commit the generated manifests to your repository

## Checklist
- [ ] Code follows the project's coding standards
- [ ] Cloud team has been made aware of intention to add a GitHub Actions Runner
- [ ] All new and existing tests pass
- [ ] The PR has been tested locally

## Additional Notes
Please review the changes and let me know if you have any questions or suggestions for improvement.