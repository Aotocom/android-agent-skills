# Android Agent Skills

A discovery catalog for the canonical Android skills in this repository.

## Install Surfaces
- Codex / open standard: root `skills/` plus this `AGENTS.md` catalog.
- Claude Code: generated `.claude/agents/` files.
- Cursor: generated `.cursor/rules/` files.

## Foundations
- `android-architecture-clean`: Apply clean architecture boundaries, use cases, repositories, and lifecycle-aware presentation models in Android projects. Path: `skills/android-architecture-clean`
- `android-coroutines-flow`: Use coroutines, Flow, structured concurrency, dispatchers, and cancellation-safe Android async pipelines. Path: `skills/android-coroutines-flow`
- `android-di-hilt`: Wire Android dependency injection with Hilt, scopes, testing overrides, and module ownership boundaries. Path: `skills/android-di-hilt`
- `android-gradle-build-logic`: Shape Android build logic with Gradle, version catalogs, plugins, convention patterns, and toolchain compatibility. Path: `skills/android-gradle-build-logic`
- `android-kotlin-core`: Use Kotlin idioms safely in Android apps, including nullability, data classes, sealed types, extension functions, and collection pipelines. Path: `skills/android-kotlin-core`
- `android-modularization`: Design Android repositories with feature, core, and build-logic modules that scale without cyclic dependencies. Path: `skills/android-modularization`

## Product Flows
- `android-navigation-deeplinks`: Handle navigation graphs, back stack behavior, app links, intents, and destination ownership for Android apps. Path: `skills/android-navigation-deeplinks`
- `android-permissions-activity-results`: Use modern permission requests, Activity Result APIs, and capability-gated UX in Android flows. Path: `skills/android-permissions-activity-results`
- `android-state-management`: Model screen state, events, reducers, and side effects for Android UIs with predictable lifecycle-aware ownership. Path: `skills/android-state-management`
- `android-ui-states-validation`: Review Android UI flows for empty, loading, error, offline, and edge-case behavior before release. Path: `skills/android-ui-states-validation`

## UI Systems
- `android-compose-accessibility`: Make Compose interfaces accessible with semantics, announcements, contrast, focus order, and adaptive touch targets. Path: `skills/android-compose-accessibility`
- `android-compose-foundations`: Build Android UI with Jetpack Compose foundations, layouts, modifiers, theming, and stable component structure. Path: `skills/android-compose-foundations`
- `android-compose-performance`: Profile and improve Compose recomposition, layout, scrolling, startup, and rendering performance in Android apps. Path: `skills/android-compose-performance`
- `android-compose-state-effects`: Manage Compose state, remember APIs, side effects, snapshots, and lifecycle-aware collection without leaks or loops. Path: `skills/android-compose-state-effects`
- `android-compose-xml-interoperability`: Bridge Compose and the View system safely during incremental migrations, interoperability screens, and shared theming. Path: `skills/android-compose-xml-interoperability`
- `android-material3-design-system`: Apply Material 3 tokens, color, type, spacing, adaptive components, and theme ownership in Android apps. Path: `skills/android-material3-design-system`
- `android-viewsystem-foundations`: Handle XML layouts, ConstraintLayout, Fragments, ViewBinding, DataBinding, and classic Android UI lifecycle patterns. Path: `skills/android-viewsystem-foundations`

## Data And Platform
- `android-local-persistence-datastore`: Persist lightweight user and app preferences with DataStore, schema-safe models, and migration-aware defaults. Path: `skills/android-local-persistence-datastore`
- `android-media-files-sharing`: Use modern Android file, media, picker, FileProvider, and share-sheet APIs with minimal permissions. Path: `skills/android-media-files-sharing`
- `android-networking-retrofit-okhttp`: Build Android networking stacks with Retrofit, OkHttp, interceptors, API contracts, and resilient error handling. Path: `skills/android-networking-retrofit-okhttp`
- `android-room-database`: Model Room entities, DAOs, transactions, migrations, schema exports, and test-safe local persistence. Path: `skills/android-room-database`
- `android-serialization-offline-sync`: Coordinate serialization, caching, conflict handling, and offline-first sync flows in Android apps. Path: `skills/android-serialization-offline-sync`
- `android-workmanager-notifications`: Schedule reliable background work, reminders, and notification delivery with WorkManager and Android execution limits. Path: `skills/android-workmanager-notifications`

## Quality And Delivery
- `android-ci-cd-release-playstore`: Automate Android CI, versioning, signing boundaries, release channels, and Play-ready delivery workflows. Path: `skills/android-ci-cd-release-playstore`
- `android-performance-observability`: Measure startup, rendering, memory, jank, vitals, logs, and crash signals for Android apps with actionable traces. Path: `skills/android-performance-observability`
- `android-security-best-practices`: Apply Android app security guidance around secrets, storage, network trust, exported components, and least privilege. Path: `skills/android-security-best-practices`
- `android-testing-ui`: Validate Android UI behavior with Compose UI tests, Espresso-style checks, accessibility assertions, and state coverage. Path: `skills/android-testing-ui`
- `android-testing-unit`: Write fast, focused Android unit tests for reducers, use cases, repositories, and lifecycle-safe state holders. Path: `skills/android-testing-unit`

## Legacy Rescue
- `android-modernization-upgrade`: Bring very old Android projects to a current supported baseline with staged upgrades, deprecated API replacement, 16 KB alignment checks, and explicit handoff to specialized skills. Path: `skills/android-modernization-upgrade`
