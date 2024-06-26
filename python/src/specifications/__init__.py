"""__init__.py module for the Specifications plugin."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from os.path import join, dirname
from aac.execute.aac_execution_result import (
    ExecutionResult,
    ExecutionStatus,
)
from aac.execute import hookimpl
from aac.context.language_context import LanguageContext
from aac.execute.plugin_runner import PluginRunner


from specifications.specifications_impl import (
    plugin_name,
    spec_csv,
    before_spec_csv_check,
)


from aac.plugins.check import run_check


specifications_aac_file_name = "specifications.aac"


def run_spec_csv(architecture_file: str, output_directory: str) -> ExecutionResult:
    """
     Generate a CSV file listing requirements.

     Args:
         architecture_file (str): The file to convert into CSV.
         output_directory (str): The directory into which the CSV file will be generated.


    Returns:
         The results of the execution of the plugin command.
    """

    result = ExecutionResult(plugin_name, "spec-csv", ExecutionStatus.SUCCESS, [])

    spec_csv_check_result = before_spec_csv_check(
        architecture_file, output_directory, run_check
    )
    if not spec_csv_check_result.is_success():
        return spec_csv_check_result
    else:
        result.add_messages(spec_csv_check_result.messages)

    spec_csv_result = spec_csv(architecture_file, output_directory)
    if not spec_csv_result.is_success():
        return spec_csv_result
    else:
        result.add_messages(spec_csv_result.messages)

    return result


@hookimpl
def register_plugin() -> None:
    """
    Registers information about the plugin for use in the CLI.
    """

    active_context = LanguageContext()
    specifications_aac_file = join(dirname(__file__), specifications_aac_file_name)
    definitions = active_context.parse_and_load(specifications_aac_file)

    specifications_plugin_definition = [
        definition for definition in definitions if definition.name == plugin_name
    ][0]

    plugin_instance = specifications_plugin_definition.instance
    for file_to_load in plugin_instance.definition_sources:
        active_context.parse_and_load(file_to_load)

    plugin_runner = PluginRunner(plugin_definition=specifications_plugin_definition)
    plugin_runner.add_command_callback("spec-csv", run_spec_csv)

    active_context.register_plugin_runner(plugin_runner)
