import os
from click.testing import CliRunner
from cwl_wrapper import app
import unittest

class TestSubworkflowCwl(unittest.TestCase):

    def setUp(self):
        self.stagein_cwl_file = os.path.join(os.path.dirname(__file__), 'data/stagein.cwl')
        self.stageout_cwl_file = os.path.join(os.path.dirname(__file__), 'data/stageout.cwl')
        self.app_cwl_file = os.path.join(os.path.dirname(__file__), 'data/dNBR.cwl')
        self.expected_wrapped_cwl = os.path.join(os.path.dirname(__file__), 'data/test_dNBR_expected.cwl')
        self.expected_usage_test = os.path.join(os.path.dirname(__file__), 'data/test_help_expected.txt')

    def test_help(self):
        runner = CliRunner()
        result = runner.invoke(app.main, ['--help'])
        with open(self.expected_usage_test) as f:
            contents = f.read()
            assert result.output.strip() == contents

    def test_dNBR(self):
        runner = CliRunner()
        result = runner.invoke(app.main, ["--stagein", self.stagein_cwl_file, "--stageout", self.stageout_cwl_file, self.app_cwl_file+"#dnbr"])
        with open(self.expected_wrapped_cwl) as f:
            contents = f.read()
            assert result.output == contents

    def test_dNBR_invalid_hashtag(self):
        runner = CliRunner()
        result = runner.invoke(app.main,["--stagein", self.stagein_cwl_file, "--stageout", self.stageout_cwl_file, self.app_cwl_file+"#invalidId"])
        assert result.exception.args[0] == "Wrong Workflow"

    def test_dNBR_empty_hashtag(self):
        runner = CliRunner()
        result = runner.invoke(app.main,["--stagein", self.stagein_cwl_file, "--stageout", self.stageout_cwl_file, self.app_cwl_file+"#"])
        assert result.exception.args[0] == "No value after the hashtag was found."