# -*- coding: utf-8 -*-
"""
GitHub自动上传脚本
使用GitHub API自动上传项目文件到仓库
"""

import os
import base64
import requests
import json
from pathlib import Path

def upload_file_to_github(token, repo, file_path, content, message="Upload file"):
    """上传单个文件到GitHub"""
    try:
        # 将文件内容编码为base64
        if isinstance(content, str):
            content_base64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        else:
            content_base64 = base64.b64encode(content).decode('utf-8')
        
        # 构建请求URL
        url = f'https://api.github.com/repos/{repo}/contents/{file_path}'
        
        # 设置请求头
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        # 构建请求数据
        data = {
            'message': message,
            'content': content_base64,
            'branch': 'main'
        }
        
        # 发送请求
        response = requests.put(url, headers=headers, json=data)
        
        if response.status_code == 201:
            print(f"✅ 成功上传: {file_path}")
            return True
        else:
            print(f"❌ 上传失败: {file_path}, 状态码: {response.status_code}")
            print(f"错误信息: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 上传 {file_path} 时发生错误: {e}")
        return False

def upload_project_to_github():
    """上传整个项目到GitHub"""
    print("=== GitHub自动上传脚本 ===")
    
    # 配置信息（请修改为您的实际信息）
    GITHUB_TOKEN = input("请输入您的GitHub Personal Access Token: ")
    GITHUB_USERNAME = input("请输入您的GitHub用户名: ")
    REPO_NAME = "akshare-api"
    
    repo = f"{GITHUB_USERNAME}/{REPO_NAME}"
    
    # 项目根目录
    project_root = Path(__file__).parent
    
    # 要上传的文件列表
    files_to_upload = [
        "README.md",
        "requirements.txt", 
        "LICENSE",
        ".gitignore",
        "stock_a_share_api_complete.py",
        "stock_market_summary_api.py",
        "stock_individual_info_api.py",
        "stock_quotes_api.py",
        "stock_realtime_data_api.py",
        "stock_historical_data_api.py",
        "stock_minute_data_api.py",
        "stock_tick_data_api.py",
        "AKShare股票数据接口完整文档.md"
    ]
    
    # 上传示例文件
    examples_files = [
        "examples/basic_usage.py",
        "examples/market_analysis.py", 
        "examples/data_visualization.py"
    ]
    
    print(f"\n开始上传项目到 {repo}...")
    
    success_count = 0
    total_count = len(files_to_upload) + len(examples_files)
    
    # 上传主要文件
    for file_path in files_to_upload:
        full_path = project_root / file_path
        if full_path.exists():
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if upload_file_to_github(GITHUB_TOKEN, repo, file_path, content, 
                                   f"Add {file_path}"):
                success_count += 1
        else:
            print(f"⚠️  文件不存在: {file_path}")
    
    # 上传示例文件
    for file_path in examples_files:
        full_path = project_root / file_path
        if full_path.exists():
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if upload_file_to_github(GITHUB_TOKEN, repo, file_path, content,
                                   f"Add {file_path}"):
                success_count += 1
        else:
            print(f"⚠️  文件不存在: {file_path}")
    
    print(f"\n=== 上传完成 ===")
    print(f"成功上传: {success_count}/{total_count} 个文件")
    print(f"仓库地址: https://github.com/{repo}")

if __name__ == "__main__":
    print("使用此脚本需要GitHub Personal Access Token")
    print("获取方法: GitHub Settings → Developer settings → Personal access tokens")
    print("需要权限: repo (完整仓库访问权限)")
    
    confirm = input("\n是否继续? (y/n): ")
    if confirm.lower() == 'y':
        upload_project_to_github()
    else:
        print("已取消上传")
