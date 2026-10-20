# 个人主页维护说明（中英文版）

## 这次新增的功能

- 已删除两版姓名上方的 AI 系统与基础设施 / AI SYSTEMS & INFRASTRUCTURE 标签。

- 顶部新增 EN / 中文切换，当前语言高亮；手机上语言按钮与导航分行排列。
- 默认首页始终为英文 `/`，不按浏览器语言自动跳转；中文版通过顶部按钮进入 `/zh/`。两页都是静态页面，正式网站的切换不依赖 JavaScript。
- 中文版提供个人简介、新闻、科研实习、教育、荣誉和学术服务的中文内容；计划名称保留加粗英文 Huawei’s Top Minds Program。
- 论文题目、作者、期刊/会议名称在两版中均使用正式英文信息，不添加中文译名。
- 两版共用论文列表、照片、邮箱、简历与学术主页链接，不需要重复维护。
- 中文版使用适合中文阅读的字体和行距；保留论文紧凑间距、期刊名称加粗及年份后的论文链接。
- 两种语言分别设置页面语言、标题、描述和 canonical；hreflang 标记两版的对应关系。

此次修改基于 GitHub master 提交 `f9f1b2b`。仅准备预览与代码，没有替你提交或发布。

## 日常改哪个文件

| 内容 | 英文 / 共用文件 | 中文文件 |
| --- | --- | --- |
| 简介、职位、研究方向、教育、学术服务 | `_data/profile.yml` | `_data/zh/profile.yml` |
| 邮箱、照片、简历、Scholar/GitHub/ORCID 链接 | `_data/profile.yml` | 自动共用，不要在中文文件中重复添加 |
| 论文（含作者、期刊、年份、链接） | `_data/publications.yml` | 自动共用 |
| 最新动态 | `_data/news.yml` | `_data/zh/news.yml` |
| 科研实习 | `_data/experience.yml` | `_data/zh/experience.yml` |
| 荣誉 | `_data/honors.yml` | `_data/zh/honors.yml` |
| 导航、栏目标题、按钮文案 | `_data/i18n.yml` 中的 `en` | 同一文件中的 `zh` |
| 字号、间距、颜色 | `assets/css/academic.css` | 同一文件末尾的中文专用规则 |
| 页面结构 | `_layouts/academic.html` | 两版共用模板 |

只改个人信息时，通常只需要编辑 `_data` 下的 YAML 文件。用空格缩进，不用 Tab。包含冒号等特殊字符的内容建议加引号。

### 新增论文

在 `_data/publications.yml` 顶部复制一条条目，更新以下字段：

```yaml
- title: "Your Paper Title"
  authors: "Haikang Diao, Coauthor A, Coauthor B"
  venue: "JSSC"
  year: 2027
  venue_full: "IEEE Journal of Solid-State Circuits"
  url: "https://ieeexplore.ieee.org/document/文章编号"
```

两版会同时新增这篇论文，Haikang Diao 自动加粗。若为共同第一作者，可加：

```yaml
  author_note: "co-first author"
```

英文显示 `(co-first author)`，中文显示 `(共同第一作者)`。推荐在作者姓名后直接添加 `*`，例如 `Haikang Diao*`。网页会自动将星号显示为右上角上标，两版均有共同第一作者图例。2026 年 UniPD / TCAS-I 论文采用这种方式。不要猜测共同作者的贡献标记。

**新增论文后，记得同步修改两份 profile.yml 的 achievements：目前为第一作者论文 11 篇（其中共同第一作者论文 2 篇）。该文字不会自动计数。**

### 新增动态

英文 `_data/news.yml` 顶部：

```yaml
- date: "Jan 2027"
  text: "Our paper was accepted by ..."
```

中文 `_data/zh/news.yml` 顶部：

```yaml
- date: "2027 年 1 月"
  text: "我们的论文被……录用。"
```

每版默认展示最新 5 条，其余在“更早动态 / Earlier news”中展开。新动态需手动添加两种语言。

### 简介、照片、简历

两份 profile.yml 的 `intro` 为当前工作，`biography` 为教育背景，`academic_research` 为求学期间研究，`achievements` 为成果与荣誉。这四段允许使用可信的 `<strong>` 和 `<a>` HTML 标签。

- 邮箱只改 `_data/profile.yml` 的 `email`，两版自动同步。
- 更换照片：覆盖 `images/profile.jpg`，或修改共用 `photo` 字段。
- 更换简历：将 PDF 放入 `files/`，修改共用 `cv` 字段。旧网站其他页面的 CV 菜单可同步修改 `_data/navigation.yml`。
- 本次未修改简历 PDF 本身，仍为原来的 2026-05-05 版本。
- 学术服务的 `TNNSRE` 沿用旧页面，请核对是否应为 `TNSRE`；如需修正，两份 profile.yml 同步改。

## 本地预览

完整源码包内有 `_preview/homepage-preview.html`，直接双击用浏览器打开，默认显示英文。右上角 EN / 中文可离线切换；论文、Scholar 和简历等在线链接仍需网络。

修改源文件后，需要重新生成预览：

1. 安装 Python 3.10 或以上，安装时勾选 Add Python to PATH。
2. 在网站文件夹打开终端，首次运行：

```powershell
py -m pip install -r tools/preview-requirements.txt
```

3. 每次修改后双击 `PREVIEW.bat`，或运行：

```powershell
py tools/preview.py --open
```

要默认打开中文：

```powershell
py tools/preview.py --lang zh --open
```

没有 `py` 时用 `python` 替代。预览 HTML 由源码生成，**不要直接编辑预览文件**。预览中的语言切换使用本地脚本，正式网站通过 `/` 和 `/zh/` 两个独立静态页面切换。

## 用 GitHub 网页上传增量包

1. 解压 `Haikang_Bilingual_GitHub_Update_v4.zip`。
2. 打开仓库 Code 页面，确认分支是 `master`，点击 **Add file → Upload files**。
3. 将解压后里面的文件和文件夹拖入仓库根目录。不要上传 ZIP，不要套一层压缩包名称文件夹。
4. 上传后的路径应直接是 `_data/i18n.yml`、`_data/zh/profile.yml`、`_pages/about-zh.md` 等。
5. 填写提交信息 `Add English and Chinese homepages`，点击 **Commit changes**。
6. 等 Actions 的 Pages 发布成功，再访问原首页与 `/zh/`，分别检查语言切换。

增量包只包含相对于上述提交新增/修改的文件，不必删除旧代码。完整源码包用于本地保存与编辑，包含全部原有资源和预览；网页上传更新时使用增量包即可。

## 直接导出静态网站（可选）

双击 `EXPORT_WEBSITE.bat` 或运行 `py tools/export_static.py`，生成 `_public/`：

- `index.html`：英文页；
- `zh/index.html`：中文页；
- `files/Haikang_Diao_CV.pdf`：共用简历；
- `_redirects`：保留旧 About 入口。

两页内嵌照片和样式，导出后可直接托管；导出器保留可用的相对语言链接。这个目录只包含个人主页与简历，历史博客/模板页面保留在完整 Jekyll 源码中。当前使用 GitHub Pages 时继续上传源码增量包即可。

## 验证范围

预览与导出使用同一 Liquid 模板、YAML 数据和 CSS。交付时检查双语内容、论文原文一致性、导航与语言链接、共一标记和压缩包完整性；并使用浏览器检查桌面与 390px 宽度布局、正式页面切换以及离线预览的往返切换。当前环境没有 Ruby/Jekyll，未执行完整的 GitHub Pages 构建，正式发布仍需确认 Actions 成功。
