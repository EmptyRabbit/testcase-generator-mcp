import os

base_dir = os.path.dirname(os.path.abspath(__file__))


def generate_test_case_tool(is_need_xmind: bool = False) -> str:
    """Load and return the prompt template for generating test cases.

    Reads the template from prompt/generate_test_case.md under the same package
    directory and replaces the placeholder {is_need_xmind} with the given value.

    Args:
        is_need_xmind: Whether to generate XMind mind map format. Defaults to False.

    Returns:
        The prompt template string with placeholders substituted.
    """
    # Resolve path to prompt template file relative to this module
    file_path = os.path.join(base_dir, "prompt", "generate_test_case.md")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace("{is_need_xmind}", str(is_need_xmind))
    return content


def markdown_to_xmind_tool() -> str:
    """Load and return the prompt template for converting Markdown to XMind.

    Reads the template from prompt/markdown_to_xmind.md under the same package
    directory and returns its content as a string.

    Returns:
        The prompt template string for converting Markdown content into XMind format.
    """
    file_path = os.path.join(base_dir, "prompt", "markdown_to_xmind.md")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
