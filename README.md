# Minecraft Plugin Engineering Skills

A practical, testable engineering skill system for building Minecraft server plugins, with Paper/Java as the primary runtime.

## Scope

This repository owns **behavior and software engineering**: product discovery, feature specifications, architecture, Java/Paper implementation, persistence, integrations, testing, performance, security, compatibility, deployment, and maintenance.

It covers complete gameplay systems including:

- Cosmetics and fashion systems: unlocks, equip slots, appearance state, permissions, persistence, menus, and integrations.
- Weapon systems: item identity, stats, abilities, cooldowns, combat events, progression, balancing, and persistence.
- Boss systems: encounter state machines, phases, telegraphs, targeting, threat, skill execution, rewards, and recovery.
- Mob systems: spawning, AI, navigation, abilities, loot, difficulty scaling, and lifecycle management.

**Visual assets are not authored here.** Models, textures, rigs, animation clips, and art direction belong to [Minecraft Game Asset Skills](https://github.com/wwh1202/minecraft-game-asset-skills). This repository defines the runtime contracts and integration tests for consuming those assets.

## Engineering principles

1. Start from player and operator needs; define observable acceptance criteria.
2. Verify the target Minecraft, Paper, Java, and dependency versions before implementation.
3. Prefer supported APIs; isolate version-specific or NMS code behind adapters.
4. Design persistence, migrations, failure recovery, and permissions explicitly.
5. Test pure logic first, then integration behavior, then a real server runtime.
6. Measure performance under realistic entity/player loads.
7. Treat third-party plugins, configs, and downloaded assets as untrusted inputs.
8. Keep evidence: commands, test output, server logs, compatibility matrix, and reproducible steps.

## Skill map

- Product: opportunity research, brainstorming, feature planning, requirements.
- Architecture: domain boundaries, event flows, persistence, configuration, integrations.
- Implementation: Paper API, Java, Gradle, commands, listeners, schedulers, data models.
- Gameplay systems: cosmetics, weapons, bosses, mobs, loot, progression, UI.
- Quality: TDD, debugging, QA, performance, security, compatibility.
- Delivery: packaging, release notes, migration, observability, maintenance.

## Status

The repository split has been created. Existing skills from the former combined repository are being migrated and reviewed in stages; the presence of a topic in this README does not mean every skill is already complete.

## Validation

Run the repository validation workflow before proposing a release. Every skill should include trigger conditions, prerequisites, a deterministic workflow, outputs, failure handling, and validation criteria.

## Related project

- [Minecraft Game Asset Skills](https://github.com/wwh1202/minecraft-game-asset-skills)
- Previous combined repository (kept as historical source during migration): https://github.com/wwh1202/minecraft-agent-skills
