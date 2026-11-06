---
name: minecraft-cosmetics-fashion-system
description: Use when implementing player fashion, outfits, cosmetic equipment, skins, wardrobe menus, unlocks, or appearance persistence in a Minecraft server plugin.
---

# Minecraft Cosmetics and Fashion System Engineering

## Scope

This skill implements the runtime system. Visual outfit concepts, geometry, textures, and animation are produced in the separate game-asset project.

## Workflow

1. Define cosmetic categories and slot rules (head, body, legs, feet, back, hand, full outfit, or project-specific slots).
2. Specify acquisition sources, ownership, unlock conditions, permissions, tradeability, expiry, and admin grants.
3. Define equip/unequip state transitions, conflict rules, visibility rules, and behavior on death, world change, quit, respawn, and server restart.
4. Choose the display mechanism only after checking the target version and dependency stack: vanilla equipment, resource-pack custom models, ItemsAdder/Oraxen-style integrations, packet libraries, or a documented alternative.
5. Define stable cosmetic IDs independent of display names and model file paths.
6. Persist ownership and equipped state transactionally; plan schema migration and cache invalidation.
7. Add anti-duplication and anti-forgery checks. Never treat lore or client-visible names as authoritative ownership.
8. Test permissions, slot conflicts, reconnects, reloads, missing packs, outdated assets, and concurrent menu actions.
9. Provide admin tooling, audit logs, configuration examples, and rollback behavior.

## Acceptance criteria

- A player cannot equip an unowned or unauthorized cosmetic.
- Equip state survives restart and recovers safely after partial failure.
- Invalid or missing asset references fail gracefully.
- Cosmetic display does not overwrite a player's real equipment or cause item duplication.
- Slot and visibility rules are deterministic and tested.
