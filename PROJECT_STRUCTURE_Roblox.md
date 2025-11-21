# Roblox Creator Docs - 프로젝트 구조 분석

## 📊 전체 구조 개요

```
creator-docs/
│
├── 📘 PLATFORM (플랫폼 소개 및 시작)
│   ├── 🚩 Overview
│   ├── 🐤 Get Started
│   ├── 🎨 Studio
│   │   ├── Interface
│   │   ├── Workspace
│   │   ├── Parts & Models
│   │   ├── Materials & Terrain
│   │   └── Physics
│   ├── 🤖 Assistant (AI 어시스턴트)
│   └── 📚 Engine API Reference
│
├── 🛠️ CREATE (생성 및 개발)
│   ├── 🎮 Experiences (경험/게임 생성)
│   │   ├── Get Started
│   │   ├── Projects
│   │   │   ├── Data Model
│   │   │   ├── Client-Server Runtime
│   │   │   ├── Instance Streaming
│   │   │   └── Collaboration
│   │   ├── 3D Workspace
│   │   │   ├── Parts (7개 문서)
│   │   │   ├── Meshes
│   │   │   ├── Models
│   │   │   ├── Materials
│   │   │   └── Terrain
│   │   ├── Physics (29개 문서)
│   │   │   ├── Assemblies
│   │   │   ├── Network Ownership
│   │   │   └── Mechanical Constraints
│   │   ├── Scripting (15개 문서)
│   │   │   ├── Luau Language (22개 문서)
│   │   │   │   ├── Types (Nil, Boolean, Number, String, Table, Enum)
│   │   │   │   ├── Data Structures (Stack, Queue, Metatable)
│   │   │   │   └── Features (Variables, Functions, Operators)
│   │   │   ├── Events & Communication
│   │   │   ├── Input & Controls
│   │   │   └── Advanced Systems
│   │   ├── UI (28개 문서)
│   │   ├── Characters (9개 문서)
│   │   │   ├── Appearance
│   │   │   ├── Emotes
│   │   │   ├── Pathfinding
│   │   │   └── Name/Health Display
│   │   ├── Audio (4개 문서)
│   │   │   ├── Assets
│   │   │   ├── Effects
│   │   │   └── Objects
│   │   ├── Effects (5개 문서)
│   │   │   ├── Beams
│   │   │   ├── Particle Emitters
│   │   │   ├── Light Sources
│   │   │   └── Trails
│   │   ├── Environment (7개 문서)
│   │   │   ├── Lighting
│   │   │   ├── Atmosphere
│   │   │   ├── Skybox
│   │   │   └── Post-Processing
│   │   ├── Chat (6개 문서)
│   │   │   ├── Bubble Chat
│   │   │   ├── Chat Window
│   │   │   ├── Text Chat
│   │   │   └── Voice Chat
│   │   ├── Input (5개 문서)
│   │   ├── Matchmaking (6개 문서)
│   │   ├── Performance Optimization (11개 문서)
│   │   └── Tutorials (135개 문서)
│   │
│   ├── 👤 Avatar (아바타 시스템)
│   │   ├── Avatar Generation
│   │   ├── In-Experience Creation
│   │   ├── Resources
│   │   └── Tutorials
│   │
│   ├── 🎨 Assets (에셋 관리)
│   │   ├── Art & Modeling
│   │   │   ├── Accessories (39개 문서)
│   │   │   ├── Characters (35개 문서)
│   │   │   ├── Modeling (17개 문서)
│   │   │   └── Emotes (4개 문서)
│   │   ├── Animation
│   │   │   ├── Capture
│   │   │   ├── Editor
│   │   │   ├── Curve Editor
│   │   │   └── Inverse Kinematics
│   │   └── Classic Clothing
│   │
│   └── ☁️ Open Cloud (Open Cloud API)
│       ├── Authentication (6개 문서)
│       ├── Guides (11개 문서)
│       ├── Reference (7개 문서)
│       └── Webhooks (2개 문서)
│
├── 📈 SCALE (확장 및 성장)
│   ├── Overview
│   ├── 🔍 Discovery (발견/검색 최적화)
│   ├── 🌍 Localization (다국어 지원)
│   ├── 📊 Analytics (분석 도구)
│   └── 🎯 Design (게임 디자인)
│
├── 💰 MONETIZE (수익화)
│   ├── Overview
│   ├── Experiences (경험 수익화)
│   ├── Avatar (아바타 수익화)
│   └── Assets (에셋 판매)
│
├── 🎓 EDUCATION (교육)
│   ├── Educator Onboarding (6개 문서)
│   ├── Adventure Game Series (7개 문서)
│   ├── Battle Royale Series (9개 문서)
│   ├── Build It Play It Series
│   │   ├── Create and Destroy (16개)
│   │   ├── Galactic Speedway (21개)
│   │   ├── Island of Move (23개)
│   │   ├── Mansion of Wonder (22개)
│   │   └── Story Games (12개)
│   ├── Lesson Plans (21개 문서)
│   ├── Resources (13개 문서)
│   └── Support (7개 문서)
│
├── 🔧 DEVELOPMENT (개발자용 API 레퍼런스)
│   ├── 📚 Engine API Reference
│   │   ├── Overview
│   │   │
│   │   ├── Classes (633개 YAML 파일)
│   │   │   ├── Core Classes
│   │   │   │   ├── Instance (모든 클래스의 기본)
│   │   │   │   ├── DataModel
│   │   │   │   ├── Workspace
│   │   │   │   └── ServiceProvider
│   │   │   │
│   │   │   ├── Scripting Classes
│   │   │   │   ├── Script, LocalScript, ModuleScript
│   │   │   │   ├── BaseScript, LuaSourceContainer
│   │   │   │   └── RunService
│   │   │   │
│   │   │   ├── Game Objects
│   │   │   │   ├── Part, MeshPart, BasePart
│   │   │   │   ├── Model, PVInstance
│   │   │   │   ├── Tool, Backpack
│   │   │   │   └── Camera
│   │   │   │
│   │   │   ├── Character & Animation
│   │   │   │   ├── Humanoid, HumanoidDescription
│   │   │   │   ├── Animation, AnimationTrack, Animator
│   │   │   │   ├── AnimationController
│   │   │   │   └── CharacterAppearance
│   │   │   │
│   │   │   ├── GUI Classes
│   │   │   │   ├── ScreenGui, Frame, TextLabel, TextButton
│   │   │   │   ├── ImageLabel, ImageButton
│   │   │   │   ├── GuiObject, GuiBase2d
│   │   │   │   └── UI Layout Classes (Grid, List, Flex 등)
│   │   │   │
│   │   │   ├── Services
│   │   │   │   ├── DataStoreService, DataStore
│   │   │   │   ├── HttpService
│   │   │   │   ├── MarketplaceService
│   │   │   │   ├── UserInputService
│   │   │   │   ├── ContextActionService
│   │   │   │   ├── TweenService
│   │   │   │   ├── TeleportService
│   │   │   │   ├── ReplicatedStorage
│   │   │   │   └── 기타 50개 이상의 서비스
│   │   │   │
│   │   │   ├── Communication
│   │   │   │   ├── RemoteEvent, RemoteFunction
│   │   │   │   └── BindableEvent, BindableFunction
│   │   │   │
│   │   │   ├── Lighting & Effects
│   │   │   │   ├── Lighting, Light, PointLight, SpotLight
│   │   │   │   ├── ParticleEmitter
│   │   │   │   ├── Beam, Trail
│   │   │   │   └── Atmosphere, Sky
│   │   │   │
│   │   │   ├── Audio
│   │   │   │   ├── Sound, SoundGroup
│   │   │   │   ├── SoundService
│   │   │   │   └── Audio Effects (Echo, Reverb, Distortion 등)
│   │   │   │
│   │   │   ├── Physics
│   │   │   │   ├── Constraints (Weld, Motor, Spring 등)
│   │   │   │   ├── BodyMover
│   │   │   │   └── Assembly
│   │   │   │
│   │   │   └── Value Objects
│   │   │       ├── BoolValue, IntValue
│   │   │       ├── NumberValue, StringValue
│   │   │       └── ValueBase
│   │   │
│   │   ├── DataTypes (35개 YAML 파일)
│   │   │   ├── Math Types
│   │   │   │   ├── Vector2, Vector3, Vector2int16, Vector3int16
│   │   │   │   ├── CFrame
│   │   │   │   ├── UDim, UDim2
│   │   │   │   └── Rect, Region3
│   │   │   ├── Color Types
│   │   │   │   ├── Color3
│   │   │   │   ├── ColorSequence, ColorSequenceKeypoint
│   │   │   │   └── BrickColor
│   │   │   ├── Raycasting Types
│   │   │   │   ├── Ray
│   │   │   │   ├── RaycastParams, RaycastResult
│   │   │   │   └── OverlapParams
│   │   │   ├── Animation Types
│   │   │   │   ├── NumberSequence, NumberSequenceKeypoint
│   │   │   │   ├── FloatCurveKey
│   │   │   │   └── RotationCurveKey
│   │   │   ├── Pathfinding Types
│   │   │   │   ├── PathWaypoint
│   │   │   │   └── Path2DControlPoint
│   │   │   └── 기타 타입들
│   │   │       ├── TweenInfo
│   │   │       ├── PhysicalProperties
│   │   │       ├── DateTime
│   │   │       ├── Font
│   │   │       └── Secret
│   │   │
│   │   ├── Enums (499개 YAML 파일)
│   │   │   ├── Material, MaterialPattern
│   │   │   ├── HumanoidRigType, HumanoidStateType
│   │   │   ├── UserInputType, UserInputState
│   │   │   ├── CameraMode, CameraType
│   │   │   ├── AnimationPriority
│   │   │   ├── ParticleEmitter 관련 (5개 이상)
│   │   │   ├── Text 관련 (TextXAlignment, TextYAlignment 등)
│   │   │   └── 기타 480개 이상의 Enum
│   │   │
│   │   ├── Globals (2개 YAML 파일)
│   │   │   ├── LuaGlobals (Luau 언어 전역 함수)
│   │   │   └── RobloxGlobals (Roblox 전역 함수)
│   │   │
│   │   └── Libraries (11개 YAML 파일)
│   │       ├── math (수학 함수)
│   │       ├── string (문자열 처리)
│   │       ├── table (테이블 조작)
│   │       ├── vector (벡터 연산)
│   │       ├── task (비동기 작업)
│   │       ├── coroutine (코루틴)
│   │       ├── debug (디버깅)
│   │       ├── os (운영체제)
│   │       ├── utf8 (UTF-8 인코딩)
│   │       ├── buffer (버퍼 처리)
│   │       └── bit32 (비트 연산)
│   │
│   └── ☁️ Cloud API Reference (Open Cloud REST API)
│       ├── Assets API (v1.json)
│       ├── DataStores API
│       │   ├── Ordered DataStores (v1.json)
│       │   └── Standard DataStores (v1.json)
│       ├── Messaging Service (v1.json)
│       ├── Developer Products API (v1.json)
│       ├── Game Passes HTTP Service (v1.json)
│       ├── Secrets Store Service (v1.json)
│       ├── Toolbox Service (v1.json)
│       ├── Universes API (v1.json)
│       ├── Open Eval API (v1.json)
│       └── OpenAPI Specification (openapi.json)
│
├── 📁 PRODUCTION (프로덕션 및 배포)
│   ├── Publishing (96개 문서)
│   │   ├── Publish Experiences and Places
│   │   ├── Account Verification
│   │   ├── GDPR and CCPA
│   │   └── DMCA Guidelines
│   ├── Game Design (128개 문서)
│   ├── Analytics
│   ├── Localization
│   ├── Promotion
│   └── Optimization
│
├── 🎨 RESOURCES (참고 자료)
│   ├── Tutorial Resources (52개 문서)
│   ├── Sample Projects
│   │   ├── The Mystery of Duvall Drive
│   │   └── Beyond the Dark
│   └── Developer Modules
│
└── 📰 NAVIGATION (네비게이션 구조)
    └── common/navigation/
        ├── documentation.yaml (메인 네비게이션)
        ├── platform.yaml
        ├── engine/
        │   ├── reference.yaml (자동 생성)
        │   ├── guides.yaml
        │   ├── tutorials.yaml
        │   ├── resources.yaml
        │   └── studio.yaml
        ├── avatar/
        ├── cloud/
        ├── monetize/
        └── scale/
```

