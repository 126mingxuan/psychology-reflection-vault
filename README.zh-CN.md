# Psychology Reflection Vault

**语言：** [English](./README.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Français](./README.fr.md)

一个 Obsidian 风格的心理反思 vault 模板，用于持续进行 AI 辅助的心理反思、会谈记录、个案理解、心理模式追踪，以及月度或年度回顾。

> 重要提示：本项目不是心理治疗、医学诊断、精神科服务或危机干预。如果你处于即时危险、自伤/自杀风险，或可能伤害他人的状态，请立即联系当地紧急服务、专业人员或可信任的人。

## 这个项目解决什么问题

普通 AI 对话经常每次都从零开始。这个 vault 把心理反思变成一个结构化、可阅读、可长期维护的 Markdown 系统，让每次会谈都能继承之前的背景，而不是反复重新介绍自己。

它适合想要：

- 建立每周或定期自我反思；
- 让 AI 对话具有连续性；
- 保存可回看的会谈记录；
- 区分事实、情绪、解释、稳定模式和下次问题；
- 用 public 模板搭建 private 个人心理 vault 的人。

## 如何使用

1. 使用这个仓库作为模板，或 fork 它。
2. 如果你会保存真实个人内容，请把工作仓库设为 private。
3. 用 Obsidian 或任意 Markdown 编辑器打开。
4. 每次反思开始前，让 AI 助手读取核心文件和 `Sessions/` 中最新的一次记录。
5. 每次反思结束后，在 `Sessions/` 保存新的记录，更新 `03_Running_Case_Formulation.md`，并且只在稳定模式变清楚时更新 `05_Psychological_Profile.md`。

## 仓库结构

- `00_Start_Here.md`：入口说明与工作边界
- `01_Client_Profile.md`：用户资料模板
- `02_Therapy_Framework.md`：心理反思框架与安全边界
- `03_Running_Case_Formulation.md`：持续个案理解模板
- `04_Session_Template.md`：单次会谈记录模板
- `05_Psychological_Profile.md`：长期心理画像模板
- `06_Scheduling_Policy.md`：自适应排期规则
- `07_Memory_Architecture.md`：分层记忆与更新规则
- `08_Public_Private_Workflow.md`：公开模板与私人数据分离流程
- `Sessions/`：单次会谈记录
- `Reports/Monthly/`：月度总结
- `Reports/Yearly/`：年度总结

## 公开与私人

这个 public 仓库只应该作为模板，包含可复用的结构、说明和空白模板。

真实个人心理反思内容应该放在单独的 private 仓库或本地文件夹里。不要公开真实会谈记录、个人经历、关系细节、风险记录、联系方式、健康信息，或任何你不希望陌生人看到的内容。

## README 语言切换是怎么做的

GitHub 没有内置的 README 语言切换按钮。常见做法是创建多个 README 文件，然后在顶部互相链接：

```text
README.md
README.zh-CN.md
README.ja.md
README.es.md
README.fr.md
```

然后在 README 顶部写：

```markdown
**Languages:** [English](./README.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Français](./README.fr.md)
```

## License

MIT
