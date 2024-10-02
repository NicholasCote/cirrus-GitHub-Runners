import yaml
import argparse

def generate_application(name):
    return {
        "apiVersion": "argoproj.io/v1alpha1",
        "kind": "Application",
        "metadata": {
            "name": f'{{{{ .Release.Name }}}}-{{{{ .Values.runners.{name}.name }}}}',
            "namespace": "argo"
        },
        "spec": {
            "project": "default",
            "sources": [
                {
                    "repoURL": "https://github.com/Gin-G/argo-k8s-stuff",
                    "path": "gha-runner-scale-set",
                    "targetRevision": "main",
                    "helm": {
                        "valueFiles": [
                            f"$values/gha-runner-scale-set/{name}-values.yaml"
                        ]
                    }
                },
                {
                    "repoURL": 'https://github.com/NicholasCote/cirrus-GitHub-Runners',
                    "targetRevision": 'main',
                    "ref": "values"
                }
            ],
            "destination": {
                "server": "https://kubernetes.default.svc",
                "namespace": "{{ .Values.namespace }}"
            },
            "syncPolicy": {
                "automated": {
                    "prune": True,
                    "selfHeal": True
                },
                "syncOptions": [
                    "CreateNamespace=true",
                    "ServerSideApply=true"
                ]
            }
        }
    }

def generate_values(git_url):
    return {
        "githubConfigUrl": f"{git_url}"
    }

def update_values_yaml(name):
    with open('GHRunner-scale-set/values.yaml', 'r') as f:
        values = yaml.safe_load(f)

    values['runners'][name] = {"name": f"{name}-runner"}

    with open('GHRunner-scale-set/values.yaml', 'w') as f:
        yaml.dump(values, f, default_flow_style=False)

def main(name, git_url):
    app = generate_application(name)
    
    output_file = 'GHRunner-scale-set/templates/' f"{name}-runner.yaml"
    with open(output_file, 'w') as f:
        yaml.dump(app, f, default_flow_style=False)

    # Generate values.yaml
    values = generate_values(git_url)

    with open('GHRunner-scale-set/' + name + '-values.yaml', 'w') as f:
        yaml.dump(values, f, default_flow_style=False)
    
    update_values_yaml(name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Argo CD Application manifests")
    parser.add_argument("name", help="Name of the repository. Will become the name to use in the GitHub Actions workflow for runs-on, ie. runs-on: gh-arc-runners-<name>-runner")
    parser.add_argument("git_url", help="Full path to the Jupyter container image to run")
    args = parser.parse_args()
    
    main(args.name, args.git_url)