## 🎯 주요 섹션별 상세 설명

### 1. PLATFORM 섹션

**목적**: 플랫폼 소개 및 기본 시작 가이드

- **Overview**: Roblox 플랫폼 개요
- **Get Started**: 시작하기 가이드
- **Studio**: Roblox Studio 사용법 (22개 문서)
  - Interface, Workspace, Parts, Materials, Physics 등
- **Assistant**: AI 어시스턴트 가이드 (3개 문서)
  - Overview, Guide, Prompt Engineering
- **Engine API Reference**: 엔진 API 참조 링크

### 2. CREATE 섹션

**목적**: 경험(게임) 생성 및 개발 가이드

#### 2.1 Experiences (경험 생성)

가장 큰 섹션으로, 게임 개발의 모든 측면을 다룹니다:

- **Get Started**: 시작하기
- **Projects**: 프로젝트 관리 (20개 문서)
  - Data Model, Client-Server Architecture, Collaboration
- **3D Workspace**: 3D 작업 공간 (6개 문서)
  - Parts, Meshes, Models, Materials, Terrain
- **Physics**: 물리 시스템 (29개 문서)
  - Assemblies, Network Ownership, Constraints
- **Scripting**: 스크립팅 (15개 문서)
  - Luau 언어, 이벤트, 통신, 입력 처리
