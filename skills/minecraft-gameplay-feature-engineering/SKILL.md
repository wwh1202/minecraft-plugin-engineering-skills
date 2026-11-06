---
name: minecraft-gameplay-feature-engineering
description: Use when designing or implementing a complete Minecraft Paper gameplay feature such as cosmetics, weapons, bosses, mobs, progression, loot, or player-facing systems.
---

# Minecraft Gameplay Feature Engineering

## Workflow

1. Identify player, administrator, and operator use cases. Separate required behavior from presentation.
2. Record target Minecraft/Paper/Java versions and all required plugin/library dependencies.
3. Define domain entities, state transitions, events, permissions, configuration, persistence, and recovery behavior.
4. Write acceptance criteria and a test matrix before implementation.
5. Implement a thin vertical slice: command or interaction → domain logic → persistence/runtime effect → feedback.
6. Add unit tests for pure logic and integration tests for event handling, persistence, permissions, and reload/restart behavior.
7. Verify on a clean Paper server matching the declared version. Capture startup logs, test commands, and expected player-visible results.
8. Review exploits, duplication, race conditions, scheduler ownership, memory leaks, and performance under load.
9. Document installation, configuration, permissions, migration, rollback, and known limitations.

## Required outputs

- Feature specification and acceptance criteria
- Dependency/version matrix
- Domain and event-flow notes
- Configuration and permission reference
- Test cases and reproducible evidence
- Release and rollback notes

## Guardrails

- Do not invent API methods; verify against the exact target API.
- Do not use synchronous database or network I/O on the server main thread.
- Do not trust client-provided item metadata or interaction state.
- Do not claim a feature is tested unless the test command and result are recorded.
