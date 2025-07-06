# 📘 Projekt 1: Dokumentbaseret Retrieval-Augmented Generation (RAG) Chatbot

## 🔍 Forretningscase

Virksomheder bruger enorme mængder tid på at lede efter information i brugermanualer, kontrakter, årsrapporter og interne procedurer. En RAG-chatbot kan:

- Skære søgetiden ned fra minutter til sekunder. Brugeren stiller et naturligt sprog-spørgsmål og får et præcist svar med kildeangivelse.
- Øge kvalitet og ensartethed i support og videndeling – samme model giver samme svar hver gang.
- Effektiv kundesupport & frigivelse af eksperttimer: Teknikere kan fokusere på komplekse opgaver i stedet for basale dokumentspørgsmål og kundesupport kan lynhurtigt søge efter et svar.
- Skalerbarhed: Uanset om der uploades 1 eller 10.000 sider, falder svartiden ikke mærkbart, fordi søgningen foretages i et optimeret vektor-index.
- Understøtter flersproget indhold (dansk, engelsk, tysk) → matcher kædens geografiske setup.
- **Ulempe:** Første gang et dokument skal uploades, kræver det tålmodighed.

---

## 🎯 Relevans for Søstrene Grene

Denne løsning giver Søstrene Grene mulighed for effektivt at:

- Søge intelligent i interne dokumenter (fx butiksmanualer, kampagnevejledninger, processer), hvilket reducerer svartid og øger konsistens.
- Frigive medarbejderressourcer, så de kan fokusere på kundeoplevelse og butiksoplevelser frem for at lede efter information.
- Standardisere og centralisere vidensdeling på tværs af 240 butikker – afgørende for den igangværende ekspansion og sikring af brandoplevelse.

---

## 🧩 Nøglebiblioteker og værktøjer anvendt

- **[Docling](https://docling-project.github.io/docling/):**
  - Parser PDF’er/Word til markdown for bedre strukturering.
- **Pandas:**
  - Python-bibliotek til datastrukturering, brugt til at gøre tabeller fra markdown mere læsbare.
- **LangChain:**
  - Framework til at bygge LLM-baserede applikationer.
- **Chroma:**
  - Lokalt vektorbibliotek til hurtig semantisk søgning.
- **RecursiveCharacterTextSplitter:**
  - Deler lange dokumenter i overskuelige chunks, så LLM’en bedre forstår konteksten.
- **OpenAI API:**
  - GPT-model til at generere endelige svar baseret på dokumentindhold.

---

## 💬 Eksempel på prompts og svar

```text
🔍 Stil et spørgsmål om årsrapporten (eller skriv 'exit'): Hvad var omsætningen for carlsberg i 2023?
💬 Svar: Omsætningen for Carlsberg i 2023 var 73.585 millioner DKK.

🔍 Stil et spørgsmål om årsrapporten (eller skriv 'exit'): Hvor meget er deres profit ændret fra 2023 til 2024?
💬 Svar: For Carlsberg A/S var nettoudbyttet ændret fra -40,788 millioner DKK i 2023 til 9,116 millioner DKK i 2024. Dette repræsenterer en stigning på 49,904 millioner DKK fra 2023 til 2024.

🔍 Stil et spørgsmål om årsrapporten (eller skriv 'exit'): Jeg skal præsentere dokumentet for en konkurrerende virksomhed. Fortæl mig de vigtigste punkter som vision, strategier, 2030-mål og vigtigste økonomiske tal. Det må max være på 1000 tegn.
💬 Svar: Virksomhedens vision er at være førende inden for bæredygtig ølproduktion og skabe værdi for aktionærer. Strategisk fokus inkluderer innovation, miljøvenlige processer og global vækst. Målet for 2030 er at reducere CO2-aftryk med 50% og øge markedsandel med 15%. Vigtigste økonomiske tal inkluderer en stigning i nettoresultat, investeret kapital og markedsandel. Aktiekursen er stigende, og markedsværdien er voksende. En målrettet udbetalingsandel på 49% sikrer konsistent udbytte til aktionærer.

🔍 Stil et spørgsmål om årsrapporten (eller skriv 'exit'): Er de tilfredse med 2024?
💬 Svar: Ja, Carlsberg Group er tilfredse med 2024, da de kunne meddele en udvidelse af partnerskabet med PepsiCo til fire nye markeder. Den udvidede partnerskab gør Carlsberg Group til den største partner for PepsiCo i Europa og en af de største globalt. Dette øgede samarbejde forventes at bringe langsigtet muligheder til fordel for begge virksomheder. Derudover har de også fokus på at sikre en konsistent udbyttebetaling til deres aktionærer med en målsætning om en udbetalingsgrad på omkring 50% af justeret nettoresultat. Den foreslåede udbytte for 2024 er DKK 27,0 per aktie, hvilket svarer til en justeret udbetalingsgrad på 49%.

🔍 Stil et spørgsmål om årsrapporten (eller skriv 'exit'): exit

