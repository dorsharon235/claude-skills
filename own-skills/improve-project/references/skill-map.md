# Skill map — need → skill

Curated hints only. The live inventory (`scripts/inventory.py`, phase 2) is the source of truth for what is installed; when they differ, trust the inventory and fix this file. "התקנה" is only for skills that are missing. Every install = scan first (see SKILL.md → Safety).

## Websites, visuals, UI
| Need | Installed skill (use first) | If missing — install |
|---|---|---|
| Overall art direction / "looks AI-made" | `design-taste-frontend` (taste-skill), `impeccable` | `npx skills add nutlope/hallmark -g` |
| Redesign an existing site without breaking it | `redesign-existing-projects` | — |
| Polish, hierarchy, critique | `impeccable`, `emil-design-eng`, `design:design-critique` | — |
| Design system / tokens | `design:design-system`, `impeccable` (document) | `npx skills add arvindrk/extract-design-system` |
| Full UI/UX knowledge base | `ui-ux-pro-max` | — |
| Premium look | `high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui` | — |
| Image comps before coding | `imagegen-frontend-web`, `image-to-code` | — |
| Mobile web feel | `mobile-native` | — |
| Stress-test with worst-case data | `break-ui` | — |
| Motion | `animate`, `review-animations`, `improve-animations`, `find-animation-opportunities`, `animation-performance` | — |
| UX copy / microcopy | `design:ux-copy` | `npx skills add coreyhaines31/marketingskills` |
| Accessibility | `design:accessibility-review` | — |
| Scroll storytelling | `anthropic-skills:scroll-craft` | — |
| React / Next.js best practice | — | `npx skills add vercel-labs/agent-skills` |

## Conversion, marketing, content
| Need | Installed | If missing |
|---|---|---|
| CRO, copy, landing page | `marketing:content-creation`, `marketing:draft-content` | `npx skills add coreyhaines31/marketingskills` |
| SEO | `marketing:seo-audit` | `npx skills add Illyism/seo-skills` |
| Text sounds AI-written | `humanizer:humanizer` | — |
| Brand review | `marketing:brand-review`, `brandkit` | — |

## Video, sound, media
| Need | Installed | If missing |
|---|---|---|
| Make / edit video from code | `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use` | `npx skills add remotion-dev/skills` |
| Launch video for the project | `brag`, `brag-slim` | — |
| Edit real footage | `ffmpeg-skill`, `anthropic-skills:edit-reel`, `anthropic-skills:video-studio` | — |
| Video looks amateur / promo film | `motionmaxxing` | — |
| Sound effects | `sfxmint:sfxmint` (free CC0 library), `genny` (generate) | — |
| UI sounds on a site | — | `npx skills add dannyjpwilliams/ui-sound-design-skill` |

## Games (Roblox)
| Need | Installed | If missing |
|---|---|---|
| Any Roblox task (entry point, routes to the rest) | `roblox` (41 roblox-* skills installed: roblox-brain + roblox-suite) | — |
| Game design, retention, monetization | `roblox-game-design`, `roblox-player-psychology`, `roblox-monetization`, `roblox-analytics` | — |
| Working in Studio | `roblox-studio-mcp`, `roblox-building`, `roblox-gui`, `roblox-npc-ai` | — |
| Code, data, speed | `roblox-luau-core`, `roblox-datastores`, `roblox-performance`, `roblox-testing` | — |
| Exploits / cheating | `roblox-security` | — |
| Before publishing | `roblox-publish-checklist` | — |
| Game sounds and music | `genny` | — |

## Documents, decks, data
| Need | Installed | If missing |
|---|---|---|
| Word / Excel / PowerPoint / PDF | `anthropic-skills:docx`, `xlsx`, `pptx`, `pdf` | — |
| Charts and dashboards | `dataviz`, `data:create-viz`, `data:build-dashboard` | — |
| Web slides | — | `/plugin marketplace add https://github.com/zarazhangrui/frontend-slides` |

## Engineering quality
| Need | Installed | If missing |
|---|---|---|
| Bugs in the code | `code-review`, `superpowers:systematic-debugging` | — |
| Simplify code | `simplify` | — |
| Deep security audit (whole project, verified findings) | `security-audit` (Cloudflare) | — |
| Risky defaults: debug on, fallback secrets, weak crypto | `insecure-defaults:audit` (Trail of Bits) | — |
| Vulnerable / abandoned packages | `supply-chain-risk-auditor:supply-chain-risk-auditor` (Trail of Bits) | — |
| Automatic code scan | `static-analysis:semgrep`, `static-analysis:codeql` (Trail of Bits) | needs `pip install semgrep` (not installed yet) |
| Review of recent changes only | `security-review` (built in) | — |
| Vibe-coded app holes | — | `npx skills add https://github.com/raroque/vibe-security-skill --skill vibe-security` |

## Research
| Need | Installed | If missing |
|---|---|---|
| Competitors, market, what users say | `anthropic-skills:deep-research`, `product-management:competitive-brief` | `/plugin marketplace add mvanhorn/last30days-skill` |
| User research synthesis | `design:user-research`, `design:research-synthesis` | — |

Full catalogue: installed toolbox (79 skills, with how to run each) + 120 more from GitHub: https://claude.ai/artifact/6StZrCyzpSqfDb7tKLyTUD

Updated 2026-11-08. Whenever a skill is installed or removed on this machine, update this table in the same step (Dor's standing order).
