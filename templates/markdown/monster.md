---
tags:
  - auto-generated
---
# {name}
_{sta_txt}_

| AC | HP | Speed |
|:---:|:---:|:---:|
| {armor_class} | {hit_points} | {speed} |

| STR | DEX | CON | INT | WIS | CHA |
|:---:|:---:|:---:|:---:|:---:|:---:|
| {ability_scores.str} | {ability_scores.dex} | {ability_scores.con} | {ability_scores.int} | {ability_scores.wis} | {ability_scores.cha} |

---
{this|temp:proficiencies}

---
{traits|optline|temp:action|delimiter:\n\n|suffix:\n}
{actions|optline|temp:action|delimiter:\n\n|prefix:## Actions\n|suffix:\n}
{reactions|optline|temp:action|delimiter:\n\n|prefix:---\n## Reactions\n|suffix:\n}
{legendaries|optline|temp:action|delimiter:\n\n|prefix:---\n## Legendary Actions\n|suffix:\n}
{mythics|optline|temp:action|delimiter:\n\n|prefix:---\n## Mythic Actions\n|suffix:\n}
{lairs|optline|temp:action|delimiter:\n\n|prefix:---\n## Lairs\n|suffix:\n}

