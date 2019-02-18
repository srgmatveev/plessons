import argparse
from analyzer import clone_github as gh


def main():
    parser = argparse.ArgumentParser(
        description='Paresr for work with clone from GitHub')
    parser.add_argument('-to', '--t', dest='to_dir',
                        help='Directory where repository is copied')
    parser.add_argument('-repo', '--r', dest='repo_url',
                        help='GitHub repository url')
    args = parser.parse_args()
    to_copy_dir = args.to_dir
    url = args.repo_url
    g_h = gh.CloneGitHub(from_url=url, to_path=to_copy_dir).clone()

if __name__ == "__main__":
    main()
