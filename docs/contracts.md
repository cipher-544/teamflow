\# TeamFlow Contracts (DRAFT, pending team approval)



\## Tool response format

Success: { "ok": true, "data": { ... } }

Failure: { "ok": false, "error": { "type": "timeout", "message": "..." } }



\## Tools

\- get\_order(order\_id)

\- get\_shipment\_status(order\_id)

\- check\_return\_policy(item\_category, days\_since\_delivery, reason)

\- check\_inventory(sku)

\- get\_payment\_record(order\_id)



\## Allowed final resolutions

\- full\_refund

\- partial\_refund

\- replacement

\- reship

\- reject\_request

\- escalate\_to\_human



