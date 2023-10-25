1. Opprettet et repository som jeg kalte softwareengineering som jeg satt til public.
2. Installerte Python application workflow.
3. Lastet opp alle prosjektfilene fra oblig 2
4. Build installerer miljø og kjører alle tester ved hver commit.

Utfordringer underveis
Jeg slet i starten med å få installert miljøet fra requirements.txt Det viste seg at
jeg først måtte klone repoet til en lokal mappe før jeg la inn prosjektfilene. Miljøet
taklet ikke at jeg hadde plassert filene i en annen mappe. Da jeg fant ut dette gikk 
oppsettet som forventet.

Jeg fikk problemer med at github ikke ville kjøre testene med en gang. Feilmeldingen gikk
på at den ikke fant modulene. Løsningen på dette var å legge inn en __init__.py -fil 
i mappene. Etter dette kjører alle testene hver gang jeg kjører en commit.
