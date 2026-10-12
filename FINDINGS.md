# Project Findings

## Remaining work

- Rotate and remove the committed API key.
- Fix the accessibility tests: `expect.soft(...)` currently has no matcher.
- Ensure the BDD chat test runs once per selected browser.
- Improve accessibility rules for SVGs, `aria-hidden`, and non-text content.
- Make the BDD answer locator more precise.
- Dispose API request contexts and validate response content.
- Synchronize the virtual environment with the pinned dependencies.
- Fix the nine Ruff errors and format the five affected Python files.
- Rename `pageAction` to `page_action`.
- Add a README, project/pytest configuration, and CI workflow.

## Resolved

- Dependencies are pinned.
- A `.gitignore` file exists.
- Browser handling uses pytest-playwright's standard fixtures and options.
- Browser selection is restricted to Chromium and Firefox.
- The API key header uses `x-api-key`.
- The repository has been initialized and committed.
