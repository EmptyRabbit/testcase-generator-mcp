# testcase-generator-mcp

基于 Model Context Protocol (MCP) 的测试用例生成服务，让 AI 助手根据需求文档、技术文档、设计稿等上下文自动生成 Markdown 格式的测试用例，并可选导出为 Xmind 思维导图。

![流程概览](https://raw.githubusercontent.com/EmptyRabbit/testcase-generator-mcp/ee46dedbbc7c6490a295649ce5ed02828f716b9a/docs/process.jpg)

## 功能特性

- **测试用例生成**：根据需求描述、技术文档等上下文生成结构化 Markdown 测试用例
- **Xmind 导出**：可选将测试用例生成为 Xmind 思维导图文件
- **多传输方式**：支持 stdio（本地）、SSE、streamable HTTP
- **本地与远程**：可在本机或作为远程 MCP 服务使用

## 使用方式

服务支持三种传输方式：

### 1. Stdio 传输（本地使用）

```bash
uvx testcase-generator-mcp stdio
```

Cursor / IDE 的 MCP 配置示例：

```json
{
  "mcpServers": {
    "testcase-generator": {
      "command": "uvx",
      "args": [
        "testcase-generator-mcp",
        "stdio"
      ]
    }
  }
}
```

### 2. SSE 传输

```bash
uvx testcase-generator-mcp sse
```

**SSE 连接配置**：

```json
{
  "mcpServers": {
    "testcase-generator": {
      "url": "http://localhost:8018/sse"
    }
  }
}
```

### 3. Streamable HTTP 传输

```bash
uvx testcase-generator-mcp streamable_http
```

**Streamable HTTP 连接配置**：

```json
{
  "mcpServers": {
    "testcase-generator": {
      "url": "http://localhost:8018/mcp"
    }
  }
}
```

## 环境变量

### SSE 与 Streamable HTTP

以 **SSE** 或 **Streamable HTTP** 方式运行时，可通过环境变量控制监听地址与端口：

| 变量             | 说明   | 默认值       |
|----------------|------|-----------|
| `FASTMCP_HOST` | 监听地址 | `0.0.0.0` |
| `FASTMCP_PORT` | 监听端口 | `8018`    |

### Stdio 传输

使用 **stdio** 时无需配置上述环境变量，按本地进程方式运行即可。

## 可用工具

### generate_test_case

根据需求文档、技术文档、设计稿等上下文生成 Markdown 格式测试用例；可选生成 Xmind 思维导图。

```python
generate_test_case(
    is_need_xmind: bool = False
) -> str
```

- `is_need_xmind`: 是否需要生成 Xmind 思维导图文件，默认为 False；仅在用户明确提及「xmind」「思维导图」等时设为 True
- `Returns`: 生成的测试用例内容 Markdown 文本；若 `is_need_xmind=True` 则同时生成 .xmind 文件

## MCP 调用示例

详见 [调用过程示例](https://github.com/EmptyRabbit/testcase-generator-mcp/blob/main/docs/call_process_example.md)

## License

MIT License，详见 [LICENSE](https://github.com/EmptyRabbit/testcase-generator-mcp/blob/main/LICENSE)
