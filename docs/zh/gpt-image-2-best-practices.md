# `gpt-image-2` 生图最佳实践

本文基于本仓库在 `sub2api` + `requests` 路径上的实测结果，以及 OpenAI 官方图像生成文档整理，目标是把“能出图”收敛成“稳定出对图”的调用规范。

---

## 1. 推荐接口

| 场景 | 推荐接口 | 说明 |
|---|---|---|
| 单张图、单提示词 | `POST /v1/images/generations` | 本仓库当前中转环境下的首选路径，稳定性最好。 |
| 需要多步工具编排 | `POST /v1/responses` + `image_generation` | 仅在你确认中转层已正确支持时使用；不要把它当默认路径。 |
| 文字很多、标签很多、注释很多 | 先生成底图，再后处理叠字 | 图像模型对复杂中文文本不稳定，后处理更可靠。 |

**硬规则**：`gpt-image-2` 的默认生图路径优先使用 `images/generations`，不要为了“看起来更统一”强行绕成 `responses`。

---

## 2. 默认参数

| 用途 | 推荐值 | 说明 |
|---|---|---|
| 全景厂区底图 | `size=2048x1152` | 横向鸟瞰图优先用这个尺寸。 |
| 快速试探 | `size=1024x1024` 或 `1280x720` | 先看构图是否跑偏。 |
| 最终成图 | `quality=high` | 需要稳定细节时使用。 |
| 草图验证 | `quality=low` 或 `medium` | 只看布局时可降档。 |
| 背景模式 | `auto` 或 `opaque` | `gpt-image-2` 不支持透明背景直出。 |

**硬规则**：如果目标是工程底图、厂区布局图、产品展示图，优先把构图跑对，再考虑局部细节。

---

## 3. 提示词策略

### 3.1 先写场景，再写主体，再写约束

推荐顺序：

1. 场景
2. 主体
3. 构图
4. 材质和氛围
5. 禁止项

示例：

```text
绘制一张真实的工业园区厂区鸟瞰工程底图，45度俯视。
场景：灰色混凝土地面、围栏、检修通道、配电柜、变压器、空调设备、消防箱、电缆桥架。
主体：多排白色长方体储能集装箱。
构图：主体占画面大部分区域，设备排列整齐，空间分隔清晰。
约束：不要任何文字，不要任何标注，不要品牌标识，不要英文，不要人物，不要车辆，不要树木遮挡。
```

### 3.2 先用动作词

建议使用“绘制”“画出”“生成一张工程底图”这类明确动作词，不要只写抽象需求。

### 3.3 避免缩写主导画面

像 `BESS`、`PCS` 这类缩写很容易把模型拉向品牌图、Logo 图、标识图。

| 做法 | 结果 | 建议 |
|---|---|---|
| 直接把 `BESS`、`PCS` 当主标题 | 容易跑成 Logo 风格 | 改写成“电池储能站”“厂区布局” |
| 一次性要求很多中文标签 | 容易乱码、漏标、错标 | 先画底图，标签后处理 |
| 只写“生成一张图” | 模型容易自发发挥 | 明确场景、主体、构图、约束 |

**硬规则**：如果你要的是“工程图”，就把工程结构写清楚；如果你要的是“品牌图”，那就单独做，不要混在同一条提示里。

---

## 4. 中文标注策略

| 任务 | 推荐做法 | 不推荐做法 |
|---|---|---|
| 少量文字 | 让模型直接画 1 到 3 个短标签 | 一次要求几十个中文字框 |
| 多个部件标注 | 先生成无文字底图，再用 SVG / PPT 后处理叠加 | 让模型一次输出全套中文标注 |
| 高准确率标注 | 图像阶段负责布局，文字阶段负责排版 | 指望图像模型同时完成布局和文字精确排版 |

**硬规则**：需要“所有部件中文标注”时，默认把它拆成两步：

1. `gpt-image-2` 只负责画底图
2. 文字标签交给后处理叠加

这比一次性生图带字稳定得多。

---

## 5. 直接调用样例

下面是本仓库当前验证过的 `requests` 方式，建议作为默认模板使用。

```python
import base64
from pathlib import Path

import requests

base_url = "https://sub2api.spdt.work/v1"
api_key = "<你的 API Key>"

session = requests.Session()
session.trust_env = False  # 避免继承错误代理

resp = session.post(
    f"{base_url}/images/generations",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    json={
        "model": "gpt-image-2",
        "prompt": "绘制一张真实的工业园区厂区鸟瞰工程底图，45度俯视。场景：灰色混凝土地面、围栏、检修通道、配电柜、变压器、空调设备、消防箱、电缆桥架。主体：多排白色长方体储能集装箱。构图：主体占画面大部分区域，设备排列整齐，空间分隔清晰。约束：不要任何文字，不要任何标注，不要品牌标识，不要英文，不要人物，不要车辆，不要树木遮挡。",
        "size": "2048x1152",
        "quality": "high",
    },
    timeout=180,
)

resp.raise_for_status()
data = resp.json()["data"][0]["b64_json"]
image_bytes = base64.b64decode(data)

out = Path("output/imagegen/bess-base.png")
out.write_bytes(image_bytes)
print(out)
```

**硬规则**：如果你用的是 Python SDK，而不是 `requests`，先确认代理环境没有把 `socks://...` 继承进去；否则会出现看似“模型失败”，实际上是传输层失败。

---

## 6. 本仓库建议默认值

| 默认项 | 建议值 | 备注 |
|---|---|---|
| 接口 | `POST /v1/images/generations` | 默认首选。 |
| 模型 | `gpt-image-2` | 单图生成首选。 |
| 尺寸 | `2048x1152` | 厂区、海报、横版工程图优先。 |
| 质量 | `high` | 最终稿默认。 |
| 代理处理 | `trust_env=False` 或清理 `HTTP_PROXY` / `HTTPS_PROXY` | 避免错误代理干扰。 |
| 中文文本 | 后处理叠加 | 不要强求模型一次性写准大量中文。 |

---

## 7. 常见失败

| 现象 | 典型原因 | 处理方式 |
|---|---|---|
| 跑成 Logo 图 | 缩写太多，品牌词太强 | 去掉 `BESS`、`PCS` 这类主导词，改写成场景描述。 |
| 文字乱码或漏标 | 中文标签太密 | 改成底图 + 后处理。 |
| 请求被代理层拦截 | 继承了错误代理 | 清理代理变量或在 `requests` 中关闭环境继承。 |
| `responses` 只出文本 | 中转层未正确支持图像工具链路 | 回退到 `images/generations`。 |
| 透明背景失败 | `gpt-image-2` 不支持透明背景直出 | 先出实底图，再本地抠图，或换别的方案。 |

---

## 8. 参考

- [OpenAI 图像生成指南](https://platform.openai.com/docs/guides/image-generation)
- [OpenAI 图像工具指南](https://platform.openai.com/docs/guides/tools-image-generation)
- [GPT Image 2 模型页](https://developers.openai.com/api/docs/models/gpt-image-2)
- [Images API 参考](https://platform.openai.com/docs/api-reference/images/generate)
