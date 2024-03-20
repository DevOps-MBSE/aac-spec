from unittest import TestCase
from typing import Tuple
from click.testing import CliRunner
from aac.execute.command_line import cli, initialize_cli
from aac.execute.aac_execution_result import ExecutionStatus


from spec.plugin.specifications.specifications_impl import plugin_name, spec_csv


class TestSpecifications(TestCase):

    def test_spec_csv(self):

        # TODO: Write success and failure unit tests for spec_csv
        self.fail("Test not yet implemented.")

    def run_spec_csv_cli_command_with_args(self, args: list[str]) -> Tuple[int, str]:
        """Utility function to invoke the CLI command with the given arguments."""
        initialize_cli()
        runner = CliRunner()
        result = runner.invoke(cli, ["spec-csv"] + args)
        exit_code = result.exit_code
        std_out = str(result.stdout)
        output_message = std_out.strip().replace("\x1b[0m", "")
        return exit_code, output_message

    def test_cli_spec_csv(self):
        args = []

        # TODO: populate args list, or pass empty list for no args

        exit_code, output_message = self.run_spec_csv_cli_command_with_args(args)

        # TODO:  perform assertions against the output message
        self.assertEqual(0, exit_code)  # asserts the command ran successfully
        self.assertTrue(len(output_message) > 0)  # asserts the command produced output
        # TODO:  assert the output message is correct
