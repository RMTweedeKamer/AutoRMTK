###{{ title }}

Leden van de Tweede Kamer der Staten-Generaal,

De stemming van {{ date }} heeft tot de volgende uitslag geleid:

{% for name, counted_votes in results.items() %}
---

{% if submissions[name] %}
[{{ submissions[name].title }}]({{ submissions[name].url }})
{% else %}
{{ name }}
{% endif %}

Voor: {{ counted_votes[1] }}  
Tegen: {{ counted_votes[-1] }}  
Onthouden: {{ counted_votes[0] }}  

{% if submissions[name] %}
{% if submissions[name].link_flair_text == 'MOTIE' %}Deze motie{% else %}Dit wetsvoorstel{% endif %} is {% if counted_votes[1] > counted_votes[-1] %}**aangenomen**{% else %}**verworpen**{% endif %}.
{% else %}
Dit amandement is {% if counted_votes[1] > counted_votes[-1] %}**aangenomen**{% else %}**verworpen**{% endif %}.
{% endif %}

{% endfor %}

---

*De opkomst was {{ opkomst_percentage }}%. Er waren {{ invalid_votes }} ongeldige stemmen.*
