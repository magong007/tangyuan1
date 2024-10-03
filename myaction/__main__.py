import argparse

parser = argparse.ArgumentParser(__name__)

parser_github = parser.add_argument_group("github")
parser_github.add_argument_group("-gt","--github-token")
parser_github.add_argument_group("-gr","--github-repository")

if __name__ == "__main__":
  arguments = parser.parse_args()
  print(f" >> {arguments.github_repository}")
