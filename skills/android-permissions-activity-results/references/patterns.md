# Android Permissions Activity Results Patterns

## Selection Notes
- Category: `product`
- Best fit when the request matches the trigger language in `SKILL.md` and the implementation focus is `Use modern permission requests, Activity Result APIs, and capability-gated UX in Android flows.`
- Reach for neighboring skills only after this skill has framed the main problem.

## Default Review Sequence
1. Confirm the user-visible journey, target device behavior, and failure states that matter.
2. Identify the owning screens, activities, destinations, and state holders for the flow.
3. Implement the flow with explicit loading, success, empty, and error handling.
4. Validate accessibility, configuration changes, and back-stack behavior in the showcase apps.
5. Escalate data, architecture, or release concerns to the specialized skills called out in the handoff notes.

## Handoff Shortlist
- `android-media-files-sharing`
- `android-testing-ui`
