# 公开模板与私人数据分离工作流

## 核心原则

公开仓库只放“系统模板”。私人仓库或本地文件夹才放“真实个人内容”。

## 推荐结构

```text
psychology-reflection-vault-public/
  模板、说明、通用规则

my-private-psychology-vault/
  真实个人资料
  真实 Sessions/
  真实 Reports/
  真实个案理解和人物侧写
```

## public 仓库可以包含

- 通用 README
- AGENTS.md 工作规则
- 会谈模板
- 记忆架构
- 排期规则
- 空白人物侧写模板
- 空白个案理解模板
- 示例结构说明

## public 仓库不应该包含

- 真实会谈记录
- 真实姓名、联系方式、地址、账号
- 家庭、亲密关系、工作单位等可识别信息
- 心理风险、病史、诊断、药物等私人内容
- AI 自动化生成的个人画像
- 任何不希望陌生人看到的内容

## 更新 public 项目的方式

当私人使用过程中发现某个“通用机制”变得更好时：

1. 先在私人 vault 中验证。
2. 把它抽象成不含个人细节的模板或规则。
3. 更新 public 项目。
4. 检查没有隐私信息后再提交和推送。

## 更新 private vault 的方式

每次真实会谈结束后：

1. 保存 `Sessions/` 会谈记录。
2. 更新 `03_Running_Case_Formulation.md`。
3. 必要时更新 `05_Psychological_Profile.md`。
4. 可选：提交到 private Git 仓库或只保留本地。
