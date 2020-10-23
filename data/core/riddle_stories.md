## enigmabot make a riddle
* ask_for_riddle OR inform_kind_of_riddle{"riddle_category": "logique"}
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## Bot proposed a riddle and user affirm without FAQ
> check_answer_about_riddle
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## Bot proposed a riddle and user affirm after FAQ
> check_answer_about_riddle_after_question_ENIGMA_Stras
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras
