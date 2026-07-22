# Portfolio Accessibility Notes

This static portfolio was designed to be straightforward to navigate with a keyboard and common browser accessibility settings.

## Implemented

- Semantic header, navigation, main, section, article, and footer landmarks
- Skip link to bypass repeated navigation
- Visible keyboard focus styles
- Descriptive link text instead of repeated “click here” labels
- High-contrast text and controls
- Responsive layout that reflows at narrow widths
- No auto-playing media or JavaScript dependency
- Meaningful alternative text for project graphics
- A `prefers-reduced-motion` rule that disables smooth scrolling
- A forced-colors fallback for key borders and controls

## Known limitations

- The site has not been formally audited against every WCAG success criterion.
- It has not been tested with every screen reader, browser, language, zoom setting, or assistive device.
- PDF accessibility depends partly on the document structure and the viewer used to open it.
- Project graphics are summaries; the linked CSV and text files provide more detailed information.

Accessibility problems should be documented with the page, browser, device, steps, expected behavior, actual behavior, and user impact.
