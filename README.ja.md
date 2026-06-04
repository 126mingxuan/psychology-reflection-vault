# AI-Assisted Therapy Support

**言語:** [English](./README.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [한국어](./README.ko.md) | [Português](./README.pt-BR.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md)

継続的で構造化された心理的対話のための、local-first な AI 支援セラピーサポートシステムです。

専門的な治療を置き換えるものではありません。目的は、低コストで心理的な継続性を支えることです。セッションノート、ケースフォーミュレーション、心理プロフィール、戦略ルーティング、スケジューリング、月次・年次統合、追跡可能な長期記憶を扱います。

> 重要: このプロジェクトはセラピー志向ですが、認可された心理療法、医学的診断、精神科医療、危機介入ではありません。差し迫った危険、自傷のリスク、または他者を傷つけるリスクがある場合は、地域の緊急サービス、資格を持つ専門家、または信頼できる人に連絡してください。

## 主な特徴

- **local-first のプライバシー**: 実際の内容は個人の作業スペースまたはローカルファイルに保存されます。プロジェクトサーバー、隠れたデータベース、内蔵テレメトリはありません。
- **人間との対話に近い継続性**: 各セッションは過去の重要な内容を引き継げます。
- **効率的な長期記憶読み取り**: `09_Continuity_Index.md`、月次レポート、年次レポートにより、全履歴を読み直さずに重要情報を見つけます。
- **セラピー志向のワークフロー**: 初期評価、構造化された対話、能動的な終了、記憶更新、次回戦略の提案。
- **適応的な戦略**: 精神力動的探索、CBT ツール、家族システム、マインドフルネス、実存的探究、人間性重視の支援、安全境界。
- **公開テンプレート、個人作業スペース**: 公開リポジトリには再利用可能な構造のみを置き、実際の個人内容は非公開にします。

## Quick Start

1. **Use this template** をクリックするか、このリポジトリを fork します。
2. 自分用の非公開作業スペースを作成します。
3. ローカルファイルワークフロー、Markdown エディタ、非公開リポジトリ、または local-first AI ワークスペースで開きます。
4. `01_Client_Profile.md` に AI に覚えてほしい背景を記入します。
5. 次のプロンプトで開始します。

```text
Read AGENTS.md, the core continuity files, 09_Continuity_Index.md,
the latest psychological profile, the running case formulation,
and the latest relevant notes in Sessions/.
If the archive is large, read monthly/yearly summaries first.
Continue from previous material instead of starting from zero.
Start with one focused opening question.
```

## Use Cases

- 継続的で低コストの心理的サポート
- 専門的治療の前後の整理
- センシティブな対話の local-first 記憶
- AI による心理的継続性の設計

## License

MIT
