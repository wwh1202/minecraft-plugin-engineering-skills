---
name: minecraft-mob-system-engineering
description: Use when implementing custom mobs, spawn systems, mob abilities, AI behavior, loot, difficulty scaling, or lifecycle management for Paper servers.
---

# Minecraft Mob System Engineering

## Workflow

1. Define mob role, biome/world rules, spawn budget, target types, difficulty tier, and intended player counterplay.
2. Specify spawn conditions, caps, despawn policy, persistence, leash/bounds, and chunk lifecycle.
3. Define AI states and transitions: idle, patrol, acquire target, approach, attack, retreat, special ability, recover, dead.
4. Verify navigation and entity API capabilities for the target Paper version and any required library.
5. Use stable mob IDs and server-side metadata; do not infer identity from a visible custom name.
6. Define damage, resistance, status effects, drops, experience, and loot-table ownership.
7. Ensure scheduled tasks and spawned helpers/projectiles are owned and cleaned up.
8. Test spawn caps, chunk unload/reload, world change, target logout, death, server restart, and plugin disable.
9. Measure pathfinding and target scans with many mobs; use bounded scans and configurable budgets.
10. Document admin spawn/test commands, tuning parameters, and asset animation/trigger dependencies.

## Acceptance criteria

- Spawn rules respect per-world and per-chunk budgets.
- Mob identity and drops cannot be spoofed by renaming ordinary entities.
- AI recovers from missing targets and unloaded chunks.
- Cleanup removes only resources owned by the mob instance.
- Performance remains bounded under configured maximum population.