- **UI**: 사용자 인터페이스 (28개 문서)
- **Characters**: 캐릭터 시스템 (9개 문서)
- **Audio**: 오디오 시스템 (4개 문서)
- **Effects**: 시각 효과 (5개 문서)
- **Environment**: 환경 설정 (7개 문서)
- **Chat**: 채팅 시스템 (6개 문서)
- **Tutorials**: 튜토리얼 (135개 문서)

#### 2.2 Avatar (아바타)

- Avatar Generation: 아바타 생성
- In-Experience Creation: 경험 내 아바타 생성
- Resources: 리소스
- Tutorials: 튜토리얼

#### 2.3 Assets (에셋)

- Art & Modeling: 아트 및 모델링
  - Accessories (39개), Characters (35개), Modeling (17개)
- Animation: 애니메이션
  - Capture, Editor, Curve Editor, IK
- Classic Clothing: 클래식 의상

#### 2.4 Open Cloud

REST API를 통한 외부 서비스 연동:
- Authentication: 인증 (6개 문서)
- Guides: 가이드 (11개 문서)
- Reference: API 참조 (7개 문서)
- Webhooks: 웹훅 (2개 문서)

### 3. SCALE 섹션

**목적**: 게임 확장 및 성장 전략

- **Overview**: 확장 개요
- **Discovery**: 발견/검색 최적화
- **Localization**: 다국어 지원
- **Analytics**: 분석 도구
- **Design**: 게임 디자인

