---
name: diagram-with-brand-kit
description: Make a clear diagram that follows a graphic kit (palette, fonts, shapes, footer): one idea, few nodes, readable labels, honest status, checked as an image before delivery. Use when you need a flow, architecture or timeline diagram for a README, website, slide or social post in a consistent look.
---

# Diagram with a brand kit

Draw one idea clearly, in the visual language the person or team already uses.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The graphic kit: colours (background, main, accent, text, lines), fonts (title, body, small labels), shapes and icon style, footer text. If there is none, ask for a logo, a site or an existing image to take them from, and write the kit down first.
- The message: one sentence saying what the reader should understand, and who the reader is.
- The content: steps, systems, data stores, people, and which parts are real, invented or simulated.
- Where it will be used (README, site, slide, social post) and the size or aspect ratio needed.

## Workflow

1. Write the message as a title. A good title states the idea ("Rules live in SQL, workflows follow them"), not the topic ("Architecture").
2. Choose the form: flow (left to right), architecture (layers or lanes), timeline, or comparison. Use one form per diagram.
3. List the nodes and the connections. Keep about ten nodes at most; if there are more, split into two diagrams or group them.
4. Give every node a kind that looks different: step, data store, human step, external system. Show human approval clearly.
5. Lay it out: main path along one line, supporting data above or below, branches to the side, lanes with short uppercase labels. Put each label where no line crosses it, keep notes to two short lines, and give connections room to breathe.
6. Apply the kit: background, text and line colours, fonts, shapes, thin consistent icons, the same corner radius everywhere, a footer and a small legend.
7. Be honest: label what is invented, simulated or untested, and do not draw connections that do not exist.
8. Render it as an image (SVG converted to PNG by a headless browser at 2x, so that web fonts load) and look at it. Fix overlapping text, lines through labels, crowded areas and anything that is hard to read at the size it will be shown.
9. Deliver the editable source (SVG or code), the PNG, alt text that describes what the diagram shows, and the kit used.

## Rules

- One idea per diagram. If the title needs "and", consider two diagrams.
- Contrast must be readable at the final size; do not rely on colour alone to carry meaning.
- Do not include real names of people, customers or confidential systems unless they are public and cleared for use.
- Keep the same wording in every language version.
- Embedded SVGs lose web fonts when shown as an image; use the PNG for places that load it as an image and keep the SVG as the source.

## Output format

```
Message (title) | Reader | Used in
Nodes: id | kind | label | note
Connections: from -> to | label
Kit: colours, fonts, shapes, footer
Files: source, image, alt text
Honesty labels: what is invented, simulated or untested
```

## Quality checks

- The title alone tells the reader what to understand.
- No text overlaps another text or a line, and nothing is cut off.
- Kinds of node are distinguishable without colour.
- The image was rendered and inspected, not only the code.
