# 个人主页维护说明

这次只替换首页的展示层，保留原有 Jekyll / GitHub Pages 仓库、论文链接、照片、简历 PDF 和其他页面。无需购买服务器或更换域名。

## 一、这次改了什么

- 将原先的博客式首页改成窄侧栏 + 正文的学术主页：侧栏放照片和联系方式，正文突出简介和研究成果。
- 正文 15px；论文作者 14px；章节标题 21px；姓名 34px。统一行距、边距、链接颜色和灰色辅助信息。
- 论文条目的上下内边距从 22px 缩至 12px；标题、作者、出处及 Paper 链接的行距/间距同步收紧；期刊/会议全称加粗；Paper 链接放在年份后面，与出处同行。
- 增加 About / Publications / Experience / CV 导航；手机上侧栏自动移到顶部。
- 原来的博士在读改为 2026 年获得北京大学博士学位。根据本人提供的信息，简介以华为计算产品线高级研究员、Top Minds 计划及昇腾系统架构/AI infra 算子设计工作开头；学术研究方向放在求学经历之后。
- 保留原有 10 篇论文，并新增 UniPD 共同第一作者论文（共 11 篇）、全部原有新闻、9 条荣誉和 3 段实习；新增博士毕业新闻与教育经历。
- 最近 5 条新闻直接展示，旧新闻用“Earlier news”展开；论文统一按“年份/会议或期刊、标题、作者、出处、Paper 链接”呈现。
- 去掉“Top-1 Journal”等主观评价和重复感叹号，润色英文；修复 `<be>` 等无效标记。
- 联系邮箱更新为 diaohaikang@alumni.pku.edu.cn；保留原有 Google Scholar、ORCID 和中文 CV 链接。CV PDF 本身没有改动，仍是原网站链接的 2026-05-05 版本。
- 审稿期刊简称 `TNNSRE` 按原文保留，请本人核对；如原意是 TNSRE，可在 profile.yml 修改。
- 增加键盘焦点提示、跳过导航入口、减少动态效果适配和打印样式。页面不依赖外部字体或前端 JavaScript。

设计参考了 Jon Barron 的研究成果优先结构和 Minimal Light 的紧凑侧栏思路，没有复制对方源码、文案或图片：
- https://jonbarron.info/
- https://minimal-light-theme.yliu.me/

## 二、以后增补内容改哪个文件

| 需要修改的内容 | 文件 |
| --- | --- |
| 姓名、简介、研究方向、邮箱、照片、CV 链接、教育经历、审稿服务 | `_data/profile.yml` |
| 新增/修改论文 | `_data/publications.yml` |
| 新增新闻 | `_data/news.yml` |
| 荣誉 | `_data/honors.yml` |
| 实习经历 | `_data/experience.yml` |
| 字号、颜色、页面宽度、间距 | `assets/css/academic.css` |
| 改变网页结构、栏目名称、导航 | `_layouts/academic.html` |

新闻日期改为 14px 半粗体，经历正文改为 15px，教育学位信息改为 14px；同时加深辅助文字颜色。毕业新闻日期为 June 2026。简介依据当前简历及本人最新补充，突出 11 篇第一/共一论文（含 2 篇共一）、6 款 CIM 加速器设计/5 款流片和荣誉；未把简历中仍处于 Major revision 的 DEAL-CIM 计入已发表论文。

一般只需要编辑 `_data` 里的文件，不用碰 HTML/CSS。

### 新增论文

在 `_data/publications.yml` 最上面复制一条，改成自己的内容。按年份从新到旧放置；这里是第一/共同第一作者论文列表。

```yaml
- title: "Your Paper Title"
  authors: "Haikang Diao, Coauthor A, Coauthor B"
  venue: "JSSC"
  year: 2027
  venue_full: "IEEE Journal of Solid-State Circuits"
  url: "https://ieeexplore.ieee.org/document/论文编号"
```

本人姓名会自动加粗。新增论文支持可选字段 `author_note: "co-first author"`，会在 Haikang Diao 姓名后直接显示共同第一作者说明，不更改作者顺序；UniPD 的题目、作者、DOI、年份及页码依据本人提供的 BibTeX。共同第一作者在姓名后加 `*`，例如 `Haikang Diao*, Haoyi Zhang*`。不要猜测尚未公布的文章链接。

### 新增新闻

在 `_data/news.yml` 最上面加：

```yaml
- date: "Jan 2027"
  text: "Our paper was accepted by ..."
```

页面自动只展示最前面的 5 条，其余放进折叠区。日期请用引号，避免 YAML 把它当成日期对象。

### 修改个人简介或简历

在 `_data/profile.yml` 修改 `intro`、`biography`、`email`、`cv` 等字段。

`intro`、`biography`、`academic_research`、`achievements` 可使用可信 HTML 链接/加粗；分别记录当前工作、教育背景、求学期间研究及代表成果，`role` / `employer` 是侧栏岗位/单位。例如 `<a href="https://...">Prof. ...</a>`。不要把未经检查的第三方 HTML 放进来。

替换简历有两种方法：
1. 把新的 PDF 放到 `files/` 下，沿用旧文件名；
2. 使用新文件名，然后修改 `profile.yml` 的 `cv` 字段；为了让旧页面的菜单同步，也修改 `_data/navigation.yml` 里的 CV 路径。

更换照片时，替换 `images/profile.jpg`，或修改 `profile.yml` 的 `photo` 字段。

