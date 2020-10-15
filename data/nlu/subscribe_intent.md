## intent:how_to_subscribe
- comment fait-on pour s'inscrire ?
- j'aimerais recevoir la newsletter
- j'aimerais être tenu au courant
- j'aimerais recevoir les dernières infos
- dernières news
- m'inscrire  
- je souhaiterais m'inscrire
- j'aimerais m'inscrire

## lookup:user_name
data/nlu/lookup_tables/prenoms.txt

## intent:inform_name
- [Bertrand](user_name)
- je m'appelle [Damien](user_name)
- je suis [Clémence](user_name)
- mon nom est [Jean](user_name)
- je suis [Georges](user_name)
- C'est [Nicolas](user_name)
- on m'appelle [Arthur]
- [Alain](user_name)
- [Mathieu](user_name)
- [Léo](user_name)
- [Léa](user_name)
- [Thierry](user_name)
- [Mélanie](user_name)
- [Pierre](user_name)
- [Lily](user_name)
- [Raymond](user_name)
- [Sylvie](user_name)
- [Florence](user_name)
- [Alxandre](user_name)
- [Claire](user_name)
- [bertrand](user_name)
- [Tom](user_name)
- [prénom:](name_prompt) [Jean-Michel](user_name)
- [prénom:](name_prompt) [Louis](user_name)
- [prénom:](name_prompt) [Edouard](user_name)
- [prénom:](name_prompt) [Aline](user_name)
- [prénom:](name_prompt) [Martine](user_name)
- [nom:](name_prompt) [Magalie](user_name)
- [prenom:](name_prompt) [Frédéric](user_name)
- [prenom:](name_prompt) [Raphaël](user_name)
- [nom:](name_prompt) [Sylvie](user_name)

## intent:inform_email
- [email@example.com](user_email)
- [jean-michel@gmail.com](user_email)
- [contact@enigmastrasbourg.com](user_email)
- [e-mail:](email_prompt) [machin@free.fr](user_email)
- [email:](email_prompt) [martine@outlook.fr](user_email)
- [mail:](email_prompt) [jeanine.lalilo@hotmail.com](user_email)
- [e-mail:](email_prompt) [michelleetJacky@hotmail.fr](user_email)
- [email:](email_prompt) [contact@yolo.fr](user_email)
- [mail:](email_prompt) [contact@yahoo.com](user_email)

## regex:user_email
- [^\n]@[^\n]

## synonym:prénom
- prenom
- nom

## synonym:email
- e-mail
- mail
