# Plugin Engineering Architecture

## Responsibility boundary

This project owns executable game behavior and server-side integration. It does not own visual design or model production.

| Feature | Plugin engineering owns | Asset creation owns |
|---|---|---|
| Fashion/cosmetics | equip state, slots, unlocks, permissions, persistence, menus, packet/runtime integration | outfit concept, silhouette, model, texture, UV, animation |
| Weapons | item identity, stats, abilities, cooldowns, combat logic, balancing, drops | weapon shape, texture, emissive details, animation/visual effects |
| Bosses | encounter state, phases, AI, targeting, damage rules, rewards, reset | creature concept, proportions, model, rig, animation, visual telegraphs |
| Mobs | spawn rules, AI, navigation, skills, loot, difficulty | creature design, model, texture, rig, animation |

## Required feature lifecycle

1. Problem statement and player/operator use cases.
2. Functional and non-functional requirements.
3. Compatibility and dependency research.
4. Domain model, events, state transitions, persistence, configuration.
5. Test plan and acceptance criteria before implementation.
6. Implementation in small vertical slices.
7. Unit tests, integration tests, and real-server verification.
8. Performance, security, exploit, and recovery review.
9. Packaging, migration notes, release, and maintenance plan.

## Asset integration contract

Every asset integration must declare:
- asset identifier and semantic version;
- target platform/runtime and supported Minecraft version range;
- resource-pack namespace and file paths;
- model/texture/animation format and required plugin or library;
- runtime trigger names and parameter schema;
- fallback behavior when the pack is absent or outdated;
- validation evidence from a clean test server.

Paper gameplay logic must not assume that Paper itself is a general-purpose skeletal animation engine. Animation playback may require a resource-pack convention, a compatible plugin/library, client-side support, or a separately documented runtime.
