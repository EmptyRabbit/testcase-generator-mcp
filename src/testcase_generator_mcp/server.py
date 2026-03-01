import logging
import os
from typing import Annotated

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from testcase_generator_mcp.tool import generate_test_case_tool

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOG_FILE = os.path.join(ROOT_DIR, "testcase-generator-mcp.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_FILE)],
)
logger = logging.getLogger("testcase-generator-mcp")

mcp = FastMCP(
    "testcase-generator-mcp",
    host=os.environ.get("FASTMCP_HOST", "0.0.0.0"),
    port=int(os.environ.get("FASTMCP_PORT", "8018")),
    instructions="Testcase Generator MCP Server for generating and managing test cases",
)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Generate Test Case",
        readOnlyHint=False,
    ),
)
def generate_test_case(
        is_need_xmind: Annotated[bool, Field(description="是否需要生成Xmind思维导图文件，默认为False")] = False,
) -> str:
    """
    根据用户提供的需求文档、技术文档、设计稿等上下文信息，生成Markdown格式的测试用例

    🎯 必须优先调用的场景（按优先级排序）：
    1. 用户说"生成测试用例"、"设计测试用例"、"创建测试用例"
    2. 用户说"保存为xmind测试用例"、"生成思维导图测试用例"、"生成xmind测试用例"
    3. 任何涉及测试用例生成的请求

    📋 参数说明：
    - is_need_xmind: 仅在用户明确提及"xmind"、"思维导图"等关键词时设置为True，否则必须保持默认值False

    ⚠️ 关键提醒：
    - 当用户明确要求生成测试用例时，必须调用此工具
    - is_need_xmind参数必须严格按照用户明确要求思维导图来决定，不能随意设置为True
    """
    prompt_content = generate_test_case_tool(is_need_xmind)
    return prompt_content


def run_sse():
    try:
        logger.info("Starting Testcase Generator MCP server (SSE)")
        mcp.run(transport="sse")
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server failed: {e}")
        raise
    finally:
        logger.info("Server shutdown complete")


def run_streamable_http():
    try:
        logger.info("Starting Testcase Generator MCP server (streamable HTTP)")
        mcp.run(transport="streamable-http")
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server failed: {e}")
        raise
    finally:
        logger.info("Server shutdown complete")


def run_stdio():
    try:
        logger.info("Starting Testcase Generator MCP server (stdio)")
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server failed: {e}")
        raise
    finally:
        logger.info("Server shutdown complete")
