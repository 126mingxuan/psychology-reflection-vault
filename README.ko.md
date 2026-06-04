# AI-Assisted Therapy Support

**언어:** [English](./README.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [한국어](./README.ko.md) | [Português](./README.pt-BR.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md)

지속적이고 구조화된 심리 대화를 위한 local-first AI 보조 치료 지원 시스템입니다.

전문 치료를 대체하지 않습니다. 목표는 낮은 비용으로 심리적 연속성을 지원하는 것입니다. 세션 노트, 사례 이해, 심리 프로필, 전략 라우팅, 일정 제안, 월간/연간 통합, 추적 가능한 장기 기억을 다룹니다.

> 중요: 이 프로젝트는 치료 지향적이지만, 면허가 있는 심리치료, 의학적 진단, 정신과 진료 또는 위기 개입이 아닙니다. 즉각적인 위험, 자해 위험, 타인에게 해를 끼칠 위험이 있다면 지역 응급 서비스, 자격 있는 전문가 또는 신뢰할 수 있는 사람에게 연락하세요.

## 핵심 특징

- **local-first 프라이버시**: 실제 내용은 개인 작업 공간이나 로컬 파일에 남습니다. 프로젝트 서버, 숨겨진 데이터베이스, 내장 텔레메트리가 없습니다.
- **사람과 대화하는 듯한 연속성**: 각 세션은 이전 핵심 내용을 이어받을 수 있습니다.
- **효율적인 장기 기억 읽기**: `09_Continuity_Index.md`, 월간 보고서, 연간 보고서를 통해 전체 기록을 다시 읽지 않고 중요한 내용을 찾습니다.
- **치료 지향 워크플로**: 초기 평가, 구조화된 대화, 능동적 마무리, 기억 업데이트, 다음 세션 전략 추천.
- **적응형 전략**: 정신역동적 탐색, CBT 도구, 가족체계, 마음챙김, 실존적 탐구, 인본주의적 지원, 안전 경계.
- **공개 템플릿과 개인 작업 공간 분리**: 공개 저장소에는 재사용 가능한 구조만 두고, 실제 개인 내용은 비공개로 유지합니다.

## Quick Start

1. **Use this template**을 클릭하거나 저장소를 fork합니다.
2. 개인 작업 공간을 비공개로 만듭니다.
3. 로컬 파일 워크플로, Markdown 편집기, 비공개 저장소 또는 local-first AI 작업 공간에서 엽니다.
4. `01_Client_Profile.md`에 AI가 기억하길 원하는 배경을 적습니다.
5. 다음 프롬프트로 시작합니다.

```text
Read AGENTS.md, the core continuity files, 09_Continuity_Index.md,
the latest psychological profile, the running case formulation,
and the latest relevant notes in Sessions/.
If the archive is large, read monthly/yearly summaries first.
Continue from previous material instead of starting from zero.
Start with one focused opening question.
```

## Use Cases

- 지속적이고 낮은 비용의 심리 지원
- 전문 치료 전후의 정리
- 민감한 대화를 위한 local-first 기억
- AI 심리 연속성 설계

## License

MIT
