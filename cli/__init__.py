"""
Initialization file for the command-line interface package.
"""

from .cli_program import CLIProgram
from .colors import *
from .constants import *

from .ini import (
    get_bool_option,
    get_float_option,
    get_int_option,
    get_json_option,
    get_str_option,
    get_str_option_with_fallback,
    get_str_options,
    read_options
)

from .io import (
    FileInfo,
    print_line,
    read_files,
    write_text_to_file
)

from .patterns import (
    color_patterns_in_text,
    combine_patterns,
    compile_patterns,
    text_has_patterns
)

from .terminal import (
    input_is_redirected,
    output_is_terminal
)

from .types import (
    CompiledPatterns,
    ErrorReporter,
    Json,
    PatternIterable
)
