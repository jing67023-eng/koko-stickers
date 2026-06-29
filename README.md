# Koko 表情包自动发布项目

这个项目用于维护 Koko 小手机表情包。以后只需要把新图片放进 `stickers/`，双击 `update.bat`，再复制生成的 `koko_import.txt` 导入 Koko。

## 目录说明

- `stickers/`：最终表情图片目录，支持 `.jpg`、`.jpeg`、`.png`、`.gif`。
- `generate_koko_import.py`：自动扫描 `stickers/` 并生成 Koko 导入文件。
- `koko_import.txt`：生成后的导入清单，格式为 `表情名 URL`。
- `update.bat`：一键提交、推送并重新生成导入清单。

## 图片地址规则

所有图片统一使用 GitHub Pages：

```text
https://jing67023-eng.github.io/koko-stickers/stickers/文件名
```

例如：

```text
猫点赞 https://jing67023-eng.github.io/koko-stickers/stickers/猫点赞.jpg
猫趴桌 https://jing67023-eng.github.io/koko-stickers/stickers/猫趴桌.gif
```

## 日常更新流程

1. 把新的表情图片放进 `stickers/`。
2. 给图片改一个没有空格的名字，例如 `猫点赞.jpg`、`猫趴桌.gif`。
3. 双击 `update.bat`。
4. 打开 `koko_import.txt`，全选复制。
5. 粘贴到 Koko 小手机的“批量添加表情包”输入框。

整个流程不需要修改代码。

## update.bat 会做什么

双击后会依次执行：

```text
git add .
git commit -m "update stickers"
git push
python generate_koko_import.py
```

也就是：

- 上传最新的 `stickers/` 到 GitHub。
- 让 GitHub Pages 可以访问这些图片。
- 重新生成本地 `koko_import.txt`。

## 手动生成导入清单

如果只想重新生成 `koko_import.txt`，可以运行：

```text
python generate_koko_import.py
```

生成格式固定为 Koko 支持的 `名字 URL`：

```text
表情名 https://jing67023-eng.github.io/koko-stickers/stickers/文件名
```

## 注意事项

- GIF 不要转成静态图，直接放进 `stickers/`。
- 文件名不要有空格。
- GitHub 仓库需要是公开仓库。
- GitHub Pages 需要在仓库设置里开启，来源选择 `main` 分支和根目录。
- 如果 `git push` 要求登录，请按 GitHub 提示完成登录或配置访问令牌。