### 4. MONETIZE 섹션

**목적**: 수익화 가이드

- **Overview**: 수익화 개요
- **Experiences**: 경험 수익화
- **Avatar**: 아바타 수익화
- **Assets**: 에셋 판매

### 5. EDUCATION 섹션

**목적**: 교육자 및 학습자 지원

- **Educator Onboarding**: 교육자 온보딩 (6개 문서)
- **Tutorial Series**: 튜토리얼 시리즈
  - Adventure Game (7개), Battle Royale (9개)
  - Build It Play It 시리즈 (94개 문서)
- **Lesson Plans**: 레슨 플랜 (21개 문서)
- **Resources**: 리소스 (13개 문서)
- **Support**: 지원 (7개 문서)

### 6. DEVELOPMENT 섹션

**목적**: 개발자를 위한 상세 API 레퍼런스

#### 6.1 Engine API Reference

**Classes (633개)**
- 모든 Roblox 엔진 클래스의 완전한 API 문서
- 계층 구조: Object → Instance → PVInstance → BasePart → Part/MeshPart
- 서비스 클래스, 스크립트 클래스, 게임 객체, GUI, 통신, 물리 등

**DataTypes (35개)**
- 수학적 타입 (Vector, CFrame, UDim)
- 색상 타입 (Color3, ColorSequence, BrickColor)
- 레이캐스팅 타입 (Ray, RaycastResult)
- 애니메이션 타입 (NumberSequence, FloatCurveKey)
- 기타 특수 타입들

**Enums (499개)**
- Material, HumanoidRigType, UserInputType
- CameraMode, AnimationPriority
- ParticleEmitter 관련
- Text 관련
- 기타 480개 이상의 열거형

**Globals (2개)**
- LuaGlobals: Luau 언어 전역 함수
- RobloxGlobals: Roblox 전역 함수

**Libraries (11개)**
- math, string, table, vector
- task, coroutine, debug, os
- utf8, buffer, bit32