YAML 使用空格缩进，不用 Tab。文字含有 `:`、`#` 等符号时建议整段放在英文双引号内；英文双引号本身需要转义。遇到格式错误，预览命令会提示文件和行号。

### 修改字体

打开 `assets/css/academic.css` 顶部：

```css
:root {
  --font-body: 15px;   /* 正文字号，例如改成 14px */
  --font-small: 14px;  /* 作者等辅助信息 */
  --page-width: 1060px;
}
```

姓名字号在 `h1`，章节标题在 `h2`，论文标题在 `.publication h3`。手机规则在文件底部的 `@media` 中。

## 三、Windows 本地修改和预览

### 现在查看这一版

直接用浏览器打开随代码提供的 `_preview/homepage-preview.html`。它包含照片和样式，可离线查看，旧新闻可展开，页内导航可用。论文、Scholar、CV 等外部链接仍需网络。

### 第一次配置

1. 安装 Python 3.10 或更新版本（从 https://www.python.org/ 下载），安装时勾选 Add Python to PATH。
2. 用 VS Code 或其他纯文本编辑器打开整个网站文件夹。
3. 在该文件夹打开终端，只需安装一次预览依赖：

```powershell
py -m pip install -r tools/preview-requirements.txt
```

若系统没有 `py` 命令，可以用 `python` 替代。

### 每次修改后

1. 编辑 `_data/*.yml` 并保存。
2. 双击根目录的 `PREVIEW.bat`。
3. 浏览器会打开重新生成的 `_preview/homepage-preview.html`。
4. 检查电脑窗口和窄窗口的显示、新闻、论文及 CV 链接。

也可以直接运行：

```powershell
py tools/preview.py --open
```

**预览文件由数据自动生成，不要直接编辑它。** 每次修改源文件后要重新执行预览；它不会自动热更新。

本地预览使用和正式首页相同的 Liquid 模板、YAML 数据及 CSS，但不执行整个 Jekyll 网站的插件与构建。因此它用于确认首页；完整构建和历史页面最终以 GitHub Pages 的构建结果为准。

## 四、确认后发布：推荐 GitHub Desktop

你无需在 GitHub 网页里逐个编辑文件。

1. 使用官方 GitHub Desktop 登录你的账号，选择 **File → Clone repository**，克隆 `haikangdiao/haikangdiao.github.io`。
2. 把这次修改后的文件覆盖到这个本地仓库。不要删除本地仓库的 `.git` 文件夹。
3. 以后直接在这个本地仓库编辑、运行预览。
4. 预览满意后，在 GitHub Desktop 查看 Changes，确认只有自己的改动。
5. 填写说明，例如 `Update publications and news`，点击 **Commit to master**，再 **Push origin**。
6. 在 GitHub 的 Actions / Pages 中等待构建成功，再打开 https://haikangdiao.github.io/ 。

首次发布本次改版，提交说明可用：`Redesign academic homepage and simplify content maintenance`。

当前交付状态：仅准备修改与预览，没有 commit/push；需你确认后再提交。

如果用命令行，先核对分支与远端，不要强制推送：

```bash
git status
git diff
# 核对完成后，选择本次变更文件，再 commit / push。
```

## 五、涉及文件与验证范围

新增：
- `_layouts/academic.html`
- `assets/css/academic.css`
- `_data/profile.yml`
- `_data/publications.yml`
- `_data/news.yml`
- `_data/honors.yml`
- `_data/experience.yml`
- `tools/preview.py`
- `tools/preview-requirements.txt`
- `PREVIEW.bat`
- `SITE_EDITING.md`

修改：`_pages/about.md`、`_config.yml`、`.gitignore`。

旧页面与原始静态资源保留。主页保留 `/`、`/about/`、`/about.html` 的原有入口（后两个由原来的 redirect-from 插件处理）。

已进行：Liquid 严格渲染、数据条数/原论文标题作者及链接迁移核对、HTML 锚点及本地资源存在检查、CSS 语法与 Git 差异检查。

限制：当前环境没有 Ruby/Jekyll 和可用于此项目的浏览器 QA 通道，因此尚未执行完整 Jekyll 构建及实际桌面/手机浏览器视觉验收。请通过预览确认视觉效果；正式提交后还需检查 GitHub Pages 构建。


## 六、不使用 GitHub：直接上传发布

安装过预览依赖后，编辑内容并双击 `EXPORT_WEBSITE.bat`，或者运行 `py tools/export_static.py`。

生成的 `_public` 文件夹就是可直接托管的网站：`index.html` 已含全部样式与照片，`files/Haikang_Diao_CV.pdf` 是简历，`_redirects` 保留 About 入口。网页显示和邮件链接使用最新校友邮箱；简历 PDF 沿用你提供的版本，未修改其中的旧邮箱或履历。

登录 Netlify 后打开 https://app.netlify.com/drop ，拖入 `_public` 文件夹（直接包含 index.html 的这一层），无需连接 GitHub。发布后确认站点允许公开访问，并用未登录的窗口打开分配的网址。

以后在原站点的 Deploys 页面上传重新生成的 `_public` 文件夹，以更新同一个网址，不要每次新建站点。也可使用 Cloudflare Pages 的 Direct Upload。

这份导出只包含当前个人主页和关联简历；旧 AcademicPages 模板的博客、教学等页面仍在完整源码中。新平台会分配新的域名，原来的 haikangdiao.github.io 仍属于 GitHub Pages。
