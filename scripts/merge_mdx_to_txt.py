#!/usr/bin/env python3
"""
合并所有 mdx 文件到一个大的 txt 文件
"""
import os
from pathlib import Path

def merge_mdx_files(source_dir, output_file):
    """
    递归查找并合并所有 .mdx 文件到一个 txt 文件

    Args:
        source_dir: 源目录路径
        output_file: 输出文件路径
    """
    source_path = Path(source_dir)

    # 递归查找所有 .mdx 文件并排序
    mdx_files = sorted(source_path.rglob("*.mdx"))

    print(f"找到 {len(mdx_files)} 个 mdx 文件")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for idx, mdx_file in enumerate(mdx_files, 1):
            # 获取相对路径用于显示
            relative_path = mdx_file.relative_to(source_path)

            print(f"处理 [{idx}/{len(mdx_files)}]: {relative_path}")

            # 写入分隔符和文件信息
            separator = "=" * 80
            outfile.write(f"\n{separator}\n")
            outfile.write(f"filename: {relative_path}\n")
            outfile.write(f"{separator}\n\n")

            # 读取并写入文件内容
            try:
                with open(mdx_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)

                    # 确保文件内容后有换行
                    if not content.endswith('\n'):
                        outfile.write('\n')

            except Exception as e:
                error_msg = f"错误：无法读取文件 {mdx_file}: {e}\n"
                print(error_msg)
                outfile.write(error_msg)

            # 在文件内容后添加空行
            outfile.write("\n")

    print(f"\n完成！所有内容已合并到: {output_file}")
    print(f"输出文件大小: {os.path.getsize(output_file) / 1024:.2f} KB")

if __name__ == "__main__":
    # 设置源目录和输出文件
    current_dir = Path(__file__).parent
    output_file = current_dir / "reactflow-docs.txt"

    print(f"源目录: {current_dir}")
    print(f"输出文件: {output_file}")
    print("-" * 80)

    merge_mdx_files(current_dir, output_file)