#### 6.2 Cloud API Reference

REST API 스펙 (JSON 형식):
- Assets, DataStores, Messaging Service
- Developer Products, Game Passes
- Secrets Store, Toolbox Service
- Universes API, Open Eval API
- OpenAPI Specification

### 7. PRODUCTION 섹션

**목적**: 프로덕션 및 배포

- **Publishing**: 퍼블리싱 (96개 문서)
- **Game Design**: 게임 디자인
- **Analytics**: 분석
- **Localization**: 현지화
- **Promotion**: 프로모션
- **Optimization**: 최적화

### 8. NAVIGATION 구조

**목적**: 문서 사이트의 메뉴 구조 정의

- **common/navigation/**: 네비게이션 설정 파일들
- YAML 형식으로 계층 구조 정의
- 콘텐츠와 네비게이션 분리로 다국어 지원 용이

---

## 📈 통계

### Engine API
- **Classes**: 633개
- **Enums**: 499개
- **DataTypes**: 35개
- **Libraries**: 11개
- **Globals**: 2개

### 전체 참조 파일
- **YAML 파일**: 약 1,189개
- **JSON 파일**: 13개 (Cloud API)
- **Markdown 파일**: 8개 (개요 및 인덱스)

### 가이드 문서
- **튜토리얼**: 135개 파일
- **프로덕션**: 96개 파일
- **프로젝트**: 20개 파일
- **Studio**: 22개 파일
- **Scripting**: 15개 파일
- **UI**: 28개 파일
- **Physics**: 29개 파일
- **기타**: 수백 개의 가이드 문서

### 에셋 파일
- **튜토리얼 에셋**: 1,410개 파일
- **교육 에셋**: 737개 파일
- **아트 에셋**: 514개 파일
- **Studio 스크린샷**: 458개 파일
- **기타**: 수천 개의 이미지, 비디오, 오디오 파일

### 총 문서 수
- **총 문서 수**: 약 2,000개 이상
  - API 참조: 1,189개 (YAML)
  - 가이드 문서: 약 500개 (Markdown)
  - 에셋 파일: 수천 개

---

## 🔗 문서 간 관계

```
PLATFORM (소개)
    ↓
CREATE (생성 가이드)
    ├── Experiences
    │   ├── Scripting → Luau Language
    │   ├── Studio Manual
    │   └── Tutorials
    │       ↓
    │   DEVELOPMENT (API 레퍼런스)
    │       ├── Engine API
    │       │   ├── Classes (633개)
    │       │   ├── DataTypes (35개)
    │       │   ├── Enums (499개)
    │       │   ├── Globals (2개)
    │       │   └── Libraries (11개)
    │       └── Cloud API
    ├── Avatar
    ├── Assets
    └── Open Cloud
        ↓
SCALE (확장)
    ├── Discovery
    ├── Localization
    ├── Analytics
    └── Design
        ↓
MONETIZE (수익화)
    ├── Experiences
    ├── Avatar
    └── Assets
        ↓
PRODUCTION (배포)
    ├── Publishing
    ├── Game Design
    └── Optimization
```

---

## 🎓 학습 경로 추천

### 초보자 경로

1. **PLATFORM** → Get Started (플랫폼 이해)
2. **CREATE** → Experiences → Get Started
3. **CREATE** → Experiences → Studio → Interface
4. **CREATE** → Experiences → Scripting → Luau → Types
5. **CREATE** → Experiences → Tutorials (기초 튜토리얼)

### 중급자 경로

1. **CREATE** → Experiences → Scripting → Events & Communication
2. **CREATE** → Experiences → Scripting → Advanced Systems
3. **CREATE** → Experiences → UI
4. **DEVELOPMENT** → Engine API → Classes (필요한 클래스만)
5. **CREATE** → Experiences → Performance Optimization

### 고급자 경로

1. **DEVELOPMENT** → Engine API Reference 전체 탐색
2. **CREATE** → Open Cloud → Guides & Reference
3. **SCALE** → Analytics, Localization
4. **PRODUCTION** → Game Design, Optimization
5. **CREATE** → Experiences → Advanced Physics

### 전문가 경로

1. **DEVELOPMENT** → Engine API → 모든 Classes, DataTypes, Enums
2. **CREATE** → Open Cloud → 모든 API 엔드포인트
3. **SCALE** → 전체 섹션
4. **PRODUCTION** → 전체 섹션
5. **MONETIZE** → 전체 섹션

---

## 📝 특징

### 1. 자동 생성 시스템
- `reference/engine/` 디렉토리의 YAML 파일들은 자동 생성됨
- 파일 상단에 "This file is automatically generated" 주석 포함
- 버그 리포트는 DevForum을 통해 제출

### 2. 계층적 구조
- 클래스 상속 관계를 `inherits`와 `descendants`로 표현
- 네비게이션 파일에서도 계층 구조 반영 (`section` 중첩)
- Object → Instance → PVInstance → BasePart → Part/MeshPart

### 3. 콘텐츠와 네비게이션 분리
- 실제 문서 콘텐츠: `content/en-us/`
- 네비게이션 구조: `content/common/navigation/`
- 콘텐츠 재사용 및 다국어 지원 용이

### 4. 다국어 지원 구조
- 현재 `en-us/` (영어)만 있으나, 구조상 다른 언어 추가 가능
- 예: `ko-kr/`, `ja-jp/` 등

### 5. 타입별 명확한 분류
- Classes, DataTypes, Enums, Globals, Libraries로 명확히 구분
- 각 카테고리별 인덱스 페이지 제공

### 6. 풍부한 메타데이터
- 각 API 항목에 `summary`, `description`, `code_samples` 포함
- 타입 정보, 기본값, 파라미터 설명 등 상세한 메타데이터
- 상속 관계, 하위 클래스 목록 등 관계 정보

### 7. 실용성 중심
- 이론보다 실전 예제와 사용법 중심
- 튜토리얼이 135개로 매우 풍부
- 샘플 프로젝트 제공

### 8. 완전한 API 레퍼런스
- 모든 클래스, Enum, DataType 문서화
- 633개 클래스, 499개 Enum, 35개 DataType
- Cloud API도 완전히 문서화

---

## 📁 파일 형식

- **`.yaml`** - API 참조 문서 (자동 생성)
  - Classes, DataTypes, Enums, Globals, Libraries
- **`.md`** - 가이드 및 튜토리얼 문서 (수동 작성)
  - Guides, Tutorials, Overview
- **`.json`** - Open Cloud API 스펙
  - REST API 엔드포인트 정의
- **`.png`, `.jpg`, `.mp4`, `.webm`** - 문서용 에셋 파일
  - 스크린샷, 비디오, 이미지

---

## 🎯 API 문서 파일 구조

### YAML 파일 구조 예시

각 API 문서는 YAML 형식으로 작성되며, 다음과 같은 구조를 가집니다:

```yaml
# 자동 생성 파일 (수동 편집 금지)
name: Instance              # API 이름
type: class                 # 타입 (class, datatype, enum)
summary: |                  # 요약 설명
description: |              # 상세 설명
inherits: [Object]          # 상속 관계
descendants: [...]          # 하위 클래스 목록
properties: [...]           # 속성 목록
methods: [...]              # 메서드 목록
events: [...]              # 이벤트 목록
callbacks: [...]           # 콜백 목록
```

### 주요 필드

- **`name`**: API 이름
- **`type`**: API 타입 (class, datatype, enum)
- **`summary`**: 간단한 요약
- **`description`**: 상세 설명 (Markdown 지원)
- **`inherits`**: 상속받는 부모 클래스
- **`descendants`**: 하위 클래스 목록
- **`properties`**: 속성 (name, type, summary, description, default)
- **`methods`**: 메서드 (name, summary, parameters, returns)
- **`events`**: 이벤트
- **`code_samples`**: 코드 예제

---

## 결론

이 프로젝트는 대규모 API 문서를 체계적으로 관리하기 위한 잘 설계된 구조를 가지고 있습니다:

1. **확장성**: 자동 생성과 수동 편집의 조화
2. **유지보수성**: 콘텐츠와 네비게이션의 분리
3. **일관성**: 표준화된 YAML 구조
4. **사용자 경험**: 계층적 네비게이션과 풍부한 메타데이터
5. **완전성**: 모든 API의 완전한 문서화
6. **실용성**: 풍부한 튜토리얼과 예제

이러한 구조는 로블록스의 방대한 API를 체계적으로 문서화하고, 개발자들이 쉽게 찾고 이해할 수 있도록 돕습니다.

