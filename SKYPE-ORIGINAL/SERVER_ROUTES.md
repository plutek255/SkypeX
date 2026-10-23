# Skype Server Routes Extracted from LibWrap.dll

## Authentication & Login (Microsoft Account)
- `https://login.live.com/oauth20_token.srf`
- `https://login.live.com/rst2.srf`
- `https://login.live-int.com/oauth20_token.srf`
- `https://login.live-int.com/rst2.srf`
- `service::login.skype.com::MBI_SSL`
- `service::login.skype.net::MBI_SSL`
- `service::ssl.live.com::MBI_SSL`

## Skype API Endpoints
- `https://api.skype.com/`
- `https://qaapi.skype.net/`
- `https://vm.skype.com/api3`
- `https://vm.skype.com/api/jsonrpc`
- `https://vm.skype.com/api`
- `https://img.vm.skype.com`
- `https://api.skype.com/users/{0}/profile/avatar`
- `https://pipe.skype.com/Client/2.0/`

## Messenger Gateway
- `s.gateway.messenger.live.com`
- `beta-s.gateway.messenger.live.com`

## DNS Servers
- `dsn[0-15].d.skype.net`

## GRS (Global Routing Service)
- `https://grsrequest.trafficmanager.net/v1/query`
- `https://grsregister.trafficmanager.net/v1/register`

## Other Services
- `https://contacts.msn.com/`
- `https://contacts.msn-int.com/`
- `https://mail.services.live.com/Sapi`
- `https://mail.services.live-int.com/Sapi`
- `https://m.hotmail.com/Microsoft-Server-ActiveSync`
- `https://int.activesync.live-int.com/Microsoft-Server-ActiveSync`
- `rendezservice.skype.com`
- `rtlc.live.com`
- `rtlc-beta.live.com`
- `edge.vm.skype.com`
- `https://qbi-frontend.qik.com`
- `http://preqavm.int.skype.net`

## SOAP/Web Service Endpoints
- `http://www.msn.com/webservices/AddressBook/BlockContact`
- `http://www.msn.com/webservices/AddressBook/AddMessengerAddress`
- `http://www.msn.com/webservices/AddressBook/FindMembershipByRole`
- `http://www.msn.com/webservices/AddressBook/CreateContact`
- `http://www.msn.com/webservices/AddressBook/DeleteMember`

## Configuration & Policy
- `https://{0}.config.skype.com/config/v1/Skype/{1}/Modern`
  - Where {0} is random "a" or "b" for load balancing
  - Where {1} is the app version

## External Links
- `http://www.skype.com/go/help.chathelp`
- `http://www.skype.com/go/support`
- `https://support.skype.com/faq/FA10946`
- `http://www.microsoft.com/`
