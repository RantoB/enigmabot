## Normal story: Greet, FAQ, Riddle, Subscribe, Faq, Goodbye
* greet: hello
  - utter_greet
* faq: combien ça coûte ?
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_propose_riddle
* affirm: yes
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* deny: no
  - utter_subscribe
* affirm: oui
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form: slot_was_set
  - form{"name": null}
  - action_ask_user_to_check_infomration
* affirm: oui
  - action_save_information
  - utter_question_on_ENIGMA_Stras
* affirm: oui
  - utter_question
* faq: combien de temps ?
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: bye
  - utter_goodbye

## Normal story: Greet, No FAQ, Riddle, Subscribe, No Faq, Goodbye
* greet: hello
  - utter_greet
* no_question: je n'ai pas de question
  - utter_propose_riddle
* affirm: yes
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* deny: no
  - utter_subscribe
* affirm: oui
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form: slot_was_set
  - form{"name": null}
  - action_ask_user_to_check_infomration
* affirm: oui
  - action_save_information
  - utter_question_on_ENIGMA_Stras
* affirm: oui
  - utter_question
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: bye
  - utter_goodbye

## Normal story: Greet, FAQ, No Riddle, Subscribe, Faq, Goodbye
* greet: hello
  - utter_greet
* faq: combien ça coûte ?
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_propose_riddle
* deny: no
  - utter_subscribe
* affirm: oui
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
  - form: slot_was_set
  - form{"name": null}
  - action_ask_user_to_check_infomration
* affirm: oui
  - action_save_information
  - utter_question_on_ENIGMA_Stras
* affirm: oui
  - utter_question
* faq: combien de temps ?
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: bye
  - utter_goodbye

## Normal story: Greet, FAQ, Riddle, No Subscribe, Faq, Goodbye
* greet: hello
  - utter_greet
* faq: combien ça coûte ?
  - respond_faq
  - utter_one_more_question
* deny: no
  - utter_propose_riddle
* affirm: yes
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* deny: no
  - utter_subscribe
* deny: no
  - utter_thanks
  - utter_goodbye
* goodbye: bye
  - utter_goodbye
