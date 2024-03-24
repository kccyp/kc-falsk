from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['test.py',
            '-F',  # 创建单个可执行文件
            '--add-data', './app/templates/*;templates',  # 添加 templates 文件夹
            '--add-data', './app/static/*;static',  
            '--add-data', './app/static/js/*;static/js',  
            '--add-data', './resources/datasets;pyecharts/datasets/.'
            ]
    # 执行 PyInstaller
    run(opts)