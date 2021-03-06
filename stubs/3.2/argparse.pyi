# Stubs for argparse (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Sequence

SUPPRESS = ... # type: Any
OPTIONAL = ... # type: Any
ZERO_OR_MORE = ... # type: Any
ONE_OR_MORE = ... # type: Any
PARSER = ... # type: Any
REMAINDER = ... # type: Any

class _AttributeHolder: ...

class HelpFormatter:
    def __init__(self, prog, indent_increment=2, max_help_position=24, width=None): ...
    def start_section(self, heading): ...
    def end_section(self): ...
    def add_text(self, text): ...
    def add_usage(self, usage, actions, groups, prefix=None): ...
    def add_argument(self, action): ...
    def add_arguments(self, actions): ...
    def format_help(self): ...

class RawDescriptionHelpFormatter(HelpFormatter): ...
class RawTextHelpFormatter(RawDescriptionHelpFormatter): ...
class ArgumentDefaultsHelpFormatter(HelpFormatter): ...
class MetavarTypeHelpFormatter(HelpFormatter): ...

class ArgumentError(Exception):
    argument_name = ... # type: Any
    message = ... # type: Any
    def __init__(self, argument, message): ...

class ArgumentTypeError(Exception): ...

class Action(_AttributeHolder):
    option_strings = ... # type: Any
    dest = ... # type: Any
    nargs = ... # type: Any
    const = ... # type: Any
    default = ... # type: Any
    type = ... # type: Any
    choices = ... # type: Any
    required = ... # type: Any
    help = ... # type: Any
    metavar = ... # type: Any
    def __init__(self, option_strings, dest, nargs=None, const=None, default=None, type=None,
                 choices=None, required=False, help=None, metavar=None): ...
    def __call__(self, parser, namespace, values, option_string=None): ...

class _StoreAction(Action):
    def __init__(self, option_strings, dest, nargs=None, const=None, default=None, type=None,
                 choices=None, required=False, help=None, metavar=None): ...
    def __call__(self, parser, namespace, values, option_string=None): ...

class _StoreConstAction(Action):
    def __init__(self, option_strings, dest, const, default=None, required=False, help=None,
                 metavar=None): ...
    def __call__(self, parser, namespace, values, option_string=None): ...

class _StoreTrueAction(_StoreConstAction):
    def __init__(self, option_strings, dest, default=False, required=False, help=None): ...

class _StoreFalseAction(_StoreConstAction):
    def __init__(self, option_strings, dest, default=True, required=False, help=None): ...

class _AppendAction(Action):
    def __init__(self, option_strings, dest, nargs=None, const=None, default=None, type=None,
                 choices=None, required=False, help=None, metavar=None): ...
    def __call__(self, parser, namespace, values, option_string=None): ...

class _AppendConstAction(Action):
    def __init__(self, option_strings, dest, const, default=None, required=False, help=None,
                 metavar=None): ...
    def __call__(self, parser, namespace, values, option_string=None): ...

class _CountAction(Action):
    def __init__(self, option_strings, dest, default=None, required=False, help=None): ...
    def __call__(self, parser, namespace, values, option_string=None): ...

class _HelpAction(Action):
    def __init__(self, option_strings, dest=..., default=..., help=None): ...
    def __call__(self, parser, namespace, values, option_string=None): ...

class _VersionAction(Action):
    version = ... # type: Any
    def __init__(self, option_strings, version=None, dest=..., default=...,
                 help=''): ...
    def __call__(self, parser, namespace, values, option_string=None): ...

class _SubParsersAction(Action):
    def __init__(self, option_strings, prog, parser_class, dest=..., help=None,
                 metavar=None): ...
    def add_parser(self, name, **kwargs): ...
    def __call__(self, parser, namespace, values, option_string=None): ...

class FileType:
    def __init__(self, mode='', bufsize=-1, encoding=None, errors=None): ...
    def __call__(self, string): ...

class Namespace(_AttributeHolder):
    def __init__(self, **kwargs): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __contains__(self, key): ...

class _ActionsContainer:
    description = ... # type: Any
    argument_default = ... # type: Any
    prefix_chars = ... # type: Any
    conflict_handler = ... # type: Any
    def __init__(self, description, prefix_chars, argument_default, conflict_handler): ...
    def register(self, registry_name, value, object): ...
    def set_defaults(self, **kwargs): ...
    def get_default(self, dest): ...
    def add_argument(self,
        *args: str,
        action: str = None,
        nargs: str = None,
        const: Any = None,
        default: Any = None,
        type: Any = None,
        choices: Any = None, # TODO: Container?
        required: bool = None,
        help: str = None,
        metavar: str = None,
        dest: str = None,
    ) -> None: ...
    def add_argument_group(self, *args, **kwargs): ...
    def add_mutually_exclusive_group(self, **kwargs): ...

class _ArgumentGroup(_ActionsContainer):
    title = ... # type: Any
    def __init__(self, container, title=None, description=None, **kwargs): ...

class _MutuallyExclusiveGroup(_ArgumentGroup):
    required = ... # type: Any
    def __init__(self, container, required=False): ...

class ArgumentParser(_AttributeHolder, _ActionsContainer):
    prog = ... # type: Any
    usage = ... # type: Any
    epilog = ... # type: Any
    formatter_class = ... # type: Any
    fromfile_prefix_chars = ... # type: Any
    add_help = ... # type: Any
    def __init__(self, prog=None, usage=None, description=None, epilog=None, parents=...,
                 formatter_class=..., prefix_chars='', fromfile_prefix_chars=None,
                 argument_default=None, conflict_handler='', add_help=True): ...
    def add_subparsers(self, **kwargs): ...
    def parse_args(self, args: Sequence[str] = None, namespace=None) -> Any: ...
    def parse_known_args(self, args=None, namespace=None): ...
    def convert_arg_line_to_args(self, arg_line): ...
    def format_usage(self): ...
    def format_help(self): ...
    def print_usage(self, file=None): ...
    def print_help(self, file=None): ...
    def exit(self, status=0, message=None): ...
    def error(self, message): ...
