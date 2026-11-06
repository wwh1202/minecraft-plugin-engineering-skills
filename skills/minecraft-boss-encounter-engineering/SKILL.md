---
name: minecraft-boss-encounter-engineering
description: Use when implementing Minecraft boss encounters, multi-phase boss AI, telegraphed abilities, arena state, threat, rewards, and recovery.
---

# Minecraft Boss Encounter Engineering

## Workflow

1. Define encounter fantasy, player count, difficulty, duration target, arena boundaries, and fail/success conditions.
2. Model the encounter as an explicit state machine: dormant, intro, active phase(s), transition, defeated, failed, cleanup.
3. Define phase thresholds, ability selection rules, cooldowns, telegraphs, target selection, movement, immunity windows, and interrupt rules.
4. Separate boss definition/configuration from encounter runtime state.
5. Give every encounter a unique ID and explicit ownership of spawned entities, tasks, temporary blocks, effects, and listeners.
6. Define persistence/recovery: server restart, chunk unload, boss despawn, arena unload, and plugin disable.
7. Implement rewards with idempotency keys so duplicate death events cannot pay twice.
8. Test solo and party fights, simultaneous encounters, player disconnects, chunk boundaries, death, reset, and plugin reload.
9. Profile entity AI, pathfinding, particle volume, target scans, and scheduler tasks under realistic player counts.
10. Verify visual telegraph IDs and animation triggers against the asset contract; gameplay must remain understandable if an optional animation fails.

## Acceptance criteria

- Encounter transitions are deterministic and cannot become stuck.
- Only encounter-owned resources are cleaned up.
- Rewards are granted once and only once.
- Bosses cannot escape defined bounds or target invalid entities.
- Failure and restart paths leave no orphan entities or repeating tasks.
