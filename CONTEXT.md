# Property Manager

A backend API for real-estate agents to manage their own private inventory of properties, listed on a map with combinable filters. Each agent has a private inventory; nothing is shared between agents.

## Language

**Imóvel** (Property):
A real-estate listing an agent manages — for sale or rent — with location, price, physical attributes, and photos.
_Avoid_: Property (in code identifiers, prefer `imovel`), listing, unit

**Corretor** (Agent):
An authenticated user of the app, identified by their Supabase Auth UUID (the JWT `sub`). Owns a private inventory of imóveis; sees and manages only their own. We store no corretor profile of our own — identity and account data live in Supabase Auth.
_Avoid_: User, broker, agency, imobiliária

**Angariação** (Listing sourcing):
How the agent acquired the listing: **Própria** (sourced by the agent themselves) or **Terceiros** (sourced via a third party, which carries a commission %).
_Avoid_: Source, acquisition

**Ativo / Inativo** (Listing status):
A listing's on-market state. **Ativo** is on-market; **Inativo** is off-market but still in inventory (reversible). Deleting an Ativo imóvel makes it Inativo; deleting an already-Inativo imóvel removes it permanently.
_Avoid_: Active/inactive (in identifiers, prefer `ativo`), archived, deleted
