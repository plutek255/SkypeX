![SkypeX](assets/logo-icon.png)
# SkypeX

The Skype Extended Support Project

A project built with passion and nostalgia for Skype on Windows 8.1.

> SkypeX is a project that attempts to patch or install a modern-backended version of Skype, a version based on the Windows 8.1 app, that **in no way** changes Skype's appearance, but connects it to a modern chat backend, starting with Matrix.

**Objective**: Create a local bridge that translates Skype protocol calls to modern protocols, starting with Matrix, allowing the Skype Windows Store app to communicate with modern chat protocols.

**Completed items will show up here as they are finished.**

---

### Phase 1: Collecting Information and Setting Up Infrastructure
- Extract main Skype files
- Analyze login flow and authentication
- Document all [server endpoints](SKYPE-ORIGINAL/SERVER_ROUTES.md)
- Technical jargon:
    - Create skeletal [Python bridge](proto/bridge.py) for prototype
    - Attempt [DNS hijacking](proto/setup_dns_hijack.sh)
    - [Extract main DLL](analysis/) for server routes and other info


---

## Minimum Viable Product (MVP)
  - Skype client connects to bridge
  - Authentication works
  - Text messages send/receive
  - Basic contact list sync
  - User moderation
        1. Users can be reported by other users or repo moderators for [certain reasons](./ToS.md) to be reviewed by repository owner or contributors
        2. Users have [repercussions](./ToS.md) that fit the infraction
  - Presence status updates

### Full Feature Set
  - All MVP features
  - File transfers
  - Group chats
  - Encryption support
  - Search and history
  - Voice/video calls
    
### Stretch Goals
  - Multi-account support
  - Message encryption
  - Voice/video calls
  - Screen sharing
  - Bots and integration
