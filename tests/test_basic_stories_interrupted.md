## Normal story: Greet, FAQ, Riddle, Subscribe, Faq, Goodbye - interrupted with faq and continue
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
* faq: quel est le prix
  - respond_faq
  - utter_ask_leave_riddle_form
* deny: no
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* deny: no
  - utter_subscribe
* affirm: oui
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* faq: quel est le prix
  - respond_faq
  - utter_ask_leave_subscribe_form
* deny: no
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

## Normal story: Greet, FAQ, Riddle, Subscribe, Faq, Goodbye- interrupted with OOS and continue
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
* out_of_scope: bite
  - respond_out_of_scope
  - utter_ask_leave_riddle_form
* deny: no
  - form{"name": "form_riddle"}
  - form: slot_was_set
  - form{"name": null}
  - utter_propose_riddle
* deny: no
  - utter_subscribe
* affirm: oui
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* out_of_scope: bite
  - respond_out_of_scope
  - utter_ask_leave_subscribe_form
* deny: no
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

## Normal story: Greet, FAQ, Riddle, Subscribe, Faq, Goodbye - interrupted with faq and leave
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
* faq: quel est le prix
  - respond_faq
  - utter_ask_leave_riddle_form
* affirm: oui
  - action_deactivate_form
  - utter_ok
  - utter_an_other_riddle
* deny: no
  - utter_subscribe
* affirm: oui
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* faq: quel est le prix
  - respond_faq
  - utter_ask_leave_subscribe_form
* affirm: oui
  - action_deactivate_form
  - utter_ok
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

## Normal story: Greet, FAQ, Riddle, Subscribe, Faq, Goodbye- interrupted with OOS and leave
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
* out_of_scope: bite
  - respond_out_of_scope
  - utter_ask_leave_riddle_form
* affirm: oui
  - action_deactivate_form
  - utter_ok
  - utter_an_other_riddle
* deny: no
  - utter_subscribe
* affirm: oui
  - form_subscribe
  - form_subscribe{"name": "form_subscribe"}
* out_of_scope: bite
  - respond_out_of_scope
  - utter_ask_leave_subscribe_form
* affirm: oui
  - action_deactivate_form
  - utter_ok
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
