## greet and 2 riddles no1
* greet: hello
  - utter_greet_and_propose_riddle
* affirm: oui
  - form_riddle
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* affirm: ok
  - form_riddle
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* deny: no
  - utter_question_on_ENIGMA_Stras
* deny: non
  - utter_thanks
  - utter_goodbye
* goodbye: ciao
  - action_listen

## greet and 2 riddles no2
* greet: hello
  - utter_greet
* ask_for_riddle: t'aurais une bonne énigme ?
  - form_riddle
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* affirm: ok
  - form_riddle
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* deny: no
  - utter_question_on_ENIGMA_Stras
* deny: non
  - utter_thanks
  - utter_goodbye
* goodbye: ciao
  - action_listen

## greet and 2 riddles no3
* inform_kind_of_riddle: tu connais une charade ?
  - form_riddle
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* affirm: ok
  - form_riddle
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* deny: no
  - utter_question_on_ENIGMA_Stras
* deny: non
  - utter_thanks
  - utter_goodbye
* goodbye: ciao
  - action_listen

## greet and 2 faq no1
* greet: bonjour
  - utter_greet
* faq: combien ça coûte ?
  - action_set_faq_slot
  - respond_faq
  - utter_one_more_question
* faq: Combien de temps est-ce que ça dure ?
  - action_set_faq_slot
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_propose_riddle
* deny: non
  - utter_before_end
  - utter_goodbye
* goodbye: a bientôt
  - action_listen

## greet and 2 faq no2
* greet: bonjour
  - utter_greet
* affirm: oui
  - utter_question
* faq: combien ça coûte ?
  - action_set_faq_slot
  - respond_faq
  - utter_one_more_question
* faq: Combien de temps est-ce que ça dure ?
  - action_set_faq_slot
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_propose_riddle
* deny: non
  - utter_before_end
  - utter_goodbye
* goodbye: a bientôt
  - action_listen

## greet and 2 faq no3
* faq: combien ça coûte ?
  - action_set_faq_slot
  - respond_faq
  - utter_one_more_question
* faq: Combien de temps est-ce que ça dure ?
  - action_set_faq_slot
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_propose_riddle
* deny: non
  - utter_before_end
  - utter_goodbye
* goodbye: a bientôt
  - action_listen

## greet, 1 riddle, 1 faq
* greet: coucou
  - utter_greet_and_propose_riddle
* affirm: wé
  - form_riddle
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* deny: non
  - utter_question_on_ENIGMA_Stras
* affirm: oui
  - utter_question
* faq: faut-il prévoir à manger ?
  - action_set_faq_slot
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: a+
  - action_listen

## greet, 1 faq, 1 riddle
* greet: coucou
  - utter_greet
* affirm: oui
  - utter_question
* faq: si la météo est mauvaise ?
  - action_set_faq_slot
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_propose_riddle
* affirm: wé
  - form_riddle
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* deny: non
  - utter_thanks
  - utter_goodbye
* goodbye: salut
  - action_listen
