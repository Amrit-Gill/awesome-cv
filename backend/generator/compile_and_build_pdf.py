import logging
import os
import subprocess
from subprocess import DEVNULL

SCRIPT_DIR = os.path.dirname(__file__)
TEX_WORKSPACE = os.path.join(SCRIPT_DIR, os.pardir, "resume_workspace")

class CompileAndBuildPdf:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def compile(self, tex_file_name):
        # subprocess.call(['xelatex', tex_file_name, '-include-directory={}'.format(TEX_WORKSPACE)], shell=False, stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
        os.system("xelatex {} -include-directory={} -output-directory={}".format(tex_file_name, TEX_WORKSPACE, TEX_WORKSPACE))