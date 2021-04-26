from invoke import task


import subprocess
import os
import requests



@task
def build_pip(context):
    import xml.etree.ElementTree as ET 
    res = requests.get('https://test.pypi.org/rss/project/ekolve-testpython/releases.xml')
    res.raise_for_status()

    git_tag_version = (
        subprocess.check_output("git describe --tags --exact-match", shell=True)
        .decode("ascii")
        .strip()
    )

    root = ET.fromstring(res.content)
    latest_version = None

    for title in root.findall('./channel/item/title'): 
        latest_version = title.text
        break
    
    current_maj, current_min, current_sub = list(map(int, latest_version.split('.')))
    next_maj, next_min, next_sub = list(map(int, git_tag_version.split('.')))

    if (next_maj > current_maj) or \
        (next_maj >= current_maj and next_min > current_min) or \
        (next_maj >= current_maj and next_min >= current_min and next_sub > current_sub):
        subprocess.check_call("python setup.py sdist bdist_wheel --universal", shell=True)
    else:
        raise Exception("Invalid version: %s is not greater than latest version %s" % (git_tag_version, latest_version))
        

@task
def deploy_pip(context):
    if 'TWINE_PASSWORD' not in os.environ:
        raise Exception("Twine token not specified in environment")
    subprocess.check_call("twine upload --repository testpypi -u __token__ dist/*", shell=True)

