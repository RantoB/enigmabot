## enigmabot make a riddle
> check_if_question_or_riddle
* ask_for_riddle OR inform_kind_of_riddle
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## Bot proposed a riddle and user affirm without question on ENIGMA Stras
> check_answer_about_riddle
* affirm
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## Bot proposed a riddle and user affirm after question on ENIGMA Stras
> check_answer_about_riddle_after_question_ENIGMA_Stras
* affirm
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras
