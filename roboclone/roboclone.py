#!/usr/local/bin/python
import argparse
import jinja2
import os
import re
from templates import classpath_template, project_template


def clone_repository(url, dest):
    if dest is not None:
        os.system("git clone {} {}".format(url, dest))
    else:
        os.system("git clone {}".format(url))


def get_project_name(url):
    regex = re.compile(r".+/(.+)\.git?")
    return re.findall(regex, url)[0]


def render_project_file():
    template = jinja2.Template(project_template)
    return template.render(project_name=get_project_name(remote_url))


def resolve_clone_destination():
    if destination is None:
        return get_project_name(remote_url)
    else:
        return destination


def write_eclipse_metadata_files():
    with open(os.path.join(resolve_clone_destination(), ".classpath"), "w") as f:
        f.write(classpath_template)
    with open(os.path.join(resolve_clone_destination(), ".project"), "w") as f:
        f.write(render_project_file())


remote_url = None
destination = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("remote_url", help="url of the remote git repository (https or ssh)")
    parser.add_argument("destination", nargs="?", help="directory to clone repository to")
    args = parser.parse_args()
    global remote_url
    global destination
    remote_url = args.remote_url
    destination = args.destination
    clone_repository(args.remote_url, args.destination)
    write_eclipse_metadata_files()

if __name__ == "__main__":
    main()