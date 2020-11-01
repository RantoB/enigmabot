## Normal story: Greet, FAQ, Riddle, Subscribe, Faq, Goodbye (/tmp/tmp24ukf7nj/afd46e71ca3a4d68b0fd797fe149c50c_test_basic_stories.md)
* greet: hello
    - utter_greet
* faq: combien ça coûte ?
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_propose_riddle
* affirm: yes
    - form_riddle   <!-- predicted: action_reset_riddle_slots -->
    - form{"name": "form_riddle"}
    - form{"name": null}
    - utter_propose_riddle
* deny: no
    - utter_subscribe
* affirm: oui
    - form_subscribe
    - form_subscribe
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


## Normal story: Greet, No FAQ, Riddle, Subscribe, No Faq, Goodbye (/tmp/tmp24ukf7nj/afd46e71ca3a4d68b0fd797fe149c50c_test_basic_stories.md)
* greet: hello
    - utter_greet
* no_question: je n'ai pas de question
    - utter_propose_riddle
* affirm: yes
    - form_riddle   <!-- predicted: action_reset_riddle_slots -->
    - form{"name": "form_riddle"}
    - form{"name": null}
    - utter_propose_riddle
* deny: no
    - utter_subscribe   <!-- predicted: utter_question_on_ENIGMA_Stras -->
* affirm: oui
    - form_subscribe
    - form_subscribe
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


## Normal story: Greet, FAQ, Riddle, No Subscribe, Faq, Goodbye (/tmp/tmp24ukf7nj/afd46e71ca3a4d68b0fd797fe149c50c_test_basic_stories.md)
* greet: hello
    - utter_greet
* faq: combien ça coûte ?
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_propose_riddle
* affirm: yes
    - form_riddle   <!-- predicted: action_reset_riddle_slots -->
    - form{"name": "form_riddle"}
    - form{"name": null}
    - utter_propose_riddle
* deny: no
    - utter_subscribe
* deny: no
    - utter_thanks
    - utter_goodbye
* goodbye: bye
    - utter_goodbye


## Normal story: Greet, FAQ, Riddle, Subscribe, Faq, Goodbye - interrupted with faq and continue (/tmp/tmp24ukf7nj/cc19080fdc994e4ab346128adb2db104_test_basic_stories_interrupted.md)
* greet: hello
    - utter_greet
* faq: combien ça coûte ?
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_propose_riddle
* affirm: yes
    - form_riddle   <!-- predicted: action_reset_riddle_slots -->
    - form{"name": "form_riddle"}
* faq: quel est le prix
    - respond_faq
    - utter_ask_leave_riddle_form
    - form{"name": "form_riddle"}
* form: deny: no
    - form{"name": null}
    - utter_propose_riddle   <!-- predicted: respond_faq -->
* deny: no
    - utter_subscribe
* affirm: oui
    - form_subscribe
    - form_subscribe
    - action_listen   <!-- predicted: action_ask_user_to_check_infomration -->
* faq: quel est le prix
    - respond_faq
    - utter_ask_leave_subscribe_form
* deny: no
    - form_subscribe
    - form{"name": null}
    - action_ask_user_to_check_infomration   <!-- predicted: form_subscribe -->
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


## Normal story: Greet, FAQ, Riddle, Subscribe, Faq, Goodbye- interrupted with OOS and continue (/tmp/tmp24ukf7nj/cc19080fdc994e4ab346128adb2db104_test_basic_stories_interrupted.md)
* greet: hello
    - utter_greet
* faq: combien ça coûte ?
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_propose_riddle
* affirm: yes
    - form_riddle   <!-- predicted: action_reset_riddle_slots -->
    - form{"name": "form_riddle"}
* out_of_scope: bite
    - respond_out_of_scope
    - utter_ask_leave_riddle_form
    - form{"name": "form_riddle"}
* form: deny: no
    - form{"name": null}
    - utter_propose_riddle   <!-- predicted: respond_out_of_scope -->
* deny: no
    - utter_subscribe
* affirm: oui
    - form_subscribe
    - form_subscribe
    - action_listen   <!-- predicted: action_ask_user_to_check_infomration -->
* out_of_scope: bite
    - respond_out_of_scope
    - utter_ask_leave_subscribe_form
* deny: no
    - form_subscribe
    - form{"name": null}
    - action_ask_user_to_check_infomration   <!-- predicted: form_subscribe -->
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


## Normal story: Greet, FAQ, Riddle, Subscribe, Faq, Goodbye - interrupted with faq and leave (/tmp/tmp24ukf7nj/cc19080fdc994e4ab346128adb2db104_test_basic_stories_interrupted.md)
* greet: hello
    - utter_greet
* faq: combien ça coûte ?
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_propose_riddle
* affirm: yes
    - form_riddle   <!-- predicted: action_reset_riddle_slots -->
    - form{"name": "form_riddle"}
* faq: quel est le prix
    - respond_faq
    - utter_ask_leave_riddle_form
* affirm: oui
    - action_deactivate_form
    - utter_ok
    - utter_an_other_riddle
* deny: no
    - utter_subscribe   <!-- predicted: utter_question_on_ENIGMA_Stras -->
* affirm: oui
    - form_subscribe
    - form_subscribe
    - action_listen   <!-- predicted: action_ask_user_to_check_infomration -->
* faq: quel est le prix
    - respond_faq   <!-- predicted: form_riddle -->
    - utter_ask_leave_subscribe_form
* affirm: oui
    - action_deactivate_form   <!-- predicted: form_riddle -->
    - utter_ok
    - utter_question_on_ENIGMA_Stras
* affirm: oui
    - utter_question
* faq: combien de temps ?
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_thanks   <!-- predicted: utter_subscribe -->
    - utter_goodbye
* goodbye: bye
    - utter_goodbye


## Normal story: Greet, FAQ, Riddle, Subscribe, Faq, Goodbye- interrupted with OOS and leave (/tmp/tmp24ukf7nj/cc19080fdc994e4ab346128adb2db104_test_basic_stories_interrupted.md)
* greet: hello
    - utter_greet
* faq: combien ça coûte ?
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_propose_riddle
* affirm: yes
    - form_riddle   <!-- predicted: action_reset_riddle_slots -->
    - form{"name": "form_riddle"}
* out_of_scope: bite
    - respond_out_of_scope
    - utter_ask_leave_riddle_form
* affirm: oui
    - action_deactivate_form
    - utter_ok
    - utter_an_other_riddle
* deny: no
    - utter_subscribe   <!-- predicted: utter_question_on_ENIGMA_Stras -->
* affirm: oui
    - form_subscribe
    - form_subscribe
    - action_listen   <!-- predicted: action_ask_user_to_check_infomration -->
* out_of_scope: bite
    - respond_out_of_scope   <!-- predicted: form_riddle -->
    - utter_ask_leave_subscribe_form
* affirm: oui
    - action_deactivate_form   <!-- predicted: form_riddle -->
    - utter_ok
    - utter_question_on_ENIGMA_Stras
* affirm: oui
    - utter_question
* faq: combien de temps ?
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_thanks   <!-- predicted: utter_subscribe -->
    - utter_goodbye
* goodbye: bye
    - utter_goodbye


