###{{ title }}

Leden van de Tweede Kamer der Staten-Generaal,

De stemming van {{ date }} heeft tot de volgende uitslag geleid:

{% for name, counted_votes in results.items() %}
---

{{ name }}

Voor: {{ counted_votes[1] }}  
Tegen: {{ counted_votes[-1] }}  
Onthouden: {{ counted_votes[0] }}  

{% if counted_votes[1] > counted_votes[-1] %}
Dit amendement is **aangenomen**.
{% else %}
Dit amendement is **verworpen**.
{% endif %}

{% endfor %}

---

*De opkomst was {{ opkomst_percentage }}%. Er waren {{ invalid_votes }} ongeldige stemmen.*
