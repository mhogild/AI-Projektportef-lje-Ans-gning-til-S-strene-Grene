# 🗞️ Projekt 2 – Personlig AI-Nyhedsassistent

## 🔍 Forretningscase

Automatiseret nyhedsindsamling og daglig personaliseret opsummering.

Der lå ikke den store udfordring i at indsamle nyheder/mails/beskeder/updates, hvilket også anses at være let tilkendeligt via copilot til Microsoft produkter. Udfordringen jeg havde givet mig selv var også at bruge ML til at forbedre relevansen af de nyheder jeg får hver dag.

Dette projekt automatiserer daglig nyhedsopsamling og filtrering med henblik på at levere 3 personligt relevante AI-nyheder til brugeren hver morgen. Målet er at den desuden via ML skal blive bedre til at vælge de mest relevante nyheder via brugerfeedback.

På den måde undgår brugeren at skulle undersøge adskillige sider og steder, men kan få det hele ét sted fra.

---

## 🎯 Relevans for Søstrene Grene

Denne AI-drevne løsning leverer:

- **Personlige AI-nyhedsopsamlinger**, fx om markedstendenser, bæredygtighed, branchetrends og leverandørforandringer – vigtig viden for HQ og butikschefer.
- **Effektivisering af vidensdeling**, så HQ nemt kan dele de tre vigtigste nyheder, uden at medarbejdere skal bruge tid på at finde dem.

## Zapier projekt (Zap a):
Følgende er en kort forklaring af automationen
![Zapier Flow – Zap A]("./Projekt 2 – Personlig AI-Nyhedsassistent/zap_a_low.png")

| Trin | Værktøj                 | Funktion                                                         |
| ---- | ----------------------- | ---------------------------------------------------------------- |
| 1    | **RSS by Zapier**       | Overvåger flere RSS-feeds for nye AI-relaterede artikler.        |
| 2    | **Formatter by Zapier** | Formaterer og gemmer dagens dato.                                |
| 3    | **Google Sheets**       | Lagrer nyhederne (titel, beskrivelse, link, dato) i et regneark. |

