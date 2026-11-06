---
name: minecraft-weapon-system-engineering
description: Use when implementing custom Minecraft weapons, weapon attributes, active abilities, cooldowns, upgrades, combat effects, or weapon progression.
---

# Minecraft Weapon System Engineering

## Workflow

1. Define weapon archetypes, rarity, identity, acquisition, upgrade paths, and intended combat role.
2. Specify damage formula, attack cadence, range, resource costs, cooldowns, critical rules, status effects, and PvE/PvP policy.
3. Use stable internal weapon IDs; validate server-side identity and state rather than trusting display name or lore.
4. Separate weapon definitions/configuration from runtime instances and player progression.
5. Implement combat through verified Paper events/APIs; isolate version-specific behavior.
6. Define ability activation, target validation, cancellation, cooldown ownership, scheduler cleanup, and logout/death behavior.
7. Add persistence for upgrades and unique instance data, including migration and anti-duplication safeguards.
8. Test edge cases: off-hand, inventory movement, death drops, item rename, anvil, enchantments, PvP, lag, reconnect, and plugin reload.
9. Benchmark expensive area effects and entity scans; cap targets and avoid unbounded per-tick work.
10. Document balance assumptions and provide reproducible combat test scenarios.

## Acceptance criteria

- Forged or modified items cannot gain privileged weapon behavior.
- Cooldowns and resource costs cannot be bypassed through event ordering or reconnects.
- Damage and status effects follow documented PvE/PvP rules.
- Weapon state remains consistent through inventory movement, death, and restart.
