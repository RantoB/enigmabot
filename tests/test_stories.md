## greet and 2 riddles no1
* greet: hello
  - utter_greet
* ask_for_riddle: une énigme
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
  - utter_subscribe
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: ciao
  - utter_goodbye

## greet and 2 riddles no2
* greet: hello
  - utter_greet
* ask_for_riddle: je souhaite faire une énigme
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
  - utter_subscribe
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: ciao
  - utter_goodbye

## greet and 2 riddles no3
* inform_kind_of_riddle: pose moi une charade
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
  - utter_subscribe
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: ciao
  - utter_goodbye

## greet and 2 faq no1
* greet: bonjour
  - utter_greet
* faq: combien ça coûte ?
  - respond_faq
  - utter_one_more_question
* faq: Combien de temps est-ce que ça dure ?
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_propose_riddle
* deny: non
  - utter_subscribe
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: a bientôt
  - utter_goodbye

## direct 2 faq
* faq: combien ça coûte ?
  - respond_faq
  - utter_one_more_question
* faq: Combien de temps est-ce que ça dure ?
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_propose_riddle
* deny: non
  - utter_subscribe
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: a bientôt
  - utter_goodbye

## greet, 1 riddle, 1 faq
* greet: coucou
  - utter_greet
* ask_for_riddle: une énigme
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
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_subscribe
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: a+
  - utter_goodbye

## greet, 1 faq, 1 riddle
* greet: coucou
  - utter_greet
* faq: si la météo est mauvaise ?
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
  - utter_subscribe
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: salut
  - utter_goodbye

## subscribe
*   how_to_subscribe: j'aimerais recevoir la newsletter
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form: slot_was_set
  - form{"name": null}
* deny: non
  - action_reset_subscribe_slots
  - utter_correct_info
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
* deny: non
  - action_reset_subscribe_slots
  - utter_correct_info
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form{"name": null}
* affirm: oui
  - action_save_information
  - utter_question_on_ENIGMA_Stras
* deny: non
  - utter_thanks
  - utter_goodbye
* goodbye: ciao
  - utter_goodbye

## subscribe and pitch question
*   how_to_subscribe: j'aimerais recevoir la newsletter
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form: slot_was_set
  - form{"name": null}
* affirm: oui
  - action_save_information
  - utter_question_on_ENIGMA_Stras
* affirm: oui
  - utter_question
* question_pitch: quels sont les jeux
  - action_which_game
* societe_mysterieuse: C'est quoi  société mystérieuse de Strasbourg
  - action_requested_game
* affirm: wé
  - action_next_game
* deny: no
  - utter_propose_riddle
* deny: nan
  - utter_thanks
  - utter_goodbye
* goodbye: ciao
  - utter_goodbye
