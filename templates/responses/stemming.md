Er zijn fouten opgetreden bij het uitbrengen van uw stem. Let u even op dat er geen hoofdletter 'o' wordt gebruikt in plaats van een nul.

{% if not_voted_on %}
* U hebt niet gestemd op: _{{ not_voted_on|join(', ') }}_.
{% endif %}
{% if not_in_voting %}
* Niet in de stemming waren: _{{ not_in_voting|sort|join(', ') }}_.
{% endif %}
{% if incorrect_keyword %}
* Ik begreep uw stem niet helemaal op: _{{ incorrect_keyword|sort|join(', ') }}_
{% endif %}
