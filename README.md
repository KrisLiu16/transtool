# TransTool

TransTool 是一个基于 Python 的工具，旨在将 JSON 格式的题目描述及相应的输入输出测试文件转换为 XML 格式。它尤其适用于将竞赛编程的测试案例转换为标准化的 XML 结构。

## 功能

- 读取 JSON 格式的题目描述文件。
- 提取存储为 `.in` 和 `.out` 格式的输入输出测试文件。
- 将提取的数据转换为 XML 结构。
- 处理 XML 格式化和美化输出。

## 项目结构



```
transtool/
│
├── modules/
│   ├── __init__.py             # 模块初始化文件
│   ├── file_operations.py      # 负责输入输出文件的读取
│   ├── xml_operations.py       # 负责 XML 的生成与格式化
│   ├── json_operations.py      # 负责 JSON 文件的读取
│   ├── util.py                 # 工具函数（换行符替换、单位转换等）
│   ├── fps_generator.py        # 生成 FPS 格式的 XML 总结构
│   ├── xml_writer.py           # 将生成的 XML 写入文件
│   ├── item_generator.py       # 生成 XML 中的单个 <item> 元素
│
├── main.py                     # 主脚本，负责组织 XML 的生成
├── README.md                   # 项目文档
└── data/                       # 存储输入输出测试数据和配置文件的文件夹
```

### 模块说明

1. **file_operations.py**: 包含从文件系统读取输入输出测试文件的函数。
2. **xml_operations.py**: 处理 XML 元素的创建、格式化以及实体替换。
3. **json_operations.py**: 提供加载和解析 JSON 配置文件的函数。
4. **util.py**: 提供工具函数，如内存单位转换、换行符替换等。
5. **fps_generator.py**: 负责生成 `<fps>` 根元素，处理多个题目的生成。
6. **xml_writer.py**: 将最终的 XML 结构写入文件并确保格式正确。
7. **item_generator.py**: 生成单个 `<item>` 元素，其中包含题目描述、测试用例和其他相关数据。

## 环境要求

- Python 3.11 或更高版本

## 安装

1. 将此仓库克隆到你的本地机器：

    ```bash
    git clone https://github.com/KrisLiu16/transtool
    cd trans-tool
    ```

2. 确保你已经安装了 Python 3.11。你可以运行以下命令来检查 Python 版本：

    ```bash
    python --version
    ```

3. 该项目仅使用 Python 标准库，无需额外依赖。

## 使用方法

1. **准备数据**: 将输入输出测试文件 (`0.in`, `0.out`, 等) 和题目的 `config.json` 文件放置在 `data/` 文件夹中。文件夹结构应类似于：

    ```
    data/
    ├── problem1/
    │   ├── config.json
    │   ├── 0.in
    │   ├── 0.out
    │   └── ...
    └── problem2/
        ├── config.json
        ├── 0.in
        ├── 0.out
        └── ...
    ```

2. **运行主脚本**:

    ```bash
    python main.py
    ```

3. **输出结果**: 生成的 XML 文件将被保存为 `combined_output.xml`，位于 `data/` 文件夹中。

## 示例

如果你在 `data/problem1/` 文件夹中有如下文件：

- `config.json` (题目的 JSON 格式描述文件)
- `0.in` 和 `0.out` (测试用例文件)

运行工具将生成一个包含该题目及其测试用例的 `combined_output.xml` 文件。

## 许可证

本项目基于 MIT 许可证发布，详情请参见 [LICENSE](LICENSE) 文件。
