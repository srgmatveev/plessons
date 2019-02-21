import os
import argparse
from analyzer import clone_github as gh
from analyzer import words_count as wc
from analyzer import console_report as cs
from analyzer import i_report as i_r
import collections





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

    wds = []

    if url is not None and to_copy_dir is not None:
        #gh.CloneGitHub(from_url=url, to_path=to_copy_dir).clone()
        wds = wc.get_top_functions_in_path(path= to_copy_dir)
        i_r.reporter(cs.ConsoleReport(wds=wds, top_size=200))
        wc.get_top_local_vars(path= to_copy_dir)

if __name__ == "__main__":
    main()